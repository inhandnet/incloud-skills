# 设备日志分析参考

## 日志查看命令

```bash
incloud device log syslog <id>        # 设备系统日志（网络/VPN/WiFi/DNS 等各模块，来自设备侧）
incloud device log mqtt <id>          # 设备与平台的 MQTT 通信记录（连接/断开/消息收发，来自平台侧）
incloud device log diagnostic <id>    # 下载诊断日志包（输出 .tar.gz 文件；--file 指定路径，否则写临时文件）
```

**先下载再分析**：日志拉取一次保存到本地文件，后续在文件中搜索和分析，避免反复请求服务端。

## 日志模块分类

### network 模块
| 日志源 | 说明 |
|--------|------|
| ih-qmi1 | 4G/5G 调制解调器通信日志 |
| redial | 拨号重连日志 |
| udhcpc | DHCP 客户端日志 |
| interface | 网络接口状态日志 |
| sdwan | SD-WAN 相关日志 |
| ih_route | 路由表变化日志 |
| lqm | 链路质量监控日志 |
| ip_passthrough | IP 透传日志 |

### connect_platform 模块
| 日志源 | 说明 |
|--------|------|
| NetworkManager | 网络连接管理日志 |
| ngrokc | 内网穿透客户端日志 |
| redial | 连接重试日志 |

### wifi 模块
| 日志源 | 说明 |
|--------|------|
| dot11d | 无线射频管理日志 |
| hostapd | WiFi 热点服务日志 |
| events | WiFi 事件日志 |

### statistics 模块
| 日志源 | 说明 |
|--------|------|
| ih_record | 设备运行记录 |
| events | 系统事件日志 |
| trafficd | 流量统计日志 |

### client 模块
| 日志源 | 说明 |
|--------|------|
| dnsmasq | DNS/DHCP 服务日志 |
| ih_record | 客户端连接记录 |
| hostapd | 客户端认证日志 |
| events | 客户端事件日志 |

### VPN 模块
| 日志源 | 说明 |
|--------|------|
| ipsecwatcher3 | IPSec 连接监控 |
| charon | strongSwan IPSec 守护进程日志 |
| ih_updown | IPSec/L2TP 隧道状态变化 |
| xl2tpd | L2TP 隧道守护进程日志 |
| vpnd | VPN 连接守护进程日志 |
| wgwatcher | WireGuard 连接监控日志 |

## 问题类型与日志源映射

### 连接问题
| 症状 | 关注日志源 |
|------|-----------|
| 设备离线/无法连接 | ih-qmi1, redial, NetworkManager, udhcpc, interface |
| 间歇性断网 | ih-qmi1, redial, lqm, ih_route |
| 网络慢/不稳定 | lqm, trafficd, ih-qmi1 |

### WiFi 问题
| 症状 | 关注日志源 |
|------|-----------|
| WiFi 无法连接 | hostapd, dot11d, events(wifi) |
| WiFi 频繁掉线 | hostapd, events(wifi), events(client) |
| 客户端连接异常 | hostapd, dnsmasq, events(client) |

### VPN 问题
| 症状 | 关注日志源 |
|------|-----------|
| IPSec 隧道问题 | ipsecwatcher3, charon, ih_updown |
| L2TP 隧道问题 | xl2tpd, vpnd, ih_updown |
| WireGuard 问题 | wgwatcher |

### 服务问题
| 症状 | 关注日志源 |
|------|-----------|
| 远程访问异常 | ngrokc, NetworkManager |
| DNS 解析问题 | dnsmasq |
| 路由问题 | ih_route, interface |

### 综合分析
| 场景 | 关注日志源 |
|------|-----------|
| 设备异常分析 | ih_record, events(statistics), trafficd |
| 性能分析 | trafficd, lqm, ih_record |

## 时间窗口建议

| 问题类型 | 建议时间窗口 |
|---------|-------------|
| 实时/当前问题 | 1-4 小时 |
| 周期性问题 | 8-24 小时 |
| 历史问题追溯 | 24-72 小时 |
| 深度分析 | 72-168 小时 |

## 日志分析方法

### 分析流程

1. **确定问题类型**：根据用户描述判断属于哪类问题
2. **选择日志源**：按照映射表确定需要关注的日志模块
3. **确定时间范围**：根据问题发生时间和类型选择合适的窗口
4. **关键信息搜索**：在日志中搜索错误关键词、状态变化、异常时间点
5. **关联分析**：将日志事件与用户描述的症状关联，定位根因

### 常见日志关键词

- 连接类：`disconnect`, `reconnect`, `timeout`, `failed`, `retry`
- 信号类：`signal lost`, `no service`, `registration`, `attach`
- VPN 类：`tunnel down`, `negotiation failed`, `authentication`, `SA expired`
- WiFi 类：`deauthentication`, `disassociation`, `association failed`
- 系统类：`OOM`, `crash`, `reboot`, `watchdog`

### 特殊情况处理

- 用户提到不完整的日期时（只有月日没有年份），选择距离当前时间最近的符合条件的日期
- 严重问题包含 DEBUG 级别日志以获取更多细节
- 性能问题重点关注统计类日志（ih_record, trafficd）
- 问题描述模糊时，选择核心监控日志源（ih-qmi1, redial, events）先做初步分析
