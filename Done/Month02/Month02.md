# Month 2 工作报告 23/08/07-23/08/31

## 自动化测试脚本更新

+ 为 ``qemu_test.py`` 添加了 x86 支持并针对 oE 2309 x86 镜像适配了 UEFI 启动，这样如果要在 rv 和 x86 上进行测试，可以用同一个脚本进行，保证 ``--addMachine`` ``--addNic`` 测试环境的一致性，也添加了更多可以在配置文件中配置的参数，修复了旧脚本的 ``-append`` 问题，同时更新了这个脚本相关的文档； pr [#15](https://github.com/brsf11/mugen-riscv/pull/15) [#18](https://github.com/brsf11/mugen-riscv/pull/18) [#20](https://github.com/brsf11/mugen-riscv/pull/20)
+ 修复 ``mugen_riscv.py`` 在复制失败日志的时候判断错误的问题 pr [#19](https://github.com/brsf11/mugen-riscv/pull/19)

## 测试工作

+ 与 ROS 小队合作对 ROS2 进行测试，复现了 ROS 小队提出的测试流程和测试结果并产出报告 [ROS2_Humble_oerv2203_test.md](./Week1/ROS_test/ROS2_Humble_oerv2203_test.md)，完成了 Qemu 平台测试安装和卸载部分的[日志和描述](https://gitee.com/yunxiangluo/open-euler-risc-v-ros2-humble/blob/master/QEMU/README.md#%E6%B5%8B%E8%AF%95%E5%AE%89%E8%A3%85%E5%92%8C%E5%8D%B8%E8%BD%BD) ，并在 VisionFive2 上完成了 ROS2 测试并产出[测试报告](https://gitee.com/yunxiangluo/open-euler-risc-v-ros2-humble/tree/master/VisionFive2) pr [!2](https://gitee.com/yunxiangluo/open-euler-risc-v-ros2-humble/pulls/2) [!13](https://gitee.com/yunxiangluo/open-euler-risc-v-ros2-humble/pulls/13) [!17](https://gitee.com/yunxiangluo/open-euler-risc-v-ros2-humble/pulls/17)
+ 进行 oErv 2309 的 mugen 测试，完成 [oe2309test2](./Week1/oe2309test2) 和 [oe2309test5 部分](./Week1/oe2309test5) 两个部分的测试用例，编写脚本生成初始表格 [gen_list.py](./Week1/oe2309test2_round1/gen_list.py) ，分析了在 2303 成功但是在 2309 失败了的测试用例，得到一个 2309 新增失败报告 [2309_new_fail.md](./Week1/oe2309test2_round1/2309_new_fail.md) ，分析了在 2303 和 2309 均 fail 的测试并提交 pr [#27](https://github.com/KotorinMinami/res_list/pull/27) [#31](https://github.com/KotorinMinami/res_list/pull/31)
+ 进行 oErv 2309 的 mugen 测试 fail 原因分类，完成了 [failureCause.csv](https://github.com/KotorinMinami/res_list/blob/bf9a721518cf2683b77307e7de820bfd1fe2e14a/oe-rv2309/failureCause.csv) 中已有错误原因的分类，产出原因分类文档 [2309_new_fail.md](./Week2/2309_new_fail.md) ，也对一些超时用例进行重测并提交重测结果 pr [#32](https://github.com/KotorinMinami/res_list/pull/32)
+ 进行 oE 2309 x86 的对比测试，在 [Alpha](http://121.36.84.172/dailybuild/openEuler-23.09/openeuler-2023-08-16-23-49-42/) 镜像完成了  [oe2309test2](./Week1/oe2309test2) 部分用例的测试工作，在 [RC1](http://121.36.84.172/dailybuild/EBS-openEuler-23.09/rc1_openeuler-2023-08-23-20-06-19/) 镜像完成了 oErv 2309 失败的测试中 [oe2309testx86_2](./Week3/oe2309testx86_2) 部分用例的测试工作，得到测试 log 并提交 pr [#36](https://github.com/KotorinMinami/res_list/pull/36)

## 单项测试

+ 在 Milkv Duo 开发板进行 pinpong 部署，产出 pinpong 安装文档 [gitee 仓库](https://gitee.com/weilin2023/pinpong-milkv-duo-doc/)

## 其他工作

+ 在 RISCV 2023 中国峰会算能展台参与服务器的运维和解说工作

## 关联的提交

+ mugen-riscv 仓库 brsf11/mugen-riscv pr [#15](https://github.com/brsf11/mugen-riscv/pull/15) [#18](https://github.com/brsf11/mugen-riscv/pull/18) [#19](https://github.com/brsf11/mugen-riscv/pull/19) [#20](https://github.com/brsf11/mugen-riscv/pull/20)
+ mugen 测试结果汇总仓库 KotorinMinami/res_list pr [#27](https://github.com/KotorinMinami/res_list/pull/27) [#31](https://github.com/KotorinMinami/res_list/pull/31) [#32](https://github.com/KotorinMinami/res_list/pull/32) [#35](https://github.com/KotorinMinami/res_list/pull/35) [#36](https://github.com/KotorinMinami/res_list/pull/36)
+ mugen openEuler RISC-V 23.09 测试结果仓库 yunxiangluo/open-euler-risc-v-23.09-test pr [!9](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/9)
+ ROS2 测试结果仓库 yunxiangluo/open-euler-risc-v-ros2-humble pr [!2](https://gitee.com/yunxiangluo/open-euler-risc-v-ros2-humble/pulls/2) [!13](https://gitee.com/yunxiangluo/open-euler-risc-v-ros2-humble/pulls/13) [!17](https://gitee.com/yunxiangluo/open-euler-risc-v-ros2-humble/pulls/17)
+ pinpong 安装文档 [gitee 仓库](https://gitee.com/weilin2023/pinpong-milkv-duo-doc/)
