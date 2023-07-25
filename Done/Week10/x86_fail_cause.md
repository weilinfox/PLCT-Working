# x86 fail 失败原因汇总

我们将测试状态为 x86 fail 的用例大致分为三类：

1. x86 和 riscv 失败原因完全一样 [class1.csv](../Week9/lists/class1.csv)
2. x86 和 riscv 失败核心原因相同，但是在 riscv 架构有独特的问题 [class2.csv](../Week9/lists/class2.csv)
3. x86 和 riscv 失败原因不同 [class3.csv](../Week9/lists/class3.csv)

又根据对于失败的具体原因，下文给出一个详细的分类。

## 测试套问题

### 测试套 suite2cases 问题

+ [rsyslog/oe_test_rsyslog_abnormal_template.sh](https://gitee.com/openeuler/mugen/blob/master/testcases/cli-test/rsyslog/oe_test_rsyslog_abnormal_template/oe_test_rsyslog_abnormal_template.sh) 这一测试用例需要 NODE2 配置，即需要 2 个节点进行测试，但是 [rsyslog.json](https://gitee.com/openeuler/mugen/blob/master/suite2cases/rsyslog.json) 中没有 "machine num" 配置。这一问题在该测试套共影响 10 个测试用例

### 测试套脚本问题

+ [os-basic/oe_test_system_log_recorded](./cause_md/os-basic/oe_test_system_log_recorded.md) ``folder=$(ls /run/log/journal/)`` 若 ``ls`` 命令输出零个（riscv）或多个（x86 两个）就会出现问题，但是并没有进行处理
+ [kernel/oe_test_cifs.sh](https://gitee.com/openeuler/mugen/blob/master/testcases/cli-test/kernel/oe_test_cifs.sh) 测试脚本测试的是 cifs 模块，但是错误信息是 vport_geneve 模块；且最后一个测试也是测试的 vport_geneve 模块，和测试套目的不相符合
   ```
   function run_test() {
       modinfo cifs |grep cifs
       CHECK_RESULT $? 0 0 "Description Module information failed to be displayed"
       lsmod | grep  cifs
       CHECK_RESULT $? 0 1 "Default installation"
       modprobe cifs
       CHECK_RESULT $? 0 0 "Module loading failure"
       lsmod | grep  cifs
       CHECK_RESULT $? 0 0 "vport_geneve not found"
       rmmod  cifs
       CHECK_RESULT $? 0 0 "vport-geneve remove failure"
       lsmod | grep  cifs
       CHECK_RESULT $? 0 1 "vport_geneve exist"
       dmesg | grep "vport_geneve" | grep -Ei 'error|fail'
       CHECK_RESULT $? 1 0 "error message was reported"
   }
   ```
+ [kmod/oe_test_depmod](./cause_md/os-basic/oe_test_depmod.md) ``symversPath=$(find / -name Module.symvers)`` 和 ``mapPath=$(find / -name System.map)`` 两个命令，若 ``ls`` 命令输出零个（x86）或多个（riscv 两个）就会出现问题，但是并没有进行处理
+ [keepalived/oe_test_service_keepalived.sh](https://gitee.com/openeuler/mugen/blob/master/testcases/cli-test/keepalived/oe_test_service_keepalived.sh) 测试脚本直接使用 ``${eth_name}`` 这一未声明的变量
   ```
   echo "global_defs {
      notification_email {
          root@localhost
      }
      smtp_server 127.0.0.1
      router_id N1
   }
   vrrp_instance VI_1 {
     state MASTER
     interface ${eth_name}
     virtual_router_id 51
     priority 100
     advert_int 1
     authentication {
        auth_type PASS
        auth_pass 1111
     }
   }" >>/etc/keepalived/keepalived.conf
   ```
+ [initscripts/oe_test_service_network.sh](https://gitee.com/openeuler/mugen/blob/master/testcases/cli-test/initscripts/oe_test_service_network.sh#L37) 测试行命令拼写错误 ``journalct --since`` ，由于该测试命令返回非 0 为成功，这行测试将永远成功（测试成功但是脚本有问题）

### 命令输出与 grep 预期不符

+ [os-basic/oe_test_dmraid](./cause_md/os-basic/oe_test_dmraid.md) ``dmraid -s`` 输出为 ``no block devices found`` ，而测试脚本预期结果为 ``no raid disks`` ，导致没有判定出 raid 不存在
+ [os-basic/oe_test_whereis](./cause_md/os-basic/oe_test_whereis.md) ``whereis --help | grep "Usage: whereis"`` 匹配失败， ``whereis --help`` 的实际输出为
   ```
   Usage:
    whereis [options] [-BMS <dir>... -f] <name>
   ```
+ [openssl/oe_test_openssl_DSA_algorithm](./cause_md/openssl/oe_test_openssl_DSA_algorithm.md) ``grep 'BEGIN DSA PRIVATE KEY'`` 失败，实际应为 ``BEGIN PRIVATE KEY`` 。同样的错误影响了 11 个测试用例
+ [openssl/oe_test_openssl_speed](./cause_md/openssl/oe_test_openssl_speed.md) ``grep "aes-128 cbc"`` 和 ``grep "sm4-cbc"`` 失败，实际应为 ``aes-128-cbc`` 和 ``SM4-CBC``
+ [iptables/oe_test_iptables-restore_01](./cause_md/iptables/oe_test_iptables-restore_01.md) 和 [iptables/oe_test_iptables-restore](./cause_md/iptables/oe_test_iptables-restore.md) ``grep "DROP       icmp"`` 失败， ``ip6tables -nvL`` 输出没有出现该字段
+ [iptables/oe_test_ip6tables-save](./cause_md/iptables/oe_test_ip6tables-save.md) ``grep -A 200 nat | grep -A 100 mangle | grep -A 80 raw | grep -A 60 security | grep filter`` ， ``ip6tables-save`` 命令实际输出没有出现这些字段
+ [klibappstream-glibeyutils/oe_test_libappstream-glib_appstream-util_03](./cause_md/klibappstream-glibeyutils/oe_test_libappstream-glib_appstream-util_03.md) ``grep http://www.ezix.org/project/wiki/HardwareLiSter`` 失败
+ [mc/oe_test_mc_base_01](./cause_md/mc/oe_test_mc_base_01.md) ``grep 'Home路径'`` 尝试 grep 中文字串，实际输出为 ``Home directory``

### 内核模块名称和预期不同

+ [kernel/oe_test_hinic](./cause_md/kernel/oe_test_hinic.md) 在 x86_64 的内核上， hinic 模块的文件名为 ``hinic.ko.xz`` ，而测试套预期文件名为 ``hinic.ko`` ，导致测试失败
+ [kmod/oe_test_insmod-lsmod](./cause_md/kernel/oe_test_insmod-lsmod.md) 在 x86_64 的内核上， raid0 模块文件名为 ``raid0.ko.xz`` 、 faulty 模块文件名为 ``faulty.ko.xz`` ，而测试套预期文件名为 ``raid0.ko`` 和 ``faulty.ko`` ，导致测试失败
+ [kmod/oe_test_modprobe](./cause_md/kernel/oe_test_modprobe.md) 在 x86_64 的内核上 dm_log 模块的文件名为 ``dm-log.ko.xz`` ，而测试套预期文件名为 ``dm-log.ko`` ，导致测试失败

### 依赖的命令没有安装也没有预装

+ os-basic/oe_test_auditctl 依赖 audit 软件包，但是它在 x86 和 riscv 均没有预装
+ [os-basic/oe_test_server_openssh_verifykey](./cause_md/os-basic/oe_test_server_openssh_verifykey.md) 依赖 policycoreutils 软件包，但是它在 x86 和 riscv 均没有预装
+ [os-basic/oe_test_uname](./cause_md/os-basic/oe_test_uname.md) 依赖 hostname 软件包，但是它在 x86 没有预装
+ [os-basic/oe_test_count_gperftools_function](./cause_md/os-basic/oe_test_count_gperftools_function.md) 依赖 gperftools-devel 软件包，但是它在 x86 和 riscv 上均没有预装；依赖 gcc-g++ 软件包，但是它在 x86 镜像上没有预装
+ [os-basic/oe_test_disk_graphics_card](./cause_md/os-basic/oe_test_disk_graphics_card.md) 依赖 pciutils 软件包，但是它在 x86 和 riscv 上均没有预装
+ 大部分 **audit** 测试用例都在 x86 和 riscv 失败了，共计 29 个，均是由于测试所需的包没有安装，这里只列举 3 个
+ [audit/oe_test_audit_ausearch](./cause_md/os-basic/oe_test_audit_ausearch.md) 依赖 audit 软件包，但是它在 x86 和 riscv 均没有预装
+ [audit/oe_test_audit_available_disk_space](./cause_md/os-basic/oe_test_audit_available_disk_space.md) 依赖 audit 软件包，但是它在 x86 和 riscv 均没有预装；依赖 service 命令，但是它在 riscv 没有预装
+ [audit/oe_test_audit_user_build_connection](./cause_md/os-basic/oe_test_audit_user_build_connection.md) 依赖 audit 软件包，但是它在 x86 和 riscv 均没有预装；依赖 service 命令，但是它在 riscv 没有预装；依赖 kernel-headers 软件包，但是它在 riscv 没有预装
+ [chrony/oe_test_service_chrony-wait](./cause_md/chrony/oe_test_service_chrony-wait.md) 依赖 chrony 软件包，但是它在 x86 和 riscv 均没有预装
+ [ebtables/oe_test_service_ebtables](./cause_md/ebtables/oe_test_service_ebtables.md) 依赖 ebtables 软件包，但是它在 x86 和 riscv 均没有预装
+ [kernel/oe_test_swap_compress](./cause_md/kernel/oe_test_swap_compress.md) 依赖 lvm2 软件包，但是它在 x86 和 riscv 上均没有预装
+ [ipmitool/oe_test_service_bmc-snmp-proxy](./cause_md/ipmitool/oe_test_service_bmc-snmp-proxy.md) 依赖 net-snmp 和 bmc-snmp-proxy 软件包，但是它们在 x86 和 riscv 上均没有预装
+ [ipmitool/oe_test_service_exchange-bmc-os-info](./cause_md/ipmitool/oe_test_service_exchange-bmc-os-info.md) 依赖 exchange-bmc-os-info 软件包，但是它在 x86 和 riscv 上均没有预装
+ [iprutils/oe_test_service_iprdump](./cause_md/iprutils/oe_test_service_iprdump.md) 依赖 iprutils 软件包，但是它在 x86 和 riscv 上均没有预装，该问题导致测试套 4 个用例全部失败
+ [ipset/oe_test_service_ipset](./cause_md/ipset/oe_test_service_ipset.md) 依赖 ipset 软件包，但是它在 x86 和 riscv 上均没有预装，该问题导致测试套 4 个用例全部失败
+ [iptables/oe_test_service_ip6tables](./cause_md/iptables/oe_test_service_ip6tables.md) 和 [iptables/oe_test_service_iptables](./cause_md/iptables/oe_test_service_iptables.md) 依赖 iptables 软件包，但是它在 x86 和 riscv 上均没有预装
+ [irqbalance/oe_test_service_irqbalance](./cause_md/irqbalance/oe_test_service_irqbalance.md) 依赖 irqbalance 软件包，但是它在 x86 和 riscv 上均没有预装
+ [kexec-tools/oe_test_service_kdump](./cause_md/kexec-tools/oe_test_service_kdump.md) 依赖 kexec-tools 软件包，但是它在 riscv 上没有预装
+ [keyutils/oe_test_keyutils-api](./cause_md/keyutils/oe_test_keyutils-api.md) 依赖 keyutils-libs-devel 软件包，但是它在 x86 和 riscv 上均没有预装
+ [libosinfo/oe_test_osinfo-db-import](./cause_md/libosinfo/oe_test_osinfo-db-import.md) 依赖 wget 软件包，但是它在 x86 上没有预装
+ [mtx/oe_test_mtx_loaderinfo](./cause_md/mtx/oe_test_mtx_loaderinfo.md) 依赖 gcc 软件包，但是它在 x86 上没有预装；依赖 kernel-devel 软件包，但是它在 x86 和 riscv 均没有预装。该问题导致测试套 5 个测试全部失败
+ [freeradius/oe_test_freeradius_freeradius-utils_radsqlrelay](./cause_md/freeradius/oe_test_freeradius_freeradius-utils_radsqlrelay.md) 依赖 mysql5 和 mysql5-server 软件包，但是它们在 x86 和 riscv 上均无法安装

### 依赖的目录和文件没有预先建立

+ [kernel/oe_test_swap_compress](./cause_md/kernel/oe_test_swap_compress.md) 测试使用的 swap 设备 ``/dev/dm-1`` 没有提前建立直接使用

### 其他问题

+ [dnf/oe_test_dnf_enabled_enablerepo](./cause_md/dnf/oe_test_dnf_enabled_enablerepo.md) 测试套编写的预期返回值不正确
+ [dnf/oe_test_dnf_list_mark](./cause_md/dnf/oe_test_dnf_list_mark.md) 测试套需要软件源中的包高于预装的包，否则将失败

### 没有考虑 qemu 环境

+ [kernel/oe_test_io_sched](./cause_md/kernel/oe_test_io_sched.md) 测试脚本使用了 ``sda`` 作为测试用块设备，而在 qemu 中通常为 ``vda`` 。

### 没有考虑 riscv

+ [os-basic/oe_test_uname](./cause_md/os-basic/oe_test_uname.md) ``uname -m | grep -E "aarch64|x86_64"`` 显然在 riscv 上无法通过

## 非测试套问题

### 软件包问题

+ [iputils/oe_test_service_ninfod](./cause_md/iputils/oe_test_service_ninfod.md) 软件包 iputils-ninfod 不存在，无法安装
+ [iputils/oe_test_service_rdisc](./cause_md/iputils/oe_test_service_rdisc.md) 没有软件包提供 rdisc.service

### 内核问题

+ [kernel/oe_test_check_huge_task](./cause_md/kernel/oe_test_check_huge_task.md) CONFIG_BOOTPARAM_HUNG_TASK_PANIC_VALUE 配置在 x86 和 riscv 没有找到
+ [kernel/oe_test_cifs](./cause_md/kernel/oe_test_cifs.md) riscv 内核缺失 cifs 模块
+ [kernel/oe_test_hinic](./cause_md/kernel/oe_test_hinic.md) riscv 内核缺失 hinic 模块
+ [kmod/oe_test_insmod-lsmod](./cause_md/kmod/oe_test_insmod-lsmod.md) riscv 内核缺失 raid0 模块和 faulty 模块
+ [kmod/oe_test_modinfo](./cause_md/kmod/oe_test_modinfo.md) riscv 内核缺失 raid1 模块和 dm_log 模块
+ [kmod/oe_test_modprobe](./cause_md/kmod/oe_test_modprobe.md) riscv 内核缺失 dm_cache 模块、 dm_mirror 模块和 dm_log 模块
+ [lvm2/oe_test_lvm2_pvmove_001](./cause_md/lvm2/oe_test_lvm2_pvmove_001.md) riscv 内核缺失 dm_mirror 模块
+ [ipmitool/oe_test_service_ipmievd](./cause_md/ipmitool/oe_test_service_ipmievd.md) x86 缺失 ipmi_si 模块， riscv 缺失 ipmi_watchdog 、 ipmi_poweroff 、 ipmi_devintf 、 ipmi_si 和 ipmi_msghandler 模块
+ [lm_sensors/oe_test_service_fancontrol](./cause_md/lm_sensors/oe_test_service_fancontrol.md) riscv 缺失 i2c-dev 和 cpuid 模块

### mugen 问题

+ [lvm2/oe_test_lvm2_pvchange_001](./cause_md/lvm2/oe_test_lvm2_pvchange_001.md) 在 x86 上， mugen 将 ``/dev/sr0`` 光驱设备也认为是可用的块设备，导致测试失败。类似问题在 lvm2 测试上导致了 个测试用例失败

### qemu 问题

经常出现 reboot 以后测试节点失联
