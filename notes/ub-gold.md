# Unifying Unsupervised Graph-Level Anomaly Detection and Out-of-Distribution Detection: A Benchmark

Yili Wang et al. · ICLR 2025 · 核对日期 2026-11-20

| 读前先确认 | 本文设定 |
| --- | --- |
| 预测对象 | 候选整图 |
| 标签条件 | 无监督图级检测，异常评估标签与分布来源取决于场景 |
| 研究场景 | 分子、社交等通用图集合 |

论文把自然语义异常、由类别指定的异常、跨数据集偏移及数据集内偏移分成四种任务。每个待排对象都是一张已经构造的图。在金融迁移中，可固定一批有独立标签的候选团伙子图，先在相同数据源做图级排序，再切换到按另一种方式采样的候选。两组各自报告标签比例和结构分布，同时保留简单图统计基线。给候选排序的 AP 不能代替从整张图发现候选时的召回率。

[正式发表记录](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e58fa42d4b7a798eef8d0d75098f87ad-Abstract-Conference.html) · [核对原文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e58fa42d4b7a798eef8d0d75098f87ad-Abstract-Conference.html) · [作者资源](https://github.com/UB-GOLD/UB-GOLD)

论文实验由原作者报告。上述 FinGraph 试验是待验证的研究问题。
