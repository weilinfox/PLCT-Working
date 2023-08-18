# Month 2 Week 2 工作报告 23/08/14-23/08/18

+ mugen 测试 fail 原因分析并 pr [#31](https://github.com/KotorinMinami/res_list/pull/31)
+ mugen 测试 fail 原因分类，完成了 [failureCause.csv](https://github.com/KotorinMinami/res_list/blob/bf9a721518cf2683b77307e7de820bfd1fe2e14a/oe-rv2309/failureCause.csv) 中已有错误原因的分类，合并了栋栋的原因分类文档 [2309_new_fail.md](./2309_new_fail.md) ；对一些超时用例进行重测并提交重测结果 pr [#32](https://github.com/KotorinMinami/res_list/pull/32)
+ 部署 [openEuler 2309 x86_64](http://121.36.84.172/dailybuild/openEuler-23.09/openeuler-2023-08-16-23-49-42/) ，发现无法使用 bios 方式或直接使用内核启动（ kp ），与景坤老师交流得知要用 UEFI 方式启动，部署成功后修改 qemu_test.py 脚本使其支持 UEFI 方式启动并更新文档 pr [#20](https://github.com/brsf11/mugen-riscv/pull/20)
