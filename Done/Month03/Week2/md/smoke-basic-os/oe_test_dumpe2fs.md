# oe_test_dumpe2fs

riscv 和 x86 失败原因一致，mke2fs 报错，无法在上面创建文件 inode

```
+ mke2fs /tmp/dumpe2fs_100k -F
mke2fs 1.47.0 (5-Feb-2023)
Discarding device blocks:   0/100       done
Creating filesystem with 100 1k blocks and 8 inodes

Allocating group tables: 0/1   done
Writing inode tables: 0/1   done
ext2fs_mkdir: Could not allocate inode in ext2 filesystem while creating /lost+found
```
