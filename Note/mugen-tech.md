# make life better —— mugen 自动化测试脚本的改进

## 我们为什么要使用 mugen

官方的介绍

mugen 是 openEuler 社区开放的测试框架，提供公共配置和方法以便社区开发者进行测试代码的编写和执行

当前的角色

mugen 具有一系列开源的测试套和测试用例，大部分测试套对一个软件包或一种功能进行测试，也有专门的测试套是对测试环境的整体功能进行全面测试。 mugen 是 openEuler 上游比较重视的测试之一，其测试结果是软件包质量的一个体现。

## 用最简单的方式使用 mugen

openEuler RISC-V 2309 一共进行的 Round1-Round4 四次针对 bashOS 的 mugen 测试中， Round1 一共测试了 273 个测试套， 2120 个测试用例。

由于测试套数量众多，最简单的方法就是跑一个循环

```bash
for t in $(cat mylist); do
    bash mugen.sh -f $t -x
done
```

这样运行 mugen 测试有两个问题：

+ 一些 mugen 测试会对测试环境的软件包、网络配置、 systemd daemon 进行一系列操作，且不见得能还原
+ 不同 mugen 测试要求的磁盘数量、测试机数量、网卡数量并不相同

显然简单使用上面的脚本无法实现测试套之间测试环境的统一，实际上也是无法完成所有测试的

## 测试环境的搭建



