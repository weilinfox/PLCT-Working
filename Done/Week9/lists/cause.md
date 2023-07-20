# 错误原因汇总

## 测试套问题


## grep 与预期不符

+ [os-basic/oe_test_dmraid](./cause_md/os-basic/oe_test_dmraid.md) ``dmraid -s`` 输出为 ``no block devices found`` ，而测试脚本预期结果为 ``no raid disks`` ，导致没有判定出 raid 不存在
+ [os-basic/oe_test_whereis](./cause_md/os-basic/oe_test_whereis.md) ``whereis --help | grep "Usage: whereis"`` 匹配失败， ``whereis --help`` 的实际输出为
   ```
   Usage:
    whereis [options] [-BMS <dir>... -f] <name>
   ```

## 依赖的命令没有安装也没有预装

+ os-basic/oe_test_auditctl 依赖 audit 软件包，但是它在 x86 和 riscv 均没有预装
+ [os-basic/oe_test_server_openssh_verifykey](./cause_md/os-basic/oe_test_server_openssh_verifykey.md) 依赖 policycoreutils 软件包，但是它在 x86 和 riscv 均没有预装
+ [os-basic/oe_test_uname](./cause_md/os-basic/oe_test_uname.md) 依赖 hostname 软件包，但是它在 x86 没有预装
+ [os-basic/oe_test_count_gperftools_function](./cause_md/os-basic/oe_test_count_gperftools_function.md) 依赖 gperftools-devel 软件包，但是它在 x86 和 riscv 上均没有预装；依赖 gcc-g++ 软件包，但是它在 x86 镜像上没有预装
+ [os-basic/oe_test_disk_graphics_card](./cause_md/os-basic/oe_test_disk_graphics_card.md) 依赖 pciutils 软件包，但是它在 x86 和 riscv 上均没有预装
+ 大部分 **audit** 测试用例都在 x86 和 riscv 失败了，共计 29 个，均是由于测试所需的包没有安装，这里只列举 3 个
+ [audit/oe_test_audit_ausearch](./cause_md/os-basic/oe_test_audit_ausearch.md) 依赖 audit 软件包，但是它在 x86 和 riscv 均没有预装
+ [audit/oe_test_audit_available_disk_space](./cause_md/os-basic/oe_test_audit_available_disk_space.md) 依赖 audit 软件包，但是它在 x86 和 riscv 均没有预装；依赖 service 命令，但是它在 riscv 没有预装
+ [audit/oe_test_audit_user_build_connection](./cause_md/os-basic/oe_test_audit_user_build_connection.md) 测试套问题， x86 和 riscv 原因基本一致，依赖 audit 软件包，但是它在 x86 和 riscv 均没有预装；依赖 service 命令，但是它在 riscv 没有预装；依赖 kernel-headers 软件包，但是它在 riscv 没有预装

## 其他问题

+ [os-basic/oe_test_system_log_recorded](./cause_md/os-basic/oe_test_system_log_recorded.md) ``folder=$(ls /run/log/journal/)``
+ [dnf/oe_test_dnf_enabled_enablerepo](./cause_md/dnf/oe_test_dnf_enabled_enablerepo.md) 测试套编写的预期返回值不正确
+ [dnf/oe_test_dnf_list_mark](./cause_md/dnf/oe_test_dnf_list_mark.md) 测试套需要软件源中的包高于预装的包，否则将失败
+ 

## 没有考虑到 riscv

+ [os-basic/oe_test_uname](./cause_md/os-basic/oe_test_uname.md) ``uname -m | grep -E "aarch64|x86_64"`` 显然在 riscv 上无法通过

