# Week 9 工作报告

+ 从所有测试筛选 x86 fail 测试 [baseOS_x86_fail.csv](./lists/baseOS_x86_fail.csv) ，分为两份 [x86fail0.txt](./lists/x86fail0.txt) 和 [x86fail1.txt](./lists/x86fail1.txt) ，我负责 x86fail0.txt 部分
+ x86fail0 除去 systemd 的 36 个用例是我以前分析过的，一共是 254 个用例。其中 155 个完成分析，其余有 99 个需要重测。<br> x86 和 riscv 重测完成 27 个， riscv 重测完成 14 个，还有 58 个没有出重测结果。
   + **没有完成**重测的 72 个中，有 3 个是超时需要重测，其他都是依赖多个节点进行测试：重测过程中前几个测试用例与其余节点通信正常，后面的测试用例与其他节点失联。
   + **完成**重测的测试中，有 18 个测试状态转为 success ， 2 个测试状态转为 fail 。
+ 完整的 x86fail0 分析结果 [cause.md](./lists/cause.md) 分析结果表格 [baseOS_x86_fail.csv](./lists/baseOS_x86_fail.csv)
