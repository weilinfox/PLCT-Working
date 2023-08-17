# fw_payload.elf

+ https://github.com/u-boot/u-boot/blob/master/doc/board/emulation/qemu-riscv.rst
+ https://github.com/ArielHeleneto/Work-PLCT/blob/master/help/build-uboot.md
+ https://github.com/ArielHeleneto/Work-PLCT/blob/master/help/build-opensbi.md

```bash
git clone https://github.com/u-boot/u-boot.git
git clone https://github.com/riscv/opensbi.git
cd u-boot

make CROSS_COMPILE=riscv64-linux-gnu- qemu-riscv64_smode_defconfig
make CROSS_COMPILE=riscv64-linux-gnu- -j12

cd ../opensbi
make CROSS_COMPILE=riscv64-linux-gnu- PLATFORM=generic FW_PAYLOAD_PATH=../u-boot/u-boot.bin -j12
file build/platform/generic/firmware/fw_payload.elf
```
