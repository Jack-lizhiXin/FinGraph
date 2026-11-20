# 金融异常数据怎么选：检测对象、标签与时间

一次检测首先要明确谁接收分数。支付授权系统为每笔支付打分，反洗钱调查员给告警排序，年报审核员筛选企业年度报告。即使三项工作都使用图模型，正类含义、训练样本和可接受的误报成本也不同。

## 新增资源与可验证的问题

| 资源与来源 | 节点、边和时间 | 可检验的问题 | 证据边界 |
| --- | --- | --- | --- |
| [FiGraph · 作者仓库](https://github.com/XiaoguangWang23/FiGraph) | 企业、个人等五类实体；投资、供应链等四类关系。2014–2022 年各一张无向快照 | 给定当时已披露的企业特征和关系，能否识别下一期的上市公司风险？ | 标签属于上市公司与年份的组合。其他实体仅提供上下文；需另查年报和处罚的披露时点。 |
| [Elliptic++ · 作者规模表](https://github.com/git-disl/EllipticPlusPlus) | 比特币交易节点、地址节点及其关系；交易视图 49 步 | 在相同交易样本上，加入历史地址关联能否改善已标注交易的识别？ | 交易和地址各有合法、非法、未知三种记录状态。原 Elliptic 是其上游，二者共享交易。地址特征与划分存在已发表的独立复核预印本。[表 4](https://arxiv.org/abs/2611.04000) |
| [SAML-D · 作者数据说明](https://github.com/BOztasUK/Anti_Money_Laundering_Transaction_Data_SAML-D) | 发送账户→接收账户，重复付款保留为独立事件，有日期和时刻 | 对极低基率合成付款，跨时间、跨场景的告警召回有何变化？ | 标签由生成器产生，场景号不能输入模型；作者注明当前下载版有别于 2023 年论文所用版。 |
| [BAF · Feedzai 与 datasheet](https://github.com/feedzai/bank-account-fraud) | 开户申请表，含月序号；无逐笔转账关系 | 月份漂移以及不同人群的误报是否削弱表格模型？ | 基础集与五种偏差变体同源。相似申请建图属于研究者的新建图规则。 |
| [SynthAML · 数据论文](https://doi.org/10.1038/s41597-023-02569-2) | 告警 ID 连接告警表和有序交易历史；没有足够的对手方字段恢复完整账户网 | 在触发时刻可见的信息下，每日固定复核量能覆盖多少后来被上报的告警？ | 标签为上报或结案，仅对业务决策建模。20,000 个告警的标签不能复制成数千万个独立交易真值。 |
| [PaySim · 作者实现及样本入口](https://github.com/EdgarLopezPhD/PaySim) | 两端钱包或其他参与实体，带模拟时间步的交易边 | 在同一生成规则下，历史邻域比金额、业务类型等交易字段增加多少信息？ | 区分模拟欺诈与系统规则告警。若决策发生在授权前，交易后余额属于未来信息。 |
| [Credit Card Fraud Detection Handbook · 生成协议](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_3_GettingStarted/SimulatedDataset.html) | 客户–终端二部图，每次支付有日期和金额 | 延迟收到反馈时，终端历史和客户历史的作用能否分开测量？ | 欺诈情景由规则注入。删除场景编号，按事件顺序构造特征；原始示例的日期是模拟日历。 |
| [FinCEN Files 交易地图 · ICIJ 取样说明](https://www.icij.org/investigations/fincen-files/download-fincen-files-transaction-data/) | 已披露案例中的付款银行、收款银行及代理行；地图所列交易在 2000–2017 年间 | 哪些跨境机构关系出现在已公开的可疑活动报告中，哪些交易由于信息残缺未入图？ | 只收录两端银行可辨认的案例，无总体分母或正常组。报告表明存在疑虑，不能给个人或机构赋定罪标签。 |
| [BABD-13 · 作者代码与数据入口](https://github.com/Y-Xiang-hub/Bitcoin-Address-Behavior-Analysis) | 比特币地址及从链上邻域提取的行为特征，公开任务有 13 个功能类别 | 服务角色能否由历史地址行为辨认？哪些地址特征需要在时间截点重算？ | 原任务是角色多分类。行为类别与已证实的异常只有在有独立标签依据时才能对齐。 |
| [MoMTSim · V2 归档](https://data.mendeley.com/datasets/zhj366m53p/2) · [数据论文表 4–5](https://pmc.ncbi.nlm.nih.gov/articles/PMC12036017/) | 模拟移动钱包参与方和逐笔交易，两种配置各 720 步 | 同一复核预算下，基率变化如何改变精确率与未检出交易数？ | 两种配置的阳性率分别为 10.20% 和 52.84%。两者同源，部署阈值不能从模拟比例直接推断。 |
| [FinFraudBench · 预印本 §3–5](https://arxiv.org/abs/2608.15177) | 从两份公开交易表建交易、客户、卡、商户、地点等六类节点；交易有标签，原协议随机切分 | 在相同训练标签预算下保留实体类型与关系类型是否改善交易判别？ | 主表在五个均衡子集报告结果，完整测试集保留原始基率。在线实验还要重建图的历史可见部分。 |
| [BitcoinHeist · UCI 原始数据卡](https://archive.ics.uci.edu/dataset/526/bitcoinheist%2Bransomware%2Baddress%2Bdataset) | 逐日从比特币图提取地址特征；UCI 发布地址×日的特征表 | 对时间上较晚或未见过的勒索收款地址，历史特征能否识别已知家族？ | white 表示未发现其为勒索地址。全天统计仅在日终完整，数据构建还过滤了小额边。 |

## 可复用的比较设计

| 问题 | 对齐后的实验单位 | 切分与报告 | 能支持的结论 |
| --- | --- | --- | --- |
| 跨生成器反洗钱 | 以 AMLWorld 和 SAML-D 的每笔有向交易为样本，对齐观察时点、币种表达、业务类型及二元标签。先在每个源内部运行时间留出，再交换训练源和测试源。 | 以验证期确定阈值和每日复核预算 K。各测试源在原始基率下单列 AP、Recall@K 和每日误报数，剔除类型真值。 | 结果说明模型对这两个生成机制的依赖；真实机构仍需独立验证。另以具有不同生成机制的 TransXion 扩展。 [AMLWorld](https://github.com/IBM/AML-Data) · [SAML-D](https://github.com/BOztasUK/Anti_Money_Laundering_Transaction_Data_SAML-D) · [TransXion](https://arxiv.org/abs/2604.17420) |
| 链上地址证据的边际贡献 | 固定 Elliptic 交易节点和已知交易标签，以相同交易分别评估“交易特征”及“交易特征加历史地址关联”。 | 固定时间折和评估样本 ID。按切分截断地址邻域，另外报告标签覆盖率。地址识别、子图分类各设独立样本和指标。 | 对同一批交易可测特征增益；Elliptic2 的候选子图成绩不能移到交易表中。 [Elliptic++](https://github.com/git-disl/EllipticPlusPlus) · [Elliptic2](https://github.com/MITIBMxGraph/Elliptic2) |
| 在告警系统中模拟标签延迟 | 用 SynthAML 的告警 ID 作为调查单位，查询触发前的交易历史。把实际未提供的反馈延迟设为实验变量，明确其为模拟假设。 | 按告警日期外推，多组反馈延迟共用同一组告警；每天只取前 K 个，报告上报覆盖率、每天误报及与简单交易统计基线的差异。 | 结果对应上报决策的筛选价值；FinCEN 地图可用于解释观察偏差，不能估计这一筛选系统的准确率。 [SynthAML](https://doi.org/10.1038/s41597-023-02569-2) · [ICIJ](https://www.icij.org/investigations/fincen-files/download-fincen-files-transaction-data/) |

把金融关系当作特征时，还要区分关系为何存在。DGraph-Fin 的关系是贷款用户登记紧急联系人；FiGraph 中出现企业投资、供应链等关系；TransXion 的有向边是一笔模拟付款。三者分别适合回答用户风险、企业年度风险和交易风险问题。若需要比较模型架构，可以在每项任务内报告相对同一基线的增益，再按任务归纳，不合并不同目标的单一排行榜。[DGraph 原论文](https://proceedings.nips.cc/paper_files/paper/2022/hash/8f1918f71972789db39ec0d85bb31110-Abstract-Datasets_and_Benchmarks.html) · [FiGraph](https://github.com/XiaoguangWang23/FiGraph) · [TransXion](https://github.com/chaos-max/TransXion)

对每个实例记录四个时间量：业务事件发生时间、输入字段可见时间、系统评分时间、调查反馈可见时间。预测时只可读取评分时已知的数据，训练时只可使用训练截点前已返回的标签。最终评测可等待反馈成熟，再注明到截点仍未知的次数和比例。真实反馈时间缺失时可做不同延迟的敏感性分析，并在结果表给出假设；时间单位仅为年或日时，避免声称具备逐分钟报警能力。

## 来源、版本与许可

- BAF 的原作者资料把数据列为 CC BY-NC-ND 4.0；FiGraph 的 README 明确写 CC BY-NC 4.0，但代码托管页面的许可证标识显示 CC BY 4.0，记录两份声明，使用前核对具体适用范围。[BAF datasheet](https://raw.githubusercontent.com/feedzai/bank-account-fraud/main/documents/datasheet.pdf) · [FiGraph 作者说明](https://github.com/XiaoguangWang23/FiGraph)
- MoMTSim 有一篇模拟器校准论文与一篇数据论文，共同支撑一个资源条目。V2 归档标 CC BY 4.0。IBM AML-Data 的仓库采用 Apache-2.0，其数据另用 CDLA-Sharing-1.0。综述统计模型论文数和独立数据源数时分别计数。[MoMTSim V2](https://data.mendeley.com/datasets/zhj366m53p/2) · [IBM 作者说明](https://github.com/IBM/AML-Data)
- 对有代码、数据和文稿多种授权对象的项目，逐项记录版本与发布条款。手册笔记本代码为 GPL-3.0、手册文字和图为 CC BY-SA 4.0。BitcoinHeist 的 UCI 数据卡单列 CC BY 4.0。此仓库汇集引文和资源描述。[手册声明](https://fraud-detection-handbook.github.io/fraud-detection-handbook/README.html) · [UCI 数据卡](https://archive.ics.uci.edu/dataset/526/bitcoinheist%2Bransomware%2Baddress%2Bdataset)

## 本轮检索记录

2026-11-20 进行了主题搜索，再回到论文、出版会议、作者仓库、机构数据归档或调查方的发布页核对。下列为实际执行过的代表性查询（多次补查同一资源不重复统计）。本轮是有针对性的扩展检索，未保存检索引擎完整返回集合，不能由此绘制完整系统综述的筛选流图。

| 查找主题 | 实际查询示例 | 最终核对的位置与取舍 |
| --- | --- | --- |
| 企业动态关系与时间 | `Xiaoguang Wang FiGraph corporate financial fraud heterogeneous title authors 2025 companion dataset uppercase doi` | 作者 README 的年度文件、目标节点列及未分类背景；出版类型以作者引文及 WWW Companion 书目核对。 |
| 比特币地址/交易投影 | `EllipticPlusPlus Elmougy Liu Demystifying Fraudulent Transactions illicit actors title KDD 2023 transactions wallets` | 作者数据规模表、地址与交易 notebooks；标为原 Elliptic 的派生资源。 |
| 合成银行告警与处置标签 | `SynthAML data alert tables counterparties transactions features synthetic Denmark reported dismissed alert_id dataset license` | 原文 Data Records、告警表归档。原论文已在书目出现，此轮只补资源条目。 |
| 手机钱包模拟、校准与版本 | `MoMTSim A labeled synthetic mobile money transaction dataset Data in Brief 2025 author number table transaction labeled dataset Mendeley v2` | 数据论文 Tables 4–5 提供两组记录数、步数、种子、标签占比；以 Mendeley V2 的 Licence 栏核对数据条款。 |
| 少标签异构交易基准 | `FinFraudBench CreditCard-Fraud BankTrans-Fraud account label time public dataset fraud graph preprint 2608.15177` | 原文 §3–5、表 1–2 与 Data Availability。主表测试先验及划分方式均单独记录。 |
| 链上功能标签、可观测负类 | `BitcoinHeist ransomware UCI dataset 2916697 license family training white missing edges` | UCI 变量字典区分 white 与已知勒索家族。数据有用，2020 年论文留作历史出处，不计入近五年新增论文。 |
| 链上与链外的外部证据 | `TxPhishScope Towards Detecting and Understanding Transaction-based Phishing on Ethereum CCS 2023 authors doi dataset github blocksecteam supplementary labeled transactions` | 对照 ACM 论文与作者公开材料。作者公开的是从系统观测得到的网站线索，不把它计成逐笔带负类的金融交易数据集。 |

公开页面、原论文和数据字典支持上面的字段判断。本轮没有下载原始交易、重跑作者的模型或验证真实系统的线上收益。
