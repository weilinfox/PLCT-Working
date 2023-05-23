# RISC-V openEuler 5.10 内核的 LTP 测试报告 

2023.5.19 weilinfox

+ OS 版本： openEuler RISC-V 23.03 V1
+ 内核版本： kernel 5.10.113
+ LTP版本： Release 20230516
+ 测试平台： LPi4A

从5月16日开始，用 20220121 版本和 20230516 版本一共完整测试了四次。由于时间比较紧张，遇到好多意外的问题，最终测试结果是由三次不完整的测试汇总起来的。

所有测试都是在 ``root`` 用户下进行的，会出现故障的测试将被跳过并单独测试。

## 搭建环境

我使用的操作系统为 Archlinux ，测试镜像为 Lichee Pi 4A 的 openEuler-23.03-V1-base.ext4.zst 。

1. 下载烧写工具和 uboot

   需要从 Sipeed 的[官方镜像](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)下载。烧写工具为 ``burn_tools.zip`` ， uboot 二进制为 ``u-boot-with-spl_0425`` 。

2. 下载并烧写测试镜像

   下载 [openEuler-23.03-V1-boot.ext4.zst](https://repo.tarsier-infra.com/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/lpi4a/openEuler-23.03-V1-boot.ext4.zst) 和 [openEuler-23.03-V1-base.ext4.zst](https://repo.tarsier-infra.com/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/lpi4a/openEuler-23.03-V1-base.ext4.zst) 。

   解压缩镜像

   ```
   $ zstd -d openEuler-23.03-V1-boot.ext4.zst
   $ zstd -d openEuler-23.03-V1-base.ext4.zst
   ```

    在掉电的情况下按住 LPi4A 的 BOOT 按钮，使用 type-c 线连接开发板和计算机 usb 口，确认连接正常后开始烧写镜像。

   ```
   $ sudo ./fastboot flash ram ./u-boot-with-spl.bin
   $ sudo ./fastboot reboot
   $ sudo ./fastboot flash uboot ./u-boot-with-spl.bin
   $ sudo ./fastboot flash boot ./openEuler-23.03-V1-boot.ext4
   $ sudo ./fastboot flash root ./openEuler-23.03-V1-base.ext4
   ```

   烧写成功后重新上电，开发板将自动引导。

3. 建立普通用户

   镜像并没有预设的普通用户，所以使用 ``root`` 用户登陆，密码为 ``openEuler12#$`` 。

   建立普通用户 ``hachi`` ，将其加入 ``wheel`` 用户组，并创建家目录 ``/home/hachi``

   ```
   # useradd -m -G wheel hachi
   ```

   设置密码

   ```
   # passwd hachi
   ```

   现在可以切换到普通用户 ``hachi``

   ```
   # su hachi
   ```

4. 配置网络

   使用 ``nmtui`` 连接到 Wifi 接入点

   ```
   $ nmtui
   ```

   也可以使用有线网络。

5. 扩展根目录

   镜像的根目录 ext4 文件系统只有 1.4G 大小，实际使用 fdisk 可以看到分区大小为 5.9G ，可以使用 ``resize2fs`` 扩展文件系统的大小。
   
   ```
   $ sudo fdisk -l
   
   Device           Start      End  Sectors  Size Type
   /dev/mmcblk0p1      34     4095     4062    2M Microsoft basic data
   /dev/mmcblk0p2    4096  1028095  1024000  500M Linux extended boot
   /dev/mmcblk0p3 1028096 13316095 12288000  5.9G Linux filesystem
   ```
   
   可以看到实际分区大小为 12288000 扇区
   
   ```
   $ sudo resize2fs /dev/mmcblk0p3 12288000s
   ```

6. 配置 SD 卡

   由于 8G emmc 无法满足测试所需磁盘空间要求，需要 SD 卡辅助。
   
   将 SD 卡插入卡槽，使用 ``fdisk`` 建立两个分区
   
   ```
   $ sudo fdisk /dev/mmcblk1
   ```
   
   建立 ext4 文件系统
   
   ```
   $ sudo mkfs.ext4 /dev/mmcblk1p1
   $ sudo mkfs.ext4 /dev/mmcblk1p2
   ```
   
   配置 fstab
   
   ```
   /dev/mmcblk1p1 /opt   auto    defaults    0 2
   /dev/mmcblk1p2 /home   auto    defaults    0 2
   /opt/swapfile   none    swap    sw      0 0
   ```
   
   我使用的是 256G 的 SD 卡，配置完成后 ``fdisk -l`` 输出如下
   
   ```
   Device         Boot     Start       End   Sectors   Size Id Type
   /dev/mmcblk1p1           2048 209717247 209715200   100G 83 Linux
   /dev/mmcblk1p2      209717248 483327999 273610752 130.5G 83 Linux
   ```
   
   挂载并复制原来 /opt 和 /home 分区下的文件，注意文件权限。

7. 设置交换空间

   交换空间配置为内存大小，这里使用的是 swap file 。

   建立 swap file
   
   ```
   $ sudo dd if=/dev/zero of=/opt/swapfile block=1024 count=8388608 status=progress
   $ sudo chmod 600 /opt/swapfile
   $ sudo mkswap /opt/swapfile
   ```

   启用 swap file
   
   ```
   $ sudo swapon /opt/swapfile
   ```
   
   配置 fstab
   
   ```
   /opt/swapfile   none    swap    sw      0 0
   ```

8. 测试用临时目录

   测试的临时文件目录默认是 ``/tmp`` ，但 openEuler 将其安装为 tmpfs ，这会导致很多测试意外失败。因此专门建立一个目录，并在运行脚本参数中指明
   
   ```
   $ sudo mkdir /opt/tmp
   ```
   
   测试中 ``/opt`` 目录足够大。

9. 配置额外的块设备

   两个额外的块设备分别是 ``LTP_DEV`` 和 ``LTP_BIG_DEV`` ，这里使用一块 U 盘，设备分别为 ``/dev/sda1`` 和 ``/dev/sda2`` ，分别为 1G 和 2G 大小，均格式化为了 ext4 文件系统。
   
   注意过大的分区反而会导致测试失败，比如 ``mkfs01_msdos_sh`` 和 ``mkfs01_vfat_sh`` 在使用 5G 大小的 ``LTP_DEV`` 时将失败。

10. 连接串口

    串口输出为丝印的 ``U0-TX`` 和 ``U0-RX`` ，分别和串口转 USB 线的 ``RX`` 和 ``TX`` 连接，同时将 LPi4A 的 ``GND`` 与串口转 USB 线的 ``GND`` 相连。在计算机上使用 ``minicom`` 或其他类似的串口调试软件进行监视。

    在 LPi4A 上， ``GND`` 为从 3.5mm 耳机接口开始第二列的两个脚， ``U0-TX`` 和 ``U0-RX`` 分别为第 5 列的上层和下层两个脚。

## 构建安装并运行 LTP

构建安装和运行 LTP 的脚本为 [start_ltp_test.sh](./start_ltp_test.sh) 。原始脚本来自[这里](https://gitee.com/hanson_fang/ltpstress-for-openeuler/blob/master/ltp/start_ltp_test.sh)，内容按照本次测试需要进行了修改。

脚本中一共有三个函数， ``install_rpm`` 安装构建和测试必须的工具， ``compile_ltp`` 构建并安装 LTP ， ``run_testcases`` 运行所有测试。前两个函数只在第一次测试时运行，之后注释掉即可。

测试的内核直接使用镜像预装的内核。

运行测试

```
$ sudo su
# ./start_ltp_test.sh
```

测试中需要特别注意的两个要跳过的用例分别为 ``proc01`` 和 ``cve-2022-4378`` 。前者无论普通用户还是 root 用户都会跑死，且进程无法杀死，后者会导致 [kernel panic](./ltp-20230516/logs/cve-2022-4378_kp.txt) 。加上 ``laokz`` 在报告中提供的可以跳过的测试用例，实际使用的列表 [skipped.5.10.0.tests](./ltp-20230516/skip.tests/skipped.5.10.0.tests)

## 主要结果

测试结果由三次不完整的测试经过手动整理和计数汇总而来，按照测试用例统计如下：
+ 失败的：21
+ 跳过的：254
+ 未知的（TCONF）：263

跳过的用例均为 ``laokz`` 在报告中提供的可以跳过的测试用例，原始列表在 [skipped.5.10.0.tests](https://gitee.com/laokz/oerv/blob/master/ltp/skipped.5.10.0.tests) 。

除了主动跳过以外的 TCONF 用例大部分是缺少模块和配置导致的，但是还没有详细统计。

失败的用例则有很多需要关注的地方。

1. 没有打的 patch

   ``vma05`` 测试报
   
   ```
   vma05 1 TFAIL: [vdso] bug not patched
   ```

2. 可能遗漏的 kernel fixes

   + ``bpf_prog06``： <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=64620e0a1e71>
   + ``inotify12``： <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=a32e697cda27>
   + ``openat04``： <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=ac6800e279a2> 和 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=426b4ca2d6a5>
   + ``hugemmap15``： <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=cbf52afdc0eb>

3. kernel panic

   ``cve-2022-4378`` 测试会导致 kernel panic
   
   ```
   [ 7571.643116] LTP: starting cve-2022-4378
   [ 7571.664481] Kernel panic - not syncing: stack-protector: Kernel stack is corrupted in: proc_get_long.constprop.0+0x156/0x156
   [ 7571.664491] SMP: stopping secondary CPUs
   [ 7571.664505] enter panic_cpufreq_notifier_call
   [ 7571.664661] finish to execute cpufreq notifier callback on panic
   [ 7571.690280] ---[ end Kernel panic - not syncing: stack-protector: Kernel stack is corrupted in: proc_get_long.constprop.0+0x156/0x156 ]---
   ```

4. 无法杀死的进程

   + ``proc01``： 无论普通用户还是 root 用户都会跑死，测试将无法继续，且进程无法杀死
   + ``read_all_proc``： 进程无法结束且无法杀死，导致该测试超时失败
   + ``fs_fill``： 测试报 ``Cannot kill test processes!`` ， ``Congratulation, likely test hit a kernel bug`` （这可能是一个内核 bug）
   
5. 未知原因导致的超时

   尽管在输出中均建议配置更大的 ``LTP_TIMEOUT_MUL`` ，实测不知道为什么 ``export LTP_TIMEOUT_MUL`` 并没有增加测试超时的时间
   + ``clock_settime03``
   + ``perf_event_open02``
   + ``read_all_proc``
   
6. 未知原因导致的 fail

   + ``leapsec01``
      ```
      leapsec01.c:84: TBROK: adjtimex status 8208 not set
      ```
   + ``epoll_pwait02``
      ```
      epoll_pwait02.c:30: TFAIL: do_epoll_pwait() returned -1, expected 1
      ```
   + ``epoll_pwait03``
      ```
      epoll_pwait03.c:33: TFAIL: do_epoll_pwait() returned -1, expected 0: ENOSYS (38)
      ```
   + ``epoll_pwait04``
      ```
      epoll_pwait04.c:25: TFAIL: with an invalid sigmask pointer expected EFAULT: ENOSYS (38)
      ```
   + ``getxattr04``
      ```
      tst_test.c:1107: TBROK: mount(/dev/sda1, mntpoint, xfs, 0, (nil)) failed: ENODEV (19)
      ```
   + ``isofs``
      ```
      isofs 1 TFAIL: mount -t iso9660 -o loop,block=512,unhide,session=2 isofs.iso /opt/tmp/ltp-znvgVECKls/LTP_isofs.VWkA3ePjkO/mnt failed unexpectedly
      ```

## 遇到的其他问题

1. SD 卡 I/O 错误

   由于板载 emmc 只有 8G ，完全无法满足测试需求，故测试中 ``/opt`` 和 ``/home`` 目录是由 SD 卡挂载的。测试期间一共遇到三次 I/O 错误，测试时均在运行 dio 测试。由于其中两次错误是由 5V type-c 供电，其中一次是由配套的 12V 适配器供电，故排除供电原因。测试使用的卡是 banq 256G A1 U3 卡，猜测这可能是 SD 卡兼容性导致的。

2. Attempting to create a too small or a too large filesystem

   一开始我使用了 5G 的 ``LTP_DEV`` 和 10G 的 ``LTP_BIG_DEV`` ，导致 ``mkfs01_msdos_sh`` 和 ``mkfs01_vfat_sh`` 两个测试失败，部分日志如下：
   
   ```
   <<<test_start>>>
   tag=mkfs01_msdos_sh stime=1684385228
   cmdline="mkfs01.sh -f msdos"
   contacts=""
   analysis=exit
   <<<test_output>>>
   tst_device.c:317: TINFO: Using test device LTP_DEV='/dev/sda1'
   mkfs01 1 TINFO: timeout per run is 0h 50m 0s
   mkfs01 1 TPASS: 'mkfs -t msdos  /dev/sda1 ' passed.
   mkfs01 2 TFAIL: 'mkfs -t msdos  /dev/sda1 16000' failed.
   Warning: block count mismatch: found 5242880 but assuming 16000.
   WARNING: Number of clusters for 32 bit FAT is less then suggested minimum.
   mkfs.msdos: Attempting to create a too small or a too large filesystem
   mkfs.fat 4.2 (2021-01-31)
   
   <<<test_start>>>
   tag=mkfs01_vfat_sh stime=1684385269
   cmdline="mkfs01.sh -f vfat"
   contacts=""
   analysis=exit
   <<<test_output>>>
   tst_device.c:317: TINFO: Using test device LTP_DEV='/dev/sda1'
   mkfs01 1 TINFO: timeout per run is 0h 50m 0s
   mkfs01 1 TPASS: 'mkfs -t vfat  /dev/sda1 ' passed.
   mkfs01 2 TFAIL: 'mkfs -t vfat  /dev/sda1 16000' failed.
   Warning: block count mismatch: found 5242880 but assuming 16000.
   WARNING: Number of clusters for 32 bit FAT is less then suggested minimum.
   mkfs.vfat: Attempting to create a too small or a too large filesystem
   mkfs.fat 4.2 (2021-01-31)
   ```

3. Failed to acquire device

   一些测试中需要使用空闲的块设备，所以测试时插入一张 U 盘来充当。测试时会出现无法访问设备的情况，报 ``TWARN: /dev/sda1 is not a block device`` 以及 ``TBROK: Failed to acquire device`` ，重测则可以正常通过。
