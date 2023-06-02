# fail 测试用例

## 初步核查到原因

### 缺失软件包

+ oerv 没有这个软件包

|测试套|测试用例|原因|
|:-:|:-:|:-:|
|lvm2|oe_test_service_lvmlocks|没有软件包 lvm2-locked|
|lvm2|oe_test_service_lvmlockd|没有软件包 lvm2-locked|

### 测试用例不适配

+ 一些测试不适用于虚拟机环境，脚本错误判断为非虚拟机环境
+ 一些测试所需的软件包在 oe x86 默认安装了，但是在 oerv 没有默认安装
+ oe x86 和 oerv 软件源配置有区别，而测试用例忽略了这些区别

|测试套|测试用例|原因|
|:-:|:-:|:-:|
|kernel|oe_test_kernel_cmd_01|测试使用 ``hostnamectl \| grep Virtualization`` 判断是否为虚拟机，而 qemu-system-riscv64 不适用这个方法|
|kernel|oe_test_service_cpupower|测试使用 ``hostnamectl \| grep Virtualization`` 判断是否为虚拟机，而 qemu-system-riscv64 不适用这个方法|
|glib2|oe_test_glib2|没有引入依赖包 kernel-headers ，引入后通过|
|dnf|oe_test_dnf_makecache_clean|测试套检查了 oerv 中没有的 OS 和 everything 源|
|dnf|oe_test_dnf_enabled_enablerepo|测试套依赖 oerv 中没有的 OS 和 everything 源，测试用例直接操作 /etc/yum.repo.d/openEuler.repo 然后把它搞坏了|
|kmod|oe_test_weak-modules|没有引入依赖包 dracut <br/>引入后 Unable to decompress /boot/initramfs-6.1.8-3.oe2303.riscv64.img: Unknown format|
|systemd|oe_test_socket_syslog|没有引入依赖包 rsyslog ，引入后通过|
|NetworkManager|oe_test_libnetfilter_conntrack|没有引入依赖包 kernel-headers ，引入后通过|

### 内核模块缺失/选项未打开

|测试套|测试用例|原因|
|:-:|:-:|:-:|
|kernel|oe_test_vport-geneve|内核模块缺失 vport-geneve|
|kernel|oe_test_xfs|内核模块缺失 xfs|
|kernel|oe_test_hqlogic|内核模块缺失 qla2xxx|
|kernel|oe_test_qxl|内核模块缺失 qxl|
|kernel|oe_test_ipip|内核模块缺失 ipip|
|kernel|oe_test_snd_aloop|内核模块缺失 snd-aloop|
|kernel|oe_test_wangxun|内核模块缺失 ngbe.ko txgbe.ko|
|kernel|oe_test_lpfc|内核模块缺失 lpfc|
|kernel|oe_test_softdog|内核模块缺失 softdog|
|kmod|oe_test_rmmod|内核模块缺失 dm_log dm_mirror dm_region_hash|
|acl|oe_test_acl_default_kernel_setting|未打开 ``CONFIG_XFS_POSIX_ACL=y``|

### 重测通过

|测试套|测试用例|原因|
|:-:|:-:|:-:|
|libarchive|oe_test_libarchive_bsdcpio|见附录|
|libuuid|oe_test_libuuid||

## 附录

### hostnamectl 输出差别

```bash
# hostnamectl
   Static hostname: n/a                                
Transient hostname: localhost
         Icon name: computer-vm
           Chassis: vm
        Machine ID: c78e8c10bbba4687b4aa7ab68adfb5e8
           Boot ID: 283d7032205441be9d9c53a0830381b9
    Virtualization: kvm
  Operating System: openEuler 23.03
            Kernel: Linux 6.1.19-7.0.0.17.oe2303.x86_64
      Architecture: x86-64
   Hardware Vendor: QEMU
    Hardware Model: Standard PC _i440FX + PIIX, 1996_

# hostnamectl 
 Static hostname: openeuler-riscv64
       Icon name: computer
      Machine ID: 7102c13a6be44f418d1f09210bcfbfd9
         Boot ID: 0bd35a14790d4f1b905b493c35105633
Operating System: openEuler 23.03
          Kernel: Linux 6.1.8-3.oe2303.riscv64
    Architecture: riscv64
```

### libarchive oe_test_libarchive_bsdcpio 出错

```bash
# bash mugen.sh -f libarchive -r oe_test_libarchive_bsdcpio
```

写出错，随机出错？

```bash
echo "111" >testfile1
```

在 oe_test_libarchive_bsdtar 这个测试中有相同的命令但是却没有问题。

### glib2 oe_test_glib2 出错

```bash
cat<<EOF>test.c
#include <glib.h>
int main(void)
{
g_print("Hello, world!\n");
return 0;
}
EOF
```

编译错误

```bash
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:195,
                 from /usr/lib/gcc/riscv64-linux-gnu/10.3.1/include/limits.h:1955
, 
                 from /usr/lib/gcc/riscv64-linux-gnu/10.3.1/include/syslimits.h::
7,  
                 from /usr/lib/gcc/riscv64-linux-gnu/10.3.1/include/limits.h:34,
                 from /usr/lib64/glib-2.0/include/glibconfig.h:11,
                 from /usr/include/glib-2.0/glib/gtypes.h:34,
                 from /usr/include/glib-2.0/glib/galloca.h:34,
                 from /usr/include/glib-2.0/glib.h:32,
                 from test.c:1:
/usr/include/bits/local_lim.h:38:10: fatal error: linux/limits.h: No such file oo
r directory
   38 | #include <linux/limits.h>
      |          ^~~~~~~~~~~~~~~~
compilation terminated.
```

### oe x86 和 oerv 软件源配置不同

riscv64 中没有的源

```
ls /var/cache/dnf/*.solv | grep "OS\|everything"
```
