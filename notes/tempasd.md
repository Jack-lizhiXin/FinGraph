# TempASD: Temporal Anomalous Subgraph Discovery in Large-Scale Dynamic Financial Networks

Xiaolin Han et al. · KDD · Research 2025 · 核对日期 2026-11-20

| 读前先确认 | 本文设定 |
| --- | --- |
| 预测对象 | 时序子图及其成员 |
| 标签条件 | 部分数据有异常训练线索，另以统计规则生成训练候选 |
| 研究场景 | 以太坊交易、NFT 交易 |

论文使用 PlusTokenPonzi、两期以太坊交易和 Blur 四个数据集。PlusToken 实验抽取 20% 已知真值用于训练；另三个没有原生异常标签的数据集以偏离本福特定律的稠密时序子图构建训练参考。它与 RevClassify 的候选子图分类形成对照。可固定观测时长和候选数，在有独立案件标注的测试部分报告发现线索和已知成员的交并比、命中与运行时间，再比较移除金额数字特征的结果。统计偏离本身只构成调查线索。

[正式发表记录](https://doi.org/10.1145/3711896.3737149) · [核对原文](https://doi.org/10.1145/3711896.3737149) · [作者资源](https://github.com/KZ-code/TempASD)

论文实验由原作者报告。上述 FinGraph 试验是待验证的研究问题。
