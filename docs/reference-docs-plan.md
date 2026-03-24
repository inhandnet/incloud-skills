# 场景化参考文档规划

## 背景

现有 3 个参考文档（diagnostics.md、signal-analysis.md、log-analysis.md）都是单设备、单技术视角。MSP 网管的日常工作是场景驱动的，需要知道如何把多个 CLI 命令串联成工作流。

LLM 本身具备网络运维通用知识，缺的是**如何用 incloud CLI 落地**。新文档定位：补充 CLI 集成的操作模式和工作流思路，不是死板流程。

## 现有文档已覆盖

| 文档 | 覆盖内容 |
|------|---------|
| diagnostics.md | 单设备离线排查、网络诊断、抓包、配置管理、固件升级、远程控制 |
| signal-analysis.md | 蜂窝信号质量评估标准和分析方法 |
| log-analysis.md | 日志模块分类、问题映射、分析方法 |

## 新增文档规划（7 个）

### 1. fleet-inspection.md — 批量巡检与健康评估

**覆盖场景**：批量离线告警、VIP 客户巡检、容量规划

**典型触发**：早上到工位看到一批告警；按 SLA 对 VIP 客户做主动巡检；客户反馈门店 Wi-Fi 越来越卡需要评估。

**核心内容**：
- 使用 `--search`、设备分组按客户/区域批量筛选设备
- 批量识别离线设备、信号边缘设备、资源紧张设备的命令组合
- 固件版本分布检查（`device group firmwares`）
- 流量使用趋势分析（`datausage`）
- 告警汇总与导出（`alert list/export` + 时间过滤）
- 容量评估的数据采集思路（perf + client + datausage 交叉分析）

**为什么需要**：LLM 不知道 incloud CLI 的分页、搜索、分组过滤的具体用法，也不知道哪些命令支持批量查询。

---

### 2. device-onboarding.md — 设备开通与批量配置

**覆盖场景**：新门店开通

**典型触发**：客户新开门店，设备已寄到，需要在平台录入并做好配置下发。

**核心内容**：
- 设备导入流程（`device import`）
- 分组分配（`device assign`）
- 配置模板复制（`device config copy`）
- 告警规则创建（`alert rule create`）
- 开通后验证清单（在线状态、配置下发状态、告警规则生效）

**为什么需要**：开通是多步骤流程，命令之间有依赖顺序（先导入→再分组→再下发配置），LLM 不知道这个编排逻辑。

---

### 3. traffic-security.md — 异常流量与安全排查

**覆盖场景**：异常流量排查

**典型触发**：监控发现某门店路由器数据用量突然暴增，平时日均 500MB 昨天跑了 15GB。

**核心内容**：
- 数据用量趋势分析（`datausage` + 时间对比）
- 终端设备排查（`device client`）
- 流量扫描（`device exec flowscan`）
- Wi-Fi 配置审计思路（config get 检查 SSID/密码强度）
- 配置变更审计（`activity list` 查看操作记录）

**为什么需要**：流量异常排查是推理链条，需要按 datausage→client→flowscan 逐步缩小范围，LLM 不知道这个排查路径。

---

### 4. sdwan-operations.md — SD-WAN 与链路冗余运维

**覆盖场景**：SD-WAN 隧道中断、主备链路切换验证

**典型触发**：客户报告门店内网 ERP 访问不了总部；按季度要求验证主备链路故障转移能力。

**核心内容**：
- SD-WAN 网络和隧道状态查看
- 隧道故障排查思路（设备在线→隧道状态→链路质量→日志）
- 上行链路监控（`device uplink`）
- 主备链路状态判断和切换验证方法
- InCloud Connector 基本运维

**为什么需要**：SD-WAN 和 Connector 的命令结构复杂（多层子命令），排查需要跨多个资源（device + sdwan + uplink），LLM 不知道这些命令之间的关联。

---

### 5. device-lifecycle.md — 设备迁移与生命周期管理

**覆盖场景**：客户合并、设备迁移

**典型触发**：两个客户合并，需要把一方的设备全部迁移到另一方的组织下并统一配置。

**核心内容**：
- 跨组织设备迁移（`device transfer`）
- 批量重新分组（`device unassign` + `device assign`）
- 配置差异对比思路（两台设备分别 config get 后对比）
- 批量配置统一（`device config copy`）
- 迁移前后的验证清单

**为什么需要**：迁移是高风险的批量写操作，需要明确的前置检查和后置验证，LLM 需要知道安全操作的编排顺序。

---

### 6. oobm-recovery.md — 带外管理与远程恢复

**覆盖场景**：带外救砖

**典型触发**：设备因配置下发错误导致 WAN 口不通，平台上显示离线，但支持 OOBM 且 SIM 卡有信号。

**核心内容**：
- OOBM 的适用场景（设备离线但 SIM 卡仍有信号）
- 建立带外连接（`oobm create/connect`）
- 通过带外通道诊断和恢复配置
- 串口管理（`oobm serial`）
- 连接清理（`oobm close`）

**为什么需要**：OOBM 是独立的管理通道，使用模式与常规操作完全不同，LLM 如果不知道这个能力就不会在设备离线时推荐它。

---

### 7. reporting.md — 数据导出与运维报表

**覆盖场景**：月度报表

**典型触发**：月底需要给客户出月度网络运维报告，包括告警统计、在线率、流量使用等。

**核心内容**：
- 告警数据导出（`alert export` + 时间范围过滤）
- 设备在线历史数据采集（`device online` 批量查询）
- 流量使用数据汇总（`datausage` + 时间对比）
- 固件版本分布统计（`device group firmwares`）
- 活动日志导出（`activity list` + 时间过滤）
- 数据聚合与报表生成思路（CLI 输出 JSON → 后处理）

**为什么需要**：报表需要跨多种资源类型汇总数据，LLM 不知道哪些命令支持时间过滤和导出，也不知道如何组合这些数据。

---

## 文档风格

每个文档包含：
- **场景描述**（开头 2-3 句话）：典型触发场景，帮 LLM 判断何时参考此文档
- **关键命令**：核心 CLI 命令和参数（代码块）
- **操作思路**：灵活的操作思路，要点列表，不是死板步骤
- **注意事项**：安全提醒、常见坑（如有）

风格定位："工具箱 + 思路指引"，不是 step-by-step 流程图。

## 需要修改的文件

| 文件 | 操作 |
|------|------|
| `skills/incloud/references/fleet-inspection.md` | 新增 |
| `skills/incloud/references/device-onboarding.md` | 新增 |
| `skills/incloud/references/traffic-security.md` | 新增 |
| `skills/incloud/references/sdwan-operations.md` | 新增 |
| `skills/incloud/references/device-lifecycle.md` | 新增 |
| `skills/incloud/references/oobm-recovery.md` | 新增 |
| `skills/incloud/references/reporting.md` | 新增 |
| `skills/incloud/SKILL.md` | 更新底部"诊断与分析参考"章节，添加新文档引用 |

## 完成后的参考文档全景

| 文档 | 定位 |
|------|------|
| diagnostics.md | 单设备故障排查与操作（已有） |
| signal-analysis.md | 信号质量评估（已有） |
| log-analysis.md | 日志分析（已有） |
| fleet-inspection.md | 批量巡检与健康评估（新增） |
| device-onboarding.md | 设备开通与配置（新增） |
| traffic-security.md | 异常流量与安全（新增） |
| sdwan-operations.md | SD-WAN 与链路冗余（新增） |
| device-lifecycle.md | 设备迁移与生命周期（新增） |
| oobm-recovery.md | 带外管理与恢复（新增） |
| reporting.md | 数据导出与报表（新增） |
