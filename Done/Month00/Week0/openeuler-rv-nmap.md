
# RISC-V openEuler 的 nmap 安全测试报告

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

   为了运行 nmap 测试，我需要将我的机器和 LPi4A 置于同一局域网下，本次测试使用的是无线局域网。

   在 LPi4A 使用 ``nmtui`` 连接到测试用的 Wifi 接入点

   ```
   $ nmtui
   ```

   将我的 Archlinux 机器也连入该 Wifi 接入点，并安装 ``nmap`` （通常已经预装）

   ```
   $ sudo pacman -S nmap
   ```

## 运行测试

测试中， LPi4A 的 IP 地址为 ``192.168.77.39`` 。

1. 测试使用的 nmap 版本

   ```
   $ nmap -v
   
   Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-13 16:03 CST
   Read data files from: /usr/bin/../share/nmap
   WARNING: No targets were specified, so 0 hosts scanned.
   Nmap done: 0 IP addresses (0 hosts up) scanned in 0.05 seconds
   ```

2. 判断目标运行的操作系统

   ```
   # nmap -O -T5 192.168.77.39
    
   Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-13 17:45 CST
   Nmap scan report for 192.168.77.39
   Host is up (0.013s latency).
   Not shown: 999 closed tcp ports (reset)
   PORT   STATE SERVICE
   22/tcp open  ssh
   MAC Address: 2E:05:47:C3:44:A6 (Unknown)
   Device type: general purpose
   Running: Linux 4.X|5.X
   OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
   OS details: Linux 4.15 - 5.6
   Network Distance: 1 hop
    
   OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
   Nmap done: 1 IP address (1 host up) scanned in 4.44 seconds
   ```

   测试得到的内核版本是错误的，正确的版本为 5.10 。

3. 运行半开扫描

   半开扫描主要目的是不让本次扫描让目标记录到。

   ```
   # nmap -sS 192.168.77.39
    
   Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-13 17:49 CST
   Nmap scan report for 192.168.77.39
   Host is up (0.012s latency).
   Not shown: 999 closed tcp ports (reset)
   PORT   STATE SERVICE
   22/tcp open  ssh
   MAC Address: 2E:05:47:C3:44:A6 (Unknown)
    
   Nmap done: 1 IP address (1 host up) scanned in 0.85 seconds
   ```

   可见 tcp 协议只有 ssh 的 22 端口是开放的。

4. 探测 ssh 服务器版本

   ```
   # nmap -v -sV -T4 -Pn 192.168.77.39
    
   Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
   Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-14 01:40 CST
   NSE: Loaded 45 scripts for scanning.
   Initiating ARP Ping Scan at 01:40
   Scanning 192.168.77.39 [1 port]
   Completed ARP Ping Scan at 01:40, 0.11s elapsed (1 total hosts)
   Initiating Parallel DNS resolution of 1 host. at 01:40
   Completed Parallel DNS resolution of 1 host. at 01:40, 0.01s elapsed
   Initiating SYN Stealth Scan at 01:40
   Scanning 192.168.77.39 [1000 ports]
   Discovered open port 22/tcp on 192.168.77.39
   Completed SYN Stealth Scan at 01:40, 0.24s elapsed (1000 total ports)
   Initiating Service scan at 01:40
   Scanning 1 service on 192.168.77.39
   Completed Service scan at 01:40, 0.08s elapsed (1 service on 1 host)
   NSE: Script scanning 192.168.77.39.
   Initiating NSE at 01:40
   Completed NSE at 01:40, 0.01s elapsed
   Initiating NSE at 01:40
   Completed NSE at 01:40, 0.00s elapsed
   Nmap scan report for 192.168.77.39
   Host is up (0.0090s latency).
   Not shown: 999 closed tcp ports (reset)
   PORT   STATE SERVICE VERSION
   22/tcp open  ssh     OpenSSH 9.1 (protocol 2.0)
   MAC Address: 2E:05:47:C3:44:A6 (Unknown)
    
   Read data files from: /usr/bin/../share/nmap
   Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
   Nmap done: 1 IP address (1 host up) scanned in 0.93 seconds
              Raw packets sent: 1001 (44.028KB) | Rcvd: 1001 (40.032KB)
   ```

   实际运行版本为 ``OpenSSH_9.1p1, OpenSSL 3.0.8 7 Feb 2023`` ，是一致的。

