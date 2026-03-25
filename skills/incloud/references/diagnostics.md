# 诊断与运维操作参考

## 设备离线排查

按以下顺序逐步排查：

```bash
incloud device get <id>                    # 1. 查看设备基本状态和最后在线时间
incloud device online <id>                 # 2. 在线/离线历史，确认掉线时间点
incloud device interface <id>              # 3. 网络接口状态，是否有接口 down
incloud device uplink <id>                 # 4. 上行链路状态，WAN 口是否正常
incloud device antenna <id>               # 5. 天线信号历史（按天线维度的 RSRP/RSRQ/SINR）
incloud device signal list <id>            # 5b. 蜂窝信号历史（整体信号质量趋势）
incloud device perf <id>                   # 6. CPU/内存/磁盘，是否资源耗尽
incloud device log syslog <id> --fetch     # 7a. 设备系统日志（网络/VPN/WiFi/DNS 等模块），实时采集（默认今天至今，可加 --after/--before 缩小范围）
incloud device log syslog <id> --after T1 --before T2 --keywords error  # 7b. 查历史系统日志（--after/--before 必填，--keywords 过滤关键词）
```

排查思路：
- 先确认设备是否真的离线（可能只是平台连接断开）
- 查看最后在线时间，判断是突然断开还是逐渐失联
- 检查网络接口和上行链路，确认物理连接状态
- 蜂窝设备检查信号质量，`antenna` 看各天线信号历史，`signal list` 看整体蜂窝信号趋势，信号弱或持续劣化可能导致频繁掉线。**判读信号数值时加载 `references/signal-analysis.md`**
- 检查资源使用率，CPU 或内存打满可能导致服务异常
- 查看日志寻找具体错误信息。**分析日志内容时加载 `references/log-analysis.md`** 获取模块分类和关键词映射

## 网络连接问题诊断

```bash
incloud device exec ping <id> --host <target>        # Ping 测试连通性
incloud device exec traceroute <id> --host <target>   # 路由追踪，定位断点
incloud device exec speedtest-config <id>              # 查看可用接口和测速节点
incloud device exec speedtest <id>                    # 速度测试，确认带宽
incloud device exec speedtest-history <id>            # 历史速度测试记录
incloud device datausage <id>                         # 数据用量，是否超限
```

诊断思路：
- ping 不通：检查路由、防火墙、DNS
- ping 通但延迟高：检查链路质量、带宽利用率
- traceroute 中间断：定位网络断点位置
- 速度慢：对比历史速度测试，确认是否劣化
- 以上手段未定位原因时，查日志寻找具体错误信息（**加载 `references/log-analysis.md`** 获取模块分类和关键词）：

```bash
incloud device log syslog <id> --fetch --keywords error     # 设备系统日志（网络/VPN/WiFi/DNS 等模块），实时采集并按关键词过滤
incloud device log syslog <id> --after T1 --before T2      # 查历史系统日志（--after/--before 必填）
incloud device log mqtt <id>                                # 设备与平台的 MQTT 通信记录（连接/断开/消息收发）
```

## 抓包与流量分析

```bash
incloud device exec interfaces <id>                  # 列出可用网络接口
incloud device exec capture <id> --interface <iface>  # 启动抓包（流式输出，支持 --download 保存 pcap）
incloud device exec cancel <id>                       # 取消运行中的任务
incloud device exec flowscan <id>                     # 启动流量扫描
incloud device exec flowscan-status <id>              # 查看流量扫描状态
```

## 配置管理

```bash
incloud device config get <id>                           # 查看当前配置
incloud device config update <id> --payload '{"key":"val"}' # 更新配置
incloud device config copy --source <id> --target <id>   # 复制配置到其他设备（支持多个 --target）
incloud device config snapshots list <id>                # 查看配置变更历史
incloud device config snapshots get <id> <snapshot-id>   # 查看某次快照详情
incloud device config snapshots diff <id> <snap1> <snap2> # 对比两个快照差异
incloud device config snapshots restore <id> <snapshot>  # 回滚到历史配置
incloud device config error <id>                         # 查看配置下发错误
incloud device config abort <id>                         # 终止待下发的配置
```

配置操作注意事项：
- 更新前先 `config get` 查看当前配置，了解现有值
- 需要构造配置 JSON 时，先用 `config schema get` 获取 JSON Schema 定义，再用 `config schema validate` 校验。详见 `references/ai-config-workflow.md`
- 复杂配置变更建议先在单台设备测试，确认无误后再用 `config copy` 批量下发
- 配置回滚前先查看快照详情，确认要恢复的版本
- 下发失败时用 `config error` 查看具体错误原因

## 固件升级

```bash
incloud firmware list --search "<model>"             # 按型号查找可用固件
incloud firmware get <firmware-id>                   # 查看固件详情
incloud device group firmwares <group-id>            # 查看分组内固件版本分布
incloud firmware job create --firmware <id> ...      # 创建 OTA 升级任务
incloud firmware job list                            # 查看升级任务列表
incloud firmware job executions <job-id>             # 查看升级执行进度
incloud firmware job cancel <job-id>                 # 取消升级任务
incloud firmware status --firmware <id>              # 查看设备升级状态
```

固件升级安全流程：
1. 用 `firmware list` 找到目标固件，确认版本号和适用型号
2. 用 `device group firmwares` 查看当前固件分布，了解升级范围
3. 明确列出受影响设备数量和版本变更（从 X.X.X 升级到 Y.Y.Y）
4. **必须获得用户明确确认后才执行**
5. 创建任务后用 `firmware job executions` 跟踪进度
6. 出现问题时用 `firmware job cancel` 及时取消

## 设备远程控制

```bash
incloud device exec reboot <id>                      # 重启设备
incloud device exec restore-defaults <id>            # 恢复出厂设置
incloud device exec method <id> <method-name>        # 调用自定义远程方法
```

**警告**：reboot 和 restore-defaults 是高危操作，执行前必须：
- 确认目标设备无误
- 告知用户操作影响（重启导致短暂离线；恢复出厂会丢失所有配置）
- 获得明确确认
