# InCloud Skill 反馈

当用户在使用 incloud skill 过程中发现问题（命令示例过时、评级标准不准、流程缺失、文档错误等），引导收集结构化反馈并通过 `incloud feedback create` 提交。

## 反馈收集流程

### 1. 从会话上下文预提取

先回顾当前会话，自动提取：
- 涉及的 skill 或 reference 文件（如 `signal-analysis.md`、`diagnostics.md`）
- AI 给出的错误建议或不准确的输出
- 用户执行过的相关命令和实际结果

### 2. 引导用户补充

逐步确认以下信息（已从上下文提取到的直接展示让用户确认，无需重复问）：

1. **哪里不对**：具体是哪个文档/哪段内容有问题
2. **实际发生了什么**：AI 给出了什么错误的建议或结果
3. **期望行为**：正确的做法应该是什么

### 3. 组装并提交

将收集的信息组装为结构化文本，写入临时文件后提交：

```bash
# 将反馈内容写入临时文件
cat > /tmp/feedback.md << 'EOF'
[signal-analysis.md] SINR 评级标准与实际输出不一致

问题：SINR=1dB 被描述为"极差"，但评级表定义 0~10 为"一般"
涉及文件：references/signal-analysis.md
实际行为：AI 输出"信号极差"
期望行为：应按评级表输出"一般"
EOF

# 提交（支持附带截图等附件）
incloud feedback create --content @/tmp/feedback.md --file screenshot.png
```

`--type` 根据内容选择（默认 `issue`）：
- `issue` — 文档错误、命令示例不对
- `suggestion` — 流程改进建议、缺失内容

## 注意事项

- `--content` 上限 1000 字，用于简要描述问题。完整会话记录、长日志等大内容保存为文件通过 `--file` 作为附件上传（单个附件上限 20MB，最多 10 个）
- 反馈内容用中文，命令和技术术语保持原样
- 不要在反馈中包含用户的认证信息、token 或敏感数据
- 内容较短时可直接用 `--content "..."` 传入，无需写文件
