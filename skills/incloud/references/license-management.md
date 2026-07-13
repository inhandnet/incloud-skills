# License 管理

## License 生命周期

```
inactivated（未激活）→ activated（已激活）→ to_be_expired（即将到期）→ expired（已到期）
```

- **inactivated**：刚购入，未绑定到任何设备
- **activated**：已绑定到设备，正在计时
- **to_be_expired**：剩余有效期 ≤ 30 天（仍可正常使用）
- **expired**：已到期，功能受限或停用

## 查询可用 License

```bash
# 查看所有未分配的 License（可按类型筛选）
incloud license list --status inactivated --attached false -o yaml

# 查看设备上当前激活的 License
incloud license list --status activated --attached true -o yaml

# 按类型筛选（type 填 slug，如 basic、professional、enterprise）
incloud license list --status inactivated --type basic -o yaml

# 查看 License 详情
incloud license get <license-id> -o yaml
```

## 分配 License 到设备

```bash
# 先查设备 ID（如只有 SN）
incloud device list -q <SN> --fields _id,serialNumber,name

# 分配 License
incloud license attach <license-id> --device <device-id>
```

**叠加（Overlay）**：若设备上已有同类型的激活 License，新 License 的时长会直接累加到已有 License 上，累计最长 10 年。命令执行前会展示预览，需要确认。

```bash
# 跳过确认
incloud license attach <license-id> --device <device-id> --yes
```

## 从设备解绑 License

解绑后，License 恢复为 **activated** 状态，可重新分配到其他设备。

```bash
incloud license detach <license-id>
```

> 注意：只有状态为 activated 或 to_be_expired 且已绑定设备的 License 才能解绑。

## 升级 License 类型

批量将多台设备的 License 从当前类型升级到更高档位。剩余天数按新旧类型的价格比例折算。

```bash
# 先查可用的 License 类型
incloud license type list -o yaml

# 升级（所有设备必须是同一当前类型）
incloud license upgrade --device-id <id1>,<id2>,<id3> --to <target-type-slug>
```

**约束**：
- 所有指定设备必须是同一个当前 License 类型
- 没有已过期 License 的设备
- 最多 1000 台设备/次

## 对齐 License 到期日（共止）

将多个 License 对齐到同一到期日期，便于统一续费管理。这是免费操作，通过重新分配剩余时长实现。

```bash
incloud license align-expiry <license-id1> <license-id2> <license-id3>
```

> 只有 activated 或 to_be_expired 状态的 License 才能参与对齐。命令会先展示对齐后的预览再确认。

## 转移 License 到其他组织

将未使用的 License 转移给另一个组织（如重新分配资源）。

```bash
# 先确认目标组织 ID
incloud org list -q <org-name> --fields _id,name

# 转移（支持批量）
incloud license transfer <license-id1> <license-id2> --org <target-org-id>
```

**约束**：只有状态为 **inactivated** 且**未绑定设备**的 License 才能转移。

## 查看操作历史

```bash
incloud license history <license-id> -o yaml
```

返回 License 的完整操作日志，包含 attach、detach、upgrade、align、extend 等事件及时间戳。

## 查看可购 License 类型

```bash
# 列出所有已发布的 License 类型
incloud license type list -o yaml

# 查看某类型的详情（含价格、功能列表、支持的产品）
incloud license type get <type-id> --expand prices -o yaml
```

## 查看订单

```bash
# 查询订单列表（默认返回所有状态）
incloud license order list -o yaml

# 筛选未完成的订单
incloud license order list --status open -o yaml

# 订单详情
incloud license order get <order-id> -o yaml
```
