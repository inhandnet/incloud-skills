# v0.5.0 (2026-07-15)

## 新功能
- **POS Ready 管理** — 新增 `pos` 命令组（clients/forwarded/device-hits/marked-clients/vendor-hits/vendor-summary/client-types 及 rules get/set/list），覆盖 POS 优先级查询、命中观测和自定义规则管理
- **POS 管理主题指南** — 新增 `references/pos-management.md`，说明 priority/default/bypass 三态含义、典型问法映射和 custom-rules 用法

## 改进
- **POS 触发词** — SKILL.md frontmatter 增加 POS 相关意图触发词，命令速查表新增 POS Ready 段
- **set-pos-ready 改造** — `device client set-pos-ready` 改用 `--level priority|default|bypass`（针对 client-id），对齐平台新的三级优先级模型

---

# v0.4.0 (2026-04-15)

## 新功能
- **知识库子代理搜索** — 新增通过 subagent 搜索知识库的能力

## 改进
- **Log local 命令文档** — 新增 `incloud device log local` 实时读取设备本地日志的用法说明、与 syslog 的场景对比和时间窗口建议
- **目录结构规范** — 将 `commands/` 移至 `references/commands/`，符合 skill 结构约定

## 其他
- 新增项目 `CLAUDE.md`，说明 `references/commands/` 为自动生成、发版需同步 `plugin.json`

---

# v0.3.0 (2026-04-01)

## 新功能
- **License 管理** — 新增完整的 license 管理命令参考（attach/detach/transfer/upgrade/align-expiry 等）

## 改进
- **README 重写** — 新增功能概览、多平台安装说明（CLI/Desktop/Web/IDE/Codex）、团队安装、故障排除等
- **Prerequisites 简化** — CLI 无需预装，skill 会自动引导安装和登录；也支持手动安装
- **Feedback 增强** — 自动采集 CLI 版本和环境信息，新增 AI 推理追踪和复现步骤模板
- **License 文档修正** — 同步 CLI 最新的 `--expand` 字段修复（order/license/history）

---

# v0.2.1 (2026-03-30)

## 改进
- **命令参考文档** — 新增 `commands/` 目录，包含完整的 CLI 命令参考，并整合到 skill 工作流中
- **`--jq` 用法说明** — 重构 `--jq` 选项说明，新增 `.total` 计数示例，更易理解

---

# v0.2.0 (2026-03-27)

## ✨ New Features

- **Device Tunnel Reference**: CLI tunnel reference with expect script for automated connections
- **Offline Diagnostics**: Offline diagnostic fallback path for device troubleshooting

## 🔧 Improvements

- Expanded CLI command coverage: tunnel, webhook, asset, overview subcommands, client expansion
- Strengthened parameter validation rules and added key flags to command cheatsheet
- Improved timezone handling guidance for time fields and CLI params
- Added download-first principle for syslog analysis workflow
- Added ID field disambiguation to prevent `_id`/`oid` confusion
- Restructured skill identity and capability description
