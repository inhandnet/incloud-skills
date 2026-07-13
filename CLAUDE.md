# incloud-skills 开发约定

## references/commands/ 是自动生成的

由 incloud-cli 的 `make docs` 生成（`cmd/docgen/main.go`），**不要手动编辑**。

CLI 命令变更后，在 incloud-cli 目录运行 `make docs` 重新生成，再提交到 incloud-skills。

## 发版流程

打新版本时**必须**同步更新 `.claude-plugin/plugin.json` 的 `version` 字段——这是 Claude Code 插件识别版本的地方，容易漏掉。

标准流程：
1. 更新 `.claude-plugin/plugin.json` 的 `version`
2. 更新 `CHANGELOG.md`（顶部新增版本段）
3. `chore: bump version to x.y.z` 单独提交
4. 打 tag `vx.y.z` 并推送
