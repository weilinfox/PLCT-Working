# oe_test_FSIO_chmod

riscv 和 x86 失败原因一致， chmod +x 测试结果不符合预期

```
+ chmod +x /tmp/test0120230911210729/test02/test03/test03.txt
++ ls -l /tmp/test0120230911210729/test02/test03
++ grep test03.txt
++ awk '{print $1}'
+ per08=-rwxr-xr-x
+ [[ -rwxr-xr-x =~ -rwxr-xr-x\. ]]
+ CHECK_RESULT 1 0 0 'The access of /tmp/test0120230911210729/test02/test03/test03.txt is error.'
+ actual_result=1
+ expect_result=0
+ mode=0
+ error_log='The access of /tmp/test0120230911210729/test02/test03/test03.txt is error.'
+ exit_mode=0
+ '[' -z 1 ']'
+ '[' 0 -eq 0 ']'
+ test 1x '!=' 0x
+ test -n 'The access of /tmp/test0120230911210729/test02/test03/test03.txt is error.'
+ LOG_ERROR 'The access of /tmp/test0120230911210729/test02/test03/test03.txt is error.'
+ message='The access of /tmp/test0120230911210729/test02/test03/test03.txt is error.'
+ python3 /root/mugen/libs/locallibs/mugen_log.py --level error --message 'The access of /tmp/test0120230911210729/test02/test03/test03.txt is error.'
Mon Sep 11 21:07:31 2023 - ERROR - The access of /tmp/test0120230911210729/test02/test03/test03.txt is error.
+ (( exec_result++ ))
+ LOG_ERROR 'oe_test_FSIO_chmod.sh line 49'
+ message='oe_test_FSIO_chmod.sh line 49'
+ python3 /root/mugen/libs/locallibs/mugen_log.py --level error --message 'oe_test_FSIO_chmod.sh line 49'
Mon Sep 11 21:07:32 2023 - ERROR - oe_test_FSIO_chmod.sh line 49
```
