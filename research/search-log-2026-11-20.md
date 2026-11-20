# FinGraph 近五年顶会检索工作记录（2026-11-20）

## 版本范围及溯源原则

以下为专题增补包的检索记录。两份附件的合并口径见[变更日志](CHANGELOG_2026-11-20.md)。专题增补包在原始 **32** 篇代表论文上新增 **34** 篇、合计 **66** 篇（2022—2026年为主，保留2022年前经典）。本轮是“结构化扩充＋重点核查”，**不是**宣称穷尽全部 CCF 顶会的系统综述，也未保存数据库原始命中总量／排除总量；后续若投稿 systematic review，应另行执行可复核的完整检索导出和 PRISMA 式筛选。所有网页核查截至 2026-11-20，不推定会议未公布论文的录用情况。

| 本轮实际检索域 | 具体检索式／词组（精炼记录） | 优先来源与核查方法 | 本轮判定／发现 |
| --- | --- | --- | --- |
| KDD 2026 | `KDD 2026 CR-Aug TransXion DyGADBench graph anomaly detection` | KDD 2026 官方 paper list，ACM DOI，作者仓库 | CR-Aug 为 C2 正常标签路线，TransXion 为 E3 合成交易边标签，DyGADBench 是动态图评测；不能混作同一预测任务 |
| NeurIPS 2022–2025 | `graph anomaly detection semi-supervised RHO GADBench BOND GGAD` | NeurIPS Proceedings 2022/23/24/25 官方页 | GADBench 标注 Datasets and Benchmarks，GGAD 和 RHO 均与少量正常标签相关；2026 截止日未发现可核验完整官方论文目录，**不臆造** |
| ICML 2022–2026 | `ICML 2025 graph-level anomaly diffusion self discriminative CurvGAD`; `ICML 2026 spectral graph anomaly HSMAD federated graph anomaly` | PMLR 2022、2024、2025、2026 原文页 | 新增图级检测、曲率、谱特征与联邦数据漂移方向；图级不自动等于金融团伙识别 |
| ICLR 2024–2026 | `ICLR graph anomaly detection ConsisGAD graph anomaly-aware pre-training` | ICLR Conference proceedings | 保留初版 ICLR ConsisGAD 与 APF；避免假装初版以外又新添 ICLR |
| WWW / The Web Conference 2025 | `WWW 2025 Guided Relation Diffusion Generation graph fraud`; `spoofing transaction graph 2025 WWW` | ACM DOI / 会议目录结果 | 补入 Grad 和 spoofing transaction detection；核对是主会论文还是其他类别后再细分 track |
| AAAI 2024–2026 | `fraud detection with extremely limited labels graph 2025 CGNN`; `AAAI 2026 BAG dynamic graph anomaly`, `2026 binary message passing semi-supervised` | AAAI Proceedings DOI/摘要 | 重点填补双类少量标签、动态图基准、无标签异配性、频域等方向 |
| IJCAI 2024–2026 | `IJCAI 2025 fraud few labeled MimbFD ABNet UNPrompt`; `IJCAI 2026 DRESS semi-supervised GRADE zero-shot CAMERA graph anomaly` | IJCAI Proceedings 官方 HTML 全文／摘要 | 2025 MimbFD 使用少量**两类**标签，UNPrompt 是源图训练后目标图零样本；2026 重点关注受限监督、跨域和测试时适配 |
| SIGMOD / VLDB / ICDE | `PVLDB transaction fraud anomaly graph temporal benchmark`; `SIGMOD graph anomaly detection benchmark money laundering`; `ICDE temporal graph fraud detection` | 相关检索命中作场景边界筛查 | 本次未将没有直接金融图预测对象、标签或交易图实验的通用时间序列/DB 管线论文硬塞进树；这是**待持续补查的空白**，不是“没有相关论文” |
| Nature / Science | `banking records financial abuse Nature 2026`, `credit card metadata Science 2015` | 期刊 DOI/原文 | 作为 F 类金融实证和数据隐私方法，不标为计算机顶会 |
| 数据资源及授权 | `DGraphFin official dataset`, `GADBench T-Finance`, `Elliptic Kaggle`, `Elliptic2 MITIBM`, `IBM AML-Data`, `AMLSim`, `TransXion` | 发布者 GitHub / 官网 / 数据 README | 独立建立 11 条 `datasets/index.json` 资源档案；明确资金流 vs 非资金流和 license 审查 |

## 一手查证入口（可复核）

- **会议录：** [IJCAI 官方](https://ijcai.org/proceedings/2025/365)（MimbFD）、[IJCAI UNPrompt](https://ijcai.org/proceedings/2025/359)、[AAAI Proceedings](https://doi.org/10.1609/aaai.v39i11.33319)（CGNN）、[ICML PMLR](https://proceedings.mlr.press/v267/cai25l.html)（AGDiff）、[NeurIPS RHO](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c273d135fed229f5724df9a0d354b36f-Abstract-Conference.html)、[ACM WWW Grad](https://doi.org/10.1145/3696410.3714520)、[KDD TransXion](https://doi.org/10.1145/3770855.3817550)。
- **实验基准：** [GADBench 作者仓库](https://github.com/squareRoot3/GADBench)（包含标签配置和 F1/AUPRC 等）、[DGraph 发布网站](https://dgraph.xinye.com/dataset)（紧急联系人图）、[Elliptic2 官方教程](https://github.com/MITIBMxGraph/Elliptic2)、[IBM AML-Data](https://github.com/IBM/AML-Data)、[TransXion 作者仓库](https://github.com/chaos-max/TransXion)。
- **版本与分类：** 同一论文按正式年份/标题/DOI 合并；会议 main、datasets & benchmarks、workshop、arXiv/未正式发表、同行评审期刊分别记 `track` 或原始 `venue`。`作者信息待核` 不视作确认。

## 检索覆盖边界与下一轮补查

1. 对每一会议按年份官方 programme 导出“全部命中论文”和筛除原因，补齐真正的定量综述证据；本轮检索经过内容相关性导向筛选，**未**逐项翻完各年份所有 session。
2. 重点补 2026 年 ICML/IJCAI 最新原文细节；同时核对 BAG、DRESS、BMP 的独立官方代码及协议。
3. 在金融领域引入交易**边**风险、团伙**子图**风险与账户**节点**风险三列可比矩阵，分别设计评测而非混同。
4. SIGMOD、VLDB、ICDE 及数据库/流图系统界（时间戳增量索引、超大图训练）仍需专题系统检索，本轮不虚构成果。
