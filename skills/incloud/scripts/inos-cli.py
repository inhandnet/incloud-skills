#!/usr/bin/env python3
"""
INOS CLI 自动化脚本 — 通过隧道登录设备执行命令

用法:
  inos-cli.py <port> <user> <password> <cmd1> [cmd2] ...
  inos-cli.py <port> <user> <password> --shell <shell-password> <cmd1> [cmd2] ...

示例:
  inos-cli.py 2226 adm 123456 "show interface" "show log" "ping 8.8.8.8"
  inos-cli.py 2226 adm 123456 --shell 64391099@inhand "uname -a" "free -m" "ip route"
"""

import re
import socket
import sys
import time

# Telnet 协议常量
IAC = b"\xff"
DONT = b"\xfe"
DO = b"\xfd"
WONT = b"\xfc"
WILL = b"\xfb"
SB = b"\xfa"
SE = b"\xf0"

RECV_BUF = 4096
DEFAULT_TIMEOUT = 30


class TelnetClient:
    """最小 telnet 客户端，仅处理协议协商，不依赖 telnetlib"""

    def __init__(self, host: str, port: int, timeout: float = DEFAULT_TIMEOUT):
        self.sock = socket.create_connection((host, port), timeout=timeout)
        self.sock.settimeout(timeout)
        self._buf = b""

    def _negotiate(self, data: bytes) -> bytes:
        """处理 telnet 协商，对所有 DO/WILL 回复 WONT/DONT"""
        out = b""
        clean = b""
        i = 0
        while i < len(data):
            if data[i : i + 1] == IAC and i + 1 < len(data):
                cmd = data[i + 1 : i + 2]
                if cmd in (DO, DONT, WILL, WONT) and i + 2 < len(data):
                    opt = data[i + 2 : i + 3]
                    if cmd == DO:
                        out += IAC + WONT + opt
                    elif cmd == WILL:
                        out += IAC + DONT + opt
                    i += 3
                elif cmd == SB:
                    # 跳过子协商
                    end = data.find(IAC + SE, i + 2)
                    i = end + 2 if end != -1 else len(data)
                elif cmd == IAC:
                    clean += IAC
                    i += 2
                else:
                    i += 2
            else:
                clean += data[i : i + 1]
                i += 1
        if out:
            self.sock.sendall(out)
        return clean

    def read_until(
        self, patterns: list[str], timeout: float = DEFAULT_TIMEOUT
    ) -> tuple[str, int]:
        """读取直到匹配任一 pattern，返回 (收到的文本, 匹配的 pattern 索引)，超时返回 -1"""
        deadline = time.time() + timeout
        text = ""
        while time.time() < deadline:
            remaining = deadline - time.time()
            if remaining <= 0:
                break
            self.sock.settimeout(max(remaining, 0.1))
            try:
                data = self.sock.recv(RECV_BUF)
                if not data:
                    break
                clean = self._negotiate(data)
                text += clean.decode("utf-8", errors="replace")
                # 检查匹配
                for i, pat in enumerate(patterns):
                    if pat in text:
                        return text, i
            except socket.timeout:
                continue
        return text, -1

    def write(self, text: str):
        self.sock.sendall(text.encode("utf-8"))

    def close(self):
        try:
            self.sock.close()
        except Exception:
            pass


# ANSI 转义序列清理
ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]|\r")


def clean_output(text: str) -> str:
    return ANSI_RE.sub("", text)


def strip_echo(text: str, cmd: str) -> str:
    """去掉命令回显（可能出现多次，带行号前缀等）"""
    lines = text.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        # 跳过纯命令回显行
        if stripped == cmd.strip():
            continue
        # 跳过带行号前缀的回显：如 "8 er# show interface"
        if cmd.strip() in stripped and re.match(r"^\d+\s+\S+[#>]", stripped):
            continue
        result.append(line)
    return "\n".join(result)


def inos_cmd(tn: TelnetClient, cmd: str, prompt_patterns: list[str]) -> str:
    """发送 INOS 命令，自动处理 --More-- 分页"""
    tn.write(cmd + "\r")
    time.sleep(0.5)
    full_output = ""

    while True:
        text, idx = tn.read_until(prompt_patterns + ["--More--"], timeout=DEFAULT_TIMEOUT)
        full_output += text
        if idx == -1:
            # 超时
            sys.stderr.write(f"\n[TIMEOUT] {cmd}\n")
            break
        elif idx == len(prompt_patterns):
            # --More-- 翻页
            tn.write(" ")
            time.sleep(0.3)
        else:
            # 匹配到提示符
            break

    return clean_output(full_output)


