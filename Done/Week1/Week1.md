# Week 1 工作报告

1. 使用 mugen 在 Qemu 测试了 ``os-basic`` 、 ``openssh`` 、 ``admin_guide`` 、 ``byacc2.0`` 、 ``autoconf213`` 、 ``auter`` 六个软件包
2. 使用 mugen 测试了 [cli0.txt](./cli0/riscv/cli0.txt) 中包含的软件包，并在 Qemu x86 重新测试了失败的软件包，生成测试报告 [mergeCause.csv](./cli0/mergeCause.csv)
3. 完善 [result_parser.py](./scripts/result_parser.py) ，基于 result_parser 编写 mugen 测试报告生成脚本 [result_merge.py](./script/result_merge.py)
