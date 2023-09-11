# openKylin RISC-V 0.9.5 版本测试报告

#### 介绍

本报告主要内容为对 openKylin RISC-V 0.9.5 版本进行测试的结果统计与错误分析。

#### 测试版本说明

本文档测试对象是于2023年1月12日发布的 openKylin RISC-V 0.9.5 版本。

#### 测试环境

在现有的测试条件下选择了以下三种环境进行测试：

| 硬件/QEMU | 硬件配置信息 |
| ----------------------------------- | ------------------------------------------------------------ |
| HiFive Unmatched | CPU: SiFive Freedom U740 SoC <br/>内存：16GB DDR4<br/>存储设备：SanDisk Ultra 32GB micro SD |
| VisionFive | CPU: JH7100 <br />内存：8GB DDR4<br />存储设备：SanDisk Ultra 32GB micro SD |
| Qemu 7.2 | CPU: 8<br />内存：8GB <br />存储设备：文件 |

#### 系统安装

- [基于官方文档优化后的QEMU安装教程](https://gitee.com/jammyjellyfish/openkylin-qemu-unmatched)

- [Visionfive官方安装教程](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

- [Unmatched官方安装教程](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

#### 测试计划

本次openKylin RISC-V 0.9.5 版本测试分为系统和重要组件测试与自动化测试。其中系统和重要组件测试根据收到的测试要求对 MYSQL 与 Python 进行了基本功能验证以及相关的脚本自动化单元测试，系统组件测试进行手动验证能否正常使用。自动化测试方面使用 autopkgtest 测试框架，对仓库中的所有软件包进行自动化测试。

#### 测试结果

- [自动化测试结果](./自动化测试)

- [系统和重要组件测试结果](系统和组件测试)

- [Visionfive测试结果](开发板测试/Visionfive)

- [Unmatched测试结果](开发板测试/Unmached)

#### 测试结论

openKylin RISC-V 0.9.5 版本按照第三测试小队的测试计划，在三种不同测试环境下进行了测试。 Visionfive 开发板上发现缺陷 5 个，Unmatched 开发板上发现缺陷 3 个，QEMU 中发现缺陷 12 个，总计缺陷 20 个。

| 缺陷名称 | 测试环境 | 缺陷说明 |
| ------- | ------- | -------- |
| 计算器取反运算 | Qemu |          |
| 计算器取相反数运算 | Qemu |          |
| 计算器显示二进制 | Qemu |          |
| 检查更新 | Qemu  |          |
| 设置时区 | Qemu |          |
| 系统升级失败 | VisionFive |          |
| 天气联网错误 | VisionFive |          |
| 不支持无线网卡 | VisionFive |          |
| 浏览器开bilibili视频打失败 | VisionFive |          |
| 浏览器不支持HTML5播放器 | VisionFive |          |
| 打开链接的网页错误 | VisionFive |          |
| 浏览器启动闪退 | Unmatched |          |
| 输入法快捷键切换失败 | Unmatched |          |
| 屏幕截图失灵 | Unmatched |          |

#### 自动化测试

- 测试范围：openKylin镜像提供的仓库中所有的软件包共40925个，其中28873个软件在仓库中无源码， 3786个软件在源码中无法解压出测试套，剩余软件为本次测试的讨论及测试范围，其中共872个测试套数，共2030个测试例。

- 测试框架：autopkgtest

- 测试方式：获取镜像中提供的软件仓中的源码，并对其运行autopkgtest -- qemu的测试，测试过程中autopkgtest会自动归类错误，备份镜像环境等。

- [详细测试结果](./自动化测试/readme.md)

- 测试结论：本次测试总共扫描了40925个软件包，其中进行了有效测试的包有872个，测试例共2030个，通过973个，失败1057个。
