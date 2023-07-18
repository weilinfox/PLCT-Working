# Week 8 工作报告

+ 从所有未分析的测试 [pickedFail.csv](https://github.com/KotorinMinami/task_apply/blob/main/pickedFail.csv) 中筛选 baseOS fail 的测试进行分析，共计 75 个测试用例。其中有 2 个更改状态为 x86 fail ； 18 个与测试环境、超时时间有关，需要手动重测重新分析。在这些重测的里面，有 11 个经过重测通过了
+ 整理并提交 pickedFail.csv 中筛选 baseOS fail 的重测日志和分析结果 pr [#15](https://github.com/KotorinMinami/res_list/commit/6d57a942a10f7d03f1328c4ab8467a4aa3723628#diff-bfa9c1df7935605b17b8b9fa1d12144452c57044c10e3ae10bc8a8468115a8b0)
+ 黄烁老师提供了一个 baseOS 测试列表 [oe.txt](../../Note/oe.txt) ，利用脚本 [baseOS-pick.py](../../Note/baseOS-pick.py) 从 [failureCause.csv](https://github.com/KotorinMinami/res_list/blob/master/failureCause.csv) 筛选 baseOS 部分的测试结果共 2093 个测试用例，再进一步筛选得到完整的 baseOS fail 清单共 175 个测试用例
+ 检查 baseOS fail 清单中是否还有没有分析的日志条目。发现 2 个样例有日志更新且更新后的结果为通过； 2 个样例日志结果为通过但是被错误标记为 fail ； 3 个样例手动重测通过； graphviz 测试套中的日志为老版本的 mugen 测得的，且日志中没有有效信息，故也进行了重测并更新条目；共更新 41 个测试用例的分析。 pr [#18](https://github.com/KotorinMinami/res_list/pull/18)

