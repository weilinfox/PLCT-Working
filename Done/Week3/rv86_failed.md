# x86 fail 用例汇总

## dnf

dnf 比较复杂，原因暂时都被写为 “oerv 和 x86 的软件源结构不同（暂定）”

## lvm2

1. 测试1～3块额外的块设备，但是 ``suite2cases/lvm2.json`` 中缺失相关配置。
2. 两个测试没有引入测试对象软件包 lvm2
3. 两个测试依赖内核模块 dm-mirror （这个内核模块在 x86 不缺）
4. ``pvs`` 相关命令有问题 ``pvs | sed -n 3p | awk {'print$4'} | grep "30.00m"`` 改为 ``pvs | awk {'print$4'} | grep "30.00m"``

在使用新的 ``lvm2.json`` 测试时发现 x86 问题更多，它会将 ``/dev/sr0`` 误认为是可用的块设备进行测试，导致测试错误。

# 附录
