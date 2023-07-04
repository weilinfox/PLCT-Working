# Month 2 工作报告

## 测试

1. 特性测试测试策略的编写 [feature_test.md](../Week5/feature_test.md) ，在周会后和 Kevin 进行了一个文档的同步 [#1](https://github.com/KevinMX/PLCT-Tarsier-Works/pull/1)
2. 完成了 mugen cli0 部分软件包 fail 和 x86_fail 的原因排查，产出两个测试报告 [riscv-failed.md](../Week2/riscv-failed.md) 和 [rv86_failed.md](../Week3/rv86_failed.md) 和汇总表格 [mergeFailure.csv](../Week3/mergeFailure.csv) 和 [mergeX86Failure.csv](../Week3/mergeX86Failure.csv)
3. 完成了 mugen rest0 部分软件包的测试， riscv 测试结果[仓库](./riscv/) 和 x86 复测结果[仓库](./x86/) 并汇总测试结果 [mergeCause.csv](./mergeCause.csv)
4. 完成了 mugen rest0 部分软件包的 fail 原因排查，产出分析结果 [mergeFailed.csv](./mergeFailed.csv)

## 提交

1. mugen cli0 fail 原因排查提交 pr [#4](https://github.com/KotorinMinami/res_list/pull/4)
2. mugen cli0 x86_fail 原因排查提交 pr [#7](https://github.com/KotorinMinami/res_list/pull/7)
3. mugen rest0 测试结果和 fail 原因排查提交 pr [#9](https://github.com/KotorinMinami/res_list/pull/9)
4. mugen-riscv.py 可能出现 utf-8 解码错误导致测试中断的情况，修复并提交 pr [#14](https://github.com/brsf11/mugen-riscv/pull/14)

## Todo

1. rest0 重测 ocaml-22.03 测试
2. 补全 systemd 缺失的两个用例
