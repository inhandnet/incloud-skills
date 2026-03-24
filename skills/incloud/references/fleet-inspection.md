# 批量巡检与健康评估参考

当需要对一批设备（按客户、区域、分组）进行整体健康检查时参考此文档。典型场景包括：收到批量离线告警需要快速定位范围、VIP 客户定期巡检、季度容量规划评估。

## 设备筛选与分组

```bash
incloud device list -q "<关键词>" --output yaml           # 按名称/SN/备注等搜索设备
incloud device list -q "<关键词>" -f _id,name,serialNumber,online    # 只返回关键字段，减少输出量
incloud device group list --output yaml                    # 查看所有分组
incloud device list --group <group-id> --output yaml       # 按分组筛选设备
```

分页遍历：默认每页 20 条，用 `--page` 和 `--limit` 翻页。批量巡检时可能需要遍历多页。

## 批量离线识别

```bash
incloud device list -q "<客户名>" -f _id,name,serialNumber,online --output yaml   # 查看在线/离线状态
incloud device online <id>                                              # 单台设备的在线历史
incloud alert list --search "offline" --after <ISO8601> --output yaml   # 查看离线告警
incloud alert export --after <ISO8601> --before <ISO8601>               # 导出指定时间范围告警
```

巡检思路：
- 先通过 `device list` 按客户/区域筛选，快速统计离线设备数量和占比
- 对离线设备查看 `device online` 确认离线时间点，判断是集中掉线还是逐步掉线
- 集中掉线：优先排查共性因素（同一运营商、同一区域、同一固件版本）
- 逐步掉线：可能是个别设备问题，逐台排查

## 信号与资源边缘设备

```bash
incloud device antenna <id>      # 蜂窝信号数据
incloud device perf <id>         # CPU/内存/磁盘使用率
incloud device uplink <id>       # 上行链路状态
```

巡检思路：
- 信号边缘设备：antenna 数据中 RSRP 在 -100 到 -110 dBm 之间的设备，容易因信号波动掉线
- 资源紧张设备：CPU 或内存持续 >80% 的设备，可能在业务高峰出问题
- 链路异常设备：uplink 显示主链路 down 或频繁切换的设备

## 固件版本分布

```bash
incloud device group firmwares <group-id> --output yaml    # 分组内固件版本分布
incloud firmware list --search "<型号>" --output yaml      # 查看该型号可用固件
```

巡检思路：
- 检查是否存在版本碎片化（同一型号多个固件版本）
- 对比最新可用固件，识别需要升级的设备
- 老旧固件可能存在已知 bug 或安全漏洞

## 流量与容量评估

```bash
incloud device datausage <id>    # 单台设备数据用量
incloud device client <id>       # 连接的终端设备列表
incloud device perf <id>         # 性能趋势数据
```

容量评估思路：
- 流量趋势：对比不同时段的 datausage，判断流量是否持续增长
- 终端密度：client 数量接近设备上限时需要考虑扩容或分流
- 资源趋势：perf 数据中 CPU/内存使用率持续上升说明负载在增长
- 交叉分析：高流量 + 高终端数 + 高资源使用率 = 需要关注的容量瓶颈

## 告警汇总

```bash
incloud alert list --after <ISO8601> --output yaml         # 查看指定时间后的告警
incloud alert list --before <ISO8601> --output yaml        # 查看指定时间前的告警
incloud alert export --after <ISO8601> --before <ISO8601>  # 导出告警数据
```

巡检思路：
- 按时间范围汇总告警，识别高频告警设备
- 重复告警的设备往往是潜在风险点
- 告警类型分布可以反映整体网络的薄弱环节
