#!/usr/bin/env bash

# The script is created for starting a riscv64 qemu virtual machine with specific parameters.

RESTORE=$(echo -en '\001\033[0m\002')
YELLOW=$(echo -en '\001\033[00;33m\002')

## Configuration
vcpu=8
memory=8
memory_append=`expr $memory \* 1024`
drive="mugen_ready.qcow2"
#fw="fw_payload_oe_uboot_2304.bin"
kernel="vmlinuz"
initrd="initrd.img"
ssh_port=12055

cmd="qemu-system-x86_64 \
  -nographic -machine pc -accel kvm \
  -smp "$vcpu" -m "$memory"G \
  -kernel "$kernel" \
  -initrd "$initrd" \
  -append 'root=/dev/vda2 rw console=ttyS0 swiotlb=1 loglevel=3 systemd.default_timeout_start_sec=600 selinux=0 highres=off earlycon'
  -drive file="$drive",format=qcow2,id=hd0,if=none \
  -object rng-random,filename=/dev/urandom,id=rng0 \
  -device virtio-vga \
  -device virtio-rng,rng=rng0 \
  -device virtio-blk,drive=hd0 \
  -device virtio-net,netdev=usernet \
  -netdev user,id=usernet,hostfwd=tcp::"$ssh_port"-:22 \
  -device qemu-xhci -usb -device usb-kbd -device usb-tablet"

echo ${YELLOW}:: Starting VM...${RESTORE}
echo ${YELLOW}:: Using following configuration${RESTORE}
echo ""
echo ${YELLOW}vCPU Cores: "$vcpu"${RESTORE}
echo ${YELLOW}Memory: "$memory"G${RESTORE}
echo ${YELLOW}Disk: "$drive"${RESTORE}
echo ${YELLOW}SSH Port: "$ssh_port"${RESTORE}
echo ""
echo ${YELLOW}:: NOTE: Make sure ONLY ONE .qcow2 file is${RESTORE}
echo ${YELLOW}in the current directory${RESTORE}
echo ""
echo ${YELLOW}:: Tip: Try setting DNS manually if QEMU user network doesn\'t work well. ${RESTORE}
echo ${YELLOW}:: HOWTO -\> https://serverfault.com/a/810639 ${RESTORE}
echo ""
echo ${YELLOW}:: Tip: If \'ping\' reports permission error, try reinstalling \'iputils\'. ${RESTORE}
echo ${YELLOW}:: HOWTO -\> \'sudo dnf reinstall iputils\' ${RESTORE}
echo ""

sleep 2

eval $cmd
