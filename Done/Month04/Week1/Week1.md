# Month 4 Week 1 工作报告 23/10/07-23/10/08

~~23/09/29-23/10/06 中秋十一双节假期~~

+ 节前 qemu_test.py 的修复 pr 合入后，对新的脚本进行了一次验证，打开 screen 功能对 [task_v2](https://github.com/weilinfox/res_list/tree/master/oe-rv2309/task_v2) 中的三列表合并为一个列表 [baseOS_v4](https://github.com/weilinfox/PLCT-Working/tree/master/Done/Month04/Week1/baseOS_v4) 测试，一共 273 个测试套，可以一次跑完不会卡住。只有 firewalld 、 systemd 这种会搞坏 sshd 的测试套需要手动干预。 参考配置 [oE23090927](https://github.com/weilinfox/PLCT-Working/tree/master/Done/Month04/Week1/oE23090927) ，在 R9 5900X 历时 11 小时，基本实现席老师说的一觉起来 log 出来
+ 同步 oErv 2309 v4 部分 log 分析结果到测试报告 pr [!74](https://gitee.com/yunxiangluo/open-euler-risc-v-23.09-test/pulls/74)
+ 完成一些技术分享的文字内容

