
# Congratulation, likely test hit a kernel bug.

## fs_fill fs_fill

```
Test timeouted, sending SIGKILL!
Test timeouted, sending SIGKILL!
Test timeouted, sending SIGKILL!
Cannot kill test processes!
Congratulation, likely test hit a kernel bug.
Exiting uncleanly...
```

# [vdso] bug not patched

## vma05 vma05.sh

```
vma05 1 TFAIL: [vdso] bug not patched
```

# _MAY_ be missing kernel fixes

## bpf_prog06 bpf_prog06

```
HINT: You _MAY_ be missing kernel fixes:

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=64620e0a1e71

HINT: You _MAY_ be vulnerable to CVE(s):

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-CVE-2021-4204
```

## inotify12 inotify12

```
HINT: You _MAY_ be missing kernel fixes:

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=a32e697cda27
```

## openat04 openat04

```
HINT: You _MAY_ be missing kernel fixes:

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=ac6800e279a2
https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=426b4ca2d6a5
```

## hugemmap15 hugemmap15

```
HINT: You _MAY_ be missing kernel fixes:

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=cbf52afdc0eb
```

# 无法完成测试 skipped

## proc01

无论普通用户还是 root 用户都会跑死，且进程无法杀死。

## cve-2022-4378

[Kernel panic](logs/cve-2022-4378_kp.txt)

日志拉到最后

# 未知原因 fail

## leapsec01 leapsec01

```
leapsec01.c:88: TINFO: 06:26:19.145258804000 adjtimex: insert leap second
leapsec01.c:88: TINFO: 06:26:19.645924345000 adjtimex: insert leap second
leapsec01.c:88: TINFO: 06:26:20.146305744000 adjtimex: insert leap second
leapsec01.c:84: TBROK: adjtimex status 8208 not set
```

## epoll_pwait02 epoll_pwait02

```
<<<test_output>>>
tst_test.c:1558: TINFO: Timeout per run is 0h 05m 00s
epoll_pwait_var.h:38: TINFO: Test epoll_pwait()
epoll_pwait02.c:27: TPASS: do_epoll_pwait() succeeded
epoll_pwait_var.h:40: TINFO: Test epoll_pwait2()
epoll_pwait02.c:30: TFAIL: do_epoll_pwait() returned -1, expected 1
```

## epoll_pwait03 epoll_pwait03

```
epoll_pwait03.c:33: TFAIL: do_epoll_pwait() returned -1, expected 0: ENOSYS (38)
tst_timer_test.c:270: TINFO: sampling function failed, exiting
tst_timer_test.c:263: TINFO: do_epoll_pwait() sleeping for 2000us 500 iterations, threshold 450.01us
epoll_pwait03.c:33: TFAIL: do_epoll_pwait() returned -1, expected 0: ENOSYS (38)
tst_timer_test.c:270: TINFO: sampling function failed, exiting
tst_timer_test.c:263: TINFO: do_epoll_pwait() sleeping for 5000us 300 iterations, threshold 450.04us
epoll_pwait03.c:33: TFAIL: do_epoll_pwait() returned -1, expected 0: ENOSYS (38)
tst_timer_test.c:270: TINFO: sampling function failed, exiting
tst_timer_test.c:263: TINFO: do_epoll_pwait() sleeping for 10000us 100 iterations, threshold 450.33us
epoll_pwait03.c:33: TFAIL: do_epoll_pwait() returned -1, expected 0: ENOSYS (38)
tst_timer_test.c:270: TINFO: sampling function failed, exiting
tst_timer_test.c:263: TINFO: do_epoll_pwait() sleeping for 25000us 50 iterations, threshold 451.29us
epoll_pwait03.c:33: TFAIL: do_epoll_pwait() returned -1, expected 0: ENOSYS (38)
tst_timer_test.c:270: TINFO: sampling function failed, exiting
tst_timer_test.c:263: TINFO: do_epoll_pwait() sleeping for 100000us 10 iterations, threshold 537.00us
epoll_pwait03.c:33: TFAIL: do_epoll_pwait() returned -1, expected 0: ENOSYS (38)
tst_timer_test.c:270: TINFO: sampling function failed, exiting
tst_timer_test.c:263: TINFO: do_epoll_pwait() sleeping for 1000000us 2 iterations, threshold 4400.00us
epoll_pwait03.c:33: TFAIL: do_epoll_pwait() returned -1, expected 0: ENOSYS (38)
tst_timer_test.c:270: TINFO: sampling function failed, exiting
```

