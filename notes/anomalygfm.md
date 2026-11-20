# AnomalyGFM: Graph Foundation Model for Zero/Few-shot Anomaly Detection

Hezhe Qiao, Chaoxi Niu, Ling Chen and Guansong Pang · KDD 2025 · 核对日期 2026-11-20

| 读前先确认 | 本文设定 |
| --- | --- |
| 预测对象 | 节点 |
| 标签条件 | 源图含正常和异常标签；目标图零标签或仅少量正常标签 |
| 研究场景 | 跨评论、金融、社交等属性图 |

原文在 11 个图数据集上研究跨图检测。与 GGAD、CR-Aug 比较时，要同时报告源图预训练监督、目标图正常标签数和目标图结构何时可见。可固定预训练权重与目标测试节点，单独估计新增正常标签的收益。

[正式发表记录](https://doi.org/10.1145/3711896.3736843) · [核对原文](https://arxiv.org/html/2502.09254v1) · [作者资源](https://github.com/mala-lab/AnomalyGFM)

论文实验由原作者报告。上述 FinGraph 试验是待验证的研究问题。
