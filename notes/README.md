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

两包共有的 [CR-Aug 精读卡](cr-aug.md) 对应仅正常标签条件下的节点识别。启动包与专题包合并时共计 18 份阅读卡覆盖 17 篇论文，MimbFD 有两份互相链接的笔记。

## 动态图综述补充精读

| 论文 | 中文阅读卡 |
| --- | --- |
| Sketch-Based Anomaly Detection in Streaming Graphs | [原文位置、结果与限制](anograph-sketch.md) |
| Unsupervised Anomaly Detection in Dynamic Graphs via Compatibility Modeling and Boundary Learning | [原文位置、结果与限制](bad-dynamic.md) |
| DP-DGAD: A Generalist Dynamic Graph Anomaly Detector with Dynamic Prototypes | [原文位置、结果与限制](dp-dgad.md) |
| A Generalizable Anomaly Detection Method in Dynamic Graphs | [原文位置、结果与限制](generaldyg.md) |
| SAD: Semi-Supervised Anomaly Detection on Dynamic Graphs | [原文位置、结果与限制](sad-dynamic.md) |
| Graph similarity learning for change-point detection in dynamic networks | [原文位置、结果与限制](siamese-network-cp.md) |
| Spade: A Real-Time Fraud Detection Framework on Evolving Graphs | [原文位置、结果与限制](spade.md) |
| BRIGHT - Graph Neural Networks in Real-time Fraud Detection | [原文位置、结果与限制](bright-cikm.md) |
| FraudGT: A Simple, Effective, and Efficient Graph Transformer for Financial Fraud Detection | [原文位置、结果与限制](fraudgt.md) |
| LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering | [原文位置、结果与限制](laundrograph.md) |
| MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions | [原文位置、结果与限制](mad-cash.md) |
| Environment-Aware Dynamic Graph Learning for Out-of-Distribution Generalization | [原文位置、结果与限制](eagle-2023.md) |
| Towards Better Evaluation for Dynamic Link Prediction | [原文位置、结果与限制](edgebank-2022.md) |
| Temporal Graph Benchmark for Machine Learning on Temporal Graphs | [原文位置、结果与限制](tgb-2023.md) |
| TGB-Seq Benchmark: Challenging Temporal GNNs with Complex Sequential Dynamics | [原文位置、结果与限制](tgbseq-2025.md) |
| ARC: A Generalist Graph Anomaly Detector with In-Context Learning | [原文位置、结果与限制](arc-2024.md) |
| GAD-NR: Graph Anomaly Detection via Neighborhood Reconstruction | [原文位置、结果与限制](gad-nr-2024.md) |
| Towards Self-Interpretable Graph-Level Anomaly Detection | [原文位置、结果与限制](signet-2023.md) |
| SpaceGNN: Multi-Space Graph Neural Network for Node Anomaly Detection with Extremely Limited Labels | [原文位置、结果与限制](spacegnn-2025.md) |
| Truncated Affinity Maximization: One-class Homophily Modeling for Graph Anomaly Detection | [原文位置、结果与限制](tam-2023.md) |
| UniGAD: Unifying Multi-level Graph Anomaly Detection | [原文位置、结果与限制](unigad-2024.md) |
| Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics | [原文位置、结果与限制](elliptic-pp-2023.md) |
| Revisiting Elliptic++ for Bitcoin Forensics: Feature Reconstruction and Leakage-Resistant Evaluation | [原文位置、结果与限制](elliptic-pp-audit-2026.md) |
| FiGraph: A Dynamic Heterogeneous Graph Dataset for Financial Anomaly Detection | [原文位置、结果与限制](figraph-2025.md) |
| FinFraudBench: A Heterogeneous Graph Benchmark for Financial Fraud Detection | [原文位置、结果与限制](finfraudbench-2026.md) |
| A labeled synthetic mobile money transaction dataset | [原文位置、结果与限制](momtsim-data-2025.md) |
| Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy | [原文位置、结果与限制](card-feedback-delay.md) |
| Towards a Rigorous Evaluation of Time-Series Anomaly Detection | [原文位置、结果与限制](rigorous-tsad.md) |
| Temporal Motif-aware Graph Test-time Adaptation for OOD Blockchain Anomaly Detection | [原文位置、结果与限制](temg-tta-2026.md) |
| VUS: effective and efficient accuracy measures for time-series anomaly detection | [原文位置、结果与限制](vus-tsad.md) |
| Graph-Based Financial Fraud Detection: A Property-Centric Survey of Static, Temporal, Cycle-Aware, and Generative Methods and Their Evaluation | [原文位置、结果与限制](slr-finprops-ale.md) |
| A systematic literature review of spatiotemporal graph and sequence learning for financial risk detection | [原文位置、结果与限制](slr-finrisk-lai.md) |
