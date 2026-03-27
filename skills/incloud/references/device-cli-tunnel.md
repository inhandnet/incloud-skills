# 设备 CLI 隧道远程操作参考

## 何时需要

大多数诊断通过 InCloud CLI 即可完成。仅在需要查看平台未暴露的信息（INOS 配置、路由表、实时日志等）时才需登录设备 CLI。

## 建立隧道

分两步执行（比 `open-cli --forward` 更可控）：

```bash
# 1. 创建隧道，获取 Tunnel ID 和 Token
incloud tunnel open-cli <device-id> --no-open

# 2. 转发到本地端口（阻塞前台）
incloud tunnel forward <tunnel-id> --token <jwt> --port <port>

# 3. 关闭
incloud tunnel close <tunnel-id>
```

## 连接协议

隧道转发的协议取决于设备类型，可能是 **Telnet** 或 **SSH**。连接前无法确定，建议先尝试 SSH，超时（banner exchange timeout）再换 Telnet。

## INOS CLI 特有行为

INOS 是映翰通专有网络操作系统，外观类似 Cisco IOS 但有差异：

- **不是 Linux Shell** — `uname`、`free`、`top`、`ip addr` 等 Linux 命令均不可用，报 `Command is not supported`
- **无法禁用分页** — `--More--` 分页只能在 expect 脚本中自动处理（用 `-exact "--More--"` 匹配后发空格翻页）
- **`adm` 登录后可能直接是特权模式（`#`）** — 此时 `enable` 直接通过不要密码。只有先 `disable` 退到用户模式（`>`）后 `enable` 才需要密码
- **退出是两层** — 特权模式 `exit` → 用户模式（`>`），再 `exit` → 确认 `Are you sure to Exit?[Y|N]`。不是一次 `exit` 直接退出
- **提示符格式复杂** — 实际格式为 `HH:MM:SS hostname#` 或带行号 `N hostname#`，匹配时用 `[#>] ` 即可

## Shell 模式（BusyBox ash）

在 INOS CLI 特权模式下输入 `inhand` 并输入密码，可进入底层 Linux shell（BusyBox ash）。进入后所有标准 Linux 命令可用（`uname`、`free`、`top`、`ip`、`logread` 等），提示符变为路径格式如 `/www #`。

shell 模式适用于 INOS CLI 无法完成的深度诊断（进程列表、内核日志、路由表细节、磁盘使用等）。`exit` 退回 INOS CLI。

> `inhand` 命令的密码因设备而异，需用户提供。

## 自动化脚本

使用 `scripts/inos-cli.py`（纯 Python 标准库，跨平台）自动处理登录、`--More--` 分页和退出：

```bash
# INOS CLI 模式
python3 scripts/inos-cli.py <port> <user> <password> "show interface" "show log" "ping 8.8.8.8"

# Shell 模式（BusyBox ash）
python3 scripts/inos-cli.py <port> <user> <password> --shell <shell-password> "uname -a" "free -m" "ip route"
```
