# mugen 测试 2309 新增 fail

| 测试套数 | 测试用例总数 | 成功 | 均成功 | 2303 失败 2309 成功 | 失败 | 均失败 | 2303 成功 2309 失败 |
|:-------:|:----------:|:---:|:-----:|:-----------------:|:----:|:-----:|:-----------------:|
|  |  |  |  |  |  |  |  |

新增失败，分析完成，详细原因在本报告中罗列。

## 重新测试通过

+ ``fio/oe_test_fio_003``
+ ``os-basic/oe_test_disk_schedule_specific``
+ ``os-basic/oe_test_IOaccess_1Gfile``
+ ``os-basic/oe_test_IOaccess_500Mfile``
+ ``os-basic/oe_test_server_mysql``
+ ``libstoragemgmt/oe_test_service_libstoragemgmt``
+ ``netcf/oe_test_service_netcf-transaction``
+ ``smoke-basic-os/oe_test_cmp``
+ ``dbus/oe_test_socket_dbus``
+ ``libosinfo/oe_test_osinfo-install-script``
+ ``quota/oe_test_service_rpc-rquotad``
+ ``quota/oe_test_service_quota_nld``

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
+ ```smoke-basic-os/oe_test_aide_init_database```中```aide --init```预期输出应该包括"AIDE initialized database at /var/lib/aide/aide.db.new.gz"但是实际输出为：
  ```bash
  Start timestamp: 2023-08-13 19:32:26 +0800 (AIDE 0.18.5)
  AIDE successfully initialized database.
  New AIDE database written to /var/lib/aide/aide.db.new.gz

  Number of entries:	51176

  ---------------------------------------------------
  The attributes of the (uncompressed) database(s):
  ---------------------------------------------------

  /var/lib/aide/aide.db.new.gz
  .......
  ```
+ ```smoke-basic-os/oe_test_rsyslog_10```中date命令的输出按空格分割第六个字符按预期为应为时区，例如```Sun Aug 13 07:34:01 PM CST 2023```但是实际输出为```Sun Aug 13 07:34:01 CST 2023```，输出按空格分割第六个字符变成了年份。


## 软件包依赖问题

