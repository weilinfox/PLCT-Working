# 无法使用 mk-sbuild 建立 schroot

autopkgbuild 推荐使用 mk-sbuild 建立 testbed ，但是 openkylin 软件源中没有该软件包，故使用 Ubuntu 20.04 LTS 的 ``ubuntu-dev-tools`` 源码包构建之

从 ``debian/control`` 中删除 pylint 和 python3-debianbts 的编译依赖以及 python3-ubuntutools 和 python3-debianbts 的依赖；向 ``debian/rules`` 添加 ``export SETUPTOOLS_USE_DISTUTILS=stdlib`` ；其他编译依赖需要手动解决

```bash
DEB_BUILD_OPTIONS=nocheck dpkg-buildpackage -uc -us
sudo apt-get install ../ubuntu-dev-tools_0.193ubuntu4~20.04.3_all.deb
mk-sbuild
```

``mk-sbuild`` 命令将添加当前用户到 ``sbuild`` 用户组，并进行一些初始化配置

配置 debootstrap

```bash
sudo cp /usr/share/debootstrap/scripts/sid /usr/share/debootstrap/scripts/yangtze
```

修改配置

```bash
diff /usr/share/debootstrap/scripts/sid /usr/share/debootstrap/scripts/yangtze
5c5
< keyring /usr/share/keyrings/debian-archive-keyring.gpg
---
> keyring /usr/share/keyrings/openkylin-archive-keyring.gpg
```

出错无法继续

```bash
mk-sbuild yangtze --debootstrap-mirror=http://archive.build.openkylin.top/openkylin/ --distro=debian
I: Target architecture can be executed
I: Retrieving InRelease 
I: Checking Release signature
I: Valid Release signature (key id 09FFC10EA273DD29A986B1108B313CEAFF592D96)
I: Retrieving Packages 
I: Validating Packages 
I: Resolving dependencies of required packages...
I: Resolving dependencies of base packages...
I: Checking component main on http://archive.build.openkylin.top/openkylin...
E: Couldn't find these debs: eatmydata
```
 
