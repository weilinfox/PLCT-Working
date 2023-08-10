# ROS2 Humble 在 openEuler 22.03 riscv64 架构上的测试

1. 无法 ``yum insatll ros-humble-* -y`` 安装
2. ros2 bag 工具测试失败，段错误

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

+ [http://123.60.74.95:3389/openEuler:/22.03:/Epol/22.03/riscv64/glog-0.3.5-1.oe2203.riscv64.rpm](http://123.60.74.95:3389/openEuler:/22.03:/Epol/22.03/riscv64/glog-0.3.5-1.oe2203.riscv64.rpm)
+ [http://123.60.74.95:3389/openEuler:/22.03:/Epol/22.03/riscv64/glog-devel-0.3.5-1.oe2203.riscv64.rpm](http://123.60.74.95:3389/openEuler:/22.03:/Epol/22.03/riscv64/glog-devel-0.3.5-1.oe2203.riscv64.rpm)
+ [http://123.60.74.95:3389/openEuler:/22.03/22.03/riscv64/suitesparse-5.10.1-2.oe2203.riscv64.rpm](http://123.60.74.95:3389/openEuler:/22.03/22.03/riscv64/suitesparse-5.10.1-2.oe2203.riscv64.rpm)
+ [http://123.60.74.95:3389/openEuler:/22.03/22.03/riscv64/suitesparse-devel-5.10.1-2.oe2203.riscv64.rpm](http://123.60.74.95:3389/openEuler:/22.03/22.03/riscv64/suitesparse-devel-5.10.1-2.oe2203.riscv64.rpm)

### 安装

安装 ros humble 组件时请安装 [packages.list](./packages.list) 中列出的包，目前 rv 上的 packages.list 共计有 1502 包

在 `packages.list` 文件所在目录执行以下命令

```bash
dnf install -y `cat packages.list`
```

安装没有出错，完整日志见 [yum_install_list.log](./log/yum_install_list.log)

### 卸载

执行以下命令卸载 `packages.list` 中所列软件

```bash
dnf remove -y `cat packages.list`
```

命令正常执行，所有软件包被卸载。

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

### 测试 colcon 编译工具相关功能

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

测试通过，输出见 [colcon.log](./log/colcon.log)

### 测试 ros 基础工具相关功能

#### 1. ros2 topic 工具

执行  `ros2 topic list`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 topic list
/parameter_events
/rosout
```

#### 2. ros2 param 工具

分别执行命令 `ros2 run demo_nodes_cpp talker`, `ros2 param list`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run demo_nodes_cpp talker
[INFO] [1691630003.915591546] [talker]: Publishing: 'Hello World: 1'
[INFO] [1691630004.912966662] [talker]: Publishing: 'Hello World: 2'
[INFO] [1691630005.912955086] [talker]: Publishing: 'Hello World: 3'
[INFO] [1691630006.913013304] [talker]: Publishing: 'Hello World: 4'
[INFO] [1691630007.913234916] [talker]: Publishing: 'Hello World: 5'
[INFO] [1691630008.914177525] [talker]: Publishing: 'Hello World: 6'
[INFO] [1691630009.914237423] [talker]: Publishing: 'Hello World: 7'
[INFO] [1691630010.914352715] [talker]: Publishing: 'Hello World: 8'
[INFO] [1691630011.914342299] [talker]: Publishing: 'Hello World: 9'
[INFO] [1691630012.913256171] [talker]: Publishing: 'Hello World: 10'
[INFO] [1691630013.913114440] [talker]: Publishing: 'Hello World: 11'
[INFO] [1691630014.912934803] [talker]: Publishing: 'Hello World: 12'
[INFO] [1691630015.912949160] [talker]: Publishing: 'Hello World: 13'
[INFO] [1691630016.913110611] [talker]: Publishing: 'Hello World: 14'
[INFO] [1691630017.913122155] [talker]: Publishing: 'Hello World: 15'
[INFO] [1691630018.913117192] [talker]: Publishing: 'Hello World: 16'
[INFO] [1691630019.913179723] [talker]: Publishing: 'Hello World: 17'
[INFO] [1691630020.913298847] [talker]: Publishing: 'Hello World: 18'
[INFO] [1691630021.913097963] [talker]: Publishing: 'Hello World: 19'
[INFO] [1691630022.912947373] [talker]: Publishing: 'Hello World: 20'
[INFO] [1691630023.912964077] [talker]: Publishing: 'Hello World: 21'
[INFO] [1691630024.914206982] [talker]: Publishing: 'Hello World: 22'
[INFO] [1691630025.914090272] [talker]: Publishing: 'Hello World: 23'
[INFO] [1691630026.914458759] [talker]: Publishing: 'Hello World: 24'
[INFO] [1691630027.914437837] [talker]: Publishing: 'Hello World: 25'
[INFO] [1691630028.914149106] [talker]: Publishing: 'Hello World: 26'
[INFO] [1691630029.914132771] [talker]: Publishing: 'Hello World: 27'
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 param list
/talker:
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  use_sim_time
```

#### 3. ros2 service 工具

分别执行命令 `ros2 run demo_nodes_cpp talker`, `ros2 service list`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run demo_nodes_cpp talker
[INFO] [1691630105.045557033] [talker]: Publishing: 'Hello World: 1'
[INFO] [1691630106.034633281] [talker]: Publishing: 'Hello World: 2'
[INFO] [1691630107.034176579] [talker]: Publishing: 'Hello World: 3'
[INFO] [1691630108.034496475] [talker]: Publishing: 'Hello World: 4'
[INFO] [1691630109.034530065] [talker]: Publishing: 'Hello World: 5'
[INFO] [1691630110.033011540] [talker]: Publishing: 'Hello World: 6'
[INFO] [1691630111.032993918] [talker]: Publishing: 'Hello World: 7'
[INFO] [1691630112.033138391] [talker]: Publishing: 'Hello World: 8'
[INFO] [1691630113.033120958] [talker]: Publishing: 'Hello World: 9'
[INFO] [1691630114.033106220] [talker]: Publishing: 'Hello World: 10'
[INFO] [1691630115.032989875] [talker]: Publishing: 'Hello World: 11'
[INFO] [1691630116.033043726] [talker]: Publishing: 'Hello World: 12'
[INFO] [1691630117.033038171] [talker]: Publishing: 'Hello World: 13'
[INFO] [1691630118.033304011] [talker]: Publishing: 'Hello World: 14'
[INFO] [1691630119.033489946] [talker]: Publishing: 'Hello World: 15'
[INFO] [1691630120.033319174] [talker]: Publishing: 'Hello World: 16'
[INFO] [1691630121.033166397] [talker]: Publishing: 'Hello World: 17'
[INFO] [1691630122.034066819] [talker]: Publishing: 'Hello World: 18'
[INFO] [1691630123.034352633] [talker]: Publishing: 'Hello World: 19'
[INFO] [1691630124.034290640] [talker]: Publishing: 'Hello World: 20'
[INFO] [1691630125.033949339] [talker]: Publishing: 'Hello World: 21'
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 service list
/talker/describe_parameters
/talker/get_parameter_types
/talker/get_parameters
/talker/list_parameters
/talker/set_parameters
/talker/set_parameters_atomically
```

#### 4. ros2 node 工具

分别执行命令 `ros2 run demo_nodes_cpp talker`, `ros2 node list`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run demo_nodes_cpp talker
[INFO] [1691630174.616271611] [talker]: Publishing: 'Hello World: 1'
[INFO] [1691630175.610126023] [talker]: Publishing: 'Hello World: 2'
[INFO] [1691630176.610311661] [talker]: Publishing: 'Hello World: 3'
[INFO] [1691630177.610734495] [talker]: Publishing: 'Hello World: 4'
[INFO] [1691630178.608985814] [talker]: Publishing: 'Hello World: 5'
[INFO] [1691630179.609012637] [talker]: Publishing: 'Hello World: 6'
[INFO] [1691630180.608999755] [talker]: Publishing: 'Hello World: 7'
[INFO] [1691630181.608988567] [talker]: Publishing: 'Hello World: 8'
[INFO] [1691630182.608965375] [talker]: Publishing: 'Hello World: 9'
[INFO] [1691630183.609191080] [talker]: Publishing: 'Hello World: 10'
[INFO] [1691630184.609047378] [talker]: Publishing: 'Hello World: 11'
[INFO] [1691630185.609097071] [talker]: Publishing: 'Hello World: 12'
[INFO] [1691630186.609008760] [talker]: Publishing: 'Hello World: 13'
[INFO] [1691630187.609117245] [talker]: Publishing: 'Hello World: 14'
[INFO] [1691630188.609166424] [talker]: Publishing: 'Hello World: 15'
[INFO] [1691630189.609188799] [talker]: Publishing: 'Hello World: 16'
[INFO] [1691630190.610270174] [talker]: Publishing: 'Hello World: 17'
[INFO] [1691630191.610322740] [talker]: Publishing: 'Hello World: 18'
[INFO] [1691630192.610414701] [talker]: Publishing: 'Hello World: 19'
[INFO] [1691630193.610407957] [talker]: Publishing: 'Hello World: 20'
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 node list
/talker
```

#### 5. ros2 bag 工具

1. record 测试

   输入 `ros2 bag record -a`, 输出如下

   ```bash
   (pyenv) [root@openEuler-riscv64 workspace]# ros2 bag record -a
   [INFO] [1691630232.600829606] [rosbag2_recorder]: Press SPACE for pausing/resuming
   [INFO] [1691630232.712627428] [rosbag2_storage]: Opened database 'rosbag2_2023_08_10-09_17_11/rosbag2_2023_08_10-09_17_11_0.db3' for READ_WRITE.
   [INFO] [1691630232.717141450] [rosbag2_recorder]: Event publisher thread: Starting
   [INFO] [1691630232.730792713] [rosbag2_recorder]: Listening for topics...
   Segmentation fault (core dumped)
   (pyenv) [root@openEuler-riscv64 workspace]# echo $?
   139
   ```

   检查当前目录，如下，测试失败

   ```bash
   (pyenv) [root@openEuler-riscv64 workspace]# ls
   rosbag2_2023_08_10-09_17_11
   (pyenv) [root@openEuler-riscv64 workspace]# ls rosbag2_2023_08_10-09_17_11/
   rosbag2_2023_08_10-09_17_11_0.db3
   ```

2. info 测试

   输入 `ros2 bag info rosbag2_2023_08_10-09_17_11`（与前文录制时创建目录一致）,输出如下，测试失败

   ```bash
   (pyenv) [root@openEuler-riscv64 workspace]# ros2 bag info rosbag2_2023_08_10-09_17_11
   Could not find metadata in bag directory rosbag2_2023_08_10-09_17_11
   ```

3. play 测试

   输入 `ros2 bag play rosbag2_2023_08_10-09_17_11`（与前文录制时创建目录一致）输出如下，测试失败

   ```bash
   (pyenv) [root@openEuler-riscv64 workspace]# ros2 bag play rosbag2_2023_08_10-09_17_11

   closing.

   closing.
   [ERROR] [1691630455.300943759] [rosbag2_storage]: No storage id specified, and no plugin found that could open URI
   No storage could be initialized from the inputs.
   ```

#### 6. ros2 launch 工具

输入 `ros2 launch demo_nodes_cpp talker_listener.launch.py`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 launch demo_nodes_cpp talker_listener.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2023-08-10-09-21-42-036963-openEuler-riscv64-14532
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [14533]
[INFO] [listener-2]: process started with pid [14535]
[talker-1] [INFO] [1691630508.120243068] [talker]: Publishing: 'Hello World: 1'
[listener-2] [INFO] [1691630508.157358707] [listener]: I heard: [Hello World: 1]
[talker-1] [INFO] [1691630509.114279292] [talker]: Publishing: 'Hello World: 2'
[listener-2] [INFO] [1691630509.121953220] [listener]: I heard: [Hello World: 2]
[talker-1] [INFO] [1691630510.114710637] [talker]: Publishing: 'Hello World: 3'
[listener-2] [INFO] [1691630510.121464162] [listener]: I heard: [Hello World: 3]
[talker-1] [INFO] [1691630511.114519477] [talker]: Publishing: 'Hello World: 4'
[listener-2] [INFO] [1691630511.121885804] [listener]: I heard: [Hello World: 4]
[talker-1] [INFO] [1691630512.114275814] [talker]: Publishing: 'Hello World: 5'
[listener-2] [INFO] [1691630512.121655842] [listener]: I heard: [Hello World: 5]
[talker-1] [INFO] [1691630513.114144550] [talker]: Publishing: 'Hello World: 6'
[listener-2] [INFO] [1691630513.122104379] [listener]: I heard: [Hello World: 6]
```

### 测试 ros 通信组件相关功能

#### topic 通讯

##### c++ 实现

分别执行 `ros2 run demo_nodes_cpp talker` 和 `ros2 run demo_nodes_cpp listener`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run demo_nodes_cpp talker
[INFO] [1691630582.878137828] [talker]: Publishing: 'Hello World: 1'
[INFO] [1691630583.866419455] [talker]: Publishing: 'Hello World: 2'
[INFO] [1691630584.866925524] [talker]: Publishing: 'Hello World: 3'
[INFO] [1691630585.866529187] [talker]: Publishing: 'Hello World: 4'
[INFO] [1691630586.866242749] [talker]: Publishing: 'Hello World: 5'
[INFO] [1691630587.866463610] [talker]: Publishing: 'Hello World: 6'
[INFO] [1691630588.866553968] [talker]: Publishing: 'Hello World: 7'
[INFO] [1691630589.866199323] [talker]: Publishing: 'Hello World: 8'
[INFO] [1691630590.865155773] [talker]: Publishing: 'Hello World: 9'
[INFO] [1691630591.865262625] [talker]: Publishing: 'Hello World: 10'
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 run demo_nodes_cpp listener
[INFO] [1691630582.915406861] [listener]: I heard: [Hello World: 1]
[INFO] [1691630583.871139572] [listener]: I heard: [Hello World: 2]
[INFO] [1691630584.874223150] [listener]: I heard: [Hello World: 3]
[INFO] [1691630585.873610413] [listener]: I heard: [Hello World: 4]
[INFO] [1691630586.871207966] [listener]: I heard: [Hello World: 5]
[INFO] [1691630587.873243134] [listener]: I heard: [Hello World: 6]
[INFO] [1691630588.874165495] [listener]: I heard: [Hello World: 7]
[INFO] [1691630589.870966940] [listener]: I heard: [Hello World: 8]
[INFO] [1691630590.867658882] [listener]: I heard: [Hello World: 9]
[INFO] [1691630591.866963931] [listener]: I heard: [Hello World: 10]
```

##### python 实现

分别执行 `ros2 run demo_nodes_py talker` 和 `ros2 run demo_nodes_py listener`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run demo_nodes_py talker
[INFO] [1691630641.179675476] [talker]: Publishing: "Hello World: 0"
[INFO] [1691630641.605958446] [talker]: Publishing: "Hello World: 1"
[INFO] [1691630642.641069714] [talker]: Publishing: "Hello World: 2"
[INFO] [1691630643.642141463] [talker]: Publishing: "Hello World: 3"
[INFO] [1691630644.610727998] [talker]: Publishing: "Hello World: 4"
[INFO] [1691630645.663489321] [talker]: Publishing: "Hello World: 5"
[INFO] [1691630646.609993776] [talker]: Publishing: "Hello World: 6"
[INFO] [1691630647.609740813] [talker]: Publishing: "Hello World: 7"
[INFO] [1691630648.610199950] [talker]: Publishing: "Hello World: 8"
[INFO] [1691630649.642356694] [talker]: Publishing: "Hello World: 9"
[INFO] [1691630650.610409016] [talker]: Publishing: "Hello World: 10"
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 run demo_nodes_py listener
[INFO] [1691630641.821454989] [listener]: I heard: [Hello World: 0]
[INFO] [1691630641.850333689] [listener]: I heard: [Hello World: 1]
[INFO] [1691630642.665133997] [listener]: I heard: [Hello World: 2]
[INFO] [1691630643.665143942] [listener]: I heard: [Hello World: 3]
[INFO] [1691630644.635439383] [listener]: I heard: [Hello World: 4]
[INFO] [1691630645.691085916] [listener]: I heard: [Hello World: 5]
[INFO] [1691630646.629947545] [listener]: I heard: [Hello World: 6]
[INFO] [1691630647.630298784] [listener]: I heard: [Hello World: 7]
[INFO] [1691630648.631278122] [listener]: I heard: [Hello World: 8]
[INFO] [1691630649.664833571] [listener]: I heard: [Hello World: 9]
[INFO] [1691630650.630717586] [listener]: I heard: [Hello World: 10]
```

#### service 通信

##### c++ 实现

分别执行 `ros2 run demo_nodes_cpp add_two_ints_server` 和 `ros2 run demo_nodes_cpp add_two_ints_client`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run demo_nodes_cpp add_two_ints_server
[INFO] [1691630691.732870108] [add_two_ints_server]: Incoming request
a: 2 b: 3
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 run demo_nodes_cpp add_two_ints_client
[INFO] [1691630691.761158603] [add_two_ints_client]: Result of add_two_ints: 5
```

##### python 实现

分别在两个终端执行 `ros2 run demo_nodes_py add_two_ints_server` 和 `ros2 run demo_nodes_py add_two_ints_client`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run demo_nodes_py add_two_ints_server
[INFO] [1691630790.313627693] [add_two_ints_server]: Incoming request
a: 2 b: 3
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 run demo_nodes_py add_two_ints_client
[INFO] [1691630790.860159439] [add_two_ints_client]: Result of add_two_ints: 5
```

### 测试 ros 坐标转换相关功能

#### 坐标转换的发布和订阅

分别在两个终端执行 `ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom` 和 `ros2 run tf2_ros tf2_echo base_link odom`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom
[WARN] [1691630838.423510164] []: Old-style arguments are deprecated; see --help for new-style arguments
[INFO] [1691630838.922832526] [static_transform_publisher_839TefedOk0xQCcy]: Spinning until stopped - publishing transform
translation: ('1.000000', '1.000000', '1.000000')
rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
from '/base_link' to '/odom'
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 run tf2_ros tf2_echo base_link odom
[INFO] [1691630838.476487030] [tf2_echo]: Waiting for transform base_link ->  odom: Invalid frame ID "base_link" passed to canTransform argument target_frame - frame does not exist
At time 0.0
- Translation: [1.000, 1.000, 1.000]
- Rotation: in Quaternion [0.000, 0.000, 0.000, 1.000]
- Rotation: in RPY (radian) [0.000, -0.000, 0.000]
- Rotation: in RPY (degree) [0.000, -0.000, 0.000]
- Matrix:
  1.000  0.000  0.000  1.000
  0.000  1.000  0.000  1.000
  0.000  0.000  1.000  1.000
  0.000  0.000  0.000  1.000
At time 0.0
- Translation: [1.000, 1.000, 1.000]
- Rotation: in Quaternion [0.000, 0.000, 0.000, 1.000]
- Rotation: in RPY (radian) [0.000, -0.000, 0.000]
- Rotation: in RPY (degree) [0.000, -0.000, 0.000]
- Matrix:
  1.000  0.000  0.000  1.000
  0.000  1.000  0.000  1.000
  0.000  0.000  1.000  1.000
  0.000  0.000  0.000  1.000
```

#### tf_monitor 监控

分别在两个终端执行 `ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom` 和 `ros2 run tf2_ros tf2_monitor`，输出如下，测试通过

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom
[WARN] [1691630959.753230867] []: Old-style arguments are deprecated; see --help for new-style arguments
[INFO] [1691630960.310397029] [static_transform_publisher_HoMwQoSi0zgBgHmj]: Spinning until stopped - publishing transform
translation: ('1.000000', '1.000000', '1.000000')
rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
from '/base_link' to '/odom'
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 run tf2_ros tf2_monitor
Gathering data on all frames for 10 seconds...



RESULTS: for all Frames

Frames:
Frame: /odom, published by <no authority available>, Average Delay: 0.0346603, Max Delay: 0.0346603

All Broadcasters:
Node: <no authority available> 1e+08 Hz, Average Delay: 0.0346603 Max Delay: 0.0346603
```

#### view_frames 保存 pdf

分别在两个终端执行 `ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom` 和 `ros2 run tf2_tools view_frames`，输出如下

```bash
(pyenv) [root@openEuler-riscv64 workspace]# ros2 run tf2_ros static_transform_publisher 1 1 1 0 0 0 /base_link /odom
[WARN] [1691631045.266240563] []: Old-style arguments are deprecated; see --help for new-style arguments
[INFO] [1691631045.730495209] [static_transform_publisher_YtiqKUFxYl8rlATj]: Spinning until stopped - publishing transform
translation: ('1.000000', '1.000000', '1.000000')
rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
from '/base_link' to '/odom'
```

```bash
(pyenv) [root@openEuler-riscv64 ~]# ros2 run tf2_tools view_frames
[INFO] [1691631053.385521785] [view_frames]: Listening to tf data for 5.0 seconds...
[INFO] [1691631058.523355940] [view_frames]: Generating graph in frames.pdf file...
[INFO] [1691631058.577874297] [view_frames]: Result:tf2_msgs.srv.FrameGraph_Response(frame_yaml="odom: \n  parent: 'base_link'\n  broadcaster: 'default_authority'\n  rate: 10000.000\n  most_recent_transform: 0.000000\n  oldest_transform: 0.000000\n  buffer_length: 0.000\n")
```

检查当前目录，存在 pdf 文件，测试通过

```bash
(pyenv) [root@openEuler-riscv64 ~]# ls
frames_2023-08-10_09.30.58.gv   frames_2023-08-10_09.30.58.pdf
```
