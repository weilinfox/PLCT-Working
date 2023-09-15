# oe_test_FSIO_sys_fs_check


x86 和 riscv 失败原因不同

riscv 下 lvcreate 结果异常

```
+ lvcreate -n test_lv120230911212124 -L 2G test_vggroup20230911210545 -y
  Volume group "test_vggroup20230911210545" has insufficient free space (124 extents): 512 required.
+ mkfs.ext4 /dev/test_vggroup20230911210545/test_lv120230911212124
mke2fs 1.47.0 (5-Feb-2023)
The file /dev/test_vggroup20230911210545/test_lv120230911212124 does not exist and no size was specified.
```

x86 下没有安装 lvcreate

```
+ lvcreate -n test_lv120230912100430 -L 2G -y
oe_test_FSIO_sys_fs_check.sh: line 26: lvcreate: command not found
```
