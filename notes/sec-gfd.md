# Revisiting Graph-Based Fraud Detection in Sight of Heterophily and Spectrum

Fan Xu, Nan Wang, Hao Wu, Xuezhi Wen, Xibin Zhao and Hai Wan · AAAI · Technical Track 2024 · 核对日期 2026-11-20

| 读前先确认 | 本文设定 |
| --- | --- |
| 预测对象 | 节点（按数据集区分账户、用户或评论） |
| 标签条件 | 双类节点标签，训练图中有未标注节点；作者称半监督 |
| 研究场景 | 评论、社交及金融账户图 |

作者以已有正常和异常节点共同训练分类器。真实邻域特征与属性近邻特征用于构造局部约束，对正常和异常施加不同假设。表 1 列出 Amazon、YelpChi、T-Finance、T-Social。宜与 BWGNN 在相同双类标签和邻域可见范围下比较；若要转到仅正常标签实验，需另设计局部约束并重跑。

[正式发表记录](https://doi.org/10.1609/aaai.v38i8.28773) · [核对原文](https://ojs.aaai.org/index.php/AAAI/article/download/28773/29483)

论文实验由原作者报告。上述 FinGraph 试验是待验证的研究问题。
