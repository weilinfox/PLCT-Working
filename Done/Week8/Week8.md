# Week 8 工作报告

+ 从所有未分析的测试 [pickedFail.csv](https://github.com/KotorinMinami/task_apply/blob/main/pickedFail.csv) 中筛选 baseOS fail 的测试进行分析并提交分析结果，共计 75 个测试用例。其中有 2 个更改状态为 x86 fail ； 18 个与测试环境、超时时间有关，需要手动重测重新分析。在这些重测的里面，有 11 个经过重测通过了
+ [rest3](https://github.com/KotorinMinami/res_list/blob/master/NeedTest/rest3) 似乎是无人认领的状态，需要进行测试

## 遇到的问题

+ 在分析 log 的时候发现，在 riscv 上没有出现的测试环境问题，在 x86 测试的出现了，是否要将 qemu_test.py 更改为同时支持 riscv 和 x86 的
+ ``os-basic`` 的 ``oe_test_chsh`` 、 ``oe_test_lastb`` 和 ``oe_test_xzcmp`` 测试脚本需要测试环境默认语言为中文，体现为使用 ``grep`` 过滤中文文本
+ ``javapackages-tools`` 没看明白
+ samba 无法正确加载动态链接库的问题，这些链接库均在 ``/usr/lib64/samba`` 目录，但是用 ``strace smbd`` 跟踪发现有部分该目录的链接库没有被加载
   ```
   openat(AT_FDCWD, "/usr/lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
   read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0\363\0\1\0\0\0\300m\2\0\0\0\0\0"..., 832) = 832
   newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=1616792, ...}, AT_EMPTY_PATH) = 0
   mmap(NULL, 1659064, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x3f91f4e000
   mprotect(0x3f920d1000, 4096, PROT_NONE) = 0
   mmap(0x3f920d2000, 20480, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x183000) = 0x3f920d2000
   mmap(0x3f920d7000, 49336, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x3f920d7000
   close(3)                                = 0
   openat(AT_FDCWD, "/usr/lib64/samba/libutil-reg-samba4.so", O_RDONLY|O_CLOEXEC) = 3
   read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\363\0\1\0\0\0P\t\0\0\0\0\0\0"..., 832) = 832
   newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=10136, ...}, AT_EMPTY_PATH) = 0
   mmap(NULL, 12408, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x3f91f4a000
   mprotect(0x3f91f4b000, 4096, PROT_NONE) = 0
   mmap(0x3f91f4c000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1000) = 0x3f91f4c000
   close(3)                                = 0
   openat(AT_FDCWD, "/usr/lib64/samba/libCHARSET3-samba4.so", O_RDONLY|O_CLOEXEC) = 3
   read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\363\0\1\0\0\0\360\r\0\0\0\0\0\0"..., 832) = 832
   newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=10168, ...}, AT_EMPTY_PATH) = 0
   mmap(NULL, 12520, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x3f91f46000
   mmap(0x3f91f48000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1000) = 0x3f91f48000
   close(3)                                = 0
   openat(AT_FDCWD, "/usr/lib64/libtdb.so.1", O_RDONLY|O_CLOEXEC) = 3
   read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\363\0\1\0\0\0\2407\0\0\0\0\0\0"..., 832) = 832
   newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=96792, ...}, AT_EMPTY_PATH) = 0
   mmap(NULL, 99104, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x3f91f2d000
   mmap(0x3f91f44000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x16000) = 0x3f91f44000
   close(3)                                = 0
   openat(AT_FDCWD, "/usr/lib64/libndr.so.3", O_RDONLY|O_CLOEXEC) = 3
   read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\363\0\1\0\0\0Pm\0\0\0\0\0\0"..., 832) = 832
   newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=117896, ...}, AT_EMPTY_PATH) = 0
   mmap(NULL, 120176, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x3f91f0f000
   mprotect(0x3f91f2a000, 4096, PROT_NONE) = 0
   mmap(0x3f91f2b000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b000) = 0x3f91f2b000
   close(3)                                = 0
   openat(AT_FDCWD, "/lib64/lp64d/tls/libmessages-util-samba4.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   newfstatat(AT_FDCWD, "/lib64/lp64d/tls", 0x3feb0901e0, 0) = -1 ENOENT (No such file or directory)
   openat(AT_FDCWD, "/lib64/lp64d/libmessages-util-samba4.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   newfstatat(AT_FDCWD, "/lib64/lp64d", {st_mode=S_IFDIR|0555, st_size=36864, ...}, 0) = 0
   openat(AT_FDCWD, "/usr/lib64/lp64d/tls/libmessages-util-samba4.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   newfstatat(AT_FDCWD, "/usr/lib64/lp64d/tls", 0x3feb0901e0, 0) = -1 ENOENT (No such file or directory)
   openat(AT_FDCWD, "/usr/lib64/lp64d/libmessages-util-samba4.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
   newfstatat(AT_FDCWD, "/usr/lib64/lp64d", {st_mode=S_IFDIR|0555, st_size=36864, ...}, 0) = 0
   mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x3f91f0d000
   writev(2, [{iov_base="smbd", iov_len=4}, {iov_base=": ", iov_len=2}, {iov_base="error while loading shared libra"..., iov_len=36}, {iov_base=": ", iov_len=2}, {iov_base="libmessages-util-samba4.so", iov_len=26}, {iov_base=": ", iov_len=2}, {iov_base="cannot open shared object file", iov_len=30}, {iov_base=": ", iov_len=2}, {iov_base="No such file or directory", iov_len=25}, {iov_base="\n", iov_len=1}], 10smbd: error while loading shared libraries: libmessages-util-samba4.so: cannot open shared object file: No such file or directory
   ) = 130
   exit_group(127)                         = ?
   +++ exited with 127 +++
   ```
