---
name: incloud-feedback
description: >-
  Use when the user wants to report a problem with incloud skill documentation,
  such as "帮我反馈", "这个不对", "skill 有问题", "命令示例不对", "文档需要更新",
  "怎么反馈", "report skill issue", or when the user encounters incorrect guidance
  from the incloud skill and wants to let the maintainer know.
version: 0.1.0
---

# InCloud Skill 反馈

当用户在使用 incloud skill 过程中发现问题（命令示例过时、评级标准不准、流程缺失、文档错误等），通过本 skill 引导收集结构化反馈并提交到 GitHub。

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

### 3. 组装 Issue 内容

```markdown
## 问题描述

{用户描述的问题}

## 涉及的 Skill 文件

{skill 或 reference 文件名}

## 实际行为

{AI 给出的错误建议，包含相关命令和输出}

## 期望行为

{用户认为正确的做法}

## 会话上下文

{相关的会话片段，帮助维护者复现和理解问题}
```

### 4. 提交

向用户展示组装好的 issue 内容，确认后提交：

1. **优先尝试 `gh`**：
   ```bash
   gh issue create --repo inhandnet/incloud-skills-feedback --title "<标题>" --body "<内容>"
   ```
2. **`gh` 不可用时**，生成预填 URL 让用户浏览器打开：
   ```
   https://github.com/inhandnet/incloud-skills-feedback/issues/new?title=<URL编码标题>&body=<URL编码内容>
   ```
   提示用户：「请在浏览器中打开以上链接提交反馈」

## 注意事项

- Issue 标题简洁，格式：`[文件名] 问题概述`，如 `[signal-analysis.md] SINR 评级标准与实际输出不一致`
- 会话上下文只保留与问题相关的片段，去除无关内容
- 反馈内容用中文，命令和技术术语保持原样
- 不要在 issue 中包含用户的认证信息、token 或敏感数据
