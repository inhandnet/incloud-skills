# incloud-skills 开发约定

## CLI 参数签名

CLI 的 flag 和子命令签名以运行中的 `incloud` 二进制为准，跑 `--help` 查。仓库里只维护 `skills/incloud/SKILL.md` 速查区的命令名，让 agent 一次搜索就能定位到命令。

CLI 新增或改名命令组后，同步更新速查区。

## 发版流程

打新版本时**必须**同步更新 `.claude-plugin/plugin.json` 的 `version` 字段——这是 Claude Code 插件识别版本的地方，容易漏掉。

标准流程：
1. 更新 `.claude-plugin/plugin.json` 的 `version`
2. 更新 `CHANGELOG.md`（顶部新增版本段）
3. `chore: bump version to x.y.z` 单独提交
4. 打 tag `vx.y.z` 并推送