5. 运行全面扫描

   ```
   # nmap -v -A 192.168.77.39
    
   Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-14 01:41 CST
   NSE: Loaded 155 scripts for scanning.
   NSE: Script Pre-scanning.
   Initiating NSE at 01:41
   Completed NSE at 01:41, 0.00s elapsed
   Initiating NSE at 01:41
   Completed NSE at 01:41, 0.00s elapsed
   Initiating NSE at 01:41
   Completed NSE at 01:41, 0.00s elapsed
   Initiating ARP Ping Scan at 01:41
   Scanning 192.168.77.39 [1 port]
   Completed ARP Ping Scan at 01:41, 0.07s elapsed (1 total hosts)
   Initiating Parallel DNS resolution of 1 host. at 01:41
   Completed Parallel DNS resolution of 1 host. at 01:41, 0.00s elapsed
   Initiating SYN Stealth Scan at 01:41
   Scanning 192.168.77.39 [1000 ports]
   Discovered open port 22/tcp on 192.168.77.39
   Completed SYN Stealth Scan at 01:41, 0.21s elapsed (1000 total ports)
   Initiating Service scan at 01:41
   Scanning 1 service on 192.168.77.39
   Completed Service scan at 01:41, 0.08s elapsed (1 service on 1 host)
   Initiating OS detection (try #1) against 192.168.77.39
   NSE: Script scanning 192.168.77.39.
   Initiating NSE at 01:41
   Completed NSE at 01:42, 5.07s elapsed
   Initiating NSE at 01:42
   Completed NSE at 01:42, 0.00s elapsed
   Initiating NSE at 01:42
   Completed NSE at 01:42, 0.00s elapsed
   Nmap scan report for 192.168.77.39
   Host is up (0.0099s latency).
   Not shown: 999 closed tcp ports (reset)
   PORT   STATE SERVICE VERSION
   22/tcp open  ssh     OpenSSH 9.1 (protocol 2.0)
   | ssh-hostkey: 
   |   256 dd826fb919b618309c28f0f7f5138979 (ECDSA)
   |_  256 55cde2eba72095af645f05606cf80e6e (ED25519)
   MAC Address: 2E:05:47:C3:44:A6 (Unknown)
   Device type: general purpose
   Running: Linux 4.X|5.X
   OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
   OS details: Linux 4.15 - 5.6
   Uptime guess: 49.623 days (since Sat Mar 25 10:44:41 2023)
   Network Distance: 1 hop
   TCP Sequence Prediction: Difficulty=261 (Good luck!)
   IP ID Sequence Generation: All zeros
    
   TRACEROUTE
   HOP RTT     ADDRESS
   1   9.93 ms 192.168.77.39
    
   NSE: Script Post-scanning.
   Initiating NSE at 01:42
   Completed NSE at 01:42, 0.00s elapsed
   Initiating NSE at 01:42
   Completed NSE at 01:42, 0.00s elapsed
   Initiating NSE at 01:42
   Completed NSE at 01:42, 0.00s elapsed
   Read data files from: /usr/bin/../share/nmap
   OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
   Nmap done: 1 IP address (1 host up) scanned in 7.39 seconds
              Raw packets sent: 1024 (46.134KB) | Rcvd: 1017 (41.430KB)
   ```

6. 扫描所有 TCP 端口

   nmap 默认只扫描低位 1024 个端口，这里扫描全部 65536 个端口。 ``-T4`` 的作用是加快扫描速度； ``-Pn`` 的作用是默认扫描的目标主机是在线的，直接跳过主机探测的阶段。

   ```
   # nmap -v -sT -T4 -Pn -p0-65535 192.168.77.39
    
   Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
   Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-14 01:38 CST
   Initiating Parallel DNS resolution of 1 host. at 01:38
   Completed Parallel DNS resolution of 1 host. at 01:38, 0.01s elapsed
   Initiating Connect Scan at 01:38
   Scanning 192.168.77.39 [65536 ports]
   Discovered open port 22/tcp on 192.168.77.39
   Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
   Connect Scan Timing: About 53.44% done; ETC: 01:38 (0:00:05 remaining)
   Stats: 0:00:08 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
   Connect Scan Timing: About 85.55% done; ETC: 01:38 (0:00:02 remaining)
   Completed Connect Scan at 01:38, 9.74s elapsed (65536 total ports)
   Nmap scan report for 192.168.77.39
   Host is up (0.0083s latency).
   Not shown: 65535 closed tcp ports (conn-refused)
   PORT   STATE SERVICE
   22/tcp open  ssh
   
   Read data files from: /usr/bin/../share/nmap
   Nmap done: 1 IP address (1 host up) scanned in 9.82 seconds
   ```

