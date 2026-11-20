# ARES: Anomaly Recognition Model For Edge Streams

Simone Mungari et al. · KDD · Research 2026 · 核对日期 2026-11-20

| 读前先确认 | 本文设定 |
| --- | --- |
| 预测对象 | 按到达时间评分的边 |
| 标签条件 | 无监督训练，验证和测试用途单列 |
| 研究场景 | 一般事件流，另有比特币信任网络 |

作者区分固定表示和随时间更新的设置，在附录的 Bitcoin Alpha、Bitcoin OTC 信任网络上，更新版本的 AP 表现随数据集而变。FinGraph 可在 TransXion 按交易到达时间先打分后更新，固定预热段与更新频率，将静态及滚动版本与滚动计数基线比较。按时间段报告 AP、告警前 K 命中和单边耗时，另列预热成本；这些指标在合成交易上体现的是模拟器所提供的异常真值。

[正式发表记录](https://doi.org/10.1145/3770854.3780242) · [核对原文](https://doi.org/10.1145/3770854.3780242) · [作者资源](https://github.com/AnomalyRecognitionModelForEdgeStreams/ARES)

论文实验由原作者报告。上述 FinGraph 试验是待验证的研究问题。
