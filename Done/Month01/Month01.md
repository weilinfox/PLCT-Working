# Month 1 工作报告 23/07/05-23/07/27

## 本月测试工作

### fail 测试用例

1. 完成 rest0 缺失的测试用例以及部分需要手动重测的测试用例 pr [#12](https://github.com/KotorinMinami/res_list/commit/6fc49cbc70c91a39eaf261a2fef64af8a1314883) [#13](https://github.com/KotorinMinami/res_list/commit/2dcda539b51a7153a76c640396ea4dd5c03addea)
2. 完成 rest1 部分的日志 fail 部分分析。 pr [#14](https://github.com/KotorinMinami/res_list/commit/eaffea9454b6df1a29d65b3cf3d3d7228f3b05dc)
3. 整理 rest0-rest3 的测试分析结果并汇总 baseOS 仅 fail 的测试用例列表 [baseOSFailed.csv](/Done/Month01/Week7/baseOSFailed.csv)
4. 从所有未分析的测试 [pickedFail.csv](https://github.com/KotorinMinami/task_apply/blob/main/pickedFail.csv) 中筛选 baseOS fail 的测试进行分析，共计 75 个测试用例。其中有 2 个更改状态为 x86 fail ； 18 个与测试环境、超时时间有关，需要手动重测重新分析。在这些重测的里面，有 11 个经过重测通过了
5. 整理并提交 pickedFail.csv 中筛选 baseOS fail 的重测日志和分析结果 pr [#15](https://github.com/KotorinMinami/res_list/commit/6d57a942a10f7d03f1328c4ab8467a4aa3723628#diff-bfa9c1df7935605b17b8b9fa1d12144452c57044c10e3ae10bc8a8468115a8b0)
6. 利用黄烁老师提供的 baseOS 测试列表 [oe.txt](/Note/oe.txt) ，编写脚本 [baseOS-pick.py](/Note/baseOS-pick.py) 从 [failureCause.csv](https://github.com/KotorinMinami/res_list/blob/master/failureCause.csv) 筛选 baseOS 部分的测试结果共 2093 个测试用例，再进一步筛选得到完整的 baseOS fail 清单共 175 个测试用例
7. 分析 baseOS fail 清单中没有分析的日志条目。发现 2 个样例有日志更新且更新后的结果为通过； 2 个样例日志结果为通过但是被错误标记为 fail ； 3 个样例手动重测通过； graphviz 测试套中的日志为老版本的 mugen 测得的，且日志中没有有效信息，故也进行了重测并更新条目；共更新 41 个测试用例的分析。 pr [#18](https://github.com/KotorinMinami/res_list/pull/18)

### x86 fail 测试用例

1. 从所有测试筛选 x86 fail 测试 [baseOS_x86_fail.csv](/Done/Month01/Week8/csv/baseOS_x86_fail.csv) ，分为两份 [x86fail0.txt](./lists/x86fail0.txt) 和 [x86fail1.txt](./lists/x86fail1.txt) 与旭昌老师合作分析，我负责 x86fail0.txt 部分共计 290 个测试用例
2. x86fail0 共 262 个用例确认为 x86 fail ，其余有 26 个测试状态转为 success ， 2 个测试状态转为 fail 。完整分析表格 [baseOS_x86_fail.csv](/Done/Month01/Week9/lists/baseOS_x86_fail.csv) ，重测日志和测试状态更新全部提交 pr [#18](https://github.com/KotorinMinami/res_list/pull/18/files) [#19](https://github.com/KotorinMinami/res_list/pull/19/files) [#21](https://github.com/KotorinMinami/res_list/pull/21/files)
3. 整理 x86fail0 问题汇总 [x86_fail_cause.md](/Done/Month01/Week10/x86_fail_cause.md) ，并将所有 x86 fail 测试分为三类：一类两个架构失败原因完全一样 [class1.csv](/Done/Month01/Week9/lists/lists/class1.csv) ，二类两个架构原因基本一样但是 riscv 有特殊的缺陷 [class2.csv](/Done/Month01/Week9/lists/class2.csv)  ，三类两个架构原因完全不同 [class3.csv](/Done/Month01/Week9/lists/lists/class3.csv)
4. 整理测试环境问题汇总 [cause.md](/Done/Month01/Week9/lists/cause.md) 
5. 整理 oerv 2303 mugen 测试文档和日志并提交到 [OERV 2303 Test](https://gitee.com/yunxiangluo/oerv-2303-test) 仓库 pr [!2](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/2)
6. 补充 baseOS 失败用例表格 [baseOSFailed.csv](https://github.com/KotorinMinami/res_list/blob/master/baseOSFailed.csv) 并提交 pr [#23](https://github.com/KotorinMinami/res_list/pull/23) [!4](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/4)

### success 测试用例

1. 测试 mugen greatsql 用例得到通过日志并提交 pr #23 [!5](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/5)

### 测试脚本

1. 在分析 x86 fail log 的时候发现，在 riscv 上没有出现的测试环境问题，在 x86 测试的出现了，所以尝试将 qemu_test.py 更改为同时支持 riscv 和 x86 的， [qemu_test.py](/Note/qemu_test.py) 。顺便修了没有 ``import sys``

## 遗留的问题

+ [baseOSFailed.csv](https://gitee.com/yunxiangluo/oerv-2303-test/blob/master/BasicTest/function/mugen/baseOSFailed.csv) 不全
+ [table.md](https://gitee.com/yunxiangluo/oerv-2303-test/blob/master/BasicTest/function/mugen/table.md) 同步不完全
+ [README.md](https://gitee.com/yunxiangluo/oerv-2303-test/blob/master/BasicTest/function/mugen/README.md) 同步不完全

## 关联的提交

+ mugen 测试结果汇总仓库 KotorinMinami/res_list pr [#12](https://github.com/KotorinMinami/res_list/commit/6fc49cbc70c91a39eaf261a2fef64af8a1314883) [#13](https://github.com/KotorinMinami/res_list/commit/2dcda539b51a7153a76c640396ea4dd5c03addea) [#14](https://github.com/KotorinMinami/res_list/commit/eaffea9454b6df1a29d65b3cf3d3d7228f3b05dc) [#15](https://github.com/KotorinMinami/res_list/commit/6d57a942a10f7d03f1328c4ab8467a4aa3723628#diff-bfa9c1df7935605b17b8b9fa1d12144452c57044c10e3ae10bc8a8468115a8b0) [#18](https://github.com/KotorinMinami/res_list/pull/18) [#23](https://github.com/KotorinMinami/res_list/pull/23)
+ oerv 2303 测试仓库 yunxiangluo/oerv-2303-test [!2](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/2) [!4](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/4) [!5](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/5)