def shell_cmd(tn: TelnetClient, cmd: str, prompt_patterns: list[str]) -> str:
    """发送 shell 命令"""
    tn.write(cmd + "\r")
    time.sleep(0.3)
    text, _ = tn.read_until(prompt_patterns, timeout=DEFAULT_TIMEOUT)
    return clean_output(text)


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    port = int(sys.argv[1])
    user = sys.argv[2]
    password = sys.argv[3]

    shell_mode = False
    shell_pass = ""
    cmd_start = 4

    if len(sys.argv) > 4 and sys.argv[4] == "--shell":
        if len(sys.argv) < 7:
            sys.stderr.write("Error: --shell requires <shell-password> and at least one command\n")
            sys.exit(1)
        shell_mode = True
        shell_pass = sys.argv[5]
        cmd_start = 6

    commands = sys.argv[cmd_start:]
    if not commands:
        sys.stderr.write("Error: at least one command required\n")
        sys.exit(1)

    # INOS 提示符匹配 pattern
    inos_prompts = ["er#", "er>"]  # 简化匹配，实际 hostname 可能不同
    shell_prompts = ["# ", "$ "]

    # 连接
    tn = TelnetClient("127.0.0.1", port)
    time.sleep(3)  # 等隧道 TLS 握手
    tn.write("\r")

    # 登录
    text, idx = tn.read_until(["login:"], timeout=DEFAULT_TIMEOUT)
    if idx == -1:
        sys.stderr.write("[ERROR] No login prompt\n")
        sys.exit(1)

    tn.write(user + "\r")
    text, idx = tn.read_until(["assword:"], timeout=DEFAULT_TIMEOUT)
    if idx == -1:
        sys.stderr.write("[ERROR] No password prompt\n")
        sys.exit(1)

    tn.write(password + "\r")

    # 等待 INOS 提示符（匹配 # 或 >）
    text, idx = tn.read_until(["# ", "> "], timeout=DEFAULT_TIMEOUT)
    if idx == -1:
        sys.stderr.write("[ERROR] Login failed or timeout\n")
        sys.exit(1)

    # 从 welcome banner 中提取实际 hostname 用于后续匹配
    # 提示符格式: "HH:MM:SS hostname# "
    m = re.search(r"\d+:\d+:\d+ (\S+)[#>]\s*$", text)
    if m:
        hostname = m.group(1)
        inos_prompts = [f"{hostname}#", f"{hostname}>"]

    print(clean_output(text), end="")
    time.sleep(0.5)

    if shell_mode:
        # 进入 shell
        tn.write("inhand\r")
        text, idx = tn.read_until(["assword:", "password:"], timeout=DEFAULT_TIMEOUT)
        if idx == -1:
            sys.stderr.write("[ERROR] No shell password prompt\n")
            sys.exit(1)

        tn.write(shell_pass + "\r")
        text, idx = tn.read_until(shell_prompts, timeout=DEFAULT_TIMEOUT)
        if "Bad password" in text:
            sys.stderr.write("[ERROR] Shell password incorrect\n")
            sys.exit(1)

        print(clean_output(text), end="")

        # 执行 shell 命令
        for cmd in commands:
            output = shell_cmd(tn, cmd, shell_prompts)
            print(output, end="")

        # 退出 shell
        tn.write("exit\r")
        tn.read_until(inos_prompts, timeout=10)

    else:
        # INOS CLI 模式
        for cmd in commands:
            output = inos_cmd(tn, cmd, inos_prompts)
            print(output, end="")

    # 退出 INOS CLI（两层）
    tn.write("exit\r")
    text, idx = tn.read_until(["Y|N", "> "], timeout=10)
    if idx == 1:
        # 从特权退到用户模式，再退一次
        tn.write("exit\r")
        tn.read_until(["Y|N"], timeout=10)
    tn.write("Y\r")
    time.sleep(1)
    tn.close()


if __name__ == "__main__":
    main()
