# openkylin licheepi4a autopkgtest with schroot

## 测试说明

autopkgtest 是运行由DEP8定义的测试套件的软件。其软件的测试套由软件上游编写，并遵循DEP8的规定

为了对本机系统进行保护，autopkgtest在运行时需要一个与本机系统相隔离的测试环境，称为 ``testbed``

由于 openkylin 1.0 没有发布 Qemu 镜像，所以这里选择使用 schroot 容器配置 testbed 进行测试

## 获取测试列表

向 ``/etc/apt/sources.list`` 添加源码包源

```bash
deb-src http://archive.build.openkylin.top/openkylin/ yangtze main cross pty
deb-src http://archive.build.openkylin.top/openkylin/ yangtze-security main cross pty
deb-src http://archive.build.openkylin.top/openkylin/ yangtze-updates main cross pty
```

刷新软件包缓存后，列出所有软件包

```bash
apt-cache pkgnames > pkgs.list
cat pkgs.list | wc -l

43205
```

获取源码包列表

```bash
cat pkgs.list | xargs apt-cache showsrc | grep Package: > pkgsrc.list.raw
cat pkgsrc.list.raw | cut -d' ' -f2 > pkgsrc.list
cat pkgsrc.list | wc -l

4955
```

软件源共有 43205 个软件包，其中 4955 个软件包有源码包

## 配置 schroot

给出 schroot 环境配置 [schroot_config](./schroot_config)

尽管 autopkgtest 推荐使用 mk-sbuild 构建 schroot 环境，但是在 openkylin 使用其配置失败，详细失败信息 [mk-sbuild.md](./mk-sbuild.md)

最后选择直接使用 openKylin-1.0-licheepi4a-riscv64.ext4 镜像作为 schroot 环境

```bash
sudo losetup /dev/loop0 openKylin-1.0-licheepi4a-riscv64.ext4
sudo mount /dev/loop0 /mnt/mmcblk
sudo cp -r /mnt/mmcblk/* /opt/chroot/openkylin-rv/
sudo cp -r /usr/lib/modules/5.10.113-gfac22a756532/ /opt/chroot/openkylin-rv/usr/lib/modules/
sudo rm /opt/chroot/openkylin-rv/etc/resolv.conf
schroot -c openkylin-rv
```

应该能够正常进入 schroot 环境

测试出现类似如下错误

```
dpkg --unpack /tmp/autopkgtest.zqh1Ik/1-autopkgtest-satdep.deb" failed with stderr "dpkg: warning: files list file for package 'udisks2' missing; assuming package has no files currently installed
```

重新安装 udisks2 软件包

```bash
sudo apt-get update
sudo apt-get reinstall udisks2
```

## 测试失败

尝试测试 vim 软件包

```bash
apt-get source vim
sudo autopkgtest vim_8.1.2269-ok5.dsc -o test -d -- schroot openkylin-rv
```

测试失败

```
autopkgtest: DBG: testbed command ['dpkg', '--status', 'autopkgtest-satdep'], kind short, sout pipe, serr pipe, env []
autopkgtest: DBG: testbed command exited with code 1
autopkgtest: WARNING: Test dependencies are unsatisfiable - calling apt install on test deps directly for further data about failing dependencies in test logs
autopkgtest: DBG: testbed command ['/bin/sh', '-ec', ' apt-get install --assume-yes --simulate autoconf cscope debhelper (>= 11~) libacl1-dev libcanberra-dev libgpmg1-dev libgtk-3-dev liblua5.2-dev libperl-dev libselinux1-dev libncurses-dev libtool-bin libxaw7-dev libxpm-dev libxt-dev lua5.2 python3-dev ruby ruby-dev tcl-dev docbook-utils docbook-xml ghostscript pdf2svg build-essential -o APT::Status-Fd=3 -o APT::Install-Recommends=False -o Dpkg::Options::=--force-confnew -o Debug::pkgProblemResolver=true 3>&2 2>&1'], kind install, sout raw, serr pipe, env ['DEBIAN_FRONTEND=noninteractive', 'APT_LISTBUGS_FRONTEND=none', 'APT_LISTCHANGES_FRONTEND=none']
autopkgtest: DBG: testbed command exited with code 2
blame: vim_8.1.2269-ok5.dsc
autopkgtest: DBG: BadPackageError Test dependencies are unsatisfiable. A common reason is that your testbed is out of date with respect to the archive, and you need to use a current testbed or run apt-get update or use -U.
badpkg: Test dependencies are unsatisfiable. A common reason is that your testbed is out of date with respect to the archive, and you need to use a current testbed or run apt-get update or use -U.
autopkgtest [14:13:14]: ERROR: erroneous package: Test dependencies are unsatisfiable. A common reason is that your testbed is out of date with respect to the archive, and you need to use a current testbed or run apt-get update or use -U.
autopkgtest: DBG: testbed stop
autopkgtest: DBG: testbed close, scratch=/tmp/autopkgtest.pUSCQV
autopkgtest: DBG: sending command to testbed: close
autopkgtest: DBG: got reply from testbed: ok
autopkgtest: DBG: sending command to testbed: quit
```

