# FinGraph 论文索引

共 73 篇。按主分支浏览，论文只收录一次。点英文题名进入原始来源，每篇附有选读理由。

[首页](../README.md) · [贡献说明](../CONTRIBUTING.md) · [JSON](papers.json) · [CSV](papers.csv)

## 分支导航

- **A 综述与入门**
  - [A1 图异常的定义与分类](#branch-1)（2 篇）
  - [A2 金融任务与时序图](#branch-2)（2 篇）
- **B 有监督识别**
  - [B1 类别不平衡与邻域伪装](#branch-3)（7 篇）
  - [B2 图结构信号与可解释性](#branch-4)（8 篇）
  - [B3 交易边与可疑子图](#branch-5)（4 篇）
- **C 半监督与稀缺标签**
  - [C1 少量双类标签与未标注样本](#branch-6)（6 篇）
  - [C2 仅少量可信正常标签](#branch-7)（4 篇）
  - [C3 已知异常与未标注样本](#branch-8)（1 篇）
- **D 前沿与对照方法**
  - [D1 无标签与自监督对照](#branch-9)（13 篇）
  - [D2 时间演化与未见异常](#branch-10)（7 篇）
  - [D3 预训练与少样本迁移](#branch-11)（6 篇）
- **E 数据与评测基准**
  - [E1 方法比较与评测协议](#branch-12)（5 篇）
  - [E2 真实图与标签来源](#branch-13)（3 篇）
  - [E3 可控制的合成交易](#branch-14)（3 篇）
- **F 金融实证与数据边界**
  - [F1 真实金融现象与外部证据](#branch-15)（1 篇）
  - [F2 交易数据的披露边界](#branch-16)（1 篇）

## A 综述与入门

<a id="branch-1"></a>
<a id="branch-a1"></a>

### A1 图异常的定义与分类

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-survey-qiao"></a>[Deep Graph Anomaly Detection: A Survey and New Perspectives](<https://doi.org/10.1109/TKDE.2025.3581578>)<br>IEEE TKDE 2025 · 综述 · Hezhe Qiao et al.<br><code>survey-qiao</code> | 多种 · 多粒度 · 通用 | 用网络架构、代理任务和异常评分三个视角读同一方法，为模型卡补全“为什么给它高分”。<br>[代码](<https://github.com/mala-lab/Awesome-Deep-Graph-Anomaly-Detection>) |
| <a id="p-survey-ma"></a>[A Comprehensive Survey on Graph Anomaly Detection With Deep Learning](<https://doi.org/10.1109/TKDE.2021.3118815>)<br>IEEE TKDE 2023 · 综述 · Xiaoxiao Ma et al.<br><code>survey-ma</code> | 多种 · 节点、边、子图及整图 · 通用 | 先按预测对象区分任务，再比较图的表示与训练方法。2021 年在线，2023 年编入正式卷期。 |

<a id="branch-2"></a>
<a id="branch-a2"></a>

### A2 金融任务与时序图

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-survey-dynamic"></a>[Anomaly Detection in Dynamic Graphs: A Comprehensive Survey](<https://doi.org/10.1145/3669906>)<br>ACM TKDD 2024 · 综述 · Ocheme Anthony Ekle and William Eberle<br><code>survey-dynamic</code> | 多种 · 动态图中的异常 · 通用时序图 | 从带时间属性的边、离散快照和动态图任务入手，记录一个模型真正用了什么时间信息。 |
| <a id="p-survey-finance"></a>[Financial fraud detection using graph neural networks: A systematic review](<https://www.sciencedirect.com/science/article/pii/S0957417423026581>)<br>Expert Systems with Applications 2024 · 综述 · Soroor Motie and Bijan Raahemi<br><code>survey-finance</code> | 多种 · 随金融任务变化 · 金融欺诈 | 梳理金融欺诈的图表示、数据和模型选择。可用来辨别信用卡、借贷与其他反欺诈任务的差异。 |

## B 有监督识别

<a id="branch-3"></a>
<a id="branch-b1"></a>

### B1 类别不平衡与邻域伪装

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-dcl-gfd"></a>[Dynamic Neighborhood Modeling via Node-Subgraph Contrastive Learning for Graph-Based Fraud Detection](<https://doi.org/10.1609/aaai.v39i12.33431>)<br>AAAI 2025 · 方法 · Zhizhi Yu, Chundong Liang, Xinglong Chang, Dongxiao He, Di Jin and Jianguo Wei<br><code>dcl-gfd</code> | 双类标签及节点—子图对比辅助信号 · 节点（按数据集区分账户、用户或评论） · 微博、电商评论及金融账户图<br>DCL-GFD、自适应邻居、类别不平衡 | 用节点与其局部子图的相似性估计异常概率，再据此调整邻居分组。静态节点实验证据与流式时序预测应分别登记。<br>[精读卡](../notes/dcl-gfd.md) |
| <a id="p-grad-2025"></a>[Grad: Guided Relation Diffusion Generation for Graph Augmentation in Graph Fraud Detection](<https://doi.org/10.1145/3696410.3714520>)<br>The Web Conference (WWW) 2025 · 方法 · Jie Yang et al.<br><code>grad-2025</code> | 有监督图对比与少数类 · 欺诈节点 · 支付欺诈 | 用关系扩散生成更可分的同类连接以增强弱欺诈信号；须区分真实边与生成边。<br>[精读卡](../notes/grad-2025.md) |
| <a id="p-mimbfd-2025"></a><a id="p-mimbfd"></a>[Mitigating Message Imbalance in Fraud Detection with Dual-View Graph Representation Learning](<https://doi.org/10.24963/ijcai.2025/365>)<br>IJCAI 2025 · 方法 · Yudan Song et al.<br><code>mimbfd-2025</code> | 少量正常和欺诈节点标签，图上另含未标注节点（§3.1） · 多关系图节点 · Amazon、YelpChi、Comp 多关系欺诈图<br>MimbFD、监督信息传播、少数类召回 | TMR、LCD 两个模块分别关注标注信息传播和局部去混杂。可固定标签预算，与 PC-GNN 及类权重基线对照，按测试节点距已知异常的距离分组比较召回。<br>[精读卡](../notes/mimbfd-2025.md) |
| <a id="p-dig-in-gnn"></a>[DiG-In-GNN: Discriminative Feature Guided GNN-Based Fraud Detector against Inconsistencies in Multi-Relation Fraud Graph](<https://doi.org/10.1609/aaai.v38i8.28785>)<br>AAAI 2024 · 方法 · Jinghui Zhang et al.<br><code>dig-in-gnn</code> | 双类监督 · 多关系图节点 · 欺诈图 | 对特征与结构不一致分别引入引导节点及邻居选择，适合比较关系类型与伪装结构。<br>[代码](<https://github.com/GraphBerry/DiG-In-GNN>) |
| <a id="p-ijcai-robust-fraud-2024"></a>[Safeguarding Fraud Detection from Attacks: A Robust Graph Learning Approach](<https://doi.org/10.24963/ijcai.2024/830>)<br>IJCAI 2024 · 方法 · Jiasheng Wu et al.<br><code>ijcai-robust-fraud-2024</code> | 欺诈标签；扰动威胁模型 · 节点 · 金融欺诈 | 特征和结构共同被扰动时评估鲁棒性，不能把随机删除边当作真实对抗行为。 |
| <a id="p-pc-gnn"></a>[Pick and Choose: A GNN-based Imbalanced Learning Approach for Fraud Detection](<https://doi.org/10.1145/3442381.3449989>)<br>The Web Conference (WWW) 2021 · 经典方法 · Yang Liu et al.<br><code>pc-gnn</code> | 双类标签 · 节点 · 图欺诈<br>经典回溯、PC-GNN | 把少数类节点采样与邻居选择分开观察，检验训练重采样能否改善稀有类排序。<br>[代码](<https://github.com/PonderLY/PC-GNN>) |
| <a id="p-care-gnn"></a>[Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters](<https://arxiv.org/abs/2008.08692>)<br>CIKM 2020 · 经典方法 · Yingtong Dou et al.<br><code>care-gnn</code> | 双类标签 · 节点 · 评论和用户欺诈<br>经典回溯 | 研究异常对象混入正常邻居时如何选择可信邻居。业务迁移时要重新解释每种边。<br>[代码](<https://github.com/YingtongDou/CARE-GNN>) |

<a id="branch-4"></a>
<a id="branch-b2"></a>

### B2 图结构信号与可解释性

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-dgp-2026"></a>[DGP: A Dual-Granularity Prompting Framework for Fraud Detection with Graph-Enhanced LLMs](<https://doi.org/10.1609/aaai.v40i18.38541>)<br>AAAI 2026 · 方法 · Y. Li et al.<br><code>dgp-2026</code> | 有监督欺诈检测 · 节点/文本属性 · 金融及其他欺诈 | 分别压缩邻居摘要和保留目标细节，适合分析图文信息瓶颈，非核心数值基线。 |
| <a id="p-fraudgnam"></a>[FraudGNAM: Inherently Interpretable Spectral GNN for Graph Fraud Detection](<https://proceedings.mlr.press/v337/lee26e.html>)<br>UAI 2026 · 方法 · Suan Lee and Jinho Kim<br><code>fraudgnam</code> | 双类标签 · 节点 · 图欺诈 | 把谱域建模和可解释的特征贡献放在同一模型里，适合讨论调查人员能读到何种解释。 |
| <a id="p-dnb-aml"></a>[Finding money launderers using heterogeneous graph neural networks](<https://doi.org/10.1016/j.jfds.2025.100175>)<br>The Journal of Finance and Data Science 2025 · 方法与银行实证 · Fredrik Johannessen and Martin Jullum<br><code>dnb-aml</code> | 基于调查记录的双类标签 · 自然人节点 · 挪威银行反洗钱<br>银行真实数据、异质图、调查标签 | 把银行交易与企业任职关系联系起来。正例表示进入调查，评价结论应按此口径解释。作者代码公开，原始银行数据受限。<br>[代码](<https://github.com/fredjo89/heterogeneous-mpnn>) |
| <a id="p-naast-gnn"></a>[NAAST-GNN: Neighborhood Adaptive Aggregation and Spectral Tuning for Graph Anomaly Detection](<https://doi.org/10.24963/ijcai.2025/317>)<br>IJCAI 2025 · 方法 · Ronghui Guo, Xiaowang Zhang, Zhizhi Yu, Minghui Zou, Sai Zhang and Zhiyong Feng<br><code>naast-gnn</code> | 双类节点标签，加权交叉熵 · 节点（按数据集区分账户、用户或评论） · 评论、社交及金融账户图<br>NAAST-GNN、频谱、自适应邻居 | 按节点类别预测和邻域构成调整聚合与谱滤波。注意论文对部分基线采用了原作成绩。<br>[精读卡](../notes/naast-gnn.md) |
| <a id="p-hogrl-2024"></a>[Effective High-order Graph Representation Learning for Credit Card Fraud Detection](<https://doi.org/10.24963/ijcai.2024/839>)<br>IJCAI 2024 · 方法 · Yao Zou and Dawei Cheng<br><code>hogrl-2024</code> | 有监督欺诈标签 · 交易/客户目标依建图定义 · 信用卡欺诈 | 高阶交易图与混合阶数专家注意力，检验多跳信息是否胜过简单规则统计。 |
| <a id="p-diam"></a>[Effective Illicit Account Detection on Large Cryptocurrency MultiGraphs](<https://doi.org/10.1145/3627673.3679707>)<br>CIKM 2024 · 方法与公开数据 · Zhihao Ding et al.<br><code>diam</code> | 已标正常与风险地址参与监督；其余地址未标注 · 账户地址节点 · 以太坊、比特币交易<br>DIAM | DIAM 从平行交易的方向和顺序形成账户表示；通过四个公开链上账户数据集检验保留重复交易是否有价值。<br>[代码](<https://github.com/TommyDzh/DIAM>) · [精读卡](../notes/diam.md) |
| <a id="p-sec-gfd"></a>[Revisiting Graph-Based Fraud Detection in Sight of Heterophily and Spectrum](<https://doi.org/10.1609/aaai.v38i8.28773>)<br>AAAI · Technical Track 2024 · 方法 · Fan Xu, Nan Wang, Hao Wu, Xuezhi Wen, Xibin Zhao and Hai Wan<br><code>sec-gfd</code> | 双类节点标签，训练图中有未标注节点；作者称半监督 · 节点（按数据集区分账户、用户或评论） · 评论、社交及金融账户图<br>图异配性、频谱、SEC-GFD | 通过混合频带滤波和局部约束比较多跳真实邻域与特征相似的邻域。复现时记录两类标签数。<br>[精读卡](../notes/sec-gfd.md) |
| <a id="p-bwgnn"></a>[Rethinking Graph Neural Networks for Anomaly Detection](<https://proceedings.mlr.press/v162/tang22b.html>)<br>ICML 2022 · 方法 · Jianheng Tang et al.<br><code>bwgnn</code> | 双类标签 · 节点 · 金融与通用属性图<br>BWGNN | BWGNN 以带通滤波捕捉被平滑掩盖的异常信号；与属性基线、邻域特征加树模型同场比较。<br>[代码](<https://github.com/squareRoot3/Rethinking-Anomaly-Detection>) · [模型卡](../models/bwgnn.md) |

<a id="branch-5"></a>
<a id="branch-b3"></a>

### B3 交易边与可疑子图

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-spoofing-2025"></a>[Multi-Granularity Augmented Graph Learning for Spoofing Transaction Detection](<https://doi.org/10.1145/3696410.3714521>)<br>The Web Conference (WWW) 2025 · 方法 · 作者信息待核<br><code>spoofing-2025</code> | 标签细节待查 · 交易 · 证券交易欺诈 | 将多粒度关系用于虚假交易识别；需与银行 AML 场景区分。 |
| <a id="p-uniform-2025"></a>[UniFORM: Towards Unified Framework for Anomaly Detection on Graphs](<https://doi.org/10.1609/aaai.v39i12.33369>)<br>AAAI 2025 · 方法 · C. Song et al.<br><code>uniform-2025</code> | 自监督/少标签 · 节点、边、图 · 多粒度图 | 用统一子图视角连接多粒度异常，注意输出和标签实体不能混为一谈。 |
| <a id="p-revclassify"></a>[Identifying Money Laundering Subgraphs on the Blockchain](<https://doi.org/10.1145/3677052.3698635>)<br>ACM ICAIF 2024 · 方法 · Kiwhan Song et al.<br><code>revclassify</code> | 有标注候选子图 · 子图 · 比特币反洗钱<br>RevClassify | 分别记录给定候选的分类效果，以及整图中找到候选的成本和召回。 |
| <a id="p-multi-gnn"></a>[Provably Powerful Graph Neural Networks for Directed Multigraphs](<https://ojs.aaai.org/index.php/AAAI/article/view/29069>)<br>AAAI 2024 · 方法 · Béni Egressy et al.<br><code>multi-gnn</code> | 双类标签 · 交易边等 · 合成反洗钱、网络钓鱼<br>Multi-GNN | 针对方向和重复边改造消息传递；用来检验把多笔往来合并为一条边究竟损失什么。 |

## C 半监督与稀缺标签

<a id="branch-6"></a>
<a id="branch-c1"></a>

### C1 少量双类标签与未标注样本

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-bmp-2026"></a>[Binary Message Passing for Generalizable Semi-Supervised Graph Anomaly Detection](<https://doi.org/10.1609/aaai.v40i19.38671>)<br>AAAI 2026 · 方法 · J. Zhang et al.<br><code>bmp-2026</code> | 有限监督（双类/正常标签配置待查） · 节点 · 通用图 | 用二叉消息路由提升异常信号传播；详细标签设置以论文正文复核。 |
| <a id="p-dress-2026"></a>[Deep Reinforcement Learning Enhanced Semi-supervised Graph Neural Network for Credit Card Fraud Detection](<https://doi.org/10.24963/ijcai.2026/801>)<br>IJCAI 2026 · 方法 · Huilin He et al.<br><code>dress-2026</code> | 2%—10% 已标签样本；双类细分需查 · 信用卡交易/目标实体待查 · 信用卡欺诈 | 特征风险 RL 与图结构风险融合，比较单纯特征工程与时间特征增益。 |
| <a id="p-rule-ot-2026"></a>[Rule-graph alignment via optimal transport for weakly supervised anomaly detection on transaction graphs](<https://doi.org/10.1007/s44443-026-01381-3>)<br>Journal of King Saud University Computer and Information Sciences 2026 · 方法 · Qiuyang Zhang et al.<br><code>rule-ot-2026</code> | 少量双类训练标签+规则诱导伪标签 · 交易节点 · Elliptic、Libra Bank 等 | 树规则路径分组编码、最优传输对齐并过滤高置信伪标签；原始 Libra Bank 设置下优势有限。 |
| <a id="p-cgnn-2025"></a>[Context-aware Graph Neural Network for Graph-based Fraud Detection with Extremely Limited Labels](<https://doi.org/10.1609/aaai.v39i11.33319>)<br>AAAI 2025 · 方法 · Pengbo Li et al.<br><code>cgnn-2025</code> | 极少双类标签+未标注节点 · 欺诈节点 · 通用欺诈图 | 类别语义分解、邻居去噪及一致性约束；应与只开放正常标签的 C2 方案分开评测。<br>[精读卡](../notes/cgnn-2025.md) |
| <a id="p-consisgad"></a>[Consistency Training with Learnable Data Augmentation for Graph Anomaly Detection with Limited Supervision](<https://proceedings.iclr.cc/paper_files/paper/2024/hash/80eecea10dc05e23db2f90c9d4567153-Abstract-Conference.html>)<br>ICLR 2024 · 方法 · Nan Chen et al.<br><code>consisgad</code> | 少量双类标签＋未标注 · 节点 · 通用属性图<br>ConsisGAD | 利用未标注节点的一致性训练。与仅正常标签方法并读时，要列出额外可用的异常标签数。<br>[代码](<https://github.com/Xtra-Computing/ConsisGAD>) |
| <a id="p-gtan"></a>[Semi-supervised Credit Card Fraud Detection via Attribute-Driven Graph Representation](<https://doi.org/10.1609/aaai.v37i12.26702>)<br>AAAI · AI for Social Impact 2023 · 方法 · Sheng Xiang et al.<br><code>gtan</code> | 部分交易有标签＋未标注 · 交易节点 · 信用卡欺诈<br>GTAN | 将交易建成节点，以时间关联与风险信息传播检测欺诈。重点核对哪些历史标签在评分时已可见。<br>[代码](<https://github.com/AI4Risk/antifraud>) |

<a id="branch-7"></a>
<a id="branch-c2"></a>

### C2 仅少量可信正常标签

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-cr-aug"></a>[CR-Aug: Community Risk-Guided Adaptive Augmentation for Semi-supervised Graph Anomaly Detection](<https://doi.org/10.1145/3770855.3818003>)<br>KDD · Research 2026 · 团队方法 · Jing Huang, Yicun Liu, Zhixin Li, Yinan Jing and Hongfeng Chai<br><code>cr-aug</code> | 仅正常标签＋未标注 · 节点 · 金融与通用属性图<br>团队公开论文 | 按社区差异指导伪异常生成，最后给节点评分。可与 GGAD 在相同正常训练节点下比较。<br>[模型卡](../models/cr-aug.md) · [精读卡](../notes/cr-aug.md) |
| <a id="p-graphnc"></a>[Normality Calibration in Semi-supervised Graph Anomaly Detection](<https://proceedings.mlr.press/v306/zeng26o.html>)<br>ICML 2026 · 方法 · Guolei Zeng et al.<br><code>graphnc</code> | 仅正常标签＋未标注 · 节点 · 通用属性图<br>GraphNC | 以预训练教师的评分分布为参照校准检测分数，同时约束已标正常节点的表征，可检查哪些正常群体被反复误报。<br>[代码](<https://github.com/mala-lab/GraphNC>) |
| <a id="p-rho"></a>[Semi-supervised Graph Anomaly Detection via Robust Homophily Learning](<https://proceedings.neurips.cc/paper_files/paper/2025/hash/c273d135fed229f5724df9a0d354b36f-Abstract-Conference.html>)<br>NeurIPS 2025 · 方法 · Guoguo Ai et al.<br><code>rho</code> | 仅正常标签＋未标注 · 节点 · 通用属性图<br>RHO | 正常节点与邻居的相似程度也不一致。用它比较“刻画正常群体”与“改进伪异常”的效果。<br>[代码](<https://github.com/mala-lab/RHO>) |
| <a id="p-ggad"></a>[Generative Semi-supervised Graph Anomaly Detection](<https://proceedings.neurips.cc/paper_files/paper/2024/hash/085b4b5d1f81ad9e057ad2b3de922ad4-Abstract-Conference.html>)<br>NeurIPS 2024 · 方法 · Hezhe Qiao et al.<br><code>ggad</code> | 仅正常标签＋未标注 · 节点 · 通用属性图<br>GGAD | 从正常节点学习并生成伪异常。它为 CR-Aug 检验社区差异是否有用提供直接对照。<br>[代码](<https://github.com/mala-lab/GGAD>) · [模型卡](../models/ggad.md) |

<a id="branch-8"></a>
<a id="branch-c3"></a>

### C3 已知异常与未标注样本

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-pu-procurement"></a>[Learning from sanctioned government suppliers: a machine learning and network science approach to detecting fraud and corruption in Mexico](<https://doi.org/10.1038/s41598-026-48873-w>)<br>Scientific Reports 2026 · 相邻场景方法 · Martí Medina-Hernández et al.<br><code>pu-procurement</code> | 受处罚供应商名下合同作代理正例，其余未标注（PU） · 采购合同 · 公共采购关联网络 | 用处罚记录和采购网络特征标记待查合同。处罚针对供应商，每份合同的具体事实仍有待核查。 |

## D 前沿与对照方法

<a id="branch-9"></a>
<a id="branch-d1"></a>

### D1 无标签与自监督对照

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-mi-gad"></a>[Beyond Local Patterns: Multiscale Inconsistency Learning for Graph Anomaly Detection](<https://doi.org/10.1609/aaai.v40i18.38546>)<br>AAAI 2026 · 方法 · J. Lian et al.<br><code>mi-gad</code> | 无监督/标签细节待查 · 节点 · 通用图 | 结合局部相似性和全局偏离分数，适合验证社区与全局互补。 |
| <a id="p-camera-2026"></a>[CAMERA: Adapting to Semantic Camouflage in Unsupervised Text-Attributed Graph Fraud Detection](<https://doi.org/10.24963/ijcai.2026/328>)<br>IJCAI 2026 · 方法 · Junjun Pan et al.<br><code>camera-2026</code> | 无监督 · 文本属性节点 · 社交/电商欺诈 | 文本伪装时融合多种偏离信号；金融交易数值图非直接适用。 |
| <a id="p-langgen-2026"></a>[Can Edge Addition Be Safe and Effective? Adjacency-Centered Augmentation via Langevin and SDE Diffusion for Self-Supervised Graph Anomaly Detection](<https://doi.org/10.24963/ijcai.2026/292>)<br>IJCAI 2026 · 方法 · Haokai Gao et al.<br><code>langgen-2026</code> | 自监督 · 节点 · 通用图 | 引导加边与属性联合扩散可否保留异常信号，考察数据时间切分条件。<br>[代码](<https://github.com/GaoHaokai222/LangGen-JointSDE>) |
| <a id="p-ltrer-2026"></a>[Graph Anomaly Detection via Feature Selection with Local Topological Residuals](<https://doi.org/10.24963/ijcai.2026/365>)<br>IJCAI 2026 · 方法 · Yazheng Zhao et al.<br><code>ltrer-2026</code> | 标签条件待查 · 节点 · 通用图 | 用局部拓扑残差选属性而非直接邻域平滑，适合与仅属性基线比较。 |
| <a id="p-hsmad-2026"></a>[HSMAD: Heterophily-Driven Spectral and Manifold Learning for Graph Anomaly Detection](<https://proceedings.mlr.press/v306/zhu26bc.html>)<br>ICML 2026 · 方法 · Chen Zhu and Yaying Zhang<br><code>hsmad-2026</code> | 标签条件待查 · 节点 · 异配图 | 异配权重谱滤波与流形路由，适合和 BWGNN 的频率响应作对照。 |
| <a id="p-m2v-ugad"></a>[Towards Multiple Missing Values-resistant Unsupervised Graph Anomaly Detection](<https://doi.org/10.1609/aaai.v40i24.39096>)<br>AAAI 2026 · 方法 · Jiazhen Chen et al.<br><code>m2v-ugad</code> | 无监督 · 节点 · 缺失属性与缺失边的图 | 双通路分别估计缺失属性和边，研究缺失处理是否掩盖真正异常。 |
| <a id="p-huge-2025"></a>[A Label-free Heterophily-guided Approach for Unsupervised Graph Fraud Detection](<https://doi.org/10.1609/aaai.v39i12.33356>)<br>AAAI 2025 · 方法 · Junjun Pan et al.<br><code>huge-2025</code> | 训练无人工标签 · 欺诈节点 · 欺诈图 | 以 HALO 无标签异配性估计引导对齐与排序；可作节点图无监督对照。 |
| <a id="p-curvgad-2025"></a>[CurvGAD: Leveraging Curvature for Enhanced Graph Anomaly Detection](<https://proceedings.mlr.press/v267/grover25a.html>)<br>ICML 2025 · 方法 · Karish Grover et al.<br><code>curvgad-2025</code> | 重建式无监督 · 节点 · 通用图 | 曲率、属性和结构异常分开重建；可与交易图中的高阶局部形态对照。<br>[代码](<https://github.com/karish-grover/curvgad>) |
| <a id="p-agdiff-2025"></a>[Leveraging Diffusion Model as Pseudo-Anomalous Graph Generator for Graph-Level Anomaly Detection](<https://proceedings.mlr.press/v267/cai25l.html>)<br>ICML 2025 · 方法 · Jinyu Cai et al.<br><code>agdiff-2025</code> | 仅正常图或极少异常 · 整图 · 通用图 | 潜空间扩散制造边界附近异常图；适用整图异常而不是账户节点的直接基线。 |
| <a id="p-megad-2025"></a>[MEGAD: A Memory-Efficient Framework for Large-Scale Attributed Graph Anomaly Detection](<https://doi.org/10.24963/ijcai.2025/406>)<br>IJCAI 2025 · 方法 · Yifan Zhang et al.<br><code>megad-2025</code> | 重建型无监督 · 节点 · 大规模属性图 | 大图内存效率与异常排序共同比较，记录峰值显存而非只报 AUROC。 |
| <a id="p-clean-view-2025"></a>[Rethinking Contrastive Learning in Graph Anomaly Detection: A Clean-View Perspective](<https://doi.org/10.24963/ijcai.2025/335>)<br>IJCAI 2025 · 方法 · Di Jin et al.<br><code>clean-view-2025</code> | 对比学习设定需核 · 节点 · 通用图 | 反思受干扰边对节点-子图相似性假设的破坏，适合研究如何筛除噪声邻域。 |
| <a id="p-sdm-2025"></a>[Self-Discriminative Modeling for Anomalous Graph Detection](<https://proceedings.mlr.press/v267/cai25k.html>)<br>ICML 2025 · 方法 · Jinyu Cai et al.<br><code>sdm-2025</code> | 训练仅正常图 · 整图 · 通用图 | 联合生成伪异常图并训练判别器，适合跨到团伙子图任务前先明确候选子图。 |
| <a id="p-cola"></a>[Anomaly Detection on Attributed Networks via Contrastive Self-Supervised Learning](<https://doi.org/10.1109/TNNLS.2021.3068344>)<br>IEEE TNNLS 2022 · 对照方法 · Yixin Liu et al.<br><code>cola</code> | 无真实标签，自监督 · 节点 · 通用属性图 | 用节点与局部子图的对比学习刻画异常。作为标签收益的对照；2021 年在线，2022 年编入卷期。<br>[代码](<https://github.com/TrustAGI-Lab/CoLA>) |

<a id="branch-10"></a>
<a id="branch-d2"></a>

### D2 时间演化与未见异常

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-ares-edge-stream"></a>[ARES: Anomaly Recognition Model For Edge Streams](<https://doi.org/10.1145/3770854.3780242>)<br>KDD · Research 2026 · 方法 · Simone Mungari et al.<br><code>ares-edge-stream</code> | 无监督训练，验证和测试用途单列 · 按到达时间评分的边 · 一般事件流，另有比特币信任网络<br>ARES | ARES 用图表示结合半空间树为流式关系评分，可作为 TransXion 交易边模型的无标签在线对照。<br>[代码](<https://github.com/AnomalyRecognitionModelForEdgeStreams/ARES>) · [精读卡](../notes/ares-edge-stream.md) |
| <a id="p-dynamic-limited"></a>[Learning Discriminative and Generalizable Anomaly Detector for Dynamic Graph with Limited Supervision](<https://proceedings.mlr.press/v306/tian26h.html>)<br>ICML 2026 · 方法 · Yuxing Tian et al.<br><code>dynamic-limited</code> | 有限异常标签或无异常标签 · 动态交互 · 通用动态图<br>动态图 | 研究动态交互和未见异常，阅读时区分“测试时刻更晚”与“异常类型未见”两种泛化。 |
| <a id="p-spectral-shifts-2026"></a>[Modeling Spectral Energy Shifts in Spatio-Temporal Graph Anomaly Detection](<https://proceedings.mlr.press/v306/liu26gb.html>)<br>ICML 2026 · 方法 · Yilin Liu et al.<br><code>spectral-shifts-2026</code> | 标签条件待查 · 节点 · 时空图 | 不仅捕捉谱能量升高，还关注伪装异常中的下降信号。 |
| <a id="p-temg-tta-2026"></a>[Temporal Motif-aware Graph Test-time Adaptation for OOD Blockchain Anomaly Detection](<https://doi.org/10.24963/ijcai.2026/802>)<br>IJCAI 2026 · 方法 · 作者信息待核<br><code>temg-tta-2026</code> | 目标测试时无标签自适应，源训练标签需核 · 交易/链上节点待查 · 区块链异常 | 时序模体与测试时适应联合应对分布外偏移；复现需核查测试时访问边界。 |
| <a id="p-abnet-2025"></a>[ABNet: Mitigating Sample Imbalance in Anomaly Detection Within Dynamic Graphs](<https://doi.org/10.24963/ijcai.2025/324>)<br>IJCAI 2025 · 方法 · Yifan Hong et al.<br><code>abnet-2025</code> | 无监督/半监督场景，正文需区分 · 动态图节点 · 动态图 | 时点差分、异常增强和元学习适配；需复核增强样本是否使用了未来时段。 |
| <a id="p-mutationguard-2025"></a>[MutationGuard: A Graph and Temporal-Spatial Neural Method for Detecting Mutation Telecommunication Fraud](<https://doi.org/10.24963/ijcai.2025/1061>)<br>IJCAI 2025 · 方法 · Haitao Bai et al.<br><code>mutationguard-2025</code> | 有标签电诈 · 通话账号/交互 · 电信欺诈 | 通信图与通话时间空间语义融合；金融账户迁移仅是研究设想，不能直接推断金融效果。 |
| <a id="p-tempasd"></a>[TempASD: Temporal Anomalous Subgraph Discovery in Large-Scale Dynamic Financial Networks](<https://doi.org/10.1145/3711896.3737149>)<br>KDD · Research 2025 · 方法与金融实证 · Xiaolin Han et al.<br><code>tempasd</code> | 部分数据有异常训练线索，另以统计规则生成训练候选 · 时序子图及其成员 · 以太坊交易、NFT 交易<br>TEMPASD | 把交易金额的首位数字分布与时序密集程度结合，直接在大型网络中搜索异常子图；区分已知案例与统计代理线索。<br>[代码](<https://github.com/KZ-code/TempASD>) · [精读卡](../notes/tempasd.md) |

<a id="branch-11"></a>
<a id="branch-d3"></a>

### D3 预训练与少样本迁移

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-grade-2026"></a>[Geometry-Aware Riemannian Residual Displacement for Cross-Broad-Domain Graph Anomaly Detection](<https://doi.org/10.24963/ijcai.2026/342>)<br>IJCAI 2026 · 方法 · Senyong Wang et al.<br><code>grade-2026</code> | 跨域零样本/少样本 · 节点 · 跨领域图 | 在属性异质、拓扑差异均较大的目标图迁移，需跟纯目标图无标签训练区分。 |
| <a id="p-mv-fgad-2026"></a>[MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning](<https://proceedings.mlr.press/v306/yan26i.html>)<br>ICML 2026 · 方法 · Junyi Yan et al.<br><code>mv-fgad-2026</code> | 联邦多客户端，监督条件待查 · 节点 · 多机构分图 | 研究分布式弱异常与结构分割下的检出；不等同于已经有合法跨机构数据。 |
| <a id="p-apf"></a>[Towards Anomaly-Aware Pre-Training and Fine-Tuning for Graph Anomaly Detection](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/dd2094ecf134f7c9740fb29640bfb620-Abstract-Conference.html>)<br>ICLR 2026 · 方法 · Yunhui Liu, Jiashun Cheng et al.<br><code>apf</code> | 无标签预训练＋少量标签微调 · 节点 · 通用属性图 | 核对预训练阶段看过的图及微调阶段使用的标签。少样本微调与目标域零标签要分别记录。<br>[代码](<https://github.com/Cloudy1225/APF>) |
| <a id="p-anomalygfm"></a>[AnomalyGFM: Graph Foundation Model for Zero/Few-shot Anomaly Detection](<https://doi.org/10.1145/3711896.3736843>)<br>KDD 2025 · 方法 · Hezhe Qiao, Chaoxi Niu, Ling Chen and Guansong Pang<br><code>anomalygfm</code> | 源图含正常和异常标签；目标图零标签或仅少量正常标签 · 节点 · 跨评论、金融、社交等属性图<br>AnomalyGFM、跨图迁移、零样本与少样本 | 用节点相对邻居的表示残差对齐正常与异常原型。在新图上比较零标签推理和少量正常标签提示调优。<br>[代码](<https://github.com/mala-lab/AnomalyGFM>) · [精读卡](../notes/anomalygfm.md) |
| <a id="p-unprompt-2025"></a>[Zero-shot Generalist Graph Anomaly Detection with Unified Neighborhood Prompts](<https://doi.org/10.24963/ijcai.2025/359>)<br>IJCAI 2025 · 方法 · Chaoxi Niu et al.<br><code>unprompt-2025</code> | 源图训练，目标图零样本 · 节点 · 跨图 | 单一源图训练后不调参迁移目标图，注意与目标图无标签可见条件分清。<br>[精读卡](../notes/unprompt-2025.md) |
| <a id="p-topoood-2024"></a>[Graph Out-of-Distribution Detection Goes Neighborhood Shaping](<https://proceedings.mlr.press/v235/bao24c.html>)<br>ICML 2024 · 方法 · Tianyi Bao et al.<br><code>topoood-2024</code> | OOD 检测，标注协议需核 · 节点 · 跨图 | 设计拓扑分布变化下的 OOD 节点检出协议，警惕异常检测与分布外检测概念混同。 |

## E 数据与评测基准

<a id="branch-12"></a>
<a id="branch-e1"></a>

### E1 方法比较与评测协议

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-bag-2026"></a><a id="p-bag-dynamic"></a>[BAG: Benchmarking Anomaly Detection on Dynamic Graphs](<https://doi.org/10.1609/aaai.v40i17.38510>)<br>AAAI 2026 · 评测基准 · Fengrui Hua, Yiyan Qi et al.<br><code>bag-2026</code> | 多种设定，按数据集和模型分别记录训练可见标签；时间切分后分别评价原有异常和人工注入异常。 · 连续时序边和快照中的动态节点 · 金融信任与社交等动态图<br>BAG | BAG 在 10 个图数据集上比较 25 个模型，明确区分自然异常和注入异常；可与 DyGADBench 配对设计压力测试。<br>[代码](<https://github.com/frhuaaa/BAG>) · [精读卡](../notes/bag-dynamic.md) |
| <a id="p-dygadbench"></a>[DyGADBench: A Comprehensive Benchmark for Anomaly Detection in Dynamic Graphs](<https://doi.org/10.1145/3770855.3817594>)<br>KDD · Datasets and Benchmarks 2026 · 基准 · Mohamed Nazim Mezhoudi et al.<br><code>dygadbench</code> | 按注入协议评测 · 时序边 · 通用动态图 | 改变注入异常的结构、强度和持续时间，关注 AP、运行成本及失效模式。<br>[代码](<https://github.com/Dastamn/dgadb>) · [精读卡](../notes/dygadbench-2026.md) |
| <a id="p-ub-gold"></a>[Unifying Unsupervised Graph-Level Anomaly Detection and Out-of-Distribution Detection: A Benchmark](<https://proceedings.iclr.cc/paper_files/paper/2025/hash/e58fa42d4b7a798eef8d0d75098f87ad-Abstract-Conference.html>)<br>ICLR 2025 · 基准 · Yili Wang et al.<br><code>ub-gold</code> | 无监督图级检测，异常评估标签与分布来源取决于场景 · 候选整图 · 分子、社交等通用图集合<br>UB | UB-GOLD 对 35 个数据集和 18 种方法作统一比较。可借鉴其设计，在独立实验中区分给定候选子图的异常与跨域偏移。<br>[代码](<https://github.com/UB-GOLD/UB-GOLD>) · [精读卡](../notes/ub-gold.md) |
| <a id="p-gadbench"></a>[GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection](<https://papers.neurips.cc/paper_files/paper/2023/hash/5eaafd67434a4cfb1cf829722c65f184-Abstract-Datasets_and_Benchmarks.html>)<br>NeurIPS · Datasets and Benchmarks 2023 · 基准 · Jianheng Tang et al.<br><code>gadbench</code> | 双类标签 · 静态节点 · 通用与金融图<br>强基线 | 比较 29 种方法与 10 个数据集。邻域特征加树模型是验证图神经网络增益的重要对照。<br>[代码](<https://github.com/squareRoot3/GADBench>) |
| <a id="p-bond"></a>[BOND: Benchmarking Unsupervised Outlier Node Detection on Static Attributed Graphs](<https://proceedings.neurips.cc/paper_files/paper/2022/hash/acc1ec4a9c780006c9aafd595104816b-Abstract.html>)<br>NeurIPS · Datasets and Benchmarks 2022 · 基准 · Kay Liu et al.<br><code>bond</code> | 无真实训练标签 · 静态节点 · 通用属性图<br>BOND | 将自然标注的异常与人工注入的异常分开，帮助判断一个方法为什么在不同图上表现悬殊。 |

<a id="branch-13"></a>
<a id="branch-e2"></a>

### E2 真实图与标签来源

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-elliptic2"></a>[The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset](<https://arxiv.org/abs/2404.19109>)<br>KDD Workshop on Machine Learning in Finance 2024 · 数据与基准 · Claudio Bellei et al.<br><code>elliptic2</code> | 有标注候选子图 · 地址簇构成的子图 · 比特币链上交易 | Elliptic2 把标签放在候选子图上。已知候选分类的实验不能直接回答从整张图找线索的问题。 |
| <a id="p-dgraph"></a>[DGraph: A Large-Scale Financial Dataset for Graph Anomaly Detection](<https://proceedings.nips.cc/paper_files/paper/2022/hash/8f1918f71972789db39ec0d85bb31110-Abstract-Datasets_and_Benchmarks.html>)<br>NeurIPS · Datasets and Benchmarks 2022 · 数据与基准 · Xuanwen Huang et al.<br><code>dgraph</code> | 目标节点有标注，另有背景节点 · 借贷用户节点 · 金融借贷联系图 | 边来自申报的紧急联系人。研究按长期逾期且多次催收未应答定义正例，背景节点另计；原节点切分结果须与跨时点评测分开。 |
| <a id="p-elliptic"></a>[Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics](<https://arxiv.org/abs/1908.02591>)<br>KDD Workshop on Anomaly Detection in Finance 2019 · 经典数据与基准 · Mark Weber et al.<br><code>elliptic</code> | 合法、非法和未知 · 交易节点 · 比特币链上交易<br>经典回溯、Elliptic | 适合双类监督和人为遮蔽异常标签的两种节点任务。核对特征所用邻居是否来自未来。 |

<a id="branch-14"></a>
<a id="branch-e3"></a>

### E3 可控制的合成交易

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-transxion"></a>[TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering](<https://doi.org/10.1145/3770855.3817550>)<br>KDD · Datasets and Benchmarks 2026 · 团队数据与基准 · Keyang Chen et al.<br><code>transxion</code> | 模拟交易标签 · 交易边 · 合成反洗钱交易<br>团队公开论文 | 保留账户间重复、带时间的资金往来，适合测试对交易边的告警排序和跨模拟器迁移。<br>[代码](<https://github.com/chaos-max/TransXion>) · [精读卡](../notes/transxion-2026.md) |
| <a id="p-synthaml"></a>[A synthetic data set to benchmark anti-money laundering methods](<https://doi.org/10.1038/s41597-023-02569-2>)<br>Scientific Data 2023 · 数据与基准 · Rasmus Ingemann Tuffveson Jensen et al.<br><code>synthaml</code> | 模拟告警处置结果 · 告警及关联交易 · 源自丹麦银行的合成数据 | 读清告警上报或驳回的标签。它支持告警筛查研究，不能直接给每笔交易赋犯罪真值。 |
| <a id="p-amlworld"></a>[Realistic Synthetic Financial Transactions for Anti-Money Laundering Models](<https://research.ibm.com/publications/realistic-synthetic-financial-transactions-for-anti-money-laundering-models>)<br>NeurIPS · Datasets and Benchmarks 2023 · 数据与基准 · Erik Altman et al.<br><code>amlworld</code> | 模拟交易标签 · 交易边 · 合成反洗钱交易 | IBM AMLworld 可与 TransXion 作跨生成器对照，区分具体生成规则带来的收益。<br>[精读卡](../notes/ibm-amlworld.md) |

## F 金融实证与数据边界

<a id="branch-15"></a>
<a id="branch-f1"></a>

### F1 真实金融现象与外部证据

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-nature-abuse"></a>[Banking records reveal characteristics of financial abuse](<https://doi.org/10.1038/s41586-026-11049-7>)<br>Nature 2026 · 跨学科实证 · Anna Trendl et al.<br><code>nature-abuse</code> | 自报经历及匹配对照 · 人及跨期资金行为 · 英国零售银行 | 以披露日为参照研究披露前的账户轨迹。可借鉴现实问题、参照组和观察窗的设计。 |

<a id="branch-16"></a>
<a id="branch-f2"></a>

### F2 交易数据的披露边界

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-science-privacy"></a>[Unique in the shopping mall: On the reidentifiability of credit card metadata](<https://doi.org/10.1126/science.1256297>)<br>Science 2015 · 跨学科经典 · Yves-Alexandre de Montjoye et al.<br><code>science-privacy</code> | 不适用 · 交易记录与个体 · 信用卡交易元数据<br>经典回溯 | 研究时空交易记录的可识别性。供讨论合作数据的可披露范围，独立于检测算法比较。 |
