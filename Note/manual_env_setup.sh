#!/bin/bash

# MUGEN_DIR=/home/hachi/mugen/mugen

WORKING_DIR=/home/hachi/mugen/com/workingDir
QEMU_QCOW2=/home/hachi/mugen/qemu-img-rc3/workingDir/mugen-ready.qcow2
QEMU_BIOS=/home/hachi/mugen/qemu-img-rc3/workingDir/fw_payload_oe_uboot_2304.bin
QEMU_SMP=4
QEMU_MEM=4
QEMU_PASSWD=openEuler12#$
QEMU_DISK_ADD=4
QEMU_HOST=4

QEMU_QCOW2=$(realpath $QEMU_QCOW2)
SCRIPT_DIR=$(cd $(dirname $0); pwd)
BRIDGE_NAME=combr0
BRIDGE_IP=10.0.0.1/24
BRIDGE_BRD=10.0.0.255
TAP_NAME=comtap
TAP_IP=10.0.0.
TAP_IP_START=2
#TAP_NAME=tap
SCREEN_SNAME=comss
QEMU_IMG=host_img
QEMU_DISK=disk_img
QEMU_MAC=52:54:00:11:45:

ip -V >/dev/null || exit -1
screen -v >/dev/null || exit -1
sudo -V >/dev/null || exit -1
netstat -V >/dev/null || exit -1
qemu-img -V >/dev/null || exit -1
qemu-system-riscv64 --version >/dev/null || exit -1

function SSH_CMD {
	expect >/dev/null << EOF
	spawn ssh -p $1 root@localhost
	expect {
		"yes/no" {
			send "yes\r"
			exp_continue
		}
		"password:" {
			send "$2\r"
		}
	}
	expect "# "
	send "$3\r"
	expect "# "
	send "exit\r"
	expect eof
	catch wait result
	exit [lindex \$result 3]
EOF
}

function SCP {
	expect >/dev/null << EOF
	spawn scp -r -P $1 root@localhost:$3 .
	expect {
		"yes/no/" {send "yes\r"}
		"password" {send "$2\r"}
	}
	expect {
		"password" {send "$2\r"}
		eof
	}
EOF
}

function SSH_CMD_OUT {
	fn=ssh_cmd_$RANDOM$RANDOM$RANDOM.log

	expect>/dev/null << EOF
	spawn ssh -p $1 root@localhost
	expect {
		"yes/no" {
			send "yes\r"
			exp_continue
		}
		"password:" {
			send "$2\r"
		}
	}
	expect "# "
	send "$3 >$fn\r"
	expect {
		"# " {
		send "exit\r"
		expect eof
		}
	}
EOF
	SCP $1 $2 $fn
	SSH_CMD $1 $2 "rm -f $fn"

	echo $fn
}

function SSH_WAIT_READY {
	sleep 10s
	while ! SSH_CMD $1 $2; do
		sleep 5s
	done
}

function SETUP_BRIDGE {
	sudo ip -B link | grep " $BRIDGE_NAME:" >/dev/null && sudo ip link del $BRIDGE_NAME type bridge
	sudo ip link add $BRIDGE_NAME type bridge
	sudo ip addr add $BRIDGE_IP broadcast $BRIDGE_BRD dev $BRIDGE_NAME
	sudo ip link set dev $BRIDGE_NAME up
}

function SETUP_TAP {
	if ip tuntap list | grep $TAP_NAME$1 >/dev/null; then
		sudo ip link set dev $TAP_NAME$1 nomaster
		sudo ip link set dev $TAP_NAME$1 down
		sudo ip tuntap del dev $TAP_NAME$1 mod tap
	fi
	sudo ip tuntap add dev $TAP_NAME$1 mod tap
	sudo ip link set dev $TAP_NAME$1 up
	sudo ip link set dev $TAP_NAME$1 master $BRIDGE_NAME
}

SETUP_BRIDGE

hostc=$QEMU_HOST
echo Setup $hostc host

