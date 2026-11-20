# 证据比较矩阵：标签条件 × 预测对象 × 可评测性

> 以下列的是作者公开论文或官方数据说明**报告的设计**，不是本仓库已完成的模型复现实验。不能把不同数据、不同训练标签数的 AUROC 排序合并为“模型优劣排行榜”。`待核` 代表需要同学打开原论文逐表检验。核验日 2026-11-20。

| 论文／来源定位 | 可获得标签与训练信号 | 评分对象／数据 | 比较基线及报告指标 | 可复现时应核查的边界 |
| --- | --- | --- | --- | --- |
| [GADBench · NeurIPS D&B 2023](https://github.com/squareRoot3/GADBench)，README Dataset Information/Benchmarking | 既有双类标签；仓库的 `--semi_supervised` **具体含义必须回看代码** | 评论、社交与金融图的**节点**；含 Elliptic/T-Finance/DGraphFin | 原仓库多模型、多次 trial，AUROC；**不是等价的纯正常标签设置** | 稀有标签的采样方式、同构/异构开关、规模差异、是否按时间切分 |
| [GTAN · AAAI 2023](https://doi.org/10.1609/aaai.v37i12.26702)，原文摘要/方法节 | 少量**正常和欺诈**标签＋未标注交易 | 信用卡交易**节点** | 作者展示半监督分类设计；效果数值待核 | 银行的事件特征是否泄漏调查完成时间；不可与正常标签-only 方法直接比 |
| [ConsisGAD · ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/80eecea10dc05e23db2f90c9d4567153-Abstract-Conference.html)，摘要/方法 | 半监督、少量双类标签（细节须逐版核） | 节点，GADBench 类 | 一致性/可学习增强，指标见原文表格 | 增强是否作用训练外节点，双类比率如何固定 |
| [CGNN · AAAI 2025](https://doi.org/10.1609/aaai.v39i11.33319)，摘要 | 极少量标注的图欺诈识别；核对是否双类皆有 | 主要是图欺诈**节点** | 对照图方法及少标签实验；结果待复核 | 用同样极少异常标签比较，而非把它叫“一类正常” |
| [MimbFD · IJCAI 2025](https://ijcai.org/proceedings/2025/365)，§3.1 / §4 / §5 | 只有少量**正常+欺诈**训练标签；其余未标注 | 图欺诈**节点**；多金融/评论对照图 | 论文讨论消息不平衡、双视图和局部混杂；实验比较在 §5 | 图注意力是否因训练图包含未来关联而信息泄漏；复核具体构图版本 |
| [GGAD · NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/085b4b5d1f81ad9e057ad2b3de922ad4-Abstract-Conference.html)，摘要及原文方法 | 少量**可信正常**标签＋未标注；伪异常不等于真异常 | 通用异常**节点** | 生成式 pseudo-anomaly；AUROC/AUPRC 见论文 | 负类增强若窥探评测异常即不可接受 |
| [RHO · NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c273d135fed229f5724df9a0d354b36f-Abstract-Conference.html)，摘要 | 正常标签 scarce 的半监督 GAD | 异常**节点** | robust homophily 频谱；指标待原文表格核查 | 正常标签数与图结构同配假设，别将所有任务默认异配 |
| [CR-Aug · KDD 2026](https://doi.org/10.1145/3770855.3818003)，团队匿名研究稿 §3.1、§4.1、Table 1；官方 KDD 著录 | 训练时仅可信**正常标签**＋未标注；社区风险指导伪异常 | Amazon、T-Finance、Reddit、Elliptic、Photo、Tolokers 上的**节点** | 团队稿比较十个基线，报道 AUROC/AUPRC；稿件设 30%训练/10%验证/60%测试，训练部分再取一半正常标签 | 上述设置和数值仅确认于团队稿，发表终稿需要比对；尤其报告的先验风险估计不可使用测试标签；论文主结果≠本库复现 |
| [GraphNC · ICML 2026](https://proceedings.mlr.press/v306/zeng26o.html)，摘要 | 少量可信正常＋正常度校准 | 异常**节点** | 校准与误差改进；统计待核 | 与 CR-Aug、GGAD 同一个正常标签采样掩码对比 |
| [UNPrompt · IJCAI 2025](https://ijcai.org/proceedings/2025/359)，§3.2–§3.5 / Table 1 | **源图**训练；目标图**零标签且不微调** | 多图**节点**（社交/评论等；不专指金融） | 与跨图对照；Table 1/3 AUROC/AUPRC | 目标图 SVD/归一化是否含无标签测试特征；若金融部署不具备目标全图，需另定义流式协议 |
| [DRESS · IJCAI 2026](https://ijcai.org/proceedings/2026/801)，摘要 | 少量异常/正常标签；原文报告 2%-10% 标注情形，具体标签类别待核 | 图异常**节点** | 半监督/强化学习对照；效果待核 | 少量标签预算须按“类别”和“成本”双轴计 |
| [BAG · AAAI 2026](https://doi.org/10.1609/aaai.v40i17.38510)，摘要 | 基准涉及多标签/动态条件，具体协议见作者 | **动态图**异常，逐任务对齐 | 时序评测协议与综合结果见原文 | 不可把动态图整图一次可见的实验说成在线系统 |
| [DyGADBench · KDD 2026](https://doi.org/10.1145/3770855.3817594)，公开摘要 | 比较不同动态场景监督口径 | 动态**节点或事件**，以原文任务表为准 | 动态 benchmark，不等于新检测器 | 公开数据来源、时间泄漏与 future edge awareness 是首要检查项 |
| [TransXion · KDD D&B 2026](https://doi.org/10.1145/3770855.3817550)，[作者 repo README](https://github.com/chaos-max/TransXion) | 仿真生成时可见交易的合成洗钱标签 | 账户图**交易边**：365天、47526账户、3029170交易、4641洗钱交易 | 构建高保真 benchmark；检测器与 AUPRC 数值待查原文 | 与 Elliptic 节点评测不同。测试历史与构造模式、账户画像、生成器种子隔离 |
| [IBM AMLWorld · NeurIPS D&B 2023](https://github.com/IBM/AML-Data)，README/DATA LICENSE | 合成交易及 AML 模式可观测真值 | 账户、交易**边**及可聚合案件；多种生成配置 | 必须逐模型评测，不能以合成强度高声称真实洗钱效果 | 数据许可 CDLA-Sharing-1.0，代码许可 Apache-2.0；同生成器虚高 |
| [Elliptic2 · 2024 Workshop/preprint](https://github.com/MITIBMxGraph/Elliptic2)，官方目录/论文 Table 1 | 仅部分候选子图已知可疑/正常；背景大量未标注 | **候选交易子图** vs 背景节点 | 多种 subgraph representation baseline | 离线候选分类不是全图可疑团伙发现；数据许可约束尚待发布者原文确认 |
| [DGraph-Fin · NeurIPS D&B 2022](https://dgraph.xinye.com/dataset)，官方 Dataset | 正常/欺诈前景用户；背景用户保留连通但不作为负类 | **用户节点**，紧急联系人边 | 官方提供随机切分与基线 | **不是资金交易图**；不能把联系人边直接解释为转账流 |
| [Rule-graph OT · 2026 同行评审期刊](https://doi.org/10.1007/s44443-026-01381-3)，出版社摘要 | 稀少监督/诱导的规则辅助伪标签 | 交易图**节点**；原文数据进一步核 | 规则路径分组＋OT；原文对部分数据的改善有限 | 该文不是顶会；不能把论文中自述增益当作本组已核证实验 |

## 横向比较结论（源于任务定义，不是本库跑出的结果）

**发现 1：金融图异常的“检测单元”并不统一。** 账户图中一条交易是边，Elliptic 原任务中一笔交易是节点，Elliptic2 的一组交易是候选子图；所以先明确样本单位，再谈排名与成本。

**发现 2：C1/C2/C3 本质不同。** C1=部分正常和异常已确认＋未标注；C2=只有可信正常＋未标注（GGAD/RHO/CR-Aug）；C3=只有已知异常＋未标注，是 PU 风格，其正例并非“所有真实异常的随机抽样”。学生必须量化正例选择偏差、延迟与 PU 污染。

**发现 3：多数通用 GAD 测试不足以证明工业可落地。** 要增加时间窗口 cutoff、标签可见日、每日 Top-K 人工核查、跨机构/跨生成器，以及误报每千笔等额外指标；这些是建议验证指标，不是现有论文已达成的结论。
