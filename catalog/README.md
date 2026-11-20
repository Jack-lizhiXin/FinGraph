# FinGraph 论文索引

共 203 篇。按主分支浏览，论文只收录一次。点英文题名进入原始来源，每篇附有选读理由。

[首页](../README.md) · [贡献说明](../CONTRIBUTING.md) · [JSON](papers.json) · [CSV](papers.csv)

## 分支导航

- **A 综述与入门**
  - [A1 图异常的定义与分类](#branch-1)（5 篇）
  - [A2 金融任务与时序图](#branch-2)（8 篇）
- **B 有监督识别**
  - [B1 类别不平衡与邻域伪装](#branch-3)（16 篇）
  - [B2 图结构信号与可解释性](#branch-4)（15 篇）
  - [B3 交易边与可疑子图](#branch-5)（11 篇）
- **C 半监督与稀缺标签**
  - [C1 少量双类标签与未标注样本](#branch-6)（7 篇）
  - [C2 仅少量可信正常标签](#branch-7)（4 篇）
  - [C3 已知异常与未标注样本](#branch-8)（1 篇）
- **D 前沿与对照方法**
  - [D1 无标签与自监督对照](#branch-9)（25 篇）
  - [D2 时间演化与未见异常](#branch-10)（11 篇）
  - [D3 预训练与少样本迁移](#branch-11)（10 篇）
- **E 数据与评测基准**
  - [E1 方法比较与评测协议](#branch-12)（12 篇）
  - [E2 真实图与标签来源](#branch-13)（7 篇）
  - [E3 可控制的合成交易](#branch-14)（6 篇）
- **F 金融实证与数据边界**
  - [F1 真实金融现象与外部证据](#branch-15)（5 篇）
  - [F2 交易数据的披露边界](#branch-16)（1 篇）
- **G 动态图检测与时间协议**
  - [G1 边流与突发交互](#branch-17)（12 篇）
  - [G2 节点轨迹与账户状态](#branch-18)（5 篇）
  - [G3 时序子图与团伙发现](#branch-19)（5 篇）
  - [G4 快照序列与结构变点](#branch-20)（9 篇）
  - [G5 时序表示与链接预测对照](#branch-21)（24 篇）
  - [G6 时间切分、反馈与告警预算](#branch-22)（4 篇）

## A 综述与入门

<a id="branch-1"></a>
<a id="branch-a1"></a>

### A1 图异常的定义与分类

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-primer-tgl-rahman"></a>[A Primer on Temporal Graph Learning](<https://doi.org/10.1145/3771693>)<br>ACM Computing Surveys 2026 · 方法教程 · Aniq Ur Rahman, Ahmed A. Elhag, Justin P. Coon<br><code>primer-tgl-rahman</code> | 依时间预测、分类等任务而异 · 时间图与时序学习任务 · 通用动态图<br>通用动态图、方法教程 | 用形式化定义区分时间图表示，再介绍其学习架构和任务。教程不提供异常识别或反洗钱系统效能实证。 |
| <a id="p-slr-dygnn-zheng"></a>[A survey of dynamic graph neural networks](<https://doi.org/10.1007/s11704-024-3853-2>)<br>Frontiers of Computer Science 2025 · 方法学综述 · Yanping Zheng, Lu Yi, Zhewei Wei<br><code>slr-dygnn-zheng</code> | 多种动态学习任务 · 演化节点、边和时变拓扑 · 通用动态图<br>通用动态图、方法学综述 | 梳理动态图神经网络学习拓扑和属性变化的多种设计。动态图编码器的预测能力须通过带异常标签的下游协议检验。 |
| <a id="p-survey-qiao"></a>[Deep Graph Anomaly Detection: A Survey and New Perspectives](<https://doi.org/10.1109/TKDE.2025.3581578>)<br>IEEE TKDE 2025 · 综述 · Hezhe Qiao et al.<br><code>survey-qiao</code> | 多种 · 多粒度 · 通用 | 用网络架构、代理任务和异常评分三个视角读同一方法，为模型卡补全“为什么给它高分”。<br>[代码](<https://github.com/mala-lab/Awesome-Deep-Graph-Anomaly-Detection>) |
| <a id="p-survey-ma"></a>[A Comprehensive Survey on Graph Anomaly Detection With Deep Learning](<https://doi.org/10.1109/TKDE.2021.3118815>)<br>IEEE TKDE 2023 · 综述 · Xiaoxiao Ma et al.<br><code>survey-ma</code> | 多种 · 节点、边、子图及整图 · 通用 | 先按预测对象区分任务，再比较图的表示与训练方法。2021 年在线，2023 年编入正式卷期。 |
| <a id="p-slr-gad-kim"></a>[Graph Anomaly Detection With Graph Neural Networks: Current Status and Challenges](<https://doi.org/10.1109/ACCESS.2022.3211306>)<br>IEEE Access 2022 · 综述 · Hwan Kim, Byung Suk Lee, Won-Yong Shin, Sungsu Lim<br><code>slr-gad-kim</code> | 多种方法 · 节点、边、子图和整图 · 通用图异常<br>通用图异常、综述 | 按图类型、异常对象和神经网络架构交叉归类。任务分类覆盖通用图，个别金融结论必须回原始数据。 |

<a id="branch-2"></a>
<a id="branch-a2"></a>

### A2 金融任务与时序图

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-slr-finrisk-lai"></a>[A systematic literature review of spatiotemporal graph and sequence learning for financial risk detection](<https://doi.org/10.1007/s44163-026-02506-3>)<br>Discover Artificial Intelligence 2026 · 综述 · Foo Zheng Lai et al.<br><code>slr-finrisk-lai</code> | 多种，来源论文分层 · 风险实体与时序记录 · 金融风险<br>金融风险、综述 | 按是否真正跨时间步递归区分图与序列混合模型。覆盖多种金融风险，结论需回到相同对象与验证条件复查。<br>[精读卡](../notes/slr-finrisk-lai.md) |
| <a id="p-slr-edgefraud-harbi"></a>[Edge-deployed graph learning for real-time telecom and financial fraud detection: a systematic survey and reference architecture](<https://doi.org/10.1007/s10791-026-10570-7>)<br>Discover Computing 2026 · 部署综述与试点 · Ahmed Harbi<br><code>slr-edgefraud-harbi</code> | 试点使用带标签的电信欺诈数据 · 电信用户与跨域交易告警 · 电信与金融欺诈<br>电信与金融欺诈、部署综述与试点 | 分开归纳系统部署、联邦训练和可审计性，并报告电信数据上的局部试点。文中系统吞吐量含推算，试点只验证部分组件。 |
| <a id="p-slr-finprops-ale"></a>[Graph-Based Financial Fraud Detection: A Property-Centric Survey of Static, Temporal, Cycle-Aware, and Generative Methods and Their Evaluation](<https://doi.org/10.62411/jcta.18143>)<br>Journal of Computing Theories and Applications 2026 · 综述 · Daniel T. Ale, E. O. Ogunti, S. A. Oyetunji, A. A. Ponnle, K. B. Adedeji<br><code>slr-finprops-ale</code> | 多种，综述证据 · 协调欺诈与资金环 · 金融欺诈<br>金融欺诈、综述 | 从时序、生成性、循环结构和内在可解释性检查方法家族。已覆盖预算指标和特征因果性，案件归并及标签成熟时间需回到逐实验的可用信息。<br>[精读卡](../notes/slr-finprops-ale.md) |
| <a id="p-cp-survey-zhou"></a>[A Survey of Change Point Detection in Dynamic Graphs](<https://doi.org/10.1109/TKDE.2024.3523857>)<br>IEEE TKDE 2025 · 综述 · Yuxuan Zhou et al.<br><code>cp-survey-zhou</code> | 综述，多种监督条件 · 结构变化时点或图上实体序列变化 · 跨域<br>动态图、变点 | 区分快照序列的拓扑变点和图结构上的数值序列变点，并梳理指标与数据。综述不提供独立的资金转账检测结果。 |
| <a id="p-slr-finlearning-li"></a>[Graph Learning-Empowered Financial Fraud Detection: Progress and Future Directions](<https://doi.org/10.34133/icomputing.0146>)<br>Intelligent Computing 2025 · 综述 · Enxia Li, Mengshi Chen, Sheng Xiang, Ling Chen<br><code>slr-finlearning-li</code> | 多种方法 · 信用卡、保险和洗钱欺诈对象 · 金融欺诈<br>金融欺诈、综述 | 按金融应用梳理图学习并讨论隐私、可扩展性、网络演化及解释。适合场景编码；每种模型的时序测试条件需由实证论文提取。 |
| <a id="p-slr-fingnn-cheng"></a>[Graph neural networks for financial fraud detection: a review](<https://doi.org/10.1007/s11704-024-40474-y>)<br>Frontiers of Computer Science 2025 · 综述 · Dawei Cheng, Yao Zou, Sheng Xiang, Changjun Jiang<br><code>slr-fingnn-cheng</code> | 多种方法 · 账户、交易及异质金融实体 · 金融欺诈<br>金融欺诈、综述 | 以同质与异质图方法连接信用卡、在线支付、保险和反洗钱应用。同一应用中的图建模方式可有多种，不能直接合并准确率。 |
| <a id="p-survey-dynamic"></a>[Anomaly Detection in Dynamic Graphs: A Comprehensive Survey](<https://doi.org/10.1145/3669906>)<br>ACM TKDD 2024 · 综述 · Ocheme Anthony Ekle and William Eberle<br><code>survey-dynamic</code> | 多种 · 动态图中的异常 · 通用时序图 | 从带时间属性的边、离散快照和动态图任务入手，记录一个模型真正用了什么时间信息。 |
| <a id="p-survey-finance"></a>[Financial fraud detection using graph neural networks: A systematic review](<https://www.sciencedirect.com/science/article/pii/S0957417423026581>)<br>Expert Systems with Applications 2024 · 综述 · Soroor Motie and Bijan Raahemi<br><code>survey-finance</code> | 多种 · 随金融任务变化 · 金融欺诈 | 梳理金融欺诈的图表示、数据和模型选择。可用来辨别信用卡、借贷与其他反欺诈任务的差异。 |

## B 有监督识别

<a id="branch-3"></a>
<a id="branch-b1"></a>

### B1 类别不平衡与邻域伪装

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-slr-cilg-ma"></a>[Class-Imbalanced Learning on Graphs: A Survey](<https://doi.org/10.1145/3718734>)<br>ACM Computing Surveys 2025 · 方法学综述 · Yihong Ma, Yijun Tian, Nuno Moniz, Nitesh V. Chawla<br><code>slr-cilg-ma</code> | 有标签的类别不平衡图学习 · 图中的少数类样本 · 通用图<br>通用图、方法学综述 | 整理数据级与算法级类别不平衡学习方法。类别不平衡不自动意味着只有正例或正常标签。<br>[代码](<https://github.com/yihongma/CILG-Papers>) |
| <a id="p-dcl-gfd"></a>[Dynamic Neighborhood Modeling via Node-Subgraph Contrastive Learning for Graph-Based Fraud Detection](<https://doi.org/10.1609/aaai.v39i12.33431>)<br>AAAI 2025 · 方法 · Zhizhi Yu, Chundong Liang, Xinglong Chang, Dongxiao He, Di Jin and Jianguo Wei<br><code>dcl-gfd</code> | 双类标签及节点—子图对比辅助信号 · 节点（按数据集区分账户、用户或评论） · 微博、电商评论及金融账户图<br>DCL-GFD、自适应邻居、类别不平衡 | 用节点与其局部子图的相似性估计异常概率，再据此调整邻居分组。静态节点实验证据与流式时序预测应分别登记。<br>[精读卡](../notes/dcl-gfd.md) |
| <a id="p-grad-2025"></a>[Grad: Guided Relation Diffusion Generation for Graph Augmentation in Graph Fraud Detection](<https://doi.org/10.1145/3696410.3714520>)<br>The Web Conference (WWW) 2025 · 方法 · Jie Yang et al.<br><code>grad-2025</code> | 有监督图对比与少数类 · 欺诈节点 · 支付欺诈 | 用关系扩散生成更可分的同类连接以增强弱欺诈信号；须区分真实边与生成边。<br>[精读卡](../notes/grad-2025.md) |
| <a id="p-context-fraud-2025"></a>[Graph neural network for fraud detection via context encoding and adaptive aggregation](<https://www.sciencedirect.com/science/article/pii/S0957417424023406>)<br>Expert Systems with Applications 2025 · 方法 · Chaoli Lou et al.<br><code>context-fraud-2025</code> | 有监督欺诈检测 · 节点 · 金融欺诈关系图<br>欺诈识别、节点 | 用行为时间频率与出度编码上下文，辅以消息随机丢弃和自适应聚合。 |
| <a id="p-mimbfd-2025"></a><a id="p-mimbfd"></a>[Mitigating Message Imbalance in Fraud Detection with Dual-View Graph Representation Learning](<https://doi.org/10.24963/ijcai.2025/365>)<br>IJCAI 2025 · 方法 · Yudan Song et al.<br><code>mimbfd-2025</code> | 少量正常和欺诈节点标签，图上另含未标注节点（§3.1） · 多关系图节点 · Amazon、YelpChi、Comp 多关系欺诈图<br>MimbFD、监督信息传播、少数类召回 | TMR、LCD 两个模块分别关注标注信息传播和局部去混杂。可固定标签预算，与 PC-GNN 及类权重基线对照，按测试节点距已知异常的距离分组比较召回。<br>[精读卡](../notes/mimbfd-2025.md) |
| <a id="p-dual-resistance-2024"></a>[A GNN-based fraud detector with dual resistance to graph disassortativity and imbalance](<https://www.sciencedirect.com/science/article/pii/S0020025524004936>)<br>Information Sciences 2024 · 方法 · Junhang Wu et al.<br><code>dual-resistance-2024</code> | 有监督，节点及边类别不平衡 · 节点 · 欺诈关系图<br>欺诈识别、节点 | 同时考虑节点类别分布、边类别不平衡及异配关系。 |
| <a id="p-dig-in-gnn"></a>[DiG-In-GNN: Discriminative Feature Guided GNN-Based Fraud Detector against Inconsistencies in Multi-Relation Fraud Graph](<https://doi.org/10.1609/aaai.v38i8.28785>)<br>AAAI 2024 · 方法 · Jinghui Zhang et al.<br><code>dig-in-gnn</code> | 双类监督 · 多关系图节点 · 欺诈图 | 对特征与结构不一致分别引入引导节点及邻居选择，适合比较关系类型与伪装结构。<br>[代码](<https://github.com/GraphBerry/DiG-In-GNN>) |
| <a id="p-igsl-2024"></a>[Improving fraud detection via imbalanced graph structure learning](<https://doi.org/10.1007/s10994-023-06464-0>)<br>Machine Learning 2024 · 方法 · Lingfei Ren et al.<br><code>igsl-2024</code> | 有监督，类别平衡采样 · 节点 · 多关系欺诈图<br>欺诈识别、节点 | 按关系和类别采样，迭代学习同配邻接，借助锚节点降低构图代价。 |
| <a id="p-ijcai-robust-fraud-2024"></a>[Safeguarding Fraud Detection from Attacks: A Robust Graph Learning Approach](<https://doi.org/10.24963/ijcai.2024/830>)<br>IJCAI 2024 · 方法 · Jiasheng Wu et al.<br><code>ijcai-robust-fraud-2024</code> | 欺诈标签；扰动威胁模型 · 节点 · 金融欺诈 | 特征和结构共同被扰动时评估鲁棒性，不能把随机删除边当作真实对抗行为。 |
| <a id="p-interactive-fraud-2023"></a>[Fraud detection on multi-relation graphs via imbalanced and interactive learning](<https://www.sciencedirect.com/science/article/pii/S0020025523007387>)<br>Information Sciences 2023 · 方法 · Xiaodi Wang, Zhonglin Liu, Jiamiao Liu, Jiayong Liu<br><code>interactive-fraud-2023</code> | 有监督，类别不平衡 · 节点 · 多关系欺诈图<br>欺诈识别、节点 | 将类别不平衡与不同关系之间的信息交互纳入检测。 |
| <a id="p-gaga-2023"></a>[Label Information Enhanced Fraud Detection against Low Homophily in Graphs](<https://doi.org/10.1145/3543507.3583373>)<br>WWW 2023 · 方法 · Yuchen Wang et al.<br><code>gaga-2023</code> | 有监督，聚合标签信息 · 节点 · 欺诈关系图<br>欺诈识别、节点 | 按邻居标签分组聚合，用 Transformer 处理低同配邻域中的多组信息。 |
| <a id="p-contrastive-fraud-2022"></a>[Contrastive graph neural network-based camouflaged fraud detector](<https://www.sciencedirect.com/science/article/pii/S0020025522011926>)<br>Information Sciences 2022 · 方法 · Zexuan Deng et al.<br><code>contrastive-fraud-2022</code> | 有监督，辅以对比学习 · 节点 · 多关系欺诈图<br>欺诈识别、节点 | 通过对比学习改进邻居相似度度量与跨关系聚合，以识别伪装节点。 |
| <a id="p-dagad-2022"></a>[DAGAD: Data Augmentation for Graph Anomaly Detection](<https://arxiv.org/abs/2210.09766>)<br>IEEE ICDM 2022 · 方法 · Fanzhen Liu et al.<br><code>dagad-2022</code> | 有监督，利用稀缺异常样本 · 节点 · 属性图<br>欺诈识别、节点 | 通过图编码融合与样本增强扩充训练集，用针对类别不平衡的目标区分正常及异常。 |
| <a id="p-h2-fdetector-2022"></a>[H2-FDetector: A GNN-based Fraud Detector with Homophilic and Heterophilic Connections](<https://doi.org/10.1145/3485447.3512195>)<br>WWW 2022 · 方法 · Fengzhao Shi et al.<br><code>h2-fdetector-2022</code> | 有监督，正常与欺诈节点 · 节点 · 欺诈关系图<br>欺诈识别、节点 | 区分同配边与异配边，分别建模邻居提供的信息。 |
| <a id="p-pc-gnn"></a>[Pick and Choose: A GNN-based Imbalanced Learning Approach for Fraud Detection](<https://doi.org/10.1145/3442381.3449989>)<br>The Web Conference (WWW) 2021 · 经典方法 · Yang Liu et al.<br><code>pc-gnn</code> | 双类标签 · 节点 · 图欺诈<br>经典回溯、PC-GNN | 把少数类节点采样与邻居选择分开观察，检验训练重采样能否改善稀有类排序。<br>[代码](<https://github.com/PonderLY/PC-GNN>) |
| <a id="p-care-gnn"></a>[Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged Fraudsters](<https://arxiv.org/abs/2008.08692>)<br>CIKM 2020 · 经典方法 · Yingtong Dou et al.<br><code>care-gnn</code> | 双类标签 · 节点 · 评论和用户欺诈<br>经典回溯 | 研究异常对象混入正常邻居时如何选择可信邻居。业务迁移时要重新解释每种边。<br>[代码](<https://github.com/YingtongDou/CARE-GNN>) |

<a id="branch-4"></a>
<a id="branch-b2"></a>

### B2 图结构信号与可解释性

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-dgp-2026"></a>[DGP: A Dual-Granularity Prompting Framework for Fraud Detection with Graph-Enhanced LLMs](<https://doi.org/10.1609/aaai.v40i18.38541>)<br>AAAI 2026 · 方法 · Y. Li et al.<br><code>dgp-2026</code> | 有监督欺诈检测 · 节点/文本属性 · 金融及其他欺诈 | 分别压缩邻居摘要和保留目标细节，适合分析图文信息瓶颈，非核心数值基线。 |
| <a id="p-weixin-credit-graph"></a>[Empowering Credit Risk Detection in Weixin Pay with Billion-Scale Deep Graph Learning](<https://doi.org/10.1145/3770855.3818397>)<br>KDD 2026 · 工业信用风险 · Xin Liu et al.<br><code>weixin-credit-graph</code> | 平台风险标签监督，标签确认与延迟需按业务数据说明复核 · 用户 · 微信支付信用风险<br>微信支付信用风险、用户 | 对大规模异构用户风险图分区，为关键节点保留跨分区上下文并对齐表示。平台风险定义不能直接映射为洗钱账户标签。 |
| <a id="p-fraudgnam"></a>[FraudGNAM: Inherently Interpretable Spectral GNN for Graph Fraud Detection](<https://proceedings.mlr.press/v337/lee26e.html>)<br>UAI 2026 · 方法 · Suan Lee and Jinho Kim<br><code>fraudgnam</code> | 双类标签 · 节点 · 图欺诈 | 把谱域建模和可解释的特征贡献放在同一模型里，适合讨论调查人员能读到何种解释。 |
| <a id="p-frequency-fraud-2026"></a>[Learning frequency-aware graph fraud detection](<https://www.sciencedirect.com/science/article/pii/S0893608026000626>)<br>Neural Networks 2026 · 方法 · Wei Zhao, Hao Chen<br><code>frequency-fraud-2026</code> | 有监督，类别不平衡 · 节点 · 欺诈关系图<br>欺诈识别、节点 | 以图频域模型 F-GNN 处理同配和异配连接并存情形。 |
| <a id="p-dnb-aml"></a>[Finding money launderers using heterogeneous graph neural networks](<https://doi.org/10.1016/j.jfds.2025.100175>)<br>The Journal of Finance and Data Science 2025 · 方法与银行实证 · Fredrik Johannessen and Martin Jullum<br><code>dnb-aml</code> | 基于调查记录的双类标签 · 自然人节点 · 挪威银行反洗钱<br>银行真实数据、异质图、调查标签 | 把银行交易与企业任职关系联系起来。正例表示进入调查，评价结论应按此口径解释。作者代码公开，原始银行数据受限。<br>[代码](<https://github.com/fredjo89/heterogeneous-mpnn>) |
| <a id="p-naast-gnn"></a>[NAAST-GNN: Neighborhood Adaptive Aggregation and Spectral Tuning for Graph Anomaly Detection](<https://doi.org/10.24963/ijcai.2025/317>)<br>IJCAI 2025 · 方法 · Ronghui Guo, Xiaowang Zhang, Zhizhi Yu, Minghui Zou, Sai Zhang and Zhiyong Feng<br><code>naast-gnn</code> | 双类节点标签，加权交叉熵 · 节点（按数据集区分账户、用户或评论） · 评论、社交及金融账户图<br>NAAST-GNN、频谱、自适应邻居 | 按节点类别预测和邻域构成调整聚合与谱滤波。注意论文对部分基线采用了原作成绩。<br>[精读卡](../notes/naast-gnn.md) |
| <a id="p-hogrl-2024"></a>[Effective High-order Graph Representation Learning for Credit Card Fraud Detection](<https://doi.org/10.24963/ijcai.2024/839>)<br>IJCAI 2024 · 方法 · Yao Zou and Dawei Cheng<br><code>hogrl-2024</code> | 有监督欺诈标签 · 交易/客户目标依建图定义 · 信用卡欺诈 | 高阶交易图与混合阶数专家注意力，检验多跳信息是否胜过简单规则统计。 |
| <a id="p-diam"></a>[Effective Illicit Account Detection on Large Cryptocurrency MultiGraphs](<https://doi.org/10.1145/3627673.3679707>)<br>CIKM 2024 · 方法与公开数据 · Zhihao Ding et al.<br><code>diam</code> | 已标正常与风险地址参与监督；其余地址未标注 · 账户地址节点 · 以太坊、比特币交易<br>DIAM | DIAM 从平行交易的方向和顺序形成账户表示；通过四个公开链上账户数据集检验保留重复交易是否有价值。<br>[代码](<https://github.com/TommyDzh/DIAM>) · [精读卡](../notes/diam.md) |
| <a id="p-gfp-icaif"></a>[Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection](<https://research.ibm.com/publications/graph-feature-preprocessor-real-time-subgraph-based-feature-extraction-for-financial-crime-detection>)<br>ACM ICAIF 2024 · 特征及强基线 · Jovan Blanuša et al.<br><code>gfp-icaif</code> | 监督学习，标签来自各数据集 · 交易边或地址，按数据集 · 合成银行交易与以太坊<br>合成银行交易与以太坊、交易边或地址，按数据集 | 在到达的交易流上维护局部模式与账户统计，再交给树模型排序。比较时需给树模型和 GNN 同一窗口、历史和算力预算。 |
| <a id="p-sec-gfd"></a>[Revisiting Graph-Based Fraud Detection in Sight of Heterophily and Spectrum](<https://doi.org/10.1609/aaai.v38i8.28773>)<br>AAAI · Technical Track 2024 · 方法 · Fan Xu, Nan Wang, Hao Wu, Xuezhi Wen, Xibin Zhao and Hai Wan<br><code>sec-gfd</code> | 双类节点标签，训练图中有未标注节点；作者称半监督 · 节点（按数据集区分账户、用户或评论） · 评论、社交及金融账户图<br>图异配性、频谱、SEC-GFD | 通过混合频带滤波和局部约束比较多跳真实邻域与特征相似的邻域。复现时记录两类标签数。<br>[精读卡](../notes/sec-gfd.md) |
| <a id="p-ghrn-2023"></a>[Addressing Heterophily in Graph Anomaly Detection: A Perspective of Graph Spectrum](<https://doi.org/10.1145/3543507.3583268>)<br>WWW 2023 · 方法 · Yuan Gao et al.<br><code>ghrn-2023</code> | 有监督，考虑异配边 · 节点 · 欺诈与异常节点图<br>欺诈识别、节点 | 从图谱信号分析异配性，按边的作用调整传播关系。<br>[代码](<https://github.com/blacksingular/GHRN>) |
| <a id="p-stream-explanation"></a>[Example-based explanations for streaming fraud detection on graphs](<https://doi.org/10.1016/j.ins.2022.11.119>)<br>Information Sciences 2023 · 方法 · Thanh Tam Nguyen et al.<br><code>stream-explanation</code> | 解释已有检测结果，非独立监督条件 · 流式欺诈检测结果的案例解释 · 网络平台欺诈<br>动态图、时间评测 | 利用图相似度从流式案例中选择有用解释，评估选择效用与速度。解释效用和命中率是不同指标，不能用解释速度代替检测性能。 |
| <a id="p-phish2vec"></a>[Tracking phishing on Ethereum: Transaction network embedding approach for accounts representation learning](<https://doi.org/10.1016/j.cose.2023.103479>)<br>Computers &amp; Security 2023 · 地址表示 · Zhutian Lin et al.<br><code>phish2vec</code> | 无监督表征，已标注地址供下游分类 · 地址节点 · 以太坊交易<br>以太坊交易、地址节点 | 将发生时间、金额和对手类型用于构造地址游走序列，配合统计特征采样。采样策略会改变负例难度，比较时需共享测试地址。 |
| <a id="p-bwgnn"></a>[Rethinking Graph Neural Networks for Anomaly Detection](<https://proceedings.mlr.press/v162/tang22b.html>)<br>ICML 2022 · 方法 · Jianheng Tang et al.<br><code>bwgnn</code> | 双类标签 · 节点 · 金融与通用属性图<br>BWGNN | BWGNN 以带通滤波捕捉被平滑掩盖的异常信号；与属性基线、邻域特征加树模型同场比较。<br>[代码](<https://github.com/squareRoot3/Rethinking-Anomaly-Detection>) · [模型卡](../models/bwgnn.md) |
| <a id="p-xfraud-vldb"></a>[xFraud: Explainable Fraud Transaction Detection](<https://doi.org/10.14778/3494124.3494128>)<br>Proceedings of the VLDB Endowment (PVLDB) 2022 · 可解释交易检测 · Susie Xi Rao et al.<br><code>xfraud-vldb</code> | 监督交易合法性分类，解释器提取局部证据 · 交易节点及相关实体 · 电商真实交易<br>电商真实交易、交易节点及相关实体 | 异构图检测器为交易打分，解释器返回与预测相关的实体和关系。局部解释的直观性不能代替有因果含义的欺诈证据。<br>[代码](<https://github.com/eBay/xFraud>) |

<a id="branch-5"></a>
<a id="branch-b3"></a>

### B3 交易边与可疑子图

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-spoofing-2025"></a>[Multi-Granularity Augmented Graph Learning for Spoofing Transaction Detection](<https://doi.org/10.1145/3696410.3714521>)<br>The Web Conference (WWW) 2025 · 方法 · Xin Liu et al.<br><code>spoofing-2025</code> | 标签细节待查 · 交易 · 证券交易欺诈 | 将多粒度关系用于虚假交易识别；需与银行 AML 场景区分。 |
| <a id="p-uniform-2025"></a>[UniFORM: Towards Unified Framework for Anomaly Detection on Graphs](<https://doi.org/10.1609/aaai.v39i12.33369>)<br>AAAI 2025 · 方法 · C. Song et al.<br><code>uniform-2025</code> | 自监督/少标签 · 节点、边、图 · 多粒度图 | 用统一子图视角连接多粒度异常，注意输出和标签实体不能混为一谈。 |
| <a id="p-fraudgt"></a>[FraudGT: A Simple, Effective, and Efficient Graph Transformer for Financial Fraud Detection](<https://doi.org/10.1145/3677052.3698648>)<br>ACM ICAIF 2024 · 方法 · Junhong Lin et al.<br><code>fraudgt</code> | 模拟器提供正常与洗钱交易标签 · 交易边 · 合成银行交易<br>合成银行交易、交易边 | 将边属性纳入图注意力，为同一账户之间的多笔交易分别评分。同一生成器的六个配置共享规则，不能用来估计真实银行命中率。<br>[代码](<https://github.com/junhongmit/FraudGT>) · [精读卡](../notes/fraudgt.md) |
| <a id="p-revclassify"></a>[Identifying Money Laundering Subgraphs on the Blockchain](<https://doi.org/10.1145/3677052.3698635>)<br>ACM ICAIF 2024 · 方法 · Kiwhan Song et al.<br><code>revclassify</code> | 有标注候选子图 · 子图 · 比特币反洗钱<br>RevClassify | 分别记录给定候选的分类效果，以及整图中找到候选的成本和召回。 |
| <a id="p-ponziguard"></a>[PonziGuard: Detecting Ponzi Schemes on Ethereum with Contract Runtime Behavior Graph (CRBG)](<https://doi.org/10.1145/3597503.3623318>)<br>ICSE 2024 · 合约图分类 · Ruichao Liang et al.<br><code>ponziguard</code> | 有真值的合约分类，另做主网应用 · 智能合约整体 · 以太坊资金盘<br>以太坊资金盘、智能合约整体 | 将运行时行为表示为图，用图分类模型筛查可能的庞氏合约。一个合约的风险分类不能直接推广到其全部交易或用户。 |
| <a id="p-multi-gnn"></a>[Provably Powerful Graph Neural Networks for Directed Multigraphs](<https://ojs.aaai.org/index.php/AAAI/article/view/29069>)<br>AAAI 2024 · 方法 · Béni Egressy et al.<br><code>multi-gnn</code> | 双类标签 · 交易边等 · 合成反洗钱、网络钓鱼<br>Multi-GNN | 针对方向和重复边改造消息传递；用来检验把多笔往来合并为一条边究竟损失什么。 |
| <a id="p-unigad-2024"></a>[UniGAD: Unifying Multi-level Graph Anomaly Detection](<https://proceedings.nips.cc/paper_files/paper/2024/hash/f57de20ab7bb1540bcac55266ebb5401-Abstract-Conference.html>)<br>NeurIPS 2024 · 方法 · Yiqing Lin et al.<br><code>unigad-2024</code> | 多任务有监督，部分标签由规则生成 · 节点、边、整图 · 多域，含 T-Finance<br>多粒度对象、节点、边、整图 | 将不同层级的目标表示成子图，联合训练并调节任务间的梯度冲突。<br>[精读卡](../notes/unigad-2024.md) |
| <a id="p-group-aware-aml"></a>[Anti-Money Laundering by Group-Aware Deep Graph Learning](<https://doi.org/10.1109/TKDE.2023.3272396>)<br>IEEE Transactions on Knowledge and Data Engineering 2023 · 团伙检测 · Dawei Cheng et al.<br><code>group-aware-aml</code> | 依据金融机构样本评估；标签是账户还是团伙须按实验核定 · 交易图中的账户及关联团伙 · 银行卡组织真实交易<br>银行卡组织真实交易、交易图中的账户及关联团伙 | 用社区中心编码和局部增强形成团伙候选，研究账户之间的协同行为。仅有论文公开的运行结果，不能重建未知标签的核查程序。 |
| <a id="p-gfdn-ecommerce"></a>[Group-based Fraud Detection Network on e-Commerce Platforms](<https://doi.org/10.1145/3580305.3599836>)<br>KDD 2023 · 群组欺诈检测 · Jianke Yu et al.<br><code>gfdn-ecommerce</code> | 用平台及竞赛标签评估团体性欺诈行为 · 顾客与商品交互中的群组作弊行为 · 电商点击关系<br>电商点击关系、顾客与商品交互中的群组作弊行为 | 在顾客—商品二部图内考虑集体交互而非仅依赖单条记录。点击作弊与银行账户交易不同，需先重新定义边和复核单位。<br>[代码](<https://github.com/yujianke100/GFDN>) |
| <a id="p-igad-2022"></a>[Dual-discriminative Graph Neural Network for Imbalanced Graph-level Anomaly Detection](<https://proceedings.neurips.cc/paper_files/paper/2022/hash/98a625423070cfc6ae3d82d4b59408a0-Abstract-Conference.html>)<br>NeurIPS 2022 · 方法 · Ge Zhang et al.<br><code>igad-2022</code> | 有监督，少数类为异常整图 · 整图 · 通用图集合<br>多粒度对象、整图 | 将属性卷积与刻画子结构的深度随机游走核结合，以点互信息损失处理类别不平衡。 |
| <a id="p-flowscope"></a>[FlowScope: Spotting Money Laundering Based on Graphs](<https://doi.org/10.1609/aaai.v34i04.5906>)<br>AAAI 2020 · 经典方法 · Xiangfeng Li et al.<br><code>flowscope</code> | 基于流结构的无标签候选发现 · 资金流路径所涉及的账户群 · 资金转移网络<br>资金转移网络、资金流路径所涉及的账户群 | 在多部图中寻找连接连续且中间节点资金流入流出接近的子图。流量近似守恒不是案件定性依据，正规中介也可能有类似结构。<br>[代码](<https://github.com/csqjxiao/FlowScope>) |

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
| <a id="p-spacegnn-2025"></a>[SpaceGNN: Multi-Space Graph Neural Network for Node Anomaly Detection with Extremely Limited Labels](<https://proceedings.iclr.cc/paper_files/paper/2025/hash/24f7b98aef14fcd68acf3c941af1b59e-Abstract-Conference.html>)<br>ICLR 2025 · 方法 · Xiangyu Dong et al.<br><code>spacegnn-2025</code> | 少量正常与异常节点标签 · 节点 · 多域，含 T-Finance 与 DGraph-Fin<br>有限标签、节点 | 综合欧氏、双曲与球面空间的预测以处理少标签节点异常。<br>[代码](<https://github.com/xydong127/SpaceGNN>) · [精读卡](../notes/spacegnn-2025.md) |
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
| <a id="p-m-glad-2026"></a>[Unsupervised Graph-Level Anomaly Detection via Multi-granular Graph Structure Learning](<https://ijcai.org/proceedings/2026/355>)<br>IJCAI 2026 · 方法 · Ge Zhang et al.<br><code>m-glad-2026</code> | 无监督整图检测 · 整图 · 多粒度图集合<br>无监督与自监督、整图 | 在不同粗化层级学习正常原型，再据各层级偏离程度判定整图异常。 |
| <a id="p-huge-2025"></a>[A Label-free Heterophily-guided Approach for Unsupervised Graph Fraud Detection](<https://doi.org/10.1609/aaai.v39i12.33356>)<br>AAAI 2025 · 方法 · Junjun Pan et al.<br><code>huge-2025</code> | 训练无人工标签 · 欺诈节点 · 欺诈图 | 以 HALO 无标签异配性估计引导对齐与排序；可作节点图无监督对照。 |
| <a id="p-curvgad-2025"></a>[CurvGAD: Leveraging Curvature for Enhanced Graph Anomaly Detection](<https://proceedings.mlr.press/v267/grover25a.html>)<br>ICML 2025 · 方法 · Karish Grover et al.<br><code>curvgad-2025</code> | 重建式无监督 · 节点 · 通用图 | 曲率、属性和结构异常分开重建；可与交易图中的高阶局部形态对照。<br>[代码](<https://github.com/karish-grover/curvgad>) |
| <a id="p-agdiff-2025"></a>[Leveraging Diffusion Model as Pseudo-Anomalous Graph Generator for Graph-Level Anomaly Detection](<https://proceedings.mlr.press/v267/cai25l.html>)<br>ICML 2025 · 方法 · Jinyu Cai et al.<br><code>agdiff-2025</code> | 仅正常图或极少异常 · 整图 · 通用图 | 潜空间扩散制造边界附近异常图；适用整图异常而不是账户节点的直接基线。 |
| <a id="p-megad-2025"></a>[MEGAD: A Memory-Efficient Framework for Large-Scale Attributed Graph Anomaly Detection](<https://doi.org/10.24963/ijcai.2025/406>)<br>IJCAI 2025 · 方法 · Yifan Zhang et al.<br><code>megad-2025</code> | 重建型无监督 · 节点 · 大规模属性图 | 大图内存效率与异常排序共同比较，记录峰值显存而非只报 AUROC。 |
| <a id="p-clean-view-2025"></a>[Rethinking Contrastive Learning in Graph Anomaly Detection: A Clean-View Perspective](<https://doi.org/10.24963/ijcai.2025/335>)<br>IJCAI 2025 · 方法 · Di Jin et al.<br><code>clean-view-2025</code> | 对比学习设定需核 · 节点 · 通用图 | 反思受干扰边对节点-子图相似性假设的破坏，适合研究如何筛除噪声邻域。 |
| <a id="p-sdm-2025"></a>[Self-Discriminative Modeling for Anomalous Graph Detection](<https://proceedings.mlr.press/v267/cai25k.html>)<br>ICML 2025 · 方法 · Jinyu Cai et al.<br><code>sdm-2025</code> | 训练仅正常图 · 整图 · 通用图 | 联合生成伪异常图并训练判别器，适合跨到团伙子图任务前先明确候选子图。 |
| <a id="p-ada-gad-2024"></a>[ADA-GAD: Anomaly-Denoised Autoencoders for Graph Anomaly Detection](<https://ojs.aaai.org/index.php/AAAI/article/view/28691>)<br>AAAI 2024 · 方法 · Junwei He et al.<br><code>ada-gad-2024</code> | 无监督重构 · 节点 · 属性图<br>无监督与自监督、节点 | 在降低异常成分的图上预训练，再利用解码器重构原始图。 |
| <a id="p-dualgad-2024"></a>[DualGAD: Dual-bootstrapped self-supervised learning for graph anomaly detection](<https://www.sciencedirect.com/science/article/pii/S002002552400433X>)<br>Information Sciences 2024 · 方法 · Hui Tang, Xun Liang, Jun Wang, Sensen Zhang<br><code>dualgad-2024</code> | 自监督，无异常类别监督 · 节点 · 属性图<br>无监督与自监督、节点 | 以双重自举式自监督学习建模属性与结构中的异常不一致。 |
| <a id="p-gad-nr-2024"></a>[GAD-NR: Graph Anomaly Detection via Neighborhood Reconstruction](<https://pmc.ncbi.nlm.nih.gov/articles/PMC11867731/>)<br>WSDM 2024 · 方法 · Amit Roy et al.<br><code>gad-nr-2024</code> | 无监督重构 · 节点 · 属性图<br>无监督与自监督、节点 | 重构自身属性、度及邻居特征分布，以邻域重构误差给节点排序。<br>[精读卡](../notes/gad-nr-2024.md) |
| <a id="p-anomman-2023"></a>[AnomMAN: Detect anomalies on multi-view attributed networks](<https://www.sciencedirect.com/science/article/pii/S0020025523000890>)<br>Information Sciences 2023 · 方法 · Linghao Chen et al.<br><code>anomman-2023</code> | 属性网络异常检测，视图重构 · 节点 · 多视图属性图<br>无监督与自监督、节点 | 通过注意力给不同关系视图赋权，联合处理属性与各类连接。 |
| <a id="p-mssgad-2023"></a>[Graph Anomaly Detection via Multi-Scale Contrastive Learning Networks with Augmented View](<https://ojs.aaai.org/index.php/AAAI/article/view/25907>)<br>AAAI 2023 · 方法 · Jingcan Duan et al.<br><code>mssgad-2023</code> | 自监督多尺度对比 · 节点 · 属性图<br>无监督与自监督、节点 | 增加子图之间的对比和增强视图，以补充节点与局部子图的关系。 |
| <a id="p-signet-2023"></a>[Towards Self-Interpretable Graph-Level Anomaly Detection](<https://proceedings.neurips.cc/paper_files/paper/2023/hash/1c6f06863df46de009a7a41b41c95cad-Abstract-Conference.html>)<br>NeurIPS 2023 · 方法 · Yixin Liu et al.<br><code>signet-2023</code> | 正常整图训练集，自监督损失 · 整图及其解释子图 · 分子、图像、合成与社交图等<br>无监督与自监督、整图及其解释子图 | 分别编码节点视图和边的对偶超图，寻找能解释整图异常分的瓶颈子图。<br>[代码](<https://github.com/yixinliu233/SIGNET>) · [精读卡](../notes/signet-2023.md) |
| <a id="p-tam-2023"></a>[Truncated Affinity Maximization: One-class Homophily Modeling for Graph Anomaly Detection](<https://papers.neurips.cc/paper_files/paper/2023/hash/9b905031125e56a557db38dff4fa8d21-Abstract-Conference.html>)<br>NeurIPS 2023 · 方法 · Hezhe Qiao, Guansong Pang<br><code>tam-2023</code> | 无标签训练 · 节点 · 属性图，社交与评论等<br>无监督与自监督、节点 | 按局部亲和度建模正常节点的同配性，在多个截断图上学习表示。<br>[代码](<https://github.com/mala-lab/TAM-master>) · [精读卡](../notes/tam-2023.md) |
| <a id="p-cola"></a>[Anomaly Detection on Attributed Networks via Contrastive Self-Supervised Learning](<https://doi.org/10.1109/TNNLS.2021.3068344>)<br>IEEE TNNLS 2022 · 对照方法 · Yixin Liu et al.<br><code>cola</code> | 无真实标签，自监督 · 节点 · 通用属性图 | 用节点与局部子图的对比学习刻画异常。作为标签收益的对照；2021 年在线，2022 年编入卷期。<br>[代码](<https://github.com/TrustAGI-Lab/CoLA>) |
| <a id="p-comga-2022"></a>[ComGA: Community-Aware Attributed Graph Anomaly Detection](<https://researchers.mq.edu.au/en/publications/comga-community-aware-attributed-graph-anomaly-detection/>)<br>WSDM 2022 · 方法 · Xuexiong Luo et al.<br><code>comga-2022</code> | 无监督 · 节点 · 静态属性图<br>无监督与自监督、节点 | 显式利用社区信息与专门设计的图卷积，识别局部、全局和结构异常节点。 |
| <a id="p-conad-2022"></a>[Contrastive Attributed Network Anomaly Detection with Data Augmentation](<https://doi.org/10.1007/978-3-031-05936-0_35>)<br>PAKDD 2022 · 方法 · Zhiming Xu et al.<br><code>conad-2022</code> | 自监督，人工增强信号 · 节点 · 属性图<br>无监督与自监督、节点 | 给属性图注入模拟异常做对比增强，训练时利用构造的异常知识。<br>[代码](<https://github.com/zhiming-xu/conad>) |
| <a id="p-laundrograph"></a>[LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering](<https://doi.org/10.1145/3533271.3561727>)<br>ACM ICAIF 2022 · 方法与银行案例 · Mário Cardoso, Pedro Saleiro, Pedro Bizarro<br><code>laundrograph</code> | 自监督，以已存在的客户—交易关系和采样非边训练 · 客户与交易之间的关系 · 真实银行转账<br>真实银行转账、客户与交易之间的关系 | 用二部图学习客户通常参与哪些交易，以链接分数衡量行为偏离。表 1 预测已发生关系与随机非边，测试正类并非经查实的洗钱交易。<br>[精读卡](../notes/laundrograph.md) |
| <a id="p-sub-cr-2022"></a>[Reconstruction Enhanced Multi-View Contrastive Learning for Anomaly Detection on Attributed Networks](<https://ijcai.org/proceedings/2022/330>)<br>IJCAI 2022 · 方法 · Jiaqiang Zhang, Senzhang Wang, Songcan Chen<br><code>sub-cr-2022</code> | 自监督对比及属性重构 · 节点 · 属性图<br>无监督与自监督、节点 | 联合局部、全局结构视图上的对比任务与掩蔽属性重构。 |

<a id="branch-10"></a>
<a id="branch-d2"></a>

### D2 时间演化与未见异常

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-ares-edge-stream"></a>[ARES: Anomaly Recognition Model For Edge Streams](<https://doi.org/10.1145/3770854.3780242>)<br>KDD · Research 2026 · 方法 · Simone Mungari et al.<br><code>ares-edge-stream</code> | 无监督训练，验证和测试用途单列 · 按到达时间评分的边 · 一般事件流，另有比特币信任网络<br>ARES | ARES 用图表示结合半空间树为流式关系评分，可作为 TransXion 交易边模型的无标签在线对照。<br>[代码](<https://github.com/AnomalyRecognitionModelForEdgeStreams/ARES>) · [精读卡](../notes/ares-edge-stream.md) |
| <a id="p-dynamic-limited"></a>[Learning Discriminative and Generalizable Anomaly Detector for Dynamic Graph with Limited Supervision](<https://proceedings.mlr.press/v306/tian26h.html>)<br>ICML 2026 · 方法 · Yuxing Tian et al.<br><code>dynamic-limited</code> | 有限异常标签或无异常标签 · 动态交互 · 通用动态图<br>动态图 | 研究动态交互和未见异常，阅读时区分“测试时刻更晚”与“异常类型未见”两种泛化。 |
| <a id="p-spectral-shifts-2026"></a>[Modeling Spectral Energy Shifts in Spatio-Temporal Graph Anomaly Detection](<https://proceedings.mlr.press/v306/liu26gb.html>)<br>ICML 2026 · 方法 · Yilin Liu et al.<br><code>spectral-shifts-2026</code> | 标签条件待查 · 节点 · 时空图 | 不仅捕捉谱能量升高，还关注伪装异常中的下降信号。 |
| <a id="p-temg-tta-2026"></a>[Temporal Motif-aware Graph Test-time Adaptation for OOD Blockchain Anomaly Detection](<https://doi.org/10.24963/ijcai.2026/802>)<br>IJCAI 2026 · 方法 · Runang He, Tongya Zheng, Huiling Peng, Yuanyu Wan, Bingde Hu, Jiawei Chen, Canghong Jin, Mingli Song, Can Wang<br><code>temg-tta-2026</code> | 源域两类标签，目标图无标签测试时适应 · 区块链地址节点 · 区块链异常 | 以时序模体和目标图无标签适应校准地址风险。不同源–目标事件的 AUC-PRC 增量应分别报告。<br>[代码](<https://github.com/LuoXishuang0712/TEMG-TTA/>) · [精读卡](../notes/temg-tta-2026.md) |
| <a id="p-bad-dynamic"></a>[Unsupervised Anomaly Detection in Dynamic Graphs via Compatibility Modeling and Boundary Learning](<https://doi.org/10.24963/ijcai.2026/322>)<br>IJCAI 2026 · 方法 · Jiachi Luo et al.<br><code>bad-dynamic</code> | 无监督拟合；对照方法中有监督分类头 · 逐次交互打分，用户状态或信任评级构成基准标签 · 在线平台、比特币信任网络<br>动态图、时间评测 | 让目标节点与来源近期邻居交叉注意，再用归一化流估计正常交互的似然。可学习身份嵌入对新用户的适用性需另测；部分基线使用的标签不同。<br>[精读卡](../notes/bad-dynamic.md) |
| <a id="p-abnet-2025"></a>[ABNet: Mitigating Sample Imbalance in Anomaly Detection Within Dynamic Graphs](<https://doi.org/10.24963/ijcai.2025/324>)<br>IJCAI 2025 · 方法 · Yifan Hong et al.<br><code>abnet-2025</code> | 无监督/半监督场景，正文需区分 · 动态图节点 · 动态图 | 时点差分、异常增强和元学习适配；需复核增强样本是否使用了未来时段。 |
| <a id="p-mutationguard-2025"></a>[MutationGuard: A Graph and Temporal-Spatial Neural Method for Detecting Mutation Telecommunication Fraud](<https://doi.org/10.24963/ijcai.2025/1061>)<br>IJCAI 2025 · 方法 · Haitao Bai et al.<br><code>mutationguard-2025</code> | 有标签电诈 · 通话账号/交互 · 电信欺诈 | 通信图与通话时间空间语义融合；金融账户迁移仅是研究设想，不能直接推断金融效果。 |
| <a id="p-taad-dynamic"></a>[TAAD: Time-varying adversarial anomaly detection in dynamic graphs](<https://doi.org/10.1016/j.ipm.2024.103912>)<br>Information Processing &amp; Management 2025 · 方法 · Guanghua Liu et al.<br><code>taad-dynamic</code> | 历史异常知识迁移，摘要未报告标签预算 · 节点 · 动态图<br>动态图、时间评测 | 通过对抗训练减少跨时期特征分布偏移，用打分器刻画正常与异常节点的表示差异。对齐隐藏分布也可能抹去实际风险变化。 |
| <a id="p-tempasd"></a>[TempASD: Temporal Anomalous Subgraph Discovery in Large-Scale Dynamic Financial Networks](<https://doi.org/10.1145/3711896.3737149>)<br>KDD · Research 2025 · 方法与金融实证 · Xiaolin Han et al.<br><code>tempasd</code> | 部分数据有异常训练线索，另以统计规则生成训练候选 · 时序子图及其成员 · 以太坊交易、NFT 交易<br>TEMPASD | 把交易金额的首位数字分布与时序密集程度结合，直接在大型网络中搜索异常子图；区分已知案例与统计代理线索。<br>[代码](<https://github.com/KZ-code/TempASD>) · [精读卡](../notes/tempasd.md) |
| <a id="p-dynacd"></a>[Community detection and anomaly prediction in dynamic networks](<https://doi.org/10.1038/s42005-024-01889-y>)<br>Communications Physics 2024 · 方法 · Hadiseh Safdari, Caterina De Bacco<br><code>dynacd</code> | 生成模型，无标签推断隐变量 · 异常边与节点社区 · 动态交互网络<br>动态图、时间评测 | 以社区结构建模常态，通过马尔可夫时序转移推断边的异常隐变量。常态社区参数的可辨识程度影响异常归因。 |
| <a id="p-bright-cikm"></a>[BRIGHT - Graph Neural Networks in Real-time Fraud Detection](<https://doi.org/10.1145/3511808.3557136>)<br>CIKM 2022 · 工程与方法 · Mingxuan Lu et al.<br><code>bright-cikm</code> | 监督交易分类，历史标签用于训练 · 新到达的支付交易 · 电商支付<br>电商支付、新到达的支付交易 | 先离线生成历史实体表示，再结合当前交易在线打分。离线批计算成本和缓存刷新频率也需计入复现。<br>[精读卡](../notes/bright-cikm.md) |

<a id="branch-11"></a>
<a id="branch-d3"></a>

### D3 预训练与少样本迁移

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-grade-2026"></a>[Geometry-Aware Riemannian Residual Displacement for Cross-Broad-Domain Graph Anomaly Detection](<https://doi.org/10.24963/ijcai.2026/342>)<br>IJCAI 2026 · 方法 · Senyong Wang et al.<br><code>grade-2026</code> | 跨域零样本/少样本 · 节点 · 跨领域图 | 在属性异质、拓扑差异均较大的目标图迁移，需跟纯目标图无标签训练区分。 |
| <a id="p-mv-fgad-2026"></a>[MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning](<https://proceedings.mlr.press/v306/yan26i.html>)<br>ICML 2026 · 方法 · Junyi Yan et al.<br><code>mv-fgad-2026</code> | 联邦多客户端，监督条件待查 · 节点 · 多机构分图 | 研究分布式弱异常与结构分割下的检出；不等同于已经有合法跨机构数据。 |
| <a id="p-apf"></a>[Towards Anomaly-Aware Pre-Training and Fine-Tuning for Graph Anomaly Detection](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/dd2094ecf134f7c9740fb29640bfb620-Abstract-Conference.html>)<br>ICLR 2026 · 方法 · Yunhui Liu, Jiashun Cheng et al.<br><code>apf</code> | 无标签预训练＋少量标签微调 · 节点 · 通用属性图 | 核对预训练阶段看过的图及微调阶段使用的标签。少样本微调与目标域零标签要分别记录。<br>[代码](<https://github.com/Cloudy1225/APF>) |
| <a id="p-anomalygfm"></a>[AnomalyGFM: Graph Foundation Model for Zero/Few-shot Anomaly Detection](<https://doi.org/10.1145/3711896.3736843>)<br>KDD 2025 · 方法 · Hezhe Qiao, Chaoxi Niu, Ling Chen and Guansong Pang<br><code>anomalygfm</code> | 源图含正常和异常标签；目标图零标签或仅少量正常标签 · 节点 · 跨评论、金融、社交等属性图<br>AnomalyGFM、跨图迁移、零样本与少样本 | 用节点相对邻居的表示残差对齐正常与异常原型。在新图上比较零标签推理和少量正常标签提示调优。<br>[代码](<https://github.com/mala-lab/AnomalyGFM>) · [精读卡](../notes/anomalygfm.md) |
| <a id="p-ia-ggad-2025"></a>[IA-GGAD: Zero-shot Generalist Graph Anomaly Detection via Invariant and Affinity Learning](<https://proceedings.neurips.cc/paper_files/paper/2025/hash/788f9787ec93e3e1f34658fb003a1f44-Abstract-Conference.html>)<br>NeurIPS 2025 · 迁移方法 · Xiong Zhang et al.<br><code>ia-ggad-2025</code> | 跨域训练，目标图零样本 · 节点 · 跨域属性图<br>跨图迁移、节点 | 分别学习对域变化稳定的特征和对结构变化较稳健的亲和度，在未见图上评分。<br>[代码](<https://github.com/kg-cc/IA-GGAD>) |
| <a id="p-unprompt-2025"></a>[Zero-shot Generalist Graph Anomaly Detection with Unified Neighborhood Prompts](<https://doi.org/10.24963/ijcai.2025/359>)<br>IJCAI 2025 · 方法 · Chaoxi Niu et al.<br><code>unprompt-2025</code> | 源图训练，目标图零样本 · 节点 · 跨图 | 单一源图训练后不调参迁移目标图，注意与目标图无标签可见条件分清。<br>[精读卡](../notes/unprompt-2025.md) |
| <a id="p-arc-2024"></a>[ARC: A Generalist Graph Anomaly Detector with In-Context Learning](<https://proceedings.neurips.cc/paper_files/paper/2024/hash/5acb720a361eecb34ee62d356859d246-Abstract-Conference.html>)<br>NeurIPS 2024 · 迁移方法 · Yixin Liu et al.<br><code>arc-2024</code> | 源图正常与异常标签；目标图仅少量正常支持节点 · 节点 · 跨域属性图<br>跨图迁移、节点 | 用平滑度对齐特征，以中心与邻域表示之差编码节点，再让少量正常支持样本参与评分。<br>[代码](<https://github.com/yixinliu233/ARC>) · [精读卡](../notes/arc-2024.md) |
| <a id="p-gcpal"></a>[Graph Contrastive Pre-training for Anti-money Laundering](<https://doi.org/10.1007/s44196-024-00720-4>)<br>International Journal of Computational Intelligence Systems 2024 · 预训练与微调 · Hanbin Lu, Haosen Wang<br><code>gcpal</code> | 无标签交易图预训练，分类环节使用标签 · 交易节点或交易边，按数据集建模 · Elliptic 与合成 AMLworld<br>Elliptic 与合成 AMLworld、交易节点或交易边，按数据集建模 | 对无标签交易网络做对比预训练，再用标注数据适配 AML 分类。完整特征可能自带邻域汇总，需与局部特征单独比较。 |
| <a id="p-topoood-2024"></a>[Graph Out-of-Distribution Detection Goes Neighborhood Shaping](<https://proceedings.mlr.press/v235/bao24c.html>)<br>ICML 2024 · 方法 · Tianyi Bao et al.<br><code>topoood-2024</code> | OOD 检测，标注协议需核 · 节点 · 跨图 | 设计拓扑分布变化下的 OOD 节点检出协议，警惕异常检测与分布外检测概念混同。 |
| <a id="p-good-d-2023"></a>[GOOD-D: On Unsupervised Graph Out-Of-Distribution Detection](<https://trust-agi.github.io/publication/wsdm-23-liu/>)<br>WSDM 2023 · 迁移方法 · Yixin Liu, Kaize Ding, Huan Liu, Shirui Pan<br><code>good-d-2023</code> | 仅无标签的域内训练图 · 整图 · 图分布外检测<br>跨图迁移、整图 | 在节点、图与组等层级对比表示，以跨视图语义不一致识别域外图。 |

## E 数据与评测基准

<a id="branch-12"></a>
<a id="branch-e1"></a>

### E1 方法比较与评测协议

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-bag-2026"></a><a id="p-bag-dynamic"></a>[BAG: Benchmarking Anomaly Detection on Dynamic Graphs](<https://doi.org/10.1609/aaai.v40i17.38510>)<br>AAAI 2026 · 评测基准 · Fengrui Hua, Yiyan Qi et al.<br><code>bag-2026</code> | 多种设定，按数据集和模型分别记录训练可见标签；时间切分后分别评价原有异常和人工注入异常。 · 连续时序边和快照中的动态节点 · 金融信任与社交等动态图<br>BAG | BAG 在 10 个图数据集上比较 25 个模型，明确区分自然异常和注入异常；可与 DyGADBench 配对设计压力测试。<br>[代码](<https://github.com/frhuaaa/BAG>) · [精读卡](../notes/bag-dynamic.md) |
| <a id="p-dygadbench"></a>[DyGADBench: A Comprehensive Benchmark for Anomaly Detection in Dynamic Graphs](<https://doi.org/10.1145/3770855.3817594>)<br>KDD · Datasets and Benchmarks 2026 · 基准 · Mohamed Nazim Mezhoudi et al.<br><code>dygadbench</code> | 按注入协议评测 · 时序边 · 通用动态图 | 改变注入异常的结构、强度和持续时间，关注 AP、运行成本及失效模式。<br>[代码](<https://github.com/Dastamn/dgadb>) · [精读卡](../notes/dygadbench-2026.md) |
| <a id="p-finfraudbench-2026"></a>[FinFraudBench: A Heterogeneous Graph Benchmark for Financial Fraud Detection](<https://arxiv.org/abs/2608.15177>)<br>arXiv preprint 2026 · 评测基准（预印本） · Yixuan Chen, Hongyu Zhan, Jie Sheng, Weiyu Han, Shuai Chen, Tianyi Zhang, Xiao Tan, Jun Xia<br><code>finfraudbench-2026</code> | 少量双类训练标签、大量未标注上下文 · 交易节点 · 从交易表派生的金融异构图<br>异构图、标签稀缺、测试基率 | 在两张交易中心异构图上统一比较图表示；区分自然基率完整测试集和主表采用的五个均衡子集，能解释不同测试流量下精度的可比范围。<br>[精读卡](../notes/finfraudbench-2026.md) |
| <a id="p-phishing-wonderland"></a>[Phishing in Wonderland: Evaluating Learning-Based Ethereum Phishing Transaction Detection and Pitfalls](<https://www.ndss-symposium.org/ndss-paper/phishing-in-wonderland-evaluating-learning-based-ethereum-phishing-transaction-detection-and-pitfalls/>)<br>NDSS Symposium 2026 · 评测 · Ahod Alghuried, David Mohaisen<br><code>phishing-wonderland</code> | 基于既有链上钓鱼标签比较多类特征与分类方法 · 链上钓鱼活动；逐实验核对交易与账户粒度 · 以太坊<br>以太坊、链上钓鱼活动；逐实验核对交易与账户粒度 | 按交易、行为和内容特征检查以太坊钓鱼检测的可靠性。文献汇总指标来自不同设定，不能直接合成排名。 |
| <a id="p-elliptic-pp-audit-2026"></a>[Revisiting Elliptic++ for Bitcoin Forensics: Feature Reconstruction and Leakage-Resistant Evaluation](<https://arxiv.org/abs/2611.04000>)<br>arXiv preprint 2026 · 评测复核（预印本） · Runlin Liang, Simon Trimborn, Noud van Giersbergen<br><code>elliptic-pp-audit-2026</code> | 仅在标签已知的地址上训练和评估 · 地址节点 · 比特币反洗钱与评测审计<br>Elliptic++、时间泄漏、独立复核 | 独立复查 Elliptic++ 的地址级模型、特征定义与切分，比较按位置划分和按地址首次出现时间划分时非法类 F1 的变化。<br>[代码](<https://github.com/DukHaanYumCha/Leakage-Resistant-Elliptic_pp>) · [精读卡](../notes/elliptic-pp-audit-2026.md) |
| <a id="p-ssl-selection-2025"></a>[Towards automated self-supervised learning for truly unsupervised graph anomaly detection](<https://link.springer.com/article/10.1007/s10618-025-01115-5>)<br>Data Mining and Knowledge Discovery 2025 · 评测研究 · Zhong Li, Yuhang Wang, Matthijs van Leeuwen<br><code>ssl-selection-2025</code> | 无标签选择模型与超参数 · 节点、检测器选择 · 通用图基准<br>公平评测、节点、检测器选择 | 比较自监督策略、超参数及组合权重，研究无标签内部评价。 |
| <a id="p-ub-gold"></a>[Unifying Unsupervised Graph-Level Anomaly Detection and Out-of-Distribution Detection: A Benchmark](<https://proceedings.iclr.cc/paper_files/paper/2025/hash/e58fa42d4b7a798eef8d0d75098f87ad-Abstract-Conference.html>)<br>ICLR 2025 · 基准 · Yili Wang et al.<br><code>ub-gold</code> | 无监督图级检测，异常评估标签与分布来源取决于场景 · 候选整图 · 分子、社交等通用图集合<br>UB | UB-GOLD 对 35 个数据集和 18 种方法作统一比较。可借鉴其设计，在独立实验中区分给定候选子图的异常与跨域偏移。<br>[代码](<https://github.com/UB-GOLD/UB-GOLD>) · [精读卡](../notes/ub-gold.md) |
| <a id="p-muse-2024"></a>[Rethinking Reconstruction-based Graph-Level Anomaly Detection: Limitations and a Simple Remedy](<https://proceedings.neurips.cc/paper_files/paper/2024/hash/ae03bdef276132fae089692445725635-Abstract-Conference.html>)<br>NeurIPS 2024 · 评测研究 · Sunwoo Kim et al.<br><code>muse-2024</code> | 重构式整图异常检测 · 整图 · 通用图集合<br>公平评测、整图 | 分析正常图平均重构误差反而更大的反例，再以多种误差摘要替代单一均值评分。 |
| <a id="p-three-revisits-2024"></a>[Three Revisits to Node-Level Graph Anomaly Detection: Outliers, Message Passing and Hyperbolic Neural Networks](<https://proceedings.mlr.press/v231/gu24a.html>)<br>LoG 2023 · PMLR 231（2024 出版） 2024 · 评测研究 · Jing Gu, Dongmian Zou<br><code>three-revisits-2024</code> | 无监督，含人工注入异常 · 节点 · 通用图评测<br>公平评测、节点 | 对比不同异常注入方法、启用或停用消息传递及双曲表示的表现。 |
| <a id="p-gadbench"></a>[GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection](<https://papers.neurips.cc/paper_files/paper/2023/hash/5eaafd67434a4cfb1cf829722c65f184-Abstract-Datasets_and_Benchmarks.html>)<br>NeurIPS · Datasets and Benchmarks 2023 · 基准 · Jianheng Tang et al.<br><code>gadbench</code> | 双类标签 · 静态节点 · 通用与金融图<br>强基线 | 比较 29 种方法与 10 个数据集。邻域特征加树模型是验证图神经网络增益的重要对照。<br>[代码](<https://github.com/squareRoot3/GADBench>) |
| <a id="p-bond"></a>[BOND: Benchmarking Unsupervised Outlier Node Detection on Static Attributed Graphs](<https://proceedings.neurips.cc/paper_files/paper/2022/hash/acc1ec4a9c780006c9aafd595104816b-Abstract.html>)<br>NeurIPS · Datasets and Benchmarks 2022 · 基准 · Kay Liu et al.<br><code>bond</code> | 无真实训练标签 · 静态节点 · 通用属性图<br>BOND | 将自然标注的异常与人工注入的异常分开，帮助判断一个方法为什么在不同图上表现悬殊。 |
| <a id="p-baf-data-2022"></a>[Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation](<https://proceedings.nips.cc/paper_files/paper/2022/hash/d9696563856bd350e4e7ac5e5812f23c-Abstract-Datasets_and_Benchmarks.html>)<br>NeurIPS Datasets and Benchmarks 2022 · 评测基准 · Sérgio Jesus, José Pombal, Duarte Alves, André Cruz, Pedro Saleiro, Rita Ribeiro, João Gama, Pedro Bizarro<br><code>baf-data-2022</code> | 合成申请级双类标签 · 开户申请（表格） · 金融开户反欺诈<br>开户申请、表格对照、公平性 | 同源申请表受控改变偏差，适合将模型随时间变化的识别能力与不同人群误报率并列观察。<br>[代码](<https://github.com/feedzai/bank-account-fraud>) |

<a id="branch-13"></a>
<a id="branch-e2"></a>

### E2 真实图与标签来源

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-figraph-2025"></a>[FiGraph: A Dynamic Heterogeneous Graph Dataset for Financial Anomaly Detection](<https://doi.org/10.1145/3701716.3715301>)<br>The Web Conference (WWW) Companion 2025 · 数据论文 · Xiaoguang Wang, Chenxu Wang, Huanlong Liu, Mengqin Wang, Tao Qin, Pinghui Wang<br><code>figraph-2025</code> | 有监督目标节点，其他节点提供上下文 · 上市公司×年 · 上市企业关系网络<br>年度快照、企业风险、异构图 | 在包含多类实体与关系的年度无向图中识别上市公司的年度异常，可检验跨年标注变化及表格、文本特征的增益。<br>[代码](<https://github.com/XiaoguangWang23/FiGraph>) · [精读卡](../notes/figraph-2025.md) |
| <a id="p-ghost-clusters"></a>[Ghost Clusters: Evaluating Attribution of Illicit Services through Cryptocurrency Tracing](<https://www.usenix.org/conference/usenixsecurity25/presentation/lubbertsen>)<br>USENIX Security 2025 · 标签审计 · Kelvin Lubbertsen, Michel van Eeten, Rolf van Wegberg<br><code>ghost-clusters</code> | 与被查封服务取得的独立真值核对 · 地址簇、服务与对应资金流 · 比特币地址归属<br>比特币地址归属、地址簇、服务与对应资金流 | 按地址重合、资金流覆盖及地址角色评估服务归属标签。执法数据只覆盖特定服务，标签遗漏不能当作正常。 |
| <a id="p-babd-2024"></a>[BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis](<https://doi.org/10.1109/TIFS.2023.3347894>)<br>IEEE Transactions on Information Forensics and Security 2024 · 数据与实证 · Yuexin Xiang, Yuchen Lei, Ding Bao, Tiantian Li, Qingqing Yang, Wenmao Liu, Wei Ren, Kim-Kwang Raymond Choo<br><code>babd-2024</code> | 有监督地址行为多分类 · 地址 · 比特币地址活动<br>地址角色、链上特征、多分类 | 构建 13 类行为标签和 148 个地址特征，研究以地址历史刻画实体功能的可行性。<br>[代码](<https://github.com/Y-Xiang-hub/Bitcoin-Address-Behavior-Analysis>) |
| <a id="p-elliptic2"></a>[The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset](<https://arxiv.org/abs/2404.19109>)<br>KDD Workshop on Machine Learning in Finance 2024 · 数据与基准 · Claudio Bellei et al.<br><code>elliptic2</code> | 有标注候选子图 · 地址簇构成的子图 · 比特币链上交易 | Elliptic2 把标签放在候选子图上。已知候选分类的实验不能直接回答从整张图找线索的问题。 |
| <a id="p-elliptic-pp-2023"></a>[Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics](<https://doi.org/10.1145/3580305.3599803>)<br>KDD 2023 · 数据与实证 · Youssef Elmougy, Ling Liu<br><code>elliptic-pp-2023</code> | 已知合法/非法标签，含未知样本 · 交易节点、地址节点（两个任务） · 比特币链上金融<br>Elliptic++、多视图、比特币 | 作者在原 Elliptic 交易集上补充地址视图，可围绕同一资金活动比较地址证据与交易证据，并分别报告两种检测对象。<br>[代码](<https://github.com/git-disl/EllipticPlusPlus>) · [精读卡](../notes/elliptic-pp-2023.md) |
| <a id="p-dgraph"></a>[DGraph: A Large-Scale Financial Dataset for Graph Anomaly Detection](<https://proceedings.nips.cc/paper_files/paper/2022/hash/8f1918f71972789db39ec0d85bb31110-Abstract-Datasets_and_Benchmarks.html>)<br>NeurIPS · Datasets and Benchmarks 2022 · 数据与基准 · Xuanwen Huang et al.<br><code>dgraph</code> | 目标节点有标注，另有背景节点 · 借贷用户节点 · 金融借贷联系图 | 边来自申报的紧急联系人。研究按长期逾期且多次催收未应答定义正例，背景节点另计；原节点切分结果须与跨时点评测分开。 |
| <a id="p-elliptic"></a>[Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics](<https://arxiv.org/abs/1908.02591>)<br>KDD Workshop on Anomaly Detection in Finance 2019 · 经典数据与基准 · Mark Weber et al.<br><code>elliptic</code> | 合法、非法和未知 · 交易节点 · 比特币链上交易<br>经典回溯、Elliptic | 适合双类监督和人为遮蔽异常标签的两种节点任务。核对特征所用邻居是否来自未来。 |

<a id="branch-14"></a>
<a id="branch-e3"></a>

### E3 可控制的合成交易

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-transxion"></a>[TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering](<https://doi.org/10.1145/3770855.3817550>)<br>KDD · Datasets and Benchmarks 2026 · 团队数据与基准 · Keyang Chen et al.<br><code>transxion</code> | 模拟交易标签 · 交易边 · 合成反洗钱交易<br>团队公开论文 | 保留账户间重复、带时间的资金往来，适合测试对交易边的告警排序和跨模拟器迁移。<br>[代码](<https://github.com/chaos-max/TransXion>) · [精读卡](../notes/transxion-2026.md) |
| <a id="p-momtsim-data-2025"></a>[A labeled synthetic mobile money transaction dataset](<https://doi.org/10.1016/j.dib.2025.111534>)<br>Data in Brief 2025 · 数据论文 · Denish Azamuke, Marriette Katarahweire, Engineer Bainomugisha<br><code>momtsim-data-2025</code> | 逐笔模拟欺诈标签 · 移动支付交易边 · 移动钱包欺诈<br>MoMTSim、基率、交易边 | 同一模拟器在两组设置下产生差距很大的正类率。用于检验告警预算及阈值敏感性时，需分开描述各配置。<br>[精读卡](../notes/momtsim-data-2025.md) |
| <a id="p-momtsim-calibration-2024"></a>[MoMTSim: A Multi-Agent-Based Simulation Platform Calibrated for Mobile Money Transactions](<https://doi.org/10.1109/ACCESS.2024.3439012>)<br>IEEE Access 2024 · 模拟器方法 · Denish Azamuke, Marriette Katarahweire, Engineer Bainomugisha<br><code>momtsim-calibration-2024</code> | 无分类训练要求；比较汇总统计 · 模拟移动支付过程 · 移动钱包<br>模拟器校准、统计验证、移动支付 | 提出移动钱包模拟器及迭代校准方法，用于检验生成交易的统计特征与业务参考数据的接近程度。 |
| <a id="p-synthaml"></a>[A synthetic data set to benchmark anti-money laundering methods](<https://doi.org/10.1038/s41597-023-02569-2>)<br>Scientific Data 2023 · 数据与基准 · Rasmus Ingemann Tuffveson Jensen et al.<br><code>synthaml</code> | 模拟告警处置结果 · 告警及关联交易 · 源自丹麦银行的合成数据 | 读清告警上报或驳回的标签。它支持告警筛查研究，不能直接给每笔交易赋犯罪真值。 |
| <a id="p-saml-data-2023"></a>[Enhancing Anti-Money Laundering: Development of a Synthetic Transaction Monitoring Dataset](<https://doi.org/10.1109/ICEBE59045.2023.00028>)<br>IEEE International Conference on e-Business Engineering (ICEBE) 2023 · 数据论文 · B. Oztas, D. Cetinkaya, F. Adedoyin, M. Budka, H. Dogan, G. Aksu<br><code>saml-data-2023</code> | 逐笔模拟标签，可受控遮蔽 · 交易边 · 合成银行反洗钱<br>SAML-D、反洗钱、合成交易 | 发布生成交易及逐笔可疑标识，给出场景字典，有利于单独检验对新型资金模式的泛化。<br>[代码](<https://github.com/BOztasUK/Anti_Money_Laundering_Transaction_Data_SAML-D>) |
| <a id="p-amlworld"></a>[Realistic Synthetic Financial Transactions for Anti-Money Laundering Models](<https://research.ibm.com/publications/realistic-synthetic-financial-transactions-for-anti-money-laundering-models>)<br>NeurIPS · Datasets and Benchmarks 2023 · 数据与基准 · Erik Altman et al.<br><code>amlworld</code> | 模拟交易标签 · 交易边 · 合成反洗钱交易 | IBM AMLworld 可与 TransXion 作跨生成器对照，区分具体生成规则带来的收益。<br>[精读卡](../notes/ibm-amlworld.md) |

## F 金融实证与数据边界

<a id="branch-15"></a>
<a id="branch-f1"></a>

### F1 真实金融现象与外部证据

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-nature-abuse"></a>[Banking records reveal characteristics of financial abuse](<https://doi.org/10.1038/s41586-026-11049-7>)<br>Nature 2026 · 跨学科实证 · Anna Trendl et al.<br><code>nature-abuse</code> | 自报经历及匹配对照 · 人及跨期资金行为 · 英国零售银行 | 以披露日为参照研究披露前的账户轨迹。可借鉴现实问题、参照组和观察窗的设计。 |
| <a id="p-mad-cash"></a>[MAD: Multicriteria Anomaly Detection of Suspicious Financial Accounts from Billions of Cash Transactions](<https://doi.org/10.1145/3711896.3737244>)<br>KDD 2025 · 无监督业务对照 · Giordano Paoletti et al.<br><code>mad-cash</code> | 无需案件标签拟合，事后按既有记录和专家复核评估 · 账户 · 意大利银行现金及相关转账<br>意大利银行现金及相关转账、账户 | 把月内借、贷和现金活动汇总到账户，结合多种指标筛选可疑账户。人工抽查名单的命中比例不能直接当作全体账户的召回率。<br>[精读卡](../notes/mad-cash.md) |
| <a id="p-nft-wash-icdcs"></a>[A Game of NFTs: Characterizing NFT Wash Trading in the Ethereum Blockchain](<https://doi.org/10.1109/ICDCS57875.2023.00018>)<br>IEEE ICDCS 2023 · 市场行为实证 · Massimo La Morgia et al.<br><code>nft-wash-icdcs</code> | 依据交易模式划定疑似清洗交易事件 · NFT 交易事件及参与地址组 · 以太坊 NFT 市场<br>以太坊 NFT 市场、NFT 交易事件及参与地址组 | 跟踪 ERC-721 资产在地址间的流转，比较交易回路与各市场交易量。重复转手与同一控制人是不同判断，规则估计值不能充当案件标签。 |
| <a id="p-txphishscope-2023"></a>[TxPhishScope: Towards Detecting and Understanding Transaction-based Phishing on Ethereum](<https://doi.org/10.1145/3576915.3623210>)<br>ACM CCS 2023 · 观测研究 · Bowen He, Yuan Chen, Zhuo Chen, Xiaohui Hu, Yufeng Hu, Lei Wu, Rui Chang, Haoyu Wang, Yajin Zhou<br><code>txphishscope-2023</code> | 防御性观测，公开材料为系统发现的案例 · 钓鱼网站及关联链上活动 · 以太坊受害资金追踪<br>链外证据、观测偏差、以太坊 | 研究联合观察网站案例和链上资金流向；公开资源以网站线索为主，适合论证从链外证据到链上实体之间的标签边界。 |
| <a id="p-guarantee-chain-kdd"></a>[Contagious Chain Risk Rating for Networked-guarantee Loans](<https://www.kdd.org/kdd2020/accepted-papers/view/contagious-chain-risk-rating-for-networked-guarantee-loans.html>)<br>KDD 2020 · 信用风险外延 · Dawei Cheng, Zhibin Niu, Yiyi Zhang<br><code>guarantee-chain-kdd</code> | 贷款违约相关结局作为监督依据 · 企业担保链 · 商业银行企业担保关系<br>商业银行企业担保关系、企业担保链 | 利用企业间担保关系预测违约风险沿链传播的可能性。担保边是信用义务，预测违约传播与识别欺诈案件为两种任务。 |

<a id="branch-16"></a>
<a id="branch-f2"></a>

### F2 交易数据的披露边界

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-science-privacy"></a>[Unique in the shopping mall: On the reidentifiability of credit card metadata](<https://doi.org/10.1126/science.1256297>)<br>Science 2015 · 跨学科经典 · Yves-Alexandre de Montjoye et al.<br><code>science-privacy</code> | 不适用 · 交易记录与个体 · 信用卡交易元数据<br>经典回溯 | 研究时空交易记录的可识别性。供讨论合作数据的可披露范围，独立于检测算法比较。 |

## G 动态图检测与时间协议

<a id="branch-17"></a>
<a id="branch-g1"></a>

### G1 边流与突发交互

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-stg-dgr"></a>[STG-DGR: Fraud Detection on Streaming Transaction Graphs with Diffusion-based Generative Replay](<https://doi.org/10.1145/3774904.3792195>)<br>The Web Conference (WWW) 2026 · 方法 · Rui Ou et al.<br><code>stg-dgr</code> | 持续学习欺诈检测；标签抵达时点须记录 · 流式交易图的待判样本 · 交易欺诈<br>动态图、时间评测 | 将计算子图分层，利用扩散模型生成人工回放样本以缓和对旧型欺诈的遗忘。不保存原样本不足以证明隐私；记忆成本应包括生成模型。 |
| <a id="p-multisnap-sketch"></a>[A Multi-Snapshot Sketching Framework for Anomaly Detection in Streaming Graphs](<https://doi.org/10.1109/ICDMW69685.2025.00192>)<br>IEEE ICDM Workshops 2025 · 方法 · Luis Olmos, Rashida Hasan<br><code>multisnap-sketch</code> | 无标签流式草图 · 边级与结构级异常 · 图边流<br>动态图、时间评测 | 利用多个快照的摘要同时追踪短时爆发与较慢变化。这是工作坊论文；快照尺度需按到达率重选。 |
| <a id="p-tstructgad"></a>[Deep Temporal and Structural Embeddings for Robust Unsupervised Anomaly Detection in Dynamic Graphs](<https://doi.org/10.1109/OJCS.2025.3584942>)<br>IEEE Open Journal of the Computer Society 2025 · 方法 · Samir Abdaljalil et al.<br><code>tstructgad</code> | 无监督重构 · 时间变化的节点表征 · 多种动态图<br>动态图、时间评测 | 用图卷积门控单元和 LSTM 联合编码，再依据自编码器的重构误差打分。重构误差会受普通高波动节点影响，不能直接解释为欺诈概率。 |
| <a id="p-long-term-gad"></a>[Long-term evolutionary patterns matter: Self-supervised anomaly detection on dynamic graphs](<https://doi.org/10.1016/j.knosys.2025.113049>)<br>Knowledge-Based Systems 2025 · 方法 · Yun Fu, Che Zhou, Jintang Li, Liang Chen<br><code>long-term-gad</code> | 自监督 · 节点 · 动态图<br>动态图、时间评测 | 状态空间模型汇总多步历史，把偏离节点长期演变规律作为异常信号。新账户缺少历史，需要单独报告冷启动表现。 |
| <a id="p-tami-2025"></a>[TAMI: Taming Heterogeneity in Temporal Interactions for Temporal Graph Link Prediction](<https://proceedings.neurips.cc/paper_files/paper/2025/hash/aa963ac256590bb7ad5fc26c68229a3a-Abstract-Conference.html>)<br>NeurIPS 2025 · 异质交互频率建模 · Zhongyi Yu, Jianqiu Wu, Zhenghao Wu, Shuhan Zhong, Weifeng Su, Chul-Ho Lee, Weipeng Zhuo<br><code>tami-2025</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 间歇往来的节点对 · 连续时间互动网络<br>时序图、低频对手、时间编码 | 组合对数间隔编码和节点对交互历史汇聚，单独处理低频关系被遗忘的问题。低频节点对的连边改善不是低频洗钱的检测结果。<br>[代码](<https://github.com/Alleinx/TAMItemporalgraph>) |
| <a id="p-fingersketch"></a>[Anomaly Detection over Streaming Graphs with Finger-Based Higher-Order Graph Sketch](<https://doi.org/10.3390/math12193092>)<br>Mathematics 2024 · 方法 · Min Lu, Qianzhen Zhang, Xianqiang Zhu<br><code>fingersketch</code> | 无标签，流式统计 · 边和子图 · 图边流<br>动态图、时间评测 | 用指纹式高阶图草图近似维护关系频次，并支持边和子图异常查询。比较不同草图须固定内存预算和数据到达速度。 |
| <a id="p-wsdm-mad"></a>[MAD: Multi-Scale Anomaly Detection in Link Streams](<https://doi.org/10.1145/3616855.3635834>)<br>WSDM 2024 · 方法 · Esteban Bautista, Laurent Brisson, Cécile Bothorel, Grégory Smits<br><code>wsdm-mad</code> | 历史互动概率参照 · 指定时刻的任意通信组合 · 稀疏通信网络<br>动态图、子图 | 联合评价出现和缺失的相互作用，用多尺度子图概率区分局部与全局异常。要先给定待查组合；缺失也可能来自采集断档。<br>[代码](<https://github.com/estbautista/MAD_Sub>) |
| <a id="p-slade"></a>[SLADE: Detecting Dynamic Anomalies in Edge Streams without Labels via Self-Supervised Learning](<https://doi.org/10.1145/3637528.3671845>)<br>KDD 2024 · 方法 · Jongha Lee, Sunwoo Kim, Kijung Shin<br><code>slade</code> | 无标签，自监督 · 交互时刻的节点状态变化 · 通用边流<br>动态图、时间评测 | 同时约束节点表征漂移、由近期交互恢复长期交互模式，通过两项任务的偏差打分。边流作为输入，节点状态作为输出；须按相同对象评测。 |
| <a id="p-taddy"></a>[Anomaly Detection in Dynamic Graphs via Transformer](<https://doi.org/10.1109/TKDE.2021.3124061>)<br>IEEE TKDE 2023 · 方法 · Yixin Liu et al.<br><code>taddy</code> | 通过负采样构造训练监督 · 动态图边 · 无属性关系图<br>动态图、时间评测 | 结合结构与时间角色的位置编码，对候选边的时空邻域做 Transformer 编码。未出现的边仅是代理负例；随机注入与真实可疑交易语义不同。 |
| <a id="p-anograph-sketch"></a>[Sketch-Based Anomaly Detection in Streaming Graphs](<https://doi.org/10.1145/3580305.3599504>)<br>KDD 2023 · 方法 · Siddharth Bhatia et al.<br><code>anograph-sketch</code> | 无监督统计打分 · 单边、窗口图 · 网络通信流<br>动态图、时间评测 | 压缩来源与去向形成高阶计数草图，在压缩矩阵内搜索局部稠密区域。四套主要评测来自网络流量；哈希碰撞和时间粒度影响定位。<br>[代码](<https://github.com/Stream-AD/AnoGraph>) · [精读卡](../notes/anograph-sketch.md) |
| <a id="p-f-fade-stream"></a>[F-FADE: Frequency Factorization for Anomaly Detection in Edge Streams](<https://doi.org/10.1145/3437963.3441806>)<br>WSDM 2021 · 奠基方法 · Yen-Yu Chang et al.<br><code>f-fade-stream</code> | 无需异常训练标签 · 带时间的边 · 通用交互网络<br>流式图 | 分解交互频次以估计节点对历史分布。频率分布偏离的论文结果不能直接估计调查命中率。<br>[代码](<https://github.com/snap-stanford/F-FADE>) |
| <a id="p-midas-stream"></a>[MIDAS: Microcluster-Based Detector of Anomalies in Edge Streams](<https://doi.org/10.1609/aaai.v34i04.5724>)<br>AAAI 2020 · 奠基方法 · Siddharth Bhatia, Bryan Hooi, Minji Yoon, Kijung Shin, Christos Faloutsos<br><code>midas-stream</code> | 无需异常训练标签 · 流式到达的边 · 通用交互网络<br>流式图 | 以草图统计节点对的突发交互，在线逐边评分。微簇或频数偏离本身不能认定洗钱。 |

<a id="branch-18"></a>
<a id="branch-g2"></a>

### G2 节点轨迹与账户状态

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-dp-dgad"></a>[DP-DGAD: A Generalist Dynamic Graph Anomaly Detector with Dynamic Prototypes](<https://doi.org/10.1145/3774904.3792268>)<br>The Web Conference (WWW) 2026 · 方法 · Jialun Zheng et al.<br><code>dp-dgad</code> | 源域预训练与目标域置信伪标签适配 · 时点交互边；将时序自中心图用作输入 · 多域动态图<br>动态图、迁移 | 缓冲区保留共享和域特异原型；以置信检测决定在目标域更新哪些样本。目标域标注可见性、模拟异常与真实标签需分别登记。<br>[精读卡](../notes/dp-dgad.md) |
| <a id="p-graphseqguard"></a>[GraphSeqGuard: Detecting Ethereum phishing scams via temporally evolving graph sequences](<https://doi.org/10.1016/j.knosys.2025.114895>)<br>Knowledge-Based Systems 2026 · 动态图序列 · Mingshun Ye et al.<br><code>graphseqguard</code> | 以地址钓鱼标签分类 · 地址节点 · 以太坊交易<br>以太坊交易、地址节点 | 按账户构造有序交易子图序列，在不同观测阶段判断地址风险。早期发现必须只用预警时刻之前的图及当时已知的标签。 |
| <a id="p-generaldyg"></a>[A Generalizable Anomaly Detection Method in Dynamic Graphs](<https://doi.org/10.1609/aaai.v39i20.35508>)<br>AAAI 2025 · 方法 · Xiao Yang, Xuejiao Zhao, Zhiqi Shen<br><code>generaldyg</code> | 训练节点和边视作正常，异常标签用于测试 · 节点和边分别评分 · 信任网络、工业控制<br>动态图、时间评测 | 抽取时间自中心图，分别提取张量图结构与序列特征。Bitcoin 测试包含注入异常；工业控制指标不能与边异常 AUC 合并。<br>[代码](<https://github.com/YXNTU/GeneralDyG>) · [精读卡](../notes/generaldyg.md) |
| <a id="p-pdtga"></a>[Phishing scams detection via temporal graph attention network in Ethereum](<https://doi.org/10.1016/j.ipm.2023.103412>)<br>Information Processing &amp; Management 2023 · 时序地址分类 · Lei Wang, Ming Xu, Hao Cheng<br><code>pdtga</code> | 地址标签监督分类 · 地址节点 · 以太坊交易<br>以太坊交易、地址节点 | 用时间图注意力融合节点和边特征，再对地址分类。规模子集之间可能共享节点，不能把它们直接视为三个独立域。 |
| <a id="p-sad-dynamic"></a>[SAD: Semi-Supervised Anomaly Detection on Dynamic Graphs](<https://doi.org/10.24963/ijcai.2023/256>)<br>IJCAI 2023 · 方法 · Sheng Tian et al.<br><code>sad-dynamic</code> | 少量正负标签与未标注节点；另有全标注实验 · 事件时点的节点状态 · 支付、社交与在线学习<br>动态图、时间评测 | 按时间缓存近期分数，估计正常参考分布，用分数接近的样本构造伪标签对比对。主表和删标签实验的监督口径不同；退课或封禁的含义不同于资金欺诈。<br>[代码](<https://github.com/D10Andy/SAD>) · [精读卡](../notes/sad-dynamic.md) |

<a id="branch-19"></a>
<a id="branch-g3"></a>

### G3 时序子图与团伙发现

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-dupin"></a>[Dupin: A Parallel Framework for Densest Subgraph Discovery in Fraud Detection on Massive Graphs](<https://doi.org/10.1145/3725287>)<br>PACMMOD (SIGMOD) 2025 · 方法 · Jiaxin Jiang et al.<br><code>dupin</code> | 密度目标，非标签分类 · 超大规模图的候选稠密子图 · 交易与电商<br>动态图、子图 | 并行化顶点剥离，支持配置密度目标，面向十亿级图的团伙候选发现。是可扩展性对照，密度不能覆盖所有资金链。 |
| <a id="p-pgdetector"></a>[Fishing for Fraudsters: Uncovering Ethereum Phishing Gangs With Blockchain Data](<https://doi.org/10.1109/TIFS.2024.3359000>)<br>IEEE Transactions on Information Forensics and Security 2024 · 已知种子的团伙发现 · Jieli Liu et al.<br><code>pgdetector</code> | 输入一个已知可疑钓鱼账户作为搜索种子 · 种子周围的潜在团伙成员 · 以太坊交易<br>以太坊交易、种子周围的潜在团伙成员 | 通过已知种子的交易社区和群组行为寻找关联地址。有种子搜索与全图无种子发现的召回不可直接比较。 |
| <a id="p-motif-madg"></a>[Motif-Level Anomaly Detection in Dynamic Graphs](<https://doi.org/10.1109/TIFS.2023.3272731>)<br>IEEE TIFS 2023 · 方法 · Zirui Yuan, Minglai Shao, Qiben Yan<br><code>motif-madg</code> | 摘要未给出训练标签预算 · 预定义模体实例 · 通用动态网络<br>动态图、子图 | 在每一快照对节点和模体实例做图卷积，用相对时间编码和注意力学习演化。输出取决于模体词表；不能等同于无约束未知团伙发现。<br>[代码](<https://github.com/zirui-yuan/MADG>) |
| <a id="p-cashout-dense"></a>[Detecting Cash-out Users via Dense Subgraphs](<https://doi.org/10.1145/3534678.3539252>)<br>KDD 2022 · 团伙识别 · Yingsheng Ji et al.<br><code>cashout-dense</code> | 标签稀缺，以稠密块结构发现候选 · 套现用户及其共同交易结构 · 商业银行信用卡<br>商业银行信用卡、套现用户及其共同交易结构 | 把信用卡交易连接组织成图，用稠密块识别聚集的套现用户。异常稠密还需和正常商圈或大商户的自然聚集区分。 |
| <a id="p-spade"></a>[Spade: A Real-Time Fraud Detection Framework on Evolving Graphs](<https://doi.org/10.14778/3570690.3570696>)<br>PVLDB 2022 · 方法 · Jiaxin Jiang et al.<br><code>spade</code> | 密度规则，无需训练标签 · 增量图中的候选稠密商户与用户群 · Grab 电商交易、在线网络<br>动态图、子图 | 边插入时局部调整顶点剥离顺序，支持按批更新和对紧急边优先处理。高密度只能生成复核候选；低密度链状行为不一定触发。<br>[代码](<https://github.com/samjjx/Spade>) · [精读卡](../notes/spade.md) |

<a id="branch-20"></a>
<a id="branch-g4"></a>

### G4 快照序列与结构变点

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-hermitian-cp"></a>[Anomaly detection in directed dynamic graphs using Hermitian Laplacian spectral analysis](<https://doi.org/10.1016/j.chaos.2026.118458>)<br>Chaos, Solitons &amp; Fractals 2026 · 方法 · Guihai Yu, Yulei Yue, Xiaopeng Li, Matjaž Perc<br><code>hermitian-cp</code> | 无监督光谱对比 · 有向网络的异常时点 · 通信、贸易关系<br>动态图、变点 | 保留边方向，以 Hermitian 拉普拉斯的谱及双窗口比较结构变化。国家间贸易网络与账户交易粒度不同。 |
| <a id="p-frechet-cp"></a>[Graph online change point detection based on fréchet statistics](<https://doi.org/10.1016/j.neucom.2025.131874>)<br>Neurocomputing 2026 · 方法 · Rui Luo, Jie Bao, Hing Cheung So, Suqun Cao, Mengqiao Xu<br><code>frechet-cp</code> | 无监督顺序检验 · 网络整体结构变点 · 模拟网络、航运等真实网络<br>动态图、变点 | 在拉普拉斯矩阵空间定义 Fréchet 均值与方差，用递推 CUSUM 式统计量发出警报。需固定基准时期和误报控制水平；检测不定位可疑账户。 |
| <a id="p-missing-network-cp"></a>[Online Network Change Point Detection With Missing Values and Temporal Dependence](<https://doi.org/10.1111/jtsa.70023>)<br>Journal of Time Series Analysis 2026 · 方法 · Haotian Xu, Paromita Dubey, Yi Yu<br><code>missing-network-cp</code> | 无监督顺序变点检验 · 网络变点 · 部分观测随机动态网络<br>动态图、变点 | 用低秩软填补估计连接结构，同时控制无变化时的错误告警。理论依赖随机网络和跳变强度等条件；缺数不是可疑交易标签。 |
| <a id="p-network-mase"></a>[Multiple network embedding for anomaly detection in time series of graphs](<https://doi.org/10.1016/j.csda.2024.108070>)<br>Computational Statistics &amp; Data Analysis 2025 · 方法 · Guodong Chen et al.<br><code>network-mase</code> | 无监督联合谱推断 · 整图及发生变化的顶点 · Enron 通信、搜索与连接组<br>动态图、时间评测 | 用多邻接谱嵌入拟合共享表示，在图与顶点两个层级查找偏离。若用全序列共同估计嵌入，只支持回顾性比较。<br>[代码](<https://github.com/gdchen94/TSG-Anomaly-Detection>) |
| <a id="p-siamese-network-cp"></a>[Graph similarity learning for change-point detection in dynamic networks](<https://doi.org/10.1007/s10994-023-06405-x>)<br>Machine Learning 2024 · 方法 · Déborah Sulem, Henry Kenlay, Mihai Cucuringu, Xiaowen Dong<br><code>siamese-network-cp</code> | 有变点标签可监督；无标签时可用光谱法预估变点 · 快照序列中的变点 · 股票收益相关网络、脑功能相关网络<br>动态图、变点 | 用孪生图网络学习快照相似度，把当前快照与短历史比较。金融实例没有变点真值；原文部分预处理用全时间段统计。<br>[精读卡](../notes/siamese-network-cp.md) |
| <a id="p-social-emergence"></a>[Temporal graphs anomaly emergence detection: benchmarking for social media interactions](<https://doi.org/10.1007/s10489-024-05821-3>)<br>Applied Intelligence 2024 · 评测基准 · Teddy Lazebnik, Or Iny<br><code>social-emergence</code> | 基准比较，多种方法 · 群体互动中的异常出现 · Twitter、Facebook<br>动态图、时间评测 | 以两个社交动态图比较12种方法，分析异常形成时的识别差异。社交群体标签不足以证明资金团伙识别能力。 |
| <a id="p-latent-evolution-cp"></a>[Latent evolution model for change point detection in time-varying networks](<https://doi.org/10.1016/j.ins.2023.119376>)<br>Information Sciences 2023 · 方法 · Yongshun Gong, Xue Dong, Jian Zhang, Meng Chen<br><code>latent-evolution-cp</code> | 预测式变点检测 · 网络快照变点 · 时变网络<br>动态图、变点 | 学习隐含演化趋势，把当前网络偏离该趋势的程度用于识别变点。须区分长期趋势变化与单次局部交易群突发。 |
| <a id="p-network-control-chart"></a>[Online monitoring of dynamic networks using flexible multivariate control charts](<https://doi.org/10.1007/s13278-023-01091-y>)<br>Social Network Analysis and Mining 2023 · 方法 · Jonathan Flossdorf, Roland Fried, Carsten Jentsch<br><code>network-control-chart</code> | 无监督，多元控制图 · 网络级变点 · 经济、社会网络<br>动态图、变点 | 联合监测多个图指标，比较参数与非参数控制图。指标选择不当会导致监测失灵；应报告零假设期间误报。 |
| <a id="p-lad-2020"></a>[Laplacian Change Point Detection for Dynamic Graphs](<https://doi.org/10.1145/3394486.3403077>)<br>KDD 2020 · 整图变点基线 · Shenyang Huang, Yasmeen Hitti, Guillaume Rabusseau, Reihaneh Rabbany<br><code>lad-2020</code> | 无监督比较图谱变化，无需逐笔风险标签 · 快照级变化时点 · 通信、投票和合成网络<br>时序图、全图变点、滑动窗口 | 取图拉普拉斯谱作为快照摘要，与短、长历史滑窗比较以定位变点。网络变点不定位涉案账户；节假日、制度切换也会导致变化。<br>[代码](<https://github.com/shenyangHuang/LAD>) |

<a id="branch-21"></a>
<a id="branch-g5"></a>

### G5 时序表示与链接预测对照

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-atnsf-2026"></a>[History Doesn’t Repeat, but Its Patterns Echo: A Parallel Pairwise Negative-Sampling Framework for Temporal Link Prediction](<https://ijcai.org/proceedings/2026/302>)<br>IJCAI 2026 · 训练负采样与排序损失 · Yongchun Jiang, Heng Zhang, Jian Gao, Xin Zheng<br><code>atnsf-2026</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 候选未来边 · 六个时序网络<br>时序图、困难负例、损失函数 | ATNSF 将历史困难负例与随机负例混合，用成对采样 softmax 和异步训练。训练采样策略带来的收益不能与更容易的测试候选混为一谈。<br>[代码](<https://github.com/yongqiu-star/ATNSF>) |
| <a id="p-tgm-2026"></a>[TGM: A Modular and Efficient Library for Machine Learning on Temporal Graphs](<https://proceedings.iclr.cc/paper_files/paper/2026/hash/d978cd64d598bbaf6a2fff1d6864d601-Abstract-Conference.html>)<br>ICLR 2026 · 可复现实验软件 · Jacob Chmura, Shenyang(Andy) Huang, Tran Gia Bao Ngo, Ali Parviz, Farimah Poursafaei, Jure Leskovec, Michael Bronstein, Guillaume Rabusseau, Matthias Fey, Reihaneh Rabbany<br><code>tgm-2026</code> | 软件支持多种下游监督，依数据定义 · 链路、节点与整图的计算任务 · 通用连续和离散时序图<br>时序图、图系统、时间粒度 | 统一离散与连续时间表示、动态节点属性和时间粒度转换，并比较效率。软件支持不同任务，不能据此判断某个业务风险模型准确。<br>[代码](<https://github.com/tgm-team/tgm>) |
| <a id="p-dyg-mamba-2025"></a>[DyG-Mamba: Continuous State Space Modeling on Dynamic Graphs](<https://proceedings.neurips.cc/paper_files/paper/2025/hash/bbba680acd2826f23928c6675a19f0e7-Abstract-Conference.html>)<br>NeurIPS 2025 · 连续时间状态空间表示 · Dongyuan Li, Shiyin Tan, Ying Zhang, Ming Jin, Shirui Pan, Manabu Okumura, Renhe Jiang<br><code>dyg-mamba-2025</code> | 链路任务用边发生信号；节点分类另用节点标签 · 未来边与节点类别 · 多域动态图<br>时序图、长历史、状态空间 | 以不规则间隔控制历史遗忘并选择性回顾信息，比较长期序列效率。金融迁移需分离长间隔与调查标签的延迟。<br>[代码](<https://github.com/Clearloveyuan/DyG-Mamba>) |
| <a id="p-craft-2025"></a>[Future Link Prediction Without Memory or Aggregation](<https://proceedings.neurips.cc/paper_files/paper/2025/hash/036912a83bdbb1fd792baf6532f102d8-Abstract-Conference.html>)<br>NeurIPS 2025 · 目标感知的交互预测 · Lu Yi, Runlin Lei, Fengran Mo, Yanping Zheng, Zhewei Wei, Yuhang Ye<br><code>craft-2025</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 重复边与首次出现的边 · 动态交互网络<br>时序图、首次关系、交叉注意力 | CRAFT 用可学习的节点标识及交叉注意力，让候选端与源端近期交互匹配。新边可发生在训练中已经出现的两个账户之间，不能等同新账户冷启动。 |
| <a id="p-dygprompt-2025"></a>[Node-Time Conditional Prompt Learning in Dynamic Graphs](<https://proceedings.iclr.cc/paper_files/paper/2025/hash/f342338902ea2d8aaf3af94b941ebba6-Abstract-Conference.html>)<br>ICLR 2025 · 时序预训练与迁移对照 · Xingtong Yu, Zhenghao Liu, Xinming Zhang, Yuan Fang<br><code>dygprompt-2025</code> | 先以历史交互预训练，后以具体下游任务监督适配 · 动态节点和下游任务 · 社交、学习和协作等动态图<br>时序图、迁移学习、时间提示 | 预训练后用节点和时间双提示适配下游目标。需控制下游标签预算、训练截止日及预训练是否触及测试期。<br>[代码](<https://github.com/gmcmt/DyGPrompt>) |
| <a id="p-tgbseq-2025"></a>[TGB-Seq Benchmark: Challenging Temporal GNNs with Complex Sequential Dynamics](<https://proceedings.iclr.cc/paper_files/paper/2025/hash/db5ca61dbc08cf5143c05ad2d1b0b2ca-Abstract-Conference.html>)<br>ICLR 2025 · 低重复边顺序基准 · Lu Yi, Jie Peng, Yanping Zheng, Fengran Mo, Zhewei Wei, Yuhang Ye, Yue Zixuan, Zengfeng Huang<br><code>tgbseq-2025</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 首次关系、未来对手 · 电影、电子商务、社交和引用等互动图<br>时序图、首次关系、顺序诊断 | 用低重复边基准和合成序列区分关系记忆与顺序利用能力。电影评分、社交关注等标签只支持未来关系预测。<br>[代码](<https://github.com/TGB-Seq/TGB-Seq>) · [精读卡](../notes/tgbseq-2025.md) |
| <a id="p-utg-2025"></a>[UTG: Towards a Unified View of Snapshot and Event Based Models for Temporal Graphs](<https://proceedings.mlr.press/v269/huang25a.html>)<br>Learning on Graphs 2025 · 快照和事件协议比较 · Shenyang Huang, Farimah Poursafaei, Reihaneh Rabbany, Guillaume Rabusseau, Emanuele Rossi<br><code>utg-2025</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 未来链接 · 事件级和快照级动态图<br>时序图、快照、事件流 | 用统一框架交叉比较快照模型与事件模型，并给出流式快照训练程序。日末聚合包含当天较晚的交易，不能直接用于日内提前预警。<br>[代码](<https://github.com/shenyangHuang/UTG>) |
| <a id="p-benchtemp-2024"></a>[BenchTemp: A General Benchmark for Evaluating Temporal Graph Neural Networks](<https://doi.org/10.1109/ICDE60146.2024.00310>)<br>ICDE 2024 · 可比性与效率基准 · Qiang Huang, Xin Wang, Susie Xi Rao, Zhichao Han, Zitao Zhang, Yongjun He, Quanqing Xu, Yang Zhao, Zhigao Zheng, Jiawei Jiang<br><code>benchtemp-2024</code> | 链路任务用交互目标，节点分类用节点标签 · 链路预测与节点分类 · 多域动态图<br>时序图、评测协议、基准 | 统一数据预处理、特征初始化、训练和评测，比较多模型的精度及效率。同一软件流程也不能统一不同机构风险标签的语义。<br>[代码](<https://github.com/johnnyhuangcs/benchtemp>) |
| <a id="p-freedyg-2024"></a>[FreeDyG: Frequency Enhanced Continuous-Time Dynamic Graph Model for Link Prediction](<https://proceedings.iclr.cc/paper_files/paper/2024/hash/21f7b745f73ce0d1f9bcea7f40b1388e-Abstract-Conference.html>)<br>ICLR 2024 · 频域时序表示 · Yuxing Tian, Yiyan Qi, Fan Guo<br><code>freedyg-2024</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 未来交互边 · 连续时间动态交互图<br>时序图、频域、周期 | 编码共同邻居比例和成对交互频率，并在频域提取周期及行为变化。观察到频率偏移本身不能确定是洗钱、节日或账期变化。<br>[代码](<https://github.com/Tianxzzz/FreeDyG>) |
| <a id="p-epod-2024"></a>[Improving Generalization of Dynamic Graph Learning via Environment Prompt](<https://papers.nips.cc/paper_files/paper/2024/hash/81c565e605161fcf25d08aa230431eba-Abstract-Conference.html>)<br>NeurIPS 2024 · 环境提示与跨期泛化 · Kuo Yang, Zhengyang Zhou, Qihe Huang, Limin Li, Yuxuan Liang, Yang Wang<br><code>epod-2024</code> | 下游预测目标，未知的环境因素由模型推断 · 节点依赖和动态子图 · 多环境动态图<br>时序图、环境推断、漂移 | EpoD 用自提示推断环境因素，并通过动态子图表征环境与节点依赖。从数据推断的环境不等于已证实的银行业务制度或操作原因。 |
| <a id="p-tpnet-2024"></a>[Improving Temporal Link Prediction via Temporal Walk Matrix Projection](<https://proceedings.neurips.cc/paper_files/paper/2024/hash/ff7bf6014f7826da531aa50f4538ee19-Abstract-Conference.html>)<br>NeurIPS 2024 · 时序路径相对编码 · Xiaodong Lu, Leilei Sun, Tongyu Zhu, Weifeng Lv<br><code>tpnet-2024</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 未来边与多跳路径 · 通用时序交互图<br>时序图、时间游走、随机投影 | 用带衰减的时序游走矩阵描述节点对，以随机特征传播近似计算。连边任务没有交代风险标签；随机近似误差需在稀有路径上复核。<br>[代码](<https://github.com/lxd99/TPNet>) |
| <a id="p-graphssm-2024"></a>[State Space Models on Temporal Graphs: A First-Principles Study](<https://proceedings.neurips.cc/paper_files/paper/2024/hash/e5ba3d6d93213db6b1d1931c6517fe1a-Abstract-Conference.html>)<br>NeurIPS 2024 · 快照状态空间表示 · Jintang Li, Ruofan Wu, Xinzhou Jin, Boqun Ma, Liang Chen, Zibin Zheng<br><code>graphssm-2024</code> | 取决于下游动态图任务，状态空间编码本身不是风险标签 · 动态图快照的状态序列 · 离散快照图<br>时序图、状态空间、快照 | 把拉普拉斯结构正则融入序列状态空间近似，形成 GraphSSM。整日快照会损失同日转账的先后和多笔细节。<br>[代码](<https://github.com/EdisonLeeeee/GraphSSM>) |
| <a id="p-tgb2-2024"></a>[TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous Graphs](<https://proceedings.neurips.cc/paper_files/paper/2024/hash/fda026cf2423a01fcbcf1e1e43ee9a50-Abstract-Datasets_and_Benchmarks_Track.html>)<br>NeurIPS 2024 · 多关系预测基准 · Julia Gastinger, Shenyang Huang, Mikhail Galkin, Erfan Loghmani, Ali Parviz, Farimah Poursafaei, Jacob Danovitch, Emanuele Rossi, Ioannis Koutis, Heiner Stuckenschmidt, Reihaneh Rabbany, Guillaume Rabusseau<br><code>tgb2-2024</code> | 由多关系图中观测到的未来链接提供目标 · 带类型的未来边 · 时序知识图谱、异质交互图<br>时序图、多关系、异质图 | 在八个数据集上统一比较未来多关系边预测，并检验维持边类型的重要性。公开基准的关系类型和真值不直接等同银行风险事件。<br>[代码](<https://github.com/JuliaGast/TGB2>) |
| <a id="p-graphmixer-2023"></a>[Do We Really Need Complicated Model Architectures For Temporal Networks?](<https://openreview.net/pdf?id=ayPPc0SyLv1>)<br>ICLR 2023 · 轻量连边基线 · Weilin Cong, Si Zhang, Jian Kang, Baichuan Yuan, Hao Wu, Xin Zhou, Hanghang Tong, Mehrdad Mahdavi<br><code>graphmixer-2023</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 未来交互边 · 通用动态网络<br>时序图、MLP、轻量基线 | 用 MLP 混合历史边、均值汇聚节点邻居，由分类头预测连边。关系出现的监督与可疑标签是两种任务。<br>[代码](<https://github.com/CongWeilin/GraphMixer>) |
| <a id="p-eagle-2023"></a>[Environment-Aware Dynamic Graph Learning for Out-of-Distribution Generalization](<https://proceedings.neurips.cc/paper_files/paper/2023/hash/9bf12308ece130daa083fb21f7faf1b6-Abstract-Conference.html>)<br>NeurIPS 2023 · 分布外时序对照 · Haonan Yuan, Qingyun Sun, Xingcheng Fu, Ziwei Zhang, Cheng Ji, Hao Peng, Jianxin Li<br><code>eagle-2023</code> | 以未来边作为目标，不提供显式环境标签 · 未来边 · COLLAB、Yelp、ACT 和受控实验<br>时序图、分布漂移、压力测试 | 推断潜在环境并寻找跨环境稳定的模式，检验边属性和节点特征漂移。流行评论或合作边的 AUC 不能代替实际交易的风险命中率。<br>[代码](<https://github.com/RingBDStack/EAGLE>) · [精读卡](../notes/eagle-2023.md) |
| <a id="p-semba-2023"></a>[Representation Learning in Continuous-Time Dynamic Signed Networks](<https://doi.org/10.1145/3583780.3615032>)<br>CIKM 2023 · 有符号时序图方法 · Kartik Sharma, Mohit Raghavendra, Yeon-Chang Lee, Anand Kumar M, Srijan Kumar<br><code>semba-2023</code> | 以已发生关系及用户给出的正负评分监督 · 带符号的未来边 · Bitcoin OTC、Bitcoin Alpha 信任评分，另含 WikiRfA 和 Epinions<br>时序图、有符号图、信任评分 | 在记忆更新中分开处理正负互动，经平衡理论指导的聚合预测未来关系符号。不信任评分不是已确认洗钱；不能用负边直接构造账户欺诈标签。 |
| <a id="p-tgb-2023"></a>[Temporal Graph Benchmark for Machine Learning on Temporal Graphs](<https://papers.nips.cc/paper/2023/hash/066b98e63313162f6562b35962671288-Abstract-Datasets_and_Benchmarks.html>)<br>NeurIPS 2023 · 带交易图的评测基准 · Shenyang Huang, Farimah Poursafaei, Jacob Danovitch, Matthias Fey, Weihua Hu, Emanuele Rossi, Jure Leskovec, Michael Bronstein, Guillaume Rabusseau, Reihaneh Rabbany<br><code>tgb-2023</code> | 由事件日志构造边目标，节点偏好来自未来窗口的归一化权重 · 交易对手边与节点偏好 · 多领域，含 ERC20 稳定币实际转账<br>时序图、稳定币、排名评测 | 固定多负例候选，用 MRR 评估目的地址排名，节点偏好另用 NDCG。该任务的正例表示转账发生，缺少合法或非法真值。<br>[代码](<https://github.com/shenyangHuang/TGB>) · [精读卡](../notes/tgb-2023.md) |
| <a id="p-dygformer-2023"></a>[Towards Better Dynamic Graph Learning: New Architecture and Unified Library](<https://proceedings.neurips.cc/paper_files/paper/2023/hash/d611019afba70d547bd595e8a4158f55-Abstract.html>)<br>NeurIPS 2023 · 动态图表示对照 · Le Yu, Leilei Sun, Bowen Du, Weifeng Lv<br><code>dygformer-2023</code> | 边发生与抽样负例；节点分类使用任务标签 · 未来交互边、动态节点 · 多域连续时间交互图<br>时序图、共现、长历史 | 从一跳交互的邻居共现和序列分块建模，提供统一实现 DyGLib。重复对手会抬高共现信号，结果应按新旧交易对分层。<br>[代码](<https://github.com/yule-BUAA/DyGLib>) |
| <a id="p-dida-2022"></a>[Dynamic Graph Neural Networks Under Spatio-Temporal Distribution Shift](<https://papers.neurips.cc/paper_files/paper/2022/hash/2857242c9e97de339ce642e75b15ff24-Abstract-Conference.html>)<br>NeurIPS 2022 · 分布偏移与不变性方法 · Zeyang Zhang, Xin Wang, Ziwei Zhang, Haoyang Li, Zhou Qin, Wenwu Zhu<br><code>dida-2022</code> | 下游任务目标与不变性正则，无金融风险标签 · 动态图预测的局部结构和特征 · 真实与合成动态图<br>时序图、分布漂移、不变性 | DIDA 解耦可变与稳定的时空模式，用干预分布下的预测差异正则化。推断出的稳定结构需用独立时间段和业务标签再验证。<br>[代码](<https://github.com/wondergo2017/DIDA>) |
| <a id="p-nat-2022"></a>[Neighborhood-Aware Scalable Temporal Network Representation Learning](<https://proceedings.mlr.press/v198/luo22a.html>)<br>Learning on Graphs 2022 · 可扩展邻域编码 · Yuhong Luo, Pan Li<br><code>nat-2022</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 节点对与局部结构 · 多类真实时序网络<br>时序图、缓存、邻域采样 | 通过字典型邻域表示和 GPU N-cache 维护抽样邻居，编码节点间共有结构。采样邻居可能漏掉稀有支付路径，需另外评估覆盖率。<br>[代码](<https://github.com/Graph-COM/Neighborhood-Aware-Temporal-Network>) |
| <a id="p-tgl-2022"></a>[TGL: A General Framework for Temporal GNN Training on Billion-Scale Graphs](<https://www.vldb.org/pvldb/vol15/p1572-zhou.pdf>)<br>PVLDB 2022 · 时序训练系统 · Hongkuan Zhou, Da Zheng, Israt Nisa, Vasileios Ioannidis, Xiang Song, George Karypis<br><code>tgl-2022</code> | 训练系统随基任务选择事件或节点标签 · 事件流上的采样和训练吞吐 · 大规模交互图训练<br>时序图、图系统、可扩展性 | 把时序采样、特征获取和训练组织成可扩展流水线，比较运行成本。论文的硬件与数据规模限制加速比的适用范围。<br>[代码](<https://github.com/amazon-science/tgl>) |
| <a id="p-edgebank-2022"></a>[Towards Better Evaluation for Dynamic Link Prediction](<https://papers.neurips.cc/paper_files/paper/2022/hash/d49042a5d49818711c401d34172f9900-Abstract-Datasets_and_Benchmarks.html>)<br>NeurIPS 2022 · 基准与无参数基线 · Farimah Poursafaei, Shenyang Huang, Kellin Pelrine, Reihaneh Rabbany<br><code>edgebank-2022</code> | 无训练参数，按已发生的边构造正例并抽样负边作评测 · 未来交互边 · 跨域交互网络，含国家贸易<br>时序图、记忆基线、负样本 | 用全历史或有限窗口的节点对记忆比较三种负采样。抽样非边没有正常交易标签，不能换算为反洗钱误报率。<br>[代码](<https://github.com/fpour/DGB>) · [精读卡](../notes/edgebank-2022.md) |
| <a id="p-caw-2021"></a>[Inductive Representation Learning in Temporal Networks via Causal Anonymous Walks](<https://openreview.net/pdf?id=KYPz4YsCPj>)<br>ICLR 2021 · 时间游走基础方法 · Yanbang Wang, Yen-Yu Chang, Yunyu Liu, Jure Leskovec, Pan Li<br><code>caw-2021</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 节点对与时间路径 · 通用动态网络<br>时序图、时间游走、归纳预测 | 按时间回溯匿名游走，以节点在路径中的相对出现信息编码局部模式。文中的 causal 指时间次序，不能证明付款行为具有因果关系。<br>[代码](<https://github.com/snap-stanford/CAW>) |
| <a id="p-tgat-2020"></a>[Inductive Representation Learning on Temporal Graphs](<https://openreview.net/pdf?id=rJeW1yHYwH>)<br>ICLR 2020 · 连续时间注意力基础方法 · Da Xu, Chuanwei Ruan, Evren Korpeoglu, Sushant Kumar, Kannan Achan<br><code>tgat-2020</code> | 观测交互提供正例，未来链接为预测目标；无需金融风险标签 · 随时间变化的节点及候选边 · 通用动态图<br>时序图、时间编码、归纳预测 | 聚合时间邻域，用函数时间编码建模属性与时间的结合。跨节点归纳成功并不意味着能够辨认新型欺诈。 |

<a id="branch-22"></a>
<a id="branch-g6"></a>

### G6 时间切分、反馈与告警预算

| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |
| --- | --- | --- |
| <a id="p-hvps-needle"></a>[Finding a needle in a haystack: A machine learning framework for anomaly detection in payment systems](<https://doi.org/10.1016/j.jfds.2025.100163>)<br>The Journal of Finance and Data Science 2025 · 支付异常基线 · Ajit Desai, Anneke Kosse, Jacob Sharples<br><code>hvps-needle</code> | 实际异常稀少，结合模拟异常评估 · 大额支付指令 · 高价值支付系统<br>高价值支付系统、大额支付指令 | 分阶段筛选待查支付并评估异常程度，为支付系统运行监测提供基线。运行异常与涉诈案件的认定机制不同；列为应用参照。 |
| <a id="p-vus-tsad"></a>[VUS: effective and efficient accuracy measures for time-series anomaly detection](<https://doi.org/10.1007/s00778-025-00907-x>)<br>The VLDB Journal 2025 · 评测与历史参照 · Paul Boniol et al.<br><code>vus-tsad</code> | 已知异常时间区间供评价 · 区间与逐点分数 · 通用时间序列<br>评测协议 | 综合不同阈值与允许时间距离下的排序表现。业务允许的发现延迟和复核成本仍需另定义。<br>[精读卡](../notes/vus-tsad.md) |
| <a id="p-rigorous-tsad"></a>[Towards a Rigorous Evaluation of Time-Series Anomaly Detection](<https://doi.org/10.1609/aaai.v36i7.20680>)<br>AAAI 2022 · 评测与历史参照 · Siwon Kim, Kukjin Choi, Hyun-Soo Choi, Byunghan Lee, Sungroh Yoon<br><code>rigorous-tsad</code> | 评测使用已知异常区间 · 时刻与异常区间 · 通用时间序列<br>评测协议 | 对照原始与区间调整后的 F1，并设无模型评分对照。服务器时间序列结果无法证明金融图上的检出效果。<br>[精读卡](../notes/rigorous-tsad.md) |
| <a id="p-card-feedback-delay"></a>[Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy](<https://doi.org/10.1109/TNNLS.2017.2736643>)<br>IEEE Transactions on Neural Networks and Learning Systems 2018 · 评测与历史参照 · Andrea Dal Pozzolo, Giacomo Boracchi, Olivier Caelen, Cesare Alippi, Gianluca Bontempi<br><code>card-feedback-delay</code> | 及时调查反馈及延迟标签 · 交易评分，按卡聚合 · 真实电商信用卡支付<br>评测协议 | 分开学习近期调查与延迟确认的交易。合作数据受限；缺少图结构增益实验。<br>[精读卡](../notes/card-feedback-delay.md) |
