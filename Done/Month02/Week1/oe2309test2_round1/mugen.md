# mugen 测试 2309 新增 fail

| 测试套数 | 测试用例总数 | 成功 | 均成功 | 2303 失败 2309 成功 | 失败 | 均失败 | 2303 成功 2309 失败 |
|:-------:|:----------:|:---:|:-----:|:-----------------:|:----:|:-----:|:-----------------:|
| 57 | 569 | 300 | 264 | 36 | 269 | 208 | 61 |

2303 和 2309 均失败的 208 个暂未排查失败原因是否相同。

有 61 个为 2309 新增失败，分析完成，详细原因在本报告中罗列。

## 测试超时

+ ``fio/oe_test_fio_003``
+ ``os-basic/oe_test_IOaccess_1Gfile``
+ ``os-basic/oe_test_IOaccess_500Mfile``

## 软件包版本升级导致 grep 失败

+ ``os-basic/oe_test_gcc_01`` 测试套预期为 ``warning: ‘i’ is used uninitialized in this function`` 但是实际输出
  ```bash
  # gcc -Wall main.c -o main
  main.c: In function 'main':
  main.c:6:4: warning: 'i' is used uninitialized [-Wuninitialized]
      6 |    printf("\n The Geek Stuff [%d]\n", i);
        |    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  main.c:5:8: note: 'i' was declared here
      5 |    int i;
        |
  ```

## 软件包依赖问题

+ ``clevis/oe_test_tang_nbde`` clevs 安装出错 nothing provides libcrypto.so.1.1()(64bit) libcrypto.so.1.1(OPENSSL_1_1_0)(64bit)
+ ``lxcfs/oe_test_service_lxcfs`` lxcfs-tools 安装出错 nothing provides libabsl_synchronization.so.2206.0.0()(64bit) needed by iSulad-2.1.2-4.oe2309.riscv64
+ ``os-basic/oe_test_virt-what`` virt-what 安装失败 nothing provides dmidecode needed by virt-what-1.25-1.oe2309.riscv64
+ ``perl-libwww-perl/*`` 软件源中没有 perl 6 ， perl-libwww-perl 安装失败 package perl-libwww-perl-6.67-1.oe2309.noarch requires perl >= 6, but none of the providers can be installed

## 镜像预装软件问题

+ ``ModemManager/oe_test_service_ModemManager`` 镜像没有预装 polkit 软件包
+ ``os-basic/oe_test_vim`` 没有预装 vim 软件包

## 其他软件包问题

+ ``os-basic/oe_test_ProcMgmt_at`` 等 systemd-253-1 问题，需要重测
+ ``os-basic/oe_test_glibc`` glibc 升级导致的问题

## 2303 没有测试

+ ``kernel/oe_test_bnx2fc`` 内核模块 scsi/hpsa.ko 不存在

## 其他问题

+ ``dnf/oe_test_dnf_check_diffenert-packages`` dnf check-update 异常推出，返回值 100 ，没有打印报错信息
+ ``fio/oe_test_fio_002`` 测试多个 fio-dedupe 命令测试失败，原因未知
+ ``openssh/oe_test_openssh_ssh-copy-id`` ssh-keygen 没有生成 pubkey 导致 /usr/bin/ssh-copy-id: ERROR: failed to open ID file '/root/.ssh/id_rsa.pub': No such file or directory
+ ``samba/oe_test_service_ctdb`` 未知原因 ctdb.service: Failed to parse PID from file /run/ctdb/ctdbd.pid: Invalid argument