## epoll_pwait04 epoll_pwait04

```
<<<test_output>>>
tst_test.c:1558: TINFO: Timeout per run is 0h 05m 00s
epoll_pwait_var.h:38: TINFO: Test epoll_pwait()
epoll_pwait04.c:25: TPASS: with an invalid sigmask pointer : EFAULT (14)
epoll_pwait_var.h:40: TINFO: Test epoll_pwait2()
epoll_pwait04.c:25: TFAIL: with an invalid sigmask pointer expected EFAULT: ENOSYS (38)
```

## getxattr04 getxattr04

```
<<<test_output>>>
tst_device.c:317: TINFO: Using test device LTP_DEV='/dev/sda1'
tst_test.c:1093: TINFO: Formatting /dev/sda1 with xfs opts='' extra opts=''
tst_test.c:1107: TBROK: mount(/dev/sda1, mntpoint, xfs, 0, (nil)) failed: ENODEV (19)
```

## isofs isofs.sh

```
<<<test_output>>>
isofs 1 TINFO: timeout per run is 0h 50m 0s
isofs 1 TPASS: mkisofs -o isofs.iso -quiet /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/files 2> /dev/null passed as expected
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,norock isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,nojoliet isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=1024,cruft isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=2048,nocompress isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=off,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=acorn,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=relaxed,map=normal isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide,session=2 isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
isofs 1 TPASS: mkisofs -o isofs.iso -quiet -J /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/files 2> /dev/null passed as expected
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,norock isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,nojoliet isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=1024,cruft isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=2048,nocompress isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=off,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=acorn,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=relaxed,map=normal isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide,session=2 isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
isofs 1 TPASS: mkisofs -o isofs.iso -quiet -hfs -D /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/files 2> /dev/null passed as expected
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,norock isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,nojoliet isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=1024,cruft isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=2048,nocompress isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=off,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=acorn,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=relaxed,map=normal isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide,session=2 isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
isofs 1 TPASS: mkisofs -o isofs.iso -quiet -R /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/files 2> /dev/null passed as expected
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,norock isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,nojoliet isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=1024,cruft isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=2048,nocompress isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=off,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=acorn,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=relaxed,map=normal isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide,session=2 isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
isofs 1 TPASS: mkisofs -o isofs.iso -quiet -R -J /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/files 2> /dev/null passed as expected
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,norock isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,nojoliet isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=1024,cruft isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=2048,nocompress isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=off,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=acorn,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=relaxed,map=normal isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide,session=2 isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
isofs 1 TPASS: mkisofs -o isofs.iso -quiet -f -l -D -J -allow-leading-dots -R /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/files 2> /dev/null passed as expected
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,norock isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,nojoliet isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=1024,cruft isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=2048,nocompress isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=off,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=acorn,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=relaxed,map=normal isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide,session=2 isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
isofs 1 TPASS: mkisofs -o isofs.iso -quiet -allow-lowercase -allow-multidot -iso-level 3 -f -l -D -J -allow-leading-dots -R /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/files 2> /dev/null passed as expected
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,norock isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,nojoliet isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=1024,cruft isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=2048,nocompress isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=off,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=strict,map=acorn,gid=bin,uid=bin isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,check=relaxed,map=normal isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
mount: /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt: unknown filesystem type 'iso9660'.
isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide,session=2 isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
```

# 超时导致 fail

## clock_settime03 clock_settime03

``export LTP_TIMEOUT_MUL`` 没有作用

```
<<<test_start>>>
tag=clock_settime03 stime=1684448780
cmdline="clock_settime03"
contacts=""
analysis=exit
<<<test_output>>>
tst_test.c:1558: TINFO: Timeout per run is 0h 05m 00s
clock_settime03.c:35: TINFO: Testing variant: syscall with old kernel spec
Test timeouted, sending SIGKILL!
tst_test.c:1612: TINFO: If you are running on slow machine, try exporting LTP_TIMEOUT_MUL > 1
tst_test.c:1614: TBROK: Test killed! (timeout?)
```

