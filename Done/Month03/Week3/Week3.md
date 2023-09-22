# Month 3 Week 3 工作报告 23/09/18-23/09/22

+ 配合开发老师给出的建议进行复现和重测，更新 bug 追踪共享文档
+ mugen 测试方法开发老师不易复现，对测试方法的说明文档进行了补充，也更新了一些过时内容 pr [!52](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/52)
+ 对一些意外失败的用例进行重新测试，共有 61 个用例状态从 fail 转为 success ，并更新测试报告 pr [!56](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/56)
+ 用 [oe2309testv2_3](https://github.com/weilinfox/PLCT-Working/blob/master/Done/Month02/Week4/oe2309testv2_3) 列表对 RC3 镜像进行重测，提交日志 pr [#53](https://github.com/KotorinMinami/res_list/pull/53)
+ 做了一些 2309 报告仓库相关的整理工作 pr [!8](https://gitee.com/yunxiangluo/openeuler-riscv-23.09-test/pulls/8) [!12](https://gitee.com/yunxiangluo/openeuler-riscv-23.09-test/pulls/12) [!57](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/57) 
+ 参加了周三的 QA 例会和周五的 QA 补充会议分享了 mugen 相关的测试结果
+ python subprocessing 遇到一些奇怪的问题，一部分虚拟机启动一半假死，影响 RC3 测试进度，故编写了使用 screen 工具将 qemu 挂后台的 [qemu_test.py](https://github.com/weilinfox/PLCT-Working/blob/master/Note/qemu_test_screen.py) 。使用 screen 另一个好处是在测试进入奇怪的状态时人工查看状态。

### 遗留问题

+ 二号机偶现外网流量向网桥走导致无法访问外网的情况，症状为 ``ip route`` 通往网桥网卡的优先级比外网可用的网卡优先级要高，可能需要排查原因以及 qemu_test.py 配置网卡的过程是否有潜在问题

