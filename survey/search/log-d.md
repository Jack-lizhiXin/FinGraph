# 静态图异常、监督条件与可比性检索日志

检索日为 2026-11-20。本文记录定向扩展的实际查询，覆盖 2022–2026 正式出版年（截至检索日）。目标是补足动态图综述中的静态对照、跨图迁移、金融节点标签协议和多粒度评测，方便与按时间回放的模型分组比较。

## 检索与核对

通过检索引擎检索 NeurIPS、ICLR、IJCAI、AAAI、PMLR、Springer 和 ScienceDirect 的会议或期刊页面，ACM 论文另用作者大学主页、作者稿、公开代码的正式出版记录交叉核对。代表性实际查询如下。

- `unsupervised graph anomaly detection Graph anomaly detection NeurIPS 2024 2025 ICML 2024 graph anomaly detection one-class graph contrastive TAM affinity details`
- `site:proceedings.neurips.cc graph anomaly detection 2022 2023 graph level graph anomalous SIGNET GLocalKD graph-level anomaly detection detector remove reference`
- `graph fraud detector 2023 2024 CIKM KDD adaptive attention fraud group imbalance GraphENS GraphSMOTE DGA-GNN fraud detection authors doi`
- `site:arxiv.org graph anomaly detection AnomalyDAE AAGNN Anomaly Detection on Attributed Networks GUIDE ComGA Graph anomaly detection 2022 2023 2024 ADA-GAD VGOD NLGAD GAD-NR`
- `GAGA Group Aggregation fraud detection label propagation 2023 authors doi`
- `"ComGA: Community-Aware" 10.1145 2022 WSDM`
- `"Contrastive Attributed Network Anomaly Detection" Springer 2022 DOI Xu`

期刊题名另行追加 `authors DOI first author` 检索。对 TAM、SIGNET、UniGAD、SpaceGNN、ARC 回看正式会议版 PDF，对 GAD-NR 回看作者存档全文，核查方法、数据、标签构造、指标及具体表格，定位记录在对应精读卡；其余条目按实际核查深度记录。检索没有保存平台全部结果的分页快照，故不给出原始命中数或系统检索召回率。

## 入选与排除

保留有一手学术来源、可辨认研究对象与方法、能说明动态图金融告警一个具体对照条件的论文，通用图和金融基准分开说明。按标题、标识符与历史目录核对重复。发表年份按会议或正式卷期，预印本以及会议对同一作品的摘要重印合并处理。

例如，Xu Yuan 等的 *Higher-order Structure Based Anomaly Detection on Attributed Networks* 虽在 2024 年上传 arXiv，作者标注 IEEE BigData 2021，未计入近五年。Li 等关于真正无监督调参的 2025 年期刊论文，及 AAAI 2026 的摘要重印，只计期刊论文一项。[作者稿及会议归属](https://arxiv.org/abs/2406.04690) · [期刊论文](https://doi.org/10.1007/s10618-025-01115-5) · [AAAI 摘要重印](https://ojs.aaai.org/index.php/AAAI/article/download/41387/45348)
