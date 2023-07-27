# Week 10 工作报告

+ 整理 mugen 测试 x86 fail 失败原因汇总并合并入文档，整理 oerv 2303 mugen 测试文档和日志并提交到 [OERV 2303 Test](https://gitee.com/yunxiangluo/oerv-2303-test) 仓库 pr [!2](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/2)
+ 整理 baseOS 失败用例表格并提交 pr [#23](https://github.com/KotorinMinami/res_list/pull/23) [!4](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/4)
+ 测试 mugen greatsql 用例得到通过日志并提交 pr #23 [!5](https://gitee.com/yunxiangluo/oerv-2303-test/pulls/5)

## 其他

+ 在分析 x86 fail log 的时候发现，在 riscv 上没有出现的测试环境问题，在 x86 测试的出现了，所以尝试将 qemu_test.py 更改为同时支持 riscv 和 x86 的，顺便修了没有 ``import sys`` [qemu_test.py](/Note/qemu_test.py)
