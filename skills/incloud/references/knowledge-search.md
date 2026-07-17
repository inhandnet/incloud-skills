# 知识库检索策略

使用 `incloud knowledge search` 检索。

用 Agent 工具启动 subagent，目标是找到与问题相关的文档原文片段返回给主流程。

给 subagent 的 prompt 说明以下几点（包括用户的原始问题和查询目标）：

- 用 `incloud knowledge search <query> --rewrite` 检索，涉及特定型号时加 `--model <model>`
- 结果不理想时自行调整关键词、拆分查询、放宽型号限制等，直到找到相关内容或确认知识库确实没有
- 知识库无结果时 fallback 到网络搜索，优先 inhandnetworks.com / inhandcloud.com，标注来源
- 返回原文片段，不摘要不改写