7. 扫描所有 UDP 端口

   ```
   # nmap -sU -T4 -Pn -p0-65535 192.168.77.39
    
   Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-13 17:53 CST
   Warning: 192.168.77.39 giving up on port because retransmission cap hit (6).
   Stats: 1:16:01 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
   UDP Scan Timing: About 5.69% done; ETC: 16:09 (20:59:18 remaining)
   Stats: 8:03:42 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
   UDP Scan Timing: About 40.79% done; ETC: 13:39 (11:42:02 remaining)
   Stats: 20:02:04 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
   UDP Scan Timing: About 99.99% done; ETC: 13:55 (0:00:07 remaining)
   Nmap scan report for 192.168.77.39
   Host is up (0.072s latency).
   Not shown: 65513 closed udp ports (port-unreach)
   PORT      STATE         SERVICE
   67/udp    open|filtered dhcps
   68/udp    open|filtered dhcpc
   5693/udp  open|filtered unknown
   6362/udp  open|filtered unknown
   16229/udp open|filtered unknown
   21262/udp open|filtered unknown
   21758/udp open|filtered unknown
   24365/udp open|filtered unknown
   27222/udp open|filtered unknown
   28138/udp open|filtered unknown
   32394/udp open|filtered unknown
   32972/udp open|filtered unknown
   33342/udp open|filtered unknown
   33931/udp open|filtered unknown
   37290/udp open|filtered unknown
   39725/udp open|filtered unknown
   40595/udp open|filtered unknown
   50163/udp open|filtered unknown
   50844/udp open|filtered unknown
   57138/udp open|filtered unknown
   57929/udp open|filtered unknown
   60962/udp open|filtered unknown
   61609/udp open|filtered unknown
   MAC Address: 2E:05:47:C3:44:A6 (Unknown)
    
   Nmap done: 1 IP address (1 host up) scanned in 73223.80 seconds
   ```

   UDP 扫描的过程非常慢，一共运行了 20 个小时。

8. 复测 UDP 端口

   复测上面扫描到的 UDP 端口是否依然存活

   ```
   # nmap -sU -Pn -p67,68,5693,6362,16229,21262,21758,24365,27222,28138,32394,32972,33342,33931,37290,39725,40595,50163,50844,57138,57929,60962,61609 192.168.77.39
    
   Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-15 16:39 CST
   Nmap scan report for 192.168.77.39
   Host is up (0.051s latency).
    
   PORT      STATE         SERVICE
   67/udp    open|filtered dhcps
   68/udp    open|filtered dhcpc
   5693/udp  closed        unknown
   6362/udp  closed        unknown
   16229/udp closed        unknown
   21262/udp closed        unknown
   21758/udp closed        unknown
   24365/udp closed        unknown
   27222/udp closed        unknown
   28138/udp closed        unknown
   32394/udp closed        unknown
   32972/udp closed        unknown
   33342/udp closed        unknown
   33931/udp closed        unknown
   37290/udp closed        unknown
   39725/udp closed        unknown
   40595/udp closed        unknown
   50163/udp closed        unknown
   50844/udp closed        unknown
   57138/udp closed        unknown
   57929/udp closed        unknown
   60962/udp closed        unknown
   61609/udp closed        unknown
   MAC Address: 2E:05:47:C3:44:A6 (Unknown)
    
   Nmap done: 1 IP address (1 host up) scanned in 19.22 seconds
   ```

   除了 DHCP 使用的服务器端 67 和客户端 68 端口一直打开，其他端口在多次扫描中时而打开时而关闭，故忽略。

## 问题分析

测试镜像默认情况下只打开了 ssh 和 DHCP 服务器。 ssh 服务器用于远程登陆，且允许了 root 和普通用户的密码登陆。由于初始的用户名和密码均是公开的，一定程度上具有安全问题，故建议在首次登陆后立即重设密码。

UDP 扫描过于缓慢， 65536 个端口一共耗时 20 小时。可以使用更快的端口扫描工具确认端口存活，再使用 nmap 进行下一步的检测。亦可直接不对 1024 以上的端口进行检测。
