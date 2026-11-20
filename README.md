# FinGraph 金融图异常检测研究社区

FinGraph collects research on **who or what is being scored, which labels are known at training time, and how financial graph detectors are evaluated**. Students and researchers can browse the [English paper titles in the catalogue](catalog/README.md), suggest a paper through an issue, or contribute a reproducible comparison. Chinese or English contributions are welcome.

围绕账户、交易与团伙，按评分对象、训练标签、时间可见性和调查预算组织证据。截至 2026-11-20，全库 **203 篇**，其中 **191 篇**发表于 2022–2026 年，**89 篇**列入综述核心矩阵。论文树含 **7 个主分支、22 个问题**，另有 **23 项数据资源**与 **50 份中文阅读卡**，覆盖 **49 篇不同论文**。

[综述写作底稿](survey/survey-design.md) · [核心方法矩阵](survey/core-matrix.md) · [课题三研究内容二路线图](survey/roadmap.md)

| 我想做什么 | 从这里开始 |
| --- | --- |
| 了解全貌或搜索一个方法 | [论文树](docs/tree.md) · [分支索引与原文](catalog/README.md) · [精读卡目录](notes/README.md) · [JSON](catalog/papers.json) · [CSV](catalog/papers.csv) |
| 准备撰写动态图金融综述 | [综述工作区](survey/README.md) · [候选文献 CSV](survey/candidates.csv) · [筛选协议](survey/protocol.md) |
| 第一次参加讨论 | [四次入门阅读](docs/reading-path.md) · [首场周会议程草案](meetings/kickoff.md) |
| 学会区分训练与评测 | [十分钟运行一个节点任务](examples/README.md) · [Elliptic 首轮实验协议](protocols/elliptic-node-pilot.md) · [运行真实 CSV 的入口](pilots/elliptic/README.md) |
| 查公开数据与检索证据 | [金融图数据资源](datasets/README.md) · [新论文检索日志](research/search-log-2026-11-20.md) · [关键论文证据比较矩阵](research/evidence-matrix-2026-11-20.md) · [学生可执行研究问题](research/research-questions-and-operations.md) |
| 接手复现 | [模型登记](models/README.md) · [BWGNN](models/bwgnn.md) · [GGAD](models/ggad.md) · [CR-Aug](models/cr-aug.md) |
| 添加一篇、组织周会或维护检索 | [贡献说明](CONTRIBUTING.md) · [检索范围和更新方法](docs/search.md) · [周会记录](meetings/README.md) · [本地运行与维护](docs/handoff.md) |

启动包另有三份专题材料，分别整理了[十篇论文及实验建议](docs/expansion.md)、[五篇方法的实验条件](docs/method-analysis.md)和[金融图数据的获取与使用条件](docs/datasets.md)。

### 本期共同问题

在同一张交易图上，历史交易本身已经提供了多少信息？加入上游邻居后，有限的告警复核名额能多发现多少已知异常？双类标签与仅正常标签的实验共享测试对象，各自在同一标签条件下与简单模型比较。

### 两项团队公开工作

- [CR-Aug](notes/cr-aug.md) 面向少量正常标签已知的节点检测，用社区差异指导伪异常生成。
- [TransXion](catalog/README.md#p-transxion) 提供带时间戳的合成交易图和边级标签，适合后续研究交易告警及跨生成器泛化。

### 两个本地命令

```bash
python3 examples/node_baselines.py
python3 scripts/catalog.py --find "C2 仅少量可信正常标签"
```

教学示例自带虚构数据，使用 Python 标准库。书目及三份候选模型卡已经建立，模型的复核状态取决于本库登记的运行和证据。[贡献流程](CONTRIBUTING.md)

### 2026-11-20 专题补录与严谨性说明

以 32 篇首版为起点，专题包的 [34 篇增量清单](research/new-additions-2026-11-20.json) 与启动包的 10 篇增量有 3 篇重合。合并时补回 7 篇启动包独有论文，详见[变更记录](research/CHANGELOG_2026-11-20.md)。专题包突出 CCF 顶会的有监督/半监督、动态图、少标签、跨图迁移、图级与事件级方法。**论文发表与证据**以原始会议录/论文为准；只有作者报告的结果不意味着 FinGraph 已复现。`datasets/index.json` 只索引发布源、不包含第三方数据。2026 年后续新稿、作者代码的可用性、部分 license 和论文细节均仍待维护者继续核查。

本库收录论文出处、中文阅读笔记、数据获取入口和实验代码。教学示例使用虚构数据。第三方论文和数据请从原发布方获取，并遵循其使用条款。

校验：`python3 scripts/catalog.py --check`；`python3 scripts/verify_extended.py`；`python3 -m unittest discover -s pilots/elliptic -p 'test_*.py'`。