## perf_event_open02 perf_event_open02

``export LTP_TIMEOUT_MUL`` 没有作用

```
perf_event_open02.c:148: TINFO: [354] value:1818025686 time_enabled:502402999 time_running:502402999
Test timeouted, sending SIGKILL!
tst_test.c:1612: TINFO: If you are running on slow machine, try exporting LTP_TIMEOUT_MUL > 1
tst_test.c:1614: TBROK: Test killed! (timeout?)
```

## read_all_proc read_all -d /proc -q -r 3

进程卡死，无法杀死。

```
read_all.c:424: TINFO: Silencing timeout warnings; consider increasing LTP_RUNTIME_MUL or removing -q
Test timeouted, sending SIGKILL!
tst_test.c:1606: TINFO: Killed the leftover descendant processes
tst_test.c:1612: TINFO: If you are running on slow machine, try exporting LTP_TIMEOUT_MUL > 1
tst_test.c:1614: TBROK: Test killed! (timeout?)
```


# Heuristic: Detected 0 irq-cpu pairs have been dissallowed

## irqbalance01 irqbalance01

```
irqbalance01.c:129: TINFO: Found 4 CPUS, 31 IRQs
irqbalance01.c:287: TFAIL: Heuristic: Detected 0 irq-cpu pairs have been dissallowed
```

# controller required, but not available

## memcontrol02 memcontrol02

包含

+ memcontrol02 memcontrol02
+ memcontrol03 memcontrol03
+ memcontrol04 memcontrol04

```
tst_cgroup.c:844: TCONF: 'memory' controller required, but not available
```

## io_control01 io_control01

```
tst_cgroup.c:844: TCONF: 'io' controller required, but not available
```

# not configured in this kernel

## fanotify10 fanotify10

```
<<<test_output>>>
tst_device.c:317: TINFO: Using test device LTP_DEV='/dev/sda1'
tst_test.c:1093: TINFO: Formatting /dev/sda1 with ext4 opts='' extra opts=''
mke2fs 1.46.5 (30-Dec-2021)
tst_test.c:1558: TINFO: Timeout per run is 0h 05m 00s
fanotify.h:158: TCONF: fanotify is not configured in this kernel
fanotify10.c:945: TWARN: unlink(fs_mnt/testdir/testfile) failed: ENOENT (2)
fanotify10.c:946: TWARN: rmdir(fs_mnt/testdir/testdir2) failed: ENOENT (2)
fanotify10.c:947: TWARN: rmdir(fs_mnt/testdir) failed: ENOENT (2)
fanotify10.c:948: TWARN: rmdir(mntpoint) failed: ENOENT (2)
fanotify.h:158: TCONF: fanotify is not configured in this kernel
fanotify10.c:945: TWARN: unlink(fs_mnt/testdir/testfile) failed: ENOENT (2)
fanotify10.c:946: TWARN: rmdir(fs_mnt/testdir/testdir2) failed: ENOENT (2)
fanotify10.c:947: TWARN: rmdir(fs_mnt/testdir) failed: ENOENT (2)
fanotify10.c:948: TWARN: rmdir(mntpoint) failed: ENOENT (2)
```

# 重测放行

## df01_sh df01.sh

重测只有一个 warning

```
df01 73 TWARN: Failed to release device '/dev/sda1'
```

## mkfs01_sh mkfs01.sh

包含

+ mkfs01_ext2_sh mkfs01.sh -f ext2
+ mkfs01_ext3_sh mkfs01.sh -f ext3
+ mkfs01_ext4_sh mkfs01.sh -f ext4
+ mkfs01_xfs_sh mkfs01.sh -f xfs
+ mkfs01_btrfs_sh mkfs01.sh -f btrfs
+ mkfs01_minix_sh mkfs01.sh -f minix
+ mkfs01_msdos_sh mkfs01.sh -f msdos
+ mkfs01_vfat_sh mkfs01.sh -f vfat
+ mkfs01_ntfs_sh mkfs01.sh -f ntfs

重测只有一个 warning

```
mkfs01 6 TWARN: Failed to release device '/dev/sda1'
```

## mkswap01_sh mkswap01.sh

重测只有一个 warning

```
mkswap01 11 TWARN: Failed to release device '/dev/sda1'
```
