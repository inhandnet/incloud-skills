# 知识库检索策略

使用 `incloud knowledge search` 检索。

用 Agent 工具启动 subagent，目标是找到与问题相关的文档原文片段返回给主流程。

给 subagent 的 prompt 说明以下几点（包括用户的原始问题和查询目标）：

- 用 `incloud knowledge search "<产品名/型号> <关键词>"` 检索（按关键词匹配，型号直接写进 query）；命中后用 `incloud knowledge read <chunk_id>` 读章节全文，需要看整篇文档结构时用 `incloud knowledge browse "<文档路径>"`
- 结果不理想时自行调整关键词、拆分查询、去掉型号改用产品名等，直到找到相关内容或确认知识库确实没有（`status: empty`）
- 回答时附上来源章节的 `url`，方便用户点击查看原文
- 知识库无结果时 fallback 到网络搜索，优先 inhandnetworks.com / inhandcloud.com，标注来源
- 返回原文片段，不摘要不改写
