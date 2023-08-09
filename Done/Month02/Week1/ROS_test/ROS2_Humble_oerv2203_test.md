# ROS2 Humble 在 openEuler 22.03 riscv64 架构上的测试

## 环境信息

### 硬件信息：
1. QEMU openEuler riscv64 虚拟机，QEMU emulator version 8.0.2
2. 处理器 smp 4
3. 内存 4GB

### 软件信息
1. OS 版本：openEuler-22.03-V2-base-qemu-preview
2. 镜像地址：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-22.03-V2-riscv64/QEMU/openEuler-22.03-V2-base-qemu-preview.qcow2.tar.zst
3. 软件源：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-22.03-V2-riscv64/repo/

### 虚拟机启动脚本

见 [start_vm.sh](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-22.03-V2-riscv64/QEMU/start_vm.sh)

## 安装和卸载测试

### 修改软件源

添加以下内容到 /etc/yum.repos.d/ROS.repo

```
[openEulerROS-humble]
name=openEulerROS-humble
baseurl=http://123.60.74.95:3389/home:/Z572:/ros/openEuler_22.03_22.03/
enabled=1
gpgcheck=0
```

安装前请先安装 4 个不在 oerv 2203 默认源里，但在 2203 obs 工程 repo 里的依赖包，包的下载 url 如下，请下载到同一目录后使用 ``dnf install ./*.rpm`` 安装

>http://123.60.74.95:3389/openEuler:/22.03:/Epol/22.03/riscv64/glog-0.3.5-1.oe2203.riscv64.rpm
>http://123.60.74.95:3389/openEuler:/22.03:/Epol/22.03/riscv64/glog-devel-0.3.5-1.oe2203.riscv64.rpm
>http://123.60.74.95:3389/openEuler:/22.03/22.03/riscv64/suitesparse-5.10.1-2.oe2203.riscv64.rpm
>http://123.60.74.95:3389/openEuler:/22.03/22.03/riscv64/suitesparse-devel-5.10.1-2.oe2203.riscv64.rpm

### 安装

安装 ros humble 组件时请安装 [packages.list](./packages.list) 中列出的包，目前 rv 上的 packages.list 共计有 1502 包

在 `packages.list` 文件所在目录执行以下命令

```bash
dnf install -y `cat packages.list`
```

安装出错，完整日志见 [yum_install_list.log](./log/yum_install_list.log)

### 卸载

执行以下命令卸载 `packages.list` 中所列软件

```bash
dnf remove -y `cat packages.list`
```

~~命令正常执行，所有软件包被卸载。~~

### 使用 yum 安装所有 ros-humble-* 包

```bash
yum insatll ros-humble-* -y
```

安装报错，完整日志见 [yum_install.log](./logs/yum_install.log)

## 功能测试

安装上述软件列表后，编辑 `~/.bashrc` 追加以下内容

```bash
source /opt/ros/humble/setup.sh
```

## 测试 colcon 编译工具相关功能

`colcon` 工具尚未打包，可以通过 `pip` 安装并进行测试，依次执行下列命令

```bash
# 新建并激活 python 虚拟环境
python3 -m venv pyenv
source pyenv/bin/activate
# 安装 colcon
pip install colcon-common-extensions
# 新建工作区并切换到此目录
mkdir -p ~/workspace/src
cd ~/workspace
# 测试编译，检查输出
colcon build
ls
```

输出如图，测试通过

![image-20230630182559035](./img/image-20230630182559035.png)

## 测试 ros 基础工具相关功能

#### 1. ros2 topic 工具

执行  `ros2 topic list`，输出如下，测试通过

![image-20230630182659250](./img/image-20230630182659250.png)

#### 2. ros2 param 工具

分别执行命令 `ros2 run demo_nodes_cpp talker`, `ros2 param list`，输出如下，测试通过

![image-20230630182823849](./img/image-20230630182823849.png)

#### 3. ros2 service 工具

分别执行命令 `ros2 run demo_nodes_cpp talker`, `ros2 service list`，输出如下，测试通过

![image-20230630182851430](./img/image-20230630182851430.png)

#### 4. ros2 node 工具

分别执行命令 `ros2 run demo_nodes_cpp talker`, `ros2 node list`，输出如下，测试通过

![image-20230630182921466](./img/image-20230630182921466.png)

#### 5. ros2 bag 工具

1. record 测试

   输入 `ros2 bag record -a`, 输出如下

   ![image-20230630183038863](./img/image-20230630183038863.png)

   检查当前目录，如下，测试通过

   ![image-20230630183055319](./img/image-20230630183055319.png)

2. info 测试

   输入 `ros2 bag info rosbag2_2023_06_30-10_30_30`（与前文录制时创建目录一致）,输出如下，测试通过

   ![image-20230630183116660](./img/image-20230630183116660.png)

3. play 测试

   输入 `ros2 bag play rosbag2_2023_06_30-10_30_30`（与前文录制时创建目录一致）输出如下，测试通过

   ![image-20230630183139960](./img/image-20230630183139960.png)

#### 6. ros2 launch 工具

输入 `ros2 launch demo_nodes_cpp talker_listener.launch.py`，输出如下，测试通过

![image-20230630183206722](./img/image-20230630183206722.png)

## 测试 ros 通信组件相关功能

### topic 通讯

#### c++ 实现

分别执行 `ros2 run demo_nodes_cpp talker` 和 `ros2 run demo_nodes_cpp listener`，输出如下，测试通过

![image-20230630183248492](./img/image-20230630183248492.png)

#### python 实现

分别执行 `ros2 run demo_nodes_py talker` 和 `ros2 run demo_nodes_py listener`，输出如下，测试通过

![image-20230630183318255](./img/image-20230630183318255.png)

### service 通信

#### c++ 实现

分别执行 `ros2 run demo_nodes_cpp add_two_ints_server` 和 `ros2 run demo_nodes_cpp add_two_ints_client`，输出如下，测试通过

![image-20230630183344529](./img/image-20230630183344529.png)

#### python 实现

分别在两个终端执行 `ros2 run demo_nodes_py add_two_ints_server` 和 `ros2 run demo_nodes_py add_two_ints_client`，输出如下，测试通过

![image-20230630183405836](./img/image-20230630183405836.png)

## 测试 ros 坐标转换相关功能

### 坐标转换的发布和订阅

分别在两个终端执行 `ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom` 和 `ros2 run tf2_ros tf2_echo base_link odom`，输出如下，测试通过

![image-20230630183435462](./img/image-20230630183435462.png)

### tf_monitor 监控

分别在两个终端执行 `ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom` 和 `ros2 run tf2_ros tf2_monitor`，输出如下，测试通过

### ![image-20230630183510730](./img/image-20230630183510730.png)view_frames 保存 pdf

分别在两个终端执行 `ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom` 和 `ros2 run tf2_tools view_frames`，输出如下

![image-20230630183554705](./img/image-20230630183554705.png)

检查当前目录，存在 pdf 文件，测试通过

![image-20230630183607833](./img/image-20230630183607833.png)
