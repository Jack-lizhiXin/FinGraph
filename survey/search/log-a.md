# 动态异常检测、边流与图变点检索记录

检索截至 **2026-11-20**。从已有 BAG、DyGADBench 等基准中的比较对象出发，沿方法名回查论文，再沿预测对象补查事件、节点、团伙与图级变点。最终记录以正式出版年份归类，因此个别较早预印本的卷期落在 2022–2026 年。英文库中的小写、连字符和预印本后缀均不作为区分论文的依据。

| 检索入口与关键词 | 去哪里核对 | 入选判断 |
| --- | --- | --- |
| `SAD GeneralDyG TADDY dynamic graph anomaly detection`、`dynamic graph anomaly detection compatibility modeling boundary learning`、`SLADE edge streams` | IJCAI、AAAI、KDD、IEEE 原文，必要时对照作者公开稿 | 记录输入是边事件还是快照、标签是在节点还是边、训练期是否人为构造负样本 |
| `Sketch-based anomaly detection streaming graphs`、`multi-scale anomaly detection in link streams`、`multi-snapshot sketching framework` | ACM、WSDM、IEEE ICDM Workshops、作者代码及论文 | 对边和窗口的两种告警分开；工作坊写明轨道 |
| `anomalous dense subgraphs edge streams`、`Spade real-time fraud evolving graphs`、`Dupin parallel densest subgraph` | PVLDB、SIGMOD、作者所在大学存档 | 增量检测与仅提高并行运算速度分别登记。扩展发表版本不重复计数 |
| `graph change point detection dynamic networks`、`missing values temporal dependence`、`Fréchet statistics graph online change point` | Springer、Elsevier、IEEE、Wiley 与作者稿 | 原始序列须有图结构。保留股票相关、航运、社交网络案例并注明迁移限制 |
| `DP-DGAD dynamic prototypes`、`STG-DGR streaming transaction graphs` | WWW 正式发表页及公开作者稿 | 区分目标域调整、无标签适配、生成回放以及完全冻结的零样本预测 |

已有索引中的 BAG、DyGADBench、TempASD、ARES 只作回溯入口。Spade+ 与 Spade 具有共同框架，本轨只登记原始方法。处理多元传感器时间序列、仅把变量的相关性当作固定邻接而未提供关系变化实验的候选，未用于补充边流直接检测条目。未把综述中的性能转述当作对应模型的全文证据，没有记录不可复核的总命中量。

可沿原始入口回查：[SAD](https://www.ijcai.org/proceedings/2023/256) · [GeneralDyG](https://ojs.aaai.org/index.php/AAAI/article/view/35508) · [KDD 草图方法](https://doi.org/10.1145/3580305.3599504) · [Spade](https://www.vldb.org/pvldb/vol16/p461-jiang.pdf) · [孪生图变点检测](https://doi.org/10.1007/s10994-023-06405-x)。
