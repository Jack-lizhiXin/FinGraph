# 公开数据与评测资源索引

本索引仅链接发布者的数据，**不包含数据文件**。许可状态是逐资源记录：`待核` 不等于可再发布。已核日期：2026-11-20。

| 数据集 | 图、检测对象及标签语义 | 下载与许可 | 风险与注意 |
| --- | --- | --- | --- |
| [Elliptic Bitcoin Transaction Graph](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set) | 交易为节点；交易间资金流为有向边；节点；交易节点：已知合法、已知非法、未知（未知不是负类） | Kaggle 登记下载；原始数据不放本库；许可：**待以原始发布页面确认** | 只使用标签已知的测试样本评估；禁止把未知视为合法；按时间切分，对邻居聚合特征核查是否使用未来时间步 |
| [Elliptic2](https://github.com/MITIBMxGraph/Elliptic2) | 全局背景簇/边；子图对应一组关联交易结构；候选子图；子图 licit/suspicious，标注覆盖部分候选子图 | 官方 GitHub 指向 Kaggle，容量较大；许可：**第三方称 CC BY-NC-ND 4.0；需回到发布者许可原文核对** | 不是交易节点或账户级识别；不可把候选子图分类结果称为全图团伙发现；原文的切分和背景共用关系要检查 |
| [DGraph-Fin](https://dgraph.xinye.com/dataset) | 用户为节点；紧急联系人关系为有向边；账户节点；前景用户类别 0 正常/1 欺诈；背景节点不参与预测但保留连通 | 官网申请或下载 DGraphFin.zip；许可：**待以发布者协议原文确认** | 紧急联系人关系不是资金交易边；原始官方随机分层需另外增加时间外推测试；背景用户不是负例 |
| [DGraph-Fin2](https://dgraph.xinye.com/dataset) | 与 DGraph-Fin 关联的用户及紧急联系人关系；账户节点/时间片；含时间变化标签；具体标记时间语义按官方数据字典 | 官网下载；许可：**待核** | 与原 DGraph-Fin 的重复账号及样本重用要排查；防止测试时标签和新边提前暴露 |
| [T-Finance (GADBench)](https://github.com/squareRoot3/GADBench) | 金融对象节点；边代表 transaction record 关系；具体映射以数据字典确认；节点；标注为异常节点/正常节点；标签原始判定过程待核 | GADBench 官方 README 指向数据链接；许可：**待核** | 高度稠密图；自环、重复边、未知标签及归一化策略需固定；别把它当交易边级预测 |
| [T-Social (GADBench)](https://github.com/squareRoot3/GADBench) | 用户节点；社交关系边；节点；节点异常标签（标注含义按原始资料核实） | GADBench 数据链接；许可：**待核** | 用于非金融外部泛化；不能据此直接推出 AML 适用性 |
| [IBM AMLWorld / AML-Data](https://github.com/IBM/AML-Data) | 账户作为节点；汇款交易记录作为有向边；可能有货币与银行属性；交易边/账户聚合；合成交易洗钱真值以及模式标签；区分 laundering edge 与 flagged account | IBM GitHub/Kaggle 下载；大文件单独管理；许可：**数据：CDLA-Sharing-1.0；仓库代码：Apache-2.0，请区分** | 按交易时点切分；避免在建图时同一 SAR 模式或生成规则泄漏到验证；禁止误称真实银行分布 |
| [TransXion](https://github.com/chaos-max/TransXion) | 账户为节点；带时间戳的交易为边；交易边；交易边是否洗钱（模拟真值）；可按账户/团伙聚合但需重新定义标签 | 公开仓库，部分数据采用 Git LFS；许可：**需核对数据文件与代码各自授权，不由仓库 LICENSE 自动推定** | 交易频率、账户泄漏、跨时间边的可视范围要按部署时点截断；跨生成器评估需要留出不同合成器 |
| [IBM AMLSim simulator](https://github.com/IBM/AMLSim) | 模拟账户为节点、交易为边；交易边/账户/模式；由生成器配置注入的可疑模式/账户等真值；标签定义随配置而异 | 克隆代码并本地模拟；许可：**代码 Apache-2.0；生成输出的数据再利用责任应另行审查** | 训练测试需换 seed、配置和类型；不应只在一个生成器生成的同分布数据上做泛化结论 |
| [Amazon Review/GADBench](https://github.com/squareRoot3/GADBench) | 评论或评论者为节点（具体版本校核）；边为评论关联；节点；评论相关欺诈标签；不是金融欺诈 | GADBench 下载；许可：**待核** | 作为跨场景对照，不能代替金融效度；不同论文版本的同名数据构图不同 |
| [YelpChi/GADBench](https://github.com/squareRoot3/GADBench) | 评论/评论者节点；多关系评论关联边，按版本核对；节点；欺诈评论节点标签；不是银行交易异常 | GADBench 下载；许可：**待核** | 尤其需要固定关系类型、邻接展开与训练标签泄漏控制 |

## 核心对齐原则

- **交易节点 ≠ 交易边。** Elliptic 节点是交易，TransXion/AMLWorld 账户图中交易为边；即便都称「transaction detection」，不能直接共用一个 AUROC 排名。
- **背景节点 ≠ 正常样本。** DGraph-Fin 的背景节点不用于目标标签预测；Elliptic 的 unknown 属于未标注而不是 licit。
- **正常已知 ≠ 双类已知。** C2 类方法（CR-Aug/GGAD）依赖可信正常，C1（GTAN/ConsisGAD）可有正常与异常，C3 应有已确认异常＋未标注，须明确风险污染率假设。
- **数据集的下载权 ≠ 再发布权。** IBM AMLWorld 数据用 CDLA-Sharing-1.0，不得与官方代码 Apache-2.0 混淆。
- **所谓公开“真实交易数据”不意味着银行验证。** 真实区块链、脱敏平台关系、仿真交易属于不同真实性层级；合作实地验证应另行设计授权、隔离和审查。

## 选型建议

本科/硕士首轮：Elliptic 时间步切分（能下载原始数据的前提下），以及 DGraph-Fin 随机与时间实验明确分离。博士专题：IBM AMLWorld 与 TransXion 的边级回测，增补 Elliptic2 的子图检索/候选分类。对工业合作方：必须补充标签到达时间、单日人工复核量和归因字段。

后续维护：每月由数据管理员逐条复核 license、访问入口和数据版本，并将核验截图或 README commit 的链接存入 PR，不把外部整包上传 GitHub。
