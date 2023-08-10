
bri="br0"
tap="tap"
ip="10.0.0.1/24"
broadcast="10.0.0.255"

drive0="/home/hachi/Desktop/Work/mugen/qemu-imgs/oerv2203/img0.qcow2"
drive1="/home/hachi/Desktop/Work/mugen/qemu-imgs/oerv2203/img1.qcow2"
fw="/home/hachi/Desktop/Work/mugen/qemu-imgs/oerv2203/fw_payload_oe_qemuvirt.elf"

vcpu=8
memory=8
memory_append=`expr $memory \* 1024`

# 宿主机虚拟网卡
sudo brctl addbr $bri
sudo ip addr add $ip broadcast $broadcast dev $bri
sudo ip link set dev $bri up

sudo tunctl -t ${tap}0 -u $(whoami)
sudo tunctl -t ${tap}1 -u $(whoami)
sudo ip link set dev ${tap}0 up
sudo ip link set dev ${tap}1 up
sudo brctl addif $bri ${tap}0
sudo brctl addif $bri ${tap}1

# qemu 1
qemu-system-riscv64 \
-nographic -machine virt \
-cpu rv64,sv39=on -smp ${vcpu} -m ${memory}G \
-audiodev pa,id=snd0 \
-kernel $fw \
-bios none \
-append 'root=/dev/vda1 rw console=ttyS0 swiotlb=1 loglevel=3 systemd.default_timeout_start_sec=600 selinux=0 highres=off mem="$memory_append"M earlycon' \
-drive file=${drive0},format=qcow2,id=hd0,if=none \
-object rng-random,filename=/dev/urandom,id=rng0 \
-device qemu-xhci -usb -device usb-kbd -device usb-tablet -device usb-audio,audiodev=snd0 -device virtio-rng-device,rng=rng0 \
-device virtio-blk-device,drive=hd0 \
-netdev tap,id=net${tap}0,ifname=${tap}0,script=no,downscript=no \
-device virtio-net-pci,netdev=net${tap}0,mac=52:54:00:11:45:01 \
-netdev user,id=usernet,hostfwd=tcp::12055-:22 \
-device virtio-net-pci,netdev=usernet,mac=52:54:00:11:45:02

# qemu 2
qemu-system-riscv64 \
-nographic -machine virt \
-cpu rv64,sv39=on -smp ${vcpu} -m ${memory}G \
-audiodev pa,id=snd0 \
-kernel $fw \
-bios none \
-append 'root=/dev/vda1 rw console=ttyS0 swiotlb=1 loglevel=3 systemd.default_timeout_start_sec=600 selinux=0 highres=off mem="$memory_append"M earlycon' \
-drive file=${drive1},format=qcow2,id=hd0,if=none \
-object rng-random,filename=/dev/urandom,id=rng0 \
-device qemu-xhci -usb -device usb-kbd -device usb-tablet -device usb-audio,audiodev=snd0 -device virtio-rng-device,rng=rng0 \
-device virtio-blk-device,drive=hd0 \
-netdev tap,id=net${tap}1,ifname=${tap}1,script=no,downscript=no \
-device virtio-net-pci,netdev=net${tap}1,mac=52:54:00:11:45:03 \
-netdev user,id=usernet,hostfwd=tcp::12056-:22 \
-device virtio-net-pci,netdev=usernet,mac=52:54:00:11:45:04

# 在 qemu 虚拟机中 查看网卡 enp0s3 可以与宿主机和外网通信 虚拟网卡 enp0s2 可以与其他 qemu 通信
"
[root@openEuler-riscv64 ~]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:54:00:11:45:01 brd ff:ff:ff:ff:ff:ff
3: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:54:00:11:45:02 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute enp0s3
       valid_lft 86170sec preferred_lft 86170sec
    inet6 fec0::5866:c67a:1a0e:6f2/64 scope site dynamic noprefixroute
       valid_lft 86174sec preferred_lft 14174sec
    inet6 fe80::a9fc:a44c:9f55:f853/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
4: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
"

# 在 qemu 虚拟机中 运行配置
# 网桥的 IP 和掩码为 $ip
# ipv4.address 每个虚拟机不要一样 也不要和网桥一样 掩码和网桥一样
# ipv4.gateway 和网桥的 IP 是一致的
nmcli c a type Ethernet con-name enp0s2 ifname enp0s2
nmcli c m enp0s2 ipv4.address 10.0.0.2/24
# qemu 2 则 nmcli c m enp0s2 ipv4.address 10.0.0.3/24
nmcli c m enp0s2 ipv4.gateway 10.0.0.1
nmcli c m enp0s2 ipv4.method manual
nmcli c up enp0s2
