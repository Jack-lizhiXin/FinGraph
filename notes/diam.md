# Effective Illicit Account Detection on Large Cryptocurrency MultiGraphs

Zhihao Ding et al. · CIKM 2024 · 核对日期 2026-11-20

| 读前先确认 | 本文设定 |
| --- | --- |
| 预测对象 | 账户地址节点 |
| 标签条件 | 已标正常与风险地址参与监督；其余地址未标注 |
| 研究场景 | 以太坊、比特币交易 |

作者对 Ethereum-S/P 与 Bitcoin-M/L 四个图评估。以太坊的风险地址来自钓鱼标记，比特币部分以赌博、混币等服务类型构造风险类别；账上每一笔交易的性质仍需另证。FinGraph 可固定测试账户和训练标签，对照有向交易序列、仅汇总笔数金额、打乱同一账户对内顺序三种输入，以 AP 和前 K 命中衡量重复边及时序是否贡献新增信息。与 Multi-GNN 对照时先对齐账户级输出。

[正式发表记录](https://doi.org/10.1145/3627673.3679707) · [核对原文](https://doi.org/10.1145/3627673.3679707) · [作者资源](https://github.com/TommyDzh/DIAM)

论文实验由原作者报告。上述 FinGraph 试验是待验证的研究问题。
