# Month 3 工作报告 23/09/01-23/09/26

## mugen 测试工作

+ 完成 oErv 和 oE 2309 RISC-V **RC1** 的 mugen 测试进行了 [oe2309testv2_3](https://github.com/weilinfox/PLCT-Working/tree/master/Done/Month02/Week4/oe2309testv2_3) 部分的测试；单独进行了 os-basic 、 firewalld 、 openssh 、 ndisc6 的重测。并提交日志 pr [#40](https://github.com/KotorinMinami/res_list/pull/40) [#41](https://github.com/KotorinMinami/res_list/pull/41/) [#42](https://github.com/KotorinMinami/res_list/pull/42) [#43](https://github.com/KotorinMinami/res_list/pull/43) [#44](https://github.com/KotorinMinami/res_list/pull/44) [!22](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/22)
+ 完成 oErv 2309 **RC2** 的 mugen 测试进行了 [oe2309testv4_1](https://github.com/weilinfox/PLCT-Working/blob/master/Done/Month03/Week2/oe2309testv4_1) 部分的测试并提交日志；完成 oE 2309 **RC3** 开展的 x86 对比测试并提交日志 pr [#45](https://github.com/KotorinMinami/res_list/pull/45) [#46](https://github.com/KotorinMinami/res_list/pull/46) [#48](https://github.com/KotorinMinami/res_list/pull/48)
+ 对 RC2 的测试和 x86 对比测试的日志进行分析 [Week2.md](https://github.com/weilinfox/PLCT-Working/blob/master/Done/Month03/Week2/Week2.md)  [独立 md 文档](https://github.com/weilinfox/PLCT-Working/tree/master/Done/Month03/Week2/md)
+ 完成 oErv 2309 **RC3** 的 mugen 测试进行了  [oe2309testv2_3](https://github.com/weilinfox/PLCT-Working/blob/master/Done/Month02/Week4/oe2309testv2_3) 部分和 os-basic 的测试，提交日志 [round3](https://github.com/weilinfox/PLCT-Working/tree/master/Done/Month03/Week3/round3) pr [#53](https://github.com/KotorinMinami/res_list/pull/53)
+ 配合开发老师对 RC1 仅 riscv 失败相关 184 个用例的重测、问题分析和修复建议的复现，得到一些重测日志并在共享文档同步 91 个用例的复测结果 [clevis](https://github.com/weilinfox/PLCT-Working/tree/master/Done/Month03/Week2/clevis) [round1_retest](https://github.com/weilinfox/PLCT-Working/tree/master/Done/Month03/Week3/round1_retest)
+ RC1 测试报告中 mugen 测试方法开发老师不易复现，故对测试方法的说明文档进行了补充，也更新了一些过时内容 pr [!52](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/52)
+ RC1 仅 riscv 失败相关用例中有 61 个用例状态从 fail 转为 success ，并更新测试报告 pr [!56](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/56)
+ RC3 测试报告中 mugen 新增仅在 riscv 失败原因进行分析，并同步分析结果进入文档 pr [!60](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/60) [!63](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/63)
+ 另外还做了一些 2309 报告仓库相关的整理工作 pr [!8](https://gitee.com/yunxiangluo/openeuler-riscv-23.09-test/pulls/8) [!12](https://gitee.com/yunxiangluo/openeuler-riscv-23.09-test/pulls/12) [!57](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/57) [!59](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/59)
+ 向上游提交两个 mugen 修复，正在观望合入进展 pr [!1992](https://gitee.com/openeuler/mugen/pulls/1992) [!1993](https://gitee.com/openeuler/mugen/pulls/1993)
+ 参加了 20 日的的 QA 例会， 22 日的 QA 补充会议分享了 mugen 相关的测试结果，旁听了 26 日的 release 会议

## mugen 测试脚本

+ mugen 自动化测试脚本在应用 python subprocessing 包产生了一些问题，编写了使用 screen 工具管理 qemu 进程的方案作为备选 [qemu_test.py](https://github.com/weilinfox/PLCT-Working/blob/master/Note/qemu_test_screen.py)
+ mugen 测试流程的改进需要利用 mugen combination 功能进行，尝试编写 combination test 的自动化测试脚本 [combination_env.sh](https://github.com/weilinfox/PLCT-Working/blob/master/Note/combination_env.sh)
+ mugen 测试常有手动测试需求，编写了自动配置手动测试环境的脚本 [manual_env_setup.sh](https://github.com/weilinfox/PLCT-Working/blob/master/Note/manual_env_setup.sh)

## 单项测试

+ 设计 openkylin 单项测试策略、完成 openkylin 的单项测试并产生测试文档和测试报告 pr [!1](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/1) [!2](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/2) [!3](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/3) [!4](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/4) [!5](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/6) [!6](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/6)
+ 更新已有的 autopkgtest 安装文档 pr [#1](https://github.com/KotorinMinami/autopkgtest_for_all_linux/pull/1)

## 其他工作

+ 向 AUR 提交 autopkgtest 的 PKGBUILD [主页](https://aur.archlinux.org/packages/autopkgtest)
+ 更新 AUR 软件包 debmake 的 PKGBUILD 到最新版本 4.4.0 并修正依赖 [主页](https://aur.archlinux.org/packages/debmake)

## 关联的提交

+ mugen 测试结果汇总仓库 KotorinMinami/res_list pr [#40](https://github.com/KotorinMinami/res_list/pull/40) [#41](https://github.com/KotorinMinami/res_list/pull/41/) [#42](https://github.com/KotorinMinami/res_list/pull/42) [#43](https://github.com/KotorinMinami/res_list/pull/43) [#44](https://github.com/KotorinMinami/res_list/pull/44) [#45](https://github.com/KotorinMinami/res_list/pull/45) [#46](https://github.com/KotorinMinami/res_list/pull/46) [#48](https://github.com/KotorinMinami/res_list/pull/48) [#53](https://github.com/KotorinMinami/res_list/pull/53)
+ oErv 2309 mugen 内部仓库 yunxiangluo/open-euler-risc-v-23.09-test pr [!22](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/22) [!52](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/52) [!56](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/56) [!57](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/57) [!59](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/59) [!60](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/60) [!63](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/63)
+ oErv 2309 mugen 交付仓库 yunxiangluo/openeuler-riscv-23.09-test pr [!8](https://gitee.com/yunxiangluo/openeuler-riscv-23.09-test/pulls/8) [!12](https://gitee.com/yunxiangluo/openeuler-riscv-23.09-test/pulls/12)
+ openkylin licheepi 测试结果仓库 yunxiangluo/openkylin-licheepi4a-test pr [!1](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/1) [!2](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/2) [!3](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/3) [!4](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/4) [!5](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/6) [!6](https://gitee.com/yunxiangluo/openkylin-licheepi4a-test/pulls/6)
+ autopkgtest 安装文档仓库 KotorinMinami/autopkgtest_for_all_linux pr [#1](https://github.com/KotorinMinami/autopkgtest_for_all_linux/pull/1)
+ mugen 上游仓库 openeuler/mugen pr [!1992](https://gitee.com/openeuler/mugen/pulls/1992) [!1993](https://gitee.com/openeuler/mugen/pulls/1993)
