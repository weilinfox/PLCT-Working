# oe_test_ip_ipv6_04

riscv 和 x86 失败原因一致，没有 ${NODE1_NIC} 环境变量

```
+ ifconfig inet6 add 4::4/64
SIOGIFINDEX: No such device
```
