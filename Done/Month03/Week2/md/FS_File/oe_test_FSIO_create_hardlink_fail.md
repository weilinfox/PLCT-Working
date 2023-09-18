# oe_test_FSIO_create_hardlink_fail

x86 和 riscv 失败原因不同

riscv 下 lvcreate 结果异常

```
++ lvcreate -n test_lv320230911211711 -L 512M test_vggroup20230911210545 -y
  Volume group "test_vggroup20230911210545" has insufficient free space (124 extents): 128 required.
++ mkfs -t xfs /dev/test_vggroup20230911210545/test_lv320230911211711
Error accessing specified device /dev/test_vggroup20230911210545/test_lv320230911211711: No such file or directory
```

x86 下没有安装 lvcreate

```
++ lvcreate -n test_lv320230912100417 -L 512M -y
../common_lib/fsio_lib.sh: line 107: lvcreate: command not found
```

