# POS Ready 管理

POS Ready 让平台识别终端（POS 收银机、支付终端等）的流量，并按优先级转发，保障关键交易在弱网/拥塞时优先传输。

## 优先级三态

终端的 `posReady.level` 有三个取值（wire/JSON 小写）：

| level      | 含义                                   |
| ---------- | -------------------------------------- |
| `priority` | 优先转发该终端的 POS 流量              |
| `default`  | 不特殊处理（等价未标记；`null` 同义）  |
| `bypass`   | 将该终端排除在 POS 处理之外            |

`posReady` 是对象，除 `level` 外还含 `lastMatchedAt`（最近命中时间）、`updatedAt`、`updatedBy`。

## 设置终端优先级

设置入口在 `device client` 组（操作对象是终端，需 client-id，不是 device-id）。

```bash
# 先查终端 ID（按 MAC/名称搜索）
incloud device client list <device-id> -q <mac-or-name> -f _id,name,mac,posReady.level

# 设为优先
incloud device client set-pos-ready <client-id> --level priority

# 排除处理
incloud device client set-pos-ready <client-id> --level bypass

# 恢复默认
incloud device client set-pos-ready <client-id> --level default
```

> `client list` / `client get` 默认字段已含 `posReady.level`，可直接确认当前状态。

## 查询已标记终端

```bash
# 全局：所有已标记 priority/bypass 的终端（可按 level/设备/组织筛选）
incloud pos clients --level priority -o yaml
incloud pos clients --device <device-id> -o yaml

# 单设备：某设备上已标记的终端
incloud pos marked-clients <device-id> --level bypass -o yaml
```

## 观测 POS 命中

“命中”指终端的流量被 POS 规则匹配并转发。

```bash
# 近期命中转发的终端（默认 24h，可按 vendor/终端类型筛选）
incloud pos forwarded --active-within 24h -o yaml
incloud pos forwarded --active-within 7d --vendor Verifone -o yaml

# 单设备命中统计（按 vendor 或 client 聚合）
incloud pos device-hits <device-id> --active-within 24h --group-by vendor -o yaml
```

## 命中时序（时间必填）

vendor-hits/summary 返回时序数据，`--after` 与 `--before` 都必填。**时序数据用 table 输出**观察趋势。

```bash
# 终端按 vendor 的命中时序（默认 5m 间隔）
incloud pos vendor-hits <device-id> <client-id> --after 2026-06-22T00:00:00 --before 2026-06-23T00:00:00 -o table

# 终端按 vendor 的命中汇总
incloud pos vendor-summary <device-id> <client-id> --after 2026-06-22 --before 2026-06-23 -o yaml
```

## 终端类型字典

```bash
# 查可用的终端类型（POS_TERMINAL 等），用于 forwarded/rules 的 clientType 取值
incloud pos client-types -o yaml
```

## 自定义规则（custom-rules）

自定义规则让管理员显式声明哪些流量算作某终端类型的 POS 流量。需 `pos-custom-rules:read/write` 权限。

```bash
# 查某设备的规则
incloud pos rules get <device-id> -o yaml

# 列出所有设备的规则
incloud pos rules list -o yaml
incloud pos rules list --device <device-id> -o yaml
```

### 下发规则

规则文件可以是裸数组，也可以是带 `rules` 字段的对象。每条规则字段：

- `type`：`add`（声明为 POS 流量）或 `mask`（排除）
- `clientType`：终端类型，大写（如 `POS_TERMINAL`，取自 `pos client-types`）
- `vendor`：厂商标签
- `protocol`、`address`、`port`：匹配的协议/地址/端口

```json
[
  {
    "type": "add",
    "clientType": "POS_TERMINAL",
    "vendor": "Verifone",
    "protocol": "tcp",
    "address": "203.0.113.10",
    "port": "443"
  }
]
```

```bash
# 从文件下发（整组替换，最多 100 条）
incloud pos rules set <device-id> --file rules.json

# 从 stdin 读取
cat rules.json | incloud pos rules set <device-id> --file -
```

> **整组替换语义**：`set` 会用文件内容覆盖该设备的全部规则。下发前务必先 `rules get` 取当前规则作为基础，避免遗漏。
> 下发后会返回 `pushOutcome`（下发结果）；若设备离线或下发失败，关注 `pushError`。

## 典型问法 → 命令

| 用户问                                   | 命令                                                        |
| ---------------------------------------- | ----------------------------------------------------------- |
| 把这个收银机设成 POS 优先                | `device client set-pos-ready <client-id> --level priority`  |
| 哪些终端被标了 POS 优先                   | `pos clients --level priority`                              |
| 这台设备上标了哪些 POS 终端              | `pos marked-clients <device-id>`                           |
| 最近哪些 POS 终端有流量命中              | `pos forwarded`                                            |
| 这台设备的 POS 命中按厂商分布            | `pos device-hits <device-id> --group-by vendor`            |
| 看某终端这段时间的 POS 命中趋势          | `pos vendor-hits <device-id> <client-id> --after --before` |
| 这台设备配了哪些 POS 自定义规则          | `pos rules get <device-id>`                                |
| 给这台设备下发一批 POS 规则              | `pos rules set <device-id> --file rules.json`              |
