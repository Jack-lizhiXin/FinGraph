# 精读卡

写卡时请说明论文用什么证据支持结论、与库里哪项工作可比，以及下一步可以用哪个最小实验来验证。新增阅读卡建议以书目 ID 命名。同一论文有多份笔记时，在主卡中链接其余笔记。

复制[精读卡模板](../templates/paper-note.md)，完成后在[结构化书目](../catalog/papers.json)的 `reading` 字段登记路径。[论文索引](../catalog/README.md)会在相应条目旁显示“精读卡”。


**本期重点精读：** [MimbFD](mimbfd-2025.md)（少量双类标签）、[CGNN](cgnn-2025.md)（极少标签）、[UNPrompt](unprompt-2025.md)（跨图零样本）、[Grad](grad-2025.md)（关系增强）、[DyGADBench](dygadbench-2026.md)（动态图评测）、[TransXion](transxion-2026.md)（金融交易边）、[IBM AMLWorld](ibm-amlworld.md)（合成数据与许可）。每张均区分“论文叙述”与“团队未复现”。

### 启动包精读卡

| 研究问题 | 对应笔记 |
| --- | --- |
| 欺诈节点如何使用邻域信息 | [SEC-GFD](sec-gfd.md) · [DCL-GFD](dcl-gfd.md) · [NAAST-GNN](naast-gnn.md) · [MimbFD 实验表笔记](mimbfd.md) |
| 源图和目标图分别提供什么监督 | [AnomalyGFM](anomalygfm.md) |
| 如何给候选子图、动态节点和边打分 | [BAG](bag-dynamic.md) · [UB-GOLD](ub-gold.md) · [TempASD](tempasd.md) · [ARES](ares-edge-stream.md) |
| 多笔交易如何帮助识别账户 | [DIAM](diam.md) |

两包共有的 [CR-Aug 精读卡](cr-aug.md) 对应仅正常标签条件下的节点识别。共计 18 份阅读卡覆盖 17 篇论文，MimbFD 有两份互相链接的笔记。
