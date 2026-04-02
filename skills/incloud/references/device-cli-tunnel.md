# 设备 CLI 隧道远程操作参考

## 何时需要

大多数诊断通过 InCloud CLI 即可完成（`device exec ping`、`device log`、`device config` 等走平台 API）。仅在需要查看平台未暴露的信息时才需直连设备 CLI：

- INOS 配置（`show running-config`）、路由表（`show ip route`）、实时日志（`show log`）
- 底层 Linux 诊断（进程、内存、磁盘、内核日志等）— 需 `--shell` 模式

## 一次性执行（推荐）

```bash
# INOS CLI 命令（默认凭证 adm/123456，但用户可能已修改，需确认）
incloud device exec cli <device-id> --user <username> --password <password> "show interface"

# BusyBox shell 命令（用 && 链接多个）
incloud device exec cli <device-id> --user <username> --password <password> \
  --shell --shell-password <shell-password> "uname -a && free -m && ip route"
```

自动管理隧道（创建 → 登录 → 执行 → 关闭），单次约 6 秒。输出已去除 telnet 协商、ANSI 转义、命令回显和提示符。

## 多轮诊断

需要根据上一步结果决定下一步时，复用隧道避免重复创建（每次约 3.5 秒）：

```bash
incloud tunnel open-cli <device-id> --no-open     # 创建隧道
incloud tunnel cli <tunnel-id> --user <username> --password <password> "show interface"
incloud tunnel cli <tunnel-id> --user <username> --password <password> "show log"
incloud tunnel close <tunnel-id>                   # 用完关闭
```

> `tunnel cli` 自动从 API 获取 token，无需 `--token`。用 `tunnel get <tunnel-id>` 查看隧道详情。

## INOS vs Shell 模式

| | INOS（默认） | Shell（`--shell`） |
|---|---|---|
| 环境 | INOS CLI（类 Cisco IOS） | BusyBox ash |
| 命令 | `show interface`、`show log`、`ping` 等 | `uname`、`free`、`ip`、`logread` 等 |
| 多命令 | 不支持链接，每次一条 | 用 `&&` 或 `;` 链接 |
| 需要 | `--user`、`--password` | 额外需 `--shell-password` |

> `--shell-password`（`inhand` 命令的密码）因设备而异，需用户提供。

## 注意事项

- 每次调用都会重新 telnet 登录，无法保持会话
- 超时命令（如 `ping`）用 `--timeout 60` 增加等待时间
- 当前仅支持 Telnet 协议设备
