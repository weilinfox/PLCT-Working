# oe_test_acpid_002

riscv 和 x86 失败原因一致， rsyslog 相关问题， acpid.service 启动后无法从 /var/log/messages 查看到启动日志

```
+ cd /etc/acpi/events/
+ cat
+ systemctl restart acpid
+ systemctl status acpid
+ grep running
     Active: active (running) since Mon 2023-09-11 19:45:07 UTC; 164ms ago
+ CHECK_RESULT 0 0 0 'Start Service failure'
+ actual_result=0
+ expect_result=0
+ mode=0
+ error_log='Start Service failure'
+ exit_mode=0
+ '[' -z 0 ']'
+ '[' 0 -eq 0 ']'
+ test 0x '!=' 0x
+ return 0
+ grep acpid /var/log/messages
+ grep loaded
+ CHECK_RESULT 1 0 0 'load Service failure'
```
