# oe_test_service_dhcpd

测试需要安装 dhcp 软件包，该软件包在 x86 镜像预装了但是在 riscv 镜像没有预装

在 x86 上 dhcpd.service 启动失败

```
× dhcpd.service - DHCPv4 Server Daemon
     Loaded: loaded (/usr/lib/systemd/system/dhcpd.service; disabled; vendor preset: disabled)
     Active: failed (Result: exit-code) since Tue 2023-06-06 18:10:35 UTC; 13s ago
       Docs: man:dhcpd(8)
             man:dhcpd.conf(5)
    Process: 2143 ExecStart=/usr/sbin/dhcpd -f -cf /etc/dhcp/dhcpd.conf -user dhcpd -group dhcpd --no-pid $DHCPDARGS (code=exited, status=1/FAILURE)
   Main PID: 2143 (code=exited, status=1/FAILURE)

Jun 06 18:10:35 localhost.localdomain dhcpd[2143]: have been made to the base software release in order to make
Jun 06 18:10:35 localhost.localdomain dhcpd[2143]: it work better with this distribution.
Jun 06 18:10:35 localhost.localdomain dhcpd[2143]: 
Jun 06 18:10:35 localhost.localdomain dhcpd[2143]: Please report issues with this software via:
Jun 06 18:10:35 localhost.localdomain dhcpd[2143]: https://gitee.com/src-openeuler/dhcp/issues
Jun 06 18:10:35 localhost.localdomain dhcpd[2143]: 
Jun 06 18:10:35 localhost.localdomain dhcpd[2143]: exiting.
Jun 06 18:10:35 localhost.localdomain systemd[1]: dhcpd.service: Main process exited, code=exited, status=1/FAILURE
Jun 06 18:10:35 localhost.localdomain systemd[1]: dhcpd.service: Failed with result 'exit-code'.
Jun 06 18:10:35 localhost.localdomain systemd[1]: Failed to start DHCPv4 Server Daemon.
```

