# oe_test_target_iprutils

测试套问题， x86 和 riscv 失败原因一致

测试套测试 iprutils.target ，该 daemon 由 iprutils 软件包提供，而测试脚本没有显式安装， x86 和 riscv 镜像也没有预装

```
+ systemctl restart iprutils.target
Failed to restart iprutils.target: Unit iprutils.target not found.
```