## 其他信息

同样的根目录和软件源配置，在 LicheePi 4A 可以正常刷新软件包缓存，而在 schroot 环境中，运行 ``apt-get update`` 无法成功刷新软件包缓存

```
(openkylin-rv)root@openkylin:~# apt-get update
命中:1 http://archive.build.openkylin.top/openkylin yangtze InRelease
命中:2 http://archive.build.openkylin.top/openkylin yangtze-security InRelease
命中:3 http://ppa.build.openkylin.top/kylinsoft/anything/openkylin yangtze InRelease
命中:4 http://archive.build.openkylin.top/openkylin yangtze-updates InRelease
忽略:5 http://archive.build.openkylin.top/openkylin yangtze/pty Sources
忽略:6 http://archive.build.openkylin.top/openkylin yangtze/main Sources
获取:7 http://archive.build.openkylin.top/openkylin yangtze/cross Sources [1,789 B]
获取:5 http://archive.build.openkylin.top/openkylin yangtze/pty Sources [16.4 kB]
错误:5 http://archive.build.openkylin.top/openkylin yangtze/pty Sources
  文件尺寸不符(17624 != 16388)。您使用的镜像正在同步中？ [IP: 124.126.103.198 80]
  Hashes of expected file:
   - Filesize:16388 [weak]
   - SHA256:9f10db0a4d6bc4129ee1bad80ca29b9cd35c90a0f0bc1adfd9305de7da3162a8
   - SHA1:3710060a2e4d3643dd07249b672f820c688a39db [weak]
   - MD5Sum:e15a566bec3ecfed601d745ba057d7cb [weak]
  Release file created at: Tue, 04 Jul 2023 07:13:01 +0000
获取:6 http://archive.build.openkylin.top/openkylin yangtze/main Sources [1,210 kB]  
错误:6 http://archive.build.openkylin.top/openkylin yangtze/main Sources
  
已下载 1,789 B，耗时 3秒 (610 B/s)
正在读取软件包列表... 完成E: 无法下载 http://archive.build.openkylin.top/openkylin/dists/yangtze/pty/source/Sources.bz2  文件尺寸不符(17624 != 16388)。您使用的镜像正在同步中？ [IP: 124.126.103.198 80]
   Hashes of expected file:
    - Filesize:16388 [weak]
    - SHA256:9f10db0a4d6bc4129ee1bad80ca29b9cd35c90a0f0bc1adfd9305de7da3162a8
    - SHA1:3710060a2e4d3643dd07249b672f820c688a39db [weak]
    - MD5Sum:e15a566bec3ecfed601d745ba057d7cb [weak]
   Release file created at: Tue, 04 Jul 2023 07:13:01 +0000
E: 无法下载 http://archive.build.openkylin.top/openkylin/dists/yangtze/main/source/Sources.bz2  
E: 部分索引文件下载失败。如果忽略它们，那将转而使用旧的索引文件。
```

## 测试结论

openkylin 1.0 不满足 autopkgtest 测试需求，无法运行测试
