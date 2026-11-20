# Mitigating Message Imbalance in Fraud Detection with Dual-View Graph Representation Learning

Yudan Song et al. · IJCAI 2025 · 核对日期 2026-11-20

| 读前先确认 | 本文设定 |
| --- | --- |
| 预测对象 | 节点 |
| 标签条件 | 双类标注节点提供监督信息，图上还含未标注节点 |
| 研究场景 | 多关系评论及欺诈图 |

表 1 在 Amazon、YelpChi、Comp 比较 AUC、召回和 F1，另在 Amazon 调整欺诈与正常样本的比例。FinGraph 可按节点距已标异常的距离分层，在各层固定告警预算，观察同一方法是否主要改善了接近已知欺诈的群体。

[正式发表记录](https://doi.org/10.24963/ijcai.2025/365) · [核对原文](https://ijcai.org/proceedings/2025/0365.pdf)

论文实验由原作者报告。上述 FinGraph 试验是待验证的研究问题。

专题增补包另有一份[标签条件与建议对照实验笔记](mimbfd-2025.md)。
