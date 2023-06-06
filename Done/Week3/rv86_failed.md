# x86 fail 用例汇总

## lvm2

1. 测试1～3块额外的块设备，但是 ``suite2cases/lvm2.json`` 中缺失相关配置。
2. 两个测试没有引入测试对象软件包 lvm2
3. 两个测试依赖内核模块 dm-mirror （这个内核模块在 x86 不缺）
4. ``pvs`` 相关命令有问题 ``pvs | sed -n 3p | awk {'print$4'} | grep "30.00m"`` 改为 ``pvs | awk {'print$4'} | grep "30.00m"``

在使用新的 ``lvm2.json`` 测试时发现 x86 问题更多，它会将 ``/dev/sr0`` 误认为是可用的块设备进行测试，导致测试错误。

## kernel

1. 检查了 cpu rdrand 特性和 ARCH_RANDOM=y 内核编译选项 （前者 qemu 选项 -cpu qemu64,+rdrand ， 后者 x86 也没有）
2. 没有配置 CONFIG_BOOTPARAM_HUNG_TASK_PANIC_VALUE 内核编译选项（x86 同理）
3. 缺失内核模块 hinic.ko  和 cifs （x86 为 hinic.ko.xz 所以也 fail ， cifs x86 有）
4. 使用了未定义的 swap 空间 /dev/dm-1 和 /dev/openeuler/swap （x86 同理）
5. 测试套写错了（见图）

![抄错测试套代码](./kernel_oe_test_cifs.png)

## hostname

测试脚本没有引入 ``hostname`` 这个软件包，这个软件包在 oerv 预装了，在 x86 没有预装。

在 oerv 上 ``/etc/sysconfig/network`` 这个文件不存在导致了测试出错，``echo "NETWORKING=yes" > /etc/sysconfig/network`` 后可以测试通过。

在 x86 上安装了这个包以后测试可以通过。

## crontabs

没搞懂原因。 oerv 和 x86 出错原因一致。

```
# crontab -u root -l -s
Cannot obtain SELinux process context
```

## dnf

dnf 比较复杂，原因暂时都被写为 “oerv 和 x86 的软件源结构不同（暂定）”

# 附录
