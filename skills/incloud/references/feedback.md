# InCloud Skill 反馈

当用户在使用 incloud skill 过程中发现问题（命令示例过时、评级标准不准、流程缺失、文档错误等），引导收集结构化反馈并通过 `incloud feedback create` 提交。

## 反馈收集流程

### 1. 自动采集环境信息

无需询问用户，直接执行以下命令收集：

```bash
incloud --version          # CLI 版本
incloud config current-context  # 当前环境
```

### 2. 从会话上下文预提取

回顾当前会话，自动提取：
- 涉及的 skill 或 reference 文件（如 `signal-analysis.md`、`diagnostics.md`）
- AI 读取了哪些文档、基于什么逻辑做出的判断（便于定位文档问题）
- AI 给出的错误建议或不准确的输出
- 用户执行过的相关命令及其实际输出

### 3. 引导用户补充

逐步确认以下信息（已从上下文提取到的直接展示让用户确认，无需重复问）：

1. **哪里不对**：具体是哪个文档/哪段内容有问题
2. **实际发生了什么**：AI 给出了什么错误的建议或结果
3. **期望行为**：正确的做法应该是什么
4. **如何复现**：触发问题的操作步骤（可选，但对排查很有帮助）

### 4. 组装并提交

将收集的信息组装为结构化文本，写入临时文件后提交：

```bash
cat > /tmp/feedback.md << 'EOF'
[incloud-skill][signal-analysis.md] SINR 评级标准与实际输出不一致

环境：dev (nezha.inhand.dev) | CLI v0.4.1 | skill v0.2.0

问题：SINR=1dB 被描述为"极差"，但评级表定义 0~10 为"一般"
涉及文件：references/signal-analysis.md
AI 推理过程：读取 signal-analysis.md 中的评级表，将 SINR=1 匹配到 <0 的"极差"区间（误读了边界值）
实际行为：AI 输出"信号极差"
期望行为：应按评级表输出"一般"
复现步骤：查询任意设备信号，当 SINR 在 0~10 范围内时触发
EOF

incloud feedback create --content @/tmp/feedback.md --file screenshot.png
```

`--type` 根据内容选择（默认 `issue`）：
- `issue` — 文档错误、命令示例不对
- `suggestion` — 流程改进建议、缺失内容

## 注意事项

- content 首行必须加 `[incloud-skill]` 前缀，便于后台按来源筛选（如 `[incloud-skill][文件名] 问题概述`）
- 环境信息行格式：`环境：<context> (<host>) | CLI <version> | skill <version>`，由 AI 自动填充，不要让用户手动填
- `--content` 优先使用文件形式（`--content @/tmp/feedback.md`），inline 字符串在内容含引号、换行等特殊字符时易被 shell 截断
- `--content` 上限 1000 字，用于简要描述问题。完整会话记录、长日志等大内容保存为文件通过 `--file` 作为附件上传（单个附件上限 20MB，最多 10 个）
- 反馈内容用中文，命令和技术术语保持原样
- 不要在反馈中包含用户的认证信息、token 或敏感数据
