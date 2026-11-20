# GeneralDyG：同一架构怎样处理节点与边两种输出

作者用带时间的自中心子图描述一个事件，再从其局部拓扑和有序历史中提取特征。Problem Definition 将训练阶段的事件视为正常，异常标签用于测试。复用同一架构不意味着边级与节点级分数具有相同含义。[AAAI 论文及实验](https://ojs.aaai.org/index.php/AAAI/article/download/35508/37663)

**两种数据怎样评。** SWaT 与 WADI 是工业控制数据；作者把这类任务作为节点级检测。Bitcoin-Alpha 与 Bitcoin-OTC 的边是用户间的信任评价，采用测试集注入异常的协议，在多个注入比例下报告 AUC 与 AP。表2单列工业节点任务的 F1，表3比较去掉自中心图、TensGNN 或 Transformer 的效果。它们回答的是不同数据生成和标签条件下的问题。[Problem Definition、数据集段、表2–4](https://ojs.aaai.org/index.php/AAAI/article/download/35508/37663)

**复现问题。** 对同一时间切分，分别在随机替换端点、真实罕见但合法的首次互动以及经标注事件上测 AP。用等大小的局部子图做消融，区分结构收益与历史上下文长度带来的收益。[作者代码](https://github.com/YXNTU/GeneralDyG)
