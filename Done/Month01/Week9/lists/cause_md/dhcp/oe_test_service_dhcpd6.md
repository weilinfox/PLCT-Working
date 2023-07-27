# oe_test_service_dhcpd6

测试需要安装 dhcp 软件包，该软件包在 x86 镜像预装了但是在 riscv 镜像没有预装

在 x86 上 dhcpd6.service 启动失败

```
× dhcpd6.service - DHCPv6 Server Daemon
     Loaded: loaded (/usr/lib/systemd/system/dhcpd6.service; disabled; vendor preset: disabled)
     Active: failed (Result: exit-code) since Tue 2023-06-06 18:09:08 UTC; 14s ago
       Docs: man:dhcpd(8)
             man:dhcpd.conf(5)
    Process: 1976 ExecStart=/usr/sbin/dhcpd -f -6 -cf /etc/dhcp/dhcpd6.conf -user dhcpd -group dhcpd --no-pid $DHCPDARGS (code=exited, status=1/FAILURE)
   Main PID: 1976 (code=exited, status=1/FAILURE)

Jun 06 18:09:08 localhost.localdomain dhcpd[1976]: have been made to the base software release in order to make
Jun 06 18:09:08 localhost.localdomain dhcpd[1976]: it work better with this distribution.
Jun 06 18:09:08 localhost.localdomain dhcpd[1976]: 
Jun 06 18:09:08 localhost.localdomain dhcpd[1976]: Please report issues with this software via:
Jun 06 18:09:08 localhost.localdomain dhcpd[1976]: https://gitee.com/src-openeuler/dhcp/issues
Jun 06 18:09:08 localhost.localdomain dhcpd[1976]: 
Jun 06 18:09:08 localhost.localdomain dhcpd[1976]: exiting.
Jun 06 18:09:08 localhost.localdomain systemd[1]: dhcpd6.service: Main process exited, code=exited, status=1/FAILURE
Jun 06 18:09:08 localhost.localdomain systemd[1]: dhcpd6.service: Failed with result 'exit-code'.
Jun 06 18:09:08 localhost.localdomain systemd[1]: Failed to start DHCPv6 Server Daemon.
```

