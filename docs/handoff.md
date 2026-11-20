# 本地运行与维护

在源码目录中执行以下命令核对书目、内部链接，并在 24 个虚构节点上运行三种方法。

```bash
python3 scripts/catalog.py --check
python3 scripts/verify_extended.py
python3 examples/node_baselines.py
```

Elliptic 的合成样例协议测试另需 NumPy 和 scikit-learn，可在 Python 虚拟环境中运行。真实数据的获取、切分和运行方法见[试验说明](../pilots/elliptic/README.md)。

```bash
python3 -m pip install -r pilots/elliptic/requirements.txt
python3 -m unittest discover -s pilots/elliptic -p 'test_*.py' -v
```

## 维护书目

书目更新完成后，在工作分支运行上述检查，再通过 Pull Request 提交。字段含义和审阅流程见[贡献说明](../CONTRIBUTING.md)。

## 第一次周会

按[首场周会议程](../meetings/kickoff.md)为双类标签和仅正常标签两条路线确定执行人、交叉复核人和共用测试对象。下一次周会可直接比较同一评测协议下的基线结果、告警预算和仍待核实的问题。