+ ``clevis/oe_test_tang_nbde`` clevs 安装出错 nothing provides libcrypto.so.1.1()(64bit) libcrypto.so.1.1(OPENSSL_1_1_0)(64bit)
+ ``iSulad/oe_test_iSulad_container`` ``lxcfs/oe_test_service_lxcfs`` lxcfs-tools 安装出错 nothing provides libabsl_synchronization.so.2206.0.0()(64bit) needed by iSulad-2.1.2-4.oe2309.riscv64
+ ``os-basic/oe_test_virt-what`` virt-what 安装失败 nothing provides dmidecode needed by virt-what-1.25-1.oe2309.riscv64
+ ``perl-libwww-perl/*`` 软件源中没有 perl 6 ， perl-libwww-perl 安装失败 package perl-libwww-perl-6.67-1.oe2309.noarch requires perl >= 6, but none of the providers can be installed
+ ``bind/oe_test_service_named`` 源中无bind软件包，可能尚未构建完成
+ ``gdm/oe_test_service_gdm`` 2309上没有gnome-shell的依赖 package gdm-1:43.0-1.oe2309.riscv64 requires gnome-shell, but none of the providers can be installed ， 缺少gcr4(riscv-64) 、libgcr-4.so.0.0.0()(64bit)、pipewire-gstreamer(riscv-64)
+ ``os-basic/oe_test_server_mariadb_compatibilty`` 软件包 mysql-server 与软件包 mariadb-server 冲突 package mysql-server-8.0.30-4.oe2309.riscv64 conflicts with mariadb-server provided by mariadb-server-4:10.5.16-3.oe2309.riscv64
+ ``rpmlint/oe_test_rpmdiff`` 软件包 rpmlint 安装时发生依赖错误 nothing provides python3.11dist(zstandard) needed by rpmlint-2.4.0-1.oe2309.noarch
+ ```smoke-basic-os/oe_test_ima_v2_manual_gen_digest_01```中缺少libcrypto.so.1.1()(64bit)、libcrypto.so.1.1(OPENSSL_1_1_0)(64bit)
+ ```openscap/oe_test_ensure_security_compliance```中缺少openscap-scanner >= 1.2.5并找不到openscap软件包
+ ``smoke-basic-os/oe_test_ipv6_dnsmasq`` 2309 中找不到 bind-utils 软件包
+ ```smoke-basic-os/oe_test_skopeo```中找不到skopeo软件包
+ ```valgrind/oe_test_valgrind```中找不到valgrind软件包和glibc-debuginfo软件包
+ ```tog-pegasus/oe_test_service_tog-pegasus```中找不到tog-pegasus软件包
+ ``lxc/oe_test_lxc_ls_monitor`` 软件包 lxcfs 依赖关系不满足 package lxcfs-tools-0.3-30.oe2309.riscv64 requires iSulad, but none of the providers can be installed

## 镜像预装软件问题

+ ``ModemManager/oe_test_service_ModemManager`` 镜像没有预装 polkit 软件包
+ ``os-basic/oe_test_vim`` 没有预装 vim 软件包
+ ``os-basic/oe_test_lastb`` secret-tool 在 03 预装了但是在 09 没有预装
+ ``smoke-basic-os/oe_test_rsyslog_04``没有预装rsyslog
+ ``smoke-basic-os/oe_test_iptables``没有预装iptables
+ ``smoke-basic-os/oe_test_os-prober_01``没有预装os-prober
+ ``smoke-basic-os/oe_test_glibc_getaddrinfo_01``缺少host命令

## 其他软件包问题

+ ``os-basic/oe_test_ProcMgmt_at`` 等 systemd-253-1 问题，需要重测
+ ``os-basic/oe_test_glibc`` glibc 升级导致的问题
+ ``smoke-basic-os/oe_test_llvm`` clang调用ld报错
  ```bash
  clang /tmp/test_llvm/llvm_test.c -o /tmp/test_llvm/test
  /usr/bin/ld: cannot find crtbeginS.o: No such file or directory
  /usr/bin/ld: cannot find -lgcc
  /usr/bin/ld: cannot find -lgcc_s
  clang-15: error: linker command failed with exit code 1 (use -v to see invocation)
  ```
+ ``smoke-basic-os/oe_test_rpm_cmd``中运行命令``yum install``报错
+ ``smoke-basic-os/oe_test_user_debug_iotop_SCEN_01``中``iotop -b -n 1 -d 10``命令未能正确显示PRIO（显示为?sys）
+ ``smoke-basic-os/oe_test_sort``中新版sort命令默认不忽略空行，导致测试失败

## 内核问题

+ ``kernel/oe_test_bnx2fc`` 内核模块 scsi/hpsa.ko 不存在
+ ``os-basic/oe_test_python3-kmod`` snd_seq 内核模块不存在

## 其他问题

+ ``dnf/oe_test_dnf_check_diffenert-packages`` dnf check-update 异常推出，返回值 100 ，没有打印报错信息
+ ``fio/oe_test_fio_002`` 测试多个 fio-dedupe 命令测试失败，原因未知
+ ``openssh/oe_test_openssh_ssh-copy-id`` ssh-keygen 没有生成 pubkey 导致 /usr/bin/ssh-copy-id: ERROR: failed to open ID file '/root/.ssh/id_rsa.pub': No such file or directory
+ ``samba/oe_test_service_ctdb`` 未知原因 ctdb.service: Failed to parse PID from file /run/ctdb/ctdbd.pid: Invalid argument
+ ``FS_File/oe_test_FSIO_check_alias`` grep: /root/.bashrc: No such file or directory，测试镜像中bash环境配置文件缺失
+ ``os-basic/oe_test_xmlsec`` 测试程序链接失败
  ```bash
  gcc -I/usr/include/libxml2 -lxml2 -lz -llzma -lm -I/usr/include/libxml2 -lxslt -lxml2 -lm -lxmlsec1 -g -D__XMLSEC_FUNCTION__=__FUNCTION__ -DXMLSEC_NO_XKMS=1 -DXMLSEC_CRYPTO_OPENSSL -DXMLSEC_CRYPTO_DYNAMIC_LOADING=1 -DUNIX_SOCKETS -DXMLSEC_NO_SIZE_T sign.c -o sign1
  /usr/bin/ld: /lib64/lp64d/libxmlsec1.so: undefined reference to `xmlIOFTPOpen@LIBXML2_2.4.30'
  /usr/bin/ld: /lib64/lp64d/libxmlsec1.so: undefined reference to `xmlIOFTPRead@LIBXML2_2.4.30'
  /usr/bin/ld: /lib64/lp64d/libxmlsec1.so: undefined reference to `xmlIOFTPClose@LIBXML2_2.4.30'
  /usr/bin/ld: /lib64/lp64d/libxmlsec1.so: undefined reference to `xmlNanoFTPInit@LIBXML2_2.4.30'
  /usr/bin/ld: /lib64/lp64d/libxmlsec1.so: undefined reference to `xmlNanoFTPCleanup@LIBXML2_2.4.30'
  /usr/bin/ld: /lib64/lp64d/libxmlsec1.so: undefined reference to `xmlIOFTPMatch@LIBXML2_2.4.30'
  collect2: error: ld returned 1 exit status
  ```
+ ``os-basic/oe_test_server_openssh_secure`` 测试失败
  ```bash
  firewall-cmd --add-port 22/tcp
  ERROR:dbus.proxies:Introspect error on :1.60:/org/fedoraproject/FirewallD1: dbus.exceptions.DBusException: org.freedesktop.DBus.Error.NoReply: Did not receive a reply. Possible causes include: the remote application did not send a reply, the message bus security policy blocked the reply, the reply timeout expired, or the network connection was broken.
  Error: Did not receive a reply. Possible causes include: the remote application did not send a reply, the message bus security policy blocked the reply, the reply timeout expired, or the network connection was broken.
  ```
+ ``libosinfo/oe_test_osinfo-db-import`` 中导出文件名按照当前时间命名，测试脚本中寻找的导出文件名是写死的
+ ``PackageKit/oe_test_packagekit_pkcon`` ``pkcon install git -y`` 报 Fatal error: Failed to check for authentication: GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.PolicyKit1 was not provided by any .service files

## 测试脚本问题

该部分略去 2303 已知的测试套问题

+ ``fontconfig/oe_test_fontconfig_fc-list`` 测试不存在
