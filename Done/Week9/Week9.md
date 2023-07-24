# Week 9 工作报告

+ 从所有测试筛选 x86 fail 测试 [baseOS_x86_fail.csv](../Week8/csv/baseOS_x86_fail.csv) ，分为两份 [x86fail0.txt](./lists/x86fail0.txt) 和 [x86fail1.txt](./lists/x86fail1.txt) ，我负责 x86fail0.txt 部分
+ x86fail0 除去 systemd 的 36 个用例是我以前分析过的，一共是 254 个用例。其中 247 个完成分析，其余有 7 个需要重测。
+ 重测的测试中，有 18 个测试状态转为 success ， 2 个测试状态转为 fail 。重测日志和测试状态更新全部提交 pr [#18](https://github.com/KotorinMinami/res_list/pull/18/files) [#19](https://github.com/KotorinMinami/res_list/pull/19/files) [#21](https://github.com/KotorinMinami/res_list/pull/21/files)
+ 导出完整的 x86fail0 分析结果和问题汇总 [cause.md](./lists/cause.md) ，完整分析结果表格 [baseOS_x86_fail.csv](./lists/baseOS_x86_fail.csv)
+ 将所有 x86 fail 测试分为三类，一类两个架构失败原因完全一样 [class1.csv](./lists/class1.csv) ，二类两个架构原因基本一样但是 riscv 有特殊的缺陷 [class2.csv](./lists/class2.csv)  ，三类两个架构原因完全不同 [class3.csv](./lists/class3.csv) 。
