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