FREE_PORT=12055
FREE_PORT_FIRST=
FREE_IP=$TAP_IP_START
FREE_MAC=0
for ((hostn=0; hostn<$hostc; hostn++)); do
	screen -ls | grep $SCREEN_SNAME$hostn >/dev/null && screen -X -S $SCREEN_SNAME$hostn quit
	sleep 1s

	qemu-img create -f qcow2 -F qcow2 -b $QEMU_QCOW2 $QEMU_IMG$hostn.qcow2 >/dev/null
	#if [[ "$hostn" == "0" ]]; then
		for ((di=1; di<=$QEMU_DISK_ADD; di++)); do
			qemu-img create -f qcow2 $QEMU_DISK$hostn-$di.qcow2 500M
		done
	#fi

	while netstat -anp 2>&1 | grep :$FREE_PORT >/dev/null; do
		((FREE_PORT++))
	done
	if [[ "$hostn" == "0" ]]; then
		FREE_PORT_FIRST=$FREE_PORT
	fi

	tapn=$TAP_NAME$hostn
	((nt=hostn+9))
	tapnn=$TAP_NAME$nt
	qemu_com="qemu-system-riscv64 -nographic -machine virt -cpu rv64,sv39=on "
	qemu_com=$qemu_com"-smp $QEMU_SMP -m ${QEMU_MEM}G "
	qemu_com=$qemu_com"-bios $QEMU_BIOS "
	qemu_com=$qemu_com"-audiodev pa,id=snd0 "
	qemu_com=$qemu_com"-drive file=$QEMU_IMG$hostn.qcow2,format=qcow2,id=hd0,if=none "
	qemu_com=$qemu_com"-object rng-random,filename=/dev/urandom,id=rng0 "
	qemu_com=$qemu_com"-device qemu-xhci -usb -device usb-kbd -device usb-tablet -device usb-audio,audiodev=snd0 "
	qemu_com=$qemu_com"-device virtio-rng-device,rng=rng0 -device virtio-blk-device,drive=hd0 "
	qemu_com=$qemu_com"-netdev tap,id=net$tapn,ifname=$tapn,script=no,downscript=no -device virtio-net-pci,netdev=net$tapn,mac="`printf "$QEMU_MAC%02x" $FREE_MAC`" "
	SETUP_TAP $FREE_MAC
	#SETUP_TAP $nt
	#((FREE_MAC++))
	#qemu_com=$qemu_com"-netdev tap,id=net$tapnn,ifname=$tapnn,script=no,downscript=no -device virtio-net-pci,netdev=net$tapnn,mac="`printf "$QEMU_MAC%02x" $FREE_MAC`" "
	((FREE_MAC++))
	qemu_com=$qemu_com"-netdev user,id=usernet,hostfwd=tcp::$FREE_PORT-:22 -device virtio-net-pci,netdev=usernet,mac="`printf "$QEMU_MAC%02x" $FREE_MAC`" "
	SETUP_TAP $FREE_MAC
	((FREE_MAC++))
	#if [[ "$hostn" == "0" ]]; then
		for ((di=1; di<=$QEMU_DISK_ADD; di++)); do
			qemu_com=$qemu_com"-drive file=$QEMU_DISK$hostn-$di.qcow2,format=qcow2,id=hd$hostn-$di,if=none -device virtio-blk-pci,drive=hd$hostn-$di "
		done
	#fi

	echo $qemu_com
	screen -S $SCREEN_SNAME$hostn -d -m $qemu_com
	sleep 1s
	if ! screen -ls | grep $SCREEN_SNAME$hostn >/dev/null; then
		echo Qemu command failed -- $qemu_com
		for ((k=0; k<$hostn; k++)); do
			screen -X -S $SCREEN_SNAME$k quit
		done
		exit -1
	fi

	SSH_WAIT_READY $FREE_PORT $QEMU_PASSWD

	tmpf=$(SSH_CMD_OUT $FREE_PORT $QEMU_PASSWD "lshw -class network | grep -A 5 'description: Ethernet interface' | grep 'logical name:' | awk '{print \\\$NF}' | grep -v 'lo'")
	if [ -e $tmpf ]; then
		nic=$(head -n 1 $tmpf)
		echo Config machine $hostn nic name $nic
		SSH_CMD $FREE_PORT $QEMU_PASSWD "nmcli c a type Ethernet con-name $nic ifname $nic"
		SSH_CMD $FREE_PORT $QEMU_PASSWD "nmcli c m $nic ipv4.address "`printf "$TAP_IP%d" $FREE_IP`"/24"
		SSH_CMD $FREE_PORT $QEMU_PASSWD "nmcli c m $nic ipv4.gateway $BRIDGE_IP"
		SSH_CMD $FREE_PORT $QEMU_PASSWD "nmcli c m $nic ipv4.method manual"
		SSH_CMD $FREE_PORT $QEMU_PASSWD "nmcli c up $nic"
		SSH_CMD $FREE_PORT $QEMU_PASSWD "rm -f /root/mugen/conf/env.conf"
		SSH_CMD $FREE_PORT $QEMU_PASSWD "bash /root/mugen/mugen.sh -c --user root --password $QEMU_PASSWD --ip "`printf "$TAP_IP%d" $FREE_IP`
		((FREE_IP++))
		rm $tmpf
	else
		echo Cannot config tap
		echo Device info $tmpf not exists
		for ((k=0; k<=$hostn; k++)); do
			screen -X -S $SCREEN_SNAME$k quit
		done
		exit -1
	fi
done

for ((ip=$TAP_IP_START+1; ip<$FREE_IP; ip++)); do
	SSH_CMD $FREE_PORT_FIRST $QEMU_PASSWD "bash /root/mugen/mugen.sh -c --user root --password $QEMU_PASSWD --ip "`printf "$TAP_IP%d" $ip`
done

