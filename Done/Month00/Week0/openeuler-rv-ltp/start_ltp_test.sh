#!/usr/bin/bash
# https://gitee.com/hanson_fang/ltpstress-for-openeuler/blob/master/ltp/start_ltp_test.sh

#set_yum_env(){
#    echo 'sslverify=false' >>/etc/yum.conf
#    \cp openEuler.repo /etc/yum.repos.d/openEuler.repo
#    ver=$(cat /etc/openEuler-latest | grep openeulerversion | awk -F= '{print $2}')
#    sed -i "s/branch/${ver}/g" /etc/yum.repos.d/openEuler.repo    
#    yum makecache
#}

install_rpm(){
    yum install -y zlib zlib-devel bc httpd net-tools gcc-c++ m4 flex byacc bison keyutils-libs-devel lksctp-tools-devel xfsprogs-devel libacl-devel openssl-devel numactl-devel libaio-devel glibc-devel libcap-devel findutils libtirpc kernel-devel kernel-headers kernel-tools glibc-headers elfutils-libelf-devel patch numactl tar automake cmake time psmisc vim git make genisoimage btrfs-progs ethtool expect-devel irqbalance nfs-utils ntfs-3g quota squashfs-tools sysstat
    dnf update -y
    sed -i '$a set number' /etc/vimrc
    echo 'export LANG=en_US.UTF-8' >> /root/.bashrc
    source /root/.bashrc
    hostnamectl set-hostname localhost
}

compile_ltp(){
    cd /opt;
    if [ ! -d "ltp" ];then
        #until (test -e "ltp")
        #do
        #    git clone https://github.com/linux-test-project/ltp.git
        #done
        #wget -c -t 30 https://github.com/linux-test-project/ltp/archive/refs/tags/20220121.zip
	wget -c -t 30 https://kgithub.com/linux-test-project/ltp/archive/refs/tags/20230516.zip
        unzip 20230516.zip && cd ltp-20230516
        make autotools
        ./configure --with-bash --with-expect --with-perl --with-python
        #make -j16
	make -j4 # LPi4A 四核
	# 安装到 /opt/ltp
        make install
    fi
}

run_testcases(){
    cd /opt/ltp;
    #./runltp |tee ltp.log #默认执行全部，scenario_groups/default中配置调度文件
    # https://gitee.com/laokz/oerv/blob/master/ltp/report.md
    # https://www.bilibili.com/video/BV1Eg4y137rq/
    # tee 比 -o 保存信息稍微多一点
    #./runltp -p -S ./skiped.test -d /opt/tmp |tee ltp.log
    export LTP_TIMEOUT_MUL=10
    ./runltp -p -S ./skipped.tests -d /opt/tmp -b /dev/sda1 -B ext4 -z /dev/sda2 -Z ext4 | tee ltp.log

}

#set_yum_env 不需要

# 首次运行 ltp 运行这两个
#install_rpm
#compile_ltp
run_testcases
