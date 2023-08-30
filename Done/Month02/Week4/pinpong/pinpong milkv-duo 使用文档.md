# pinpong milkv-duo使用文档

## 一、连接mikv-duo进入操作系统

### 1、安装对应的驱动

[https://milkv.io/zh/docs/duo/getting-started/setup](https://milkv.io/zh/docs/duo/getting-started/setup)

### 2、使用MobaXterm通过ssh方式连接milkv-duo   密码：milkv

![image-20230822111906051](https://forum.sophgo.com/uploads/default/original/1X/b0851878696345dd72ea166db8f26de28b144387.png)

### 3、安装pinpong库

成功连接milv-duo后，从左边进入/usr/lib/python3.9/site-packages文件夹，将下载好的pinpong库直接复制进去（根据不同的python版本修改路劲）。

![](https://forum.sophgo.com/uploads/default/original/1X/bde0b608bde31c51bb6aee5e0b0c9c351b6eaee1.png)

### 4、进入pinpong库

```
cd /usr/lib/python3.9/site-packeges/pinpong/example/milkv-duo   
```

![](https://forum.sophgo.com/uploads/default/original/1X/fd9b19915083fb5ce4ecf7038d0fc3b67d17b023.png)

通过ls命令查看支持的例程。

### 5、运行例程

通过vi命令打开对应的例程，通过python直接运行例程。

GPIO：以blink.py为例，调用Board()，输入板子名称，生成对应的板子对象，然后调用对应的方法begin()进行初始化。再使用Pin()犯法操作对应的引脚，使用GPIO则传入数字引脚号以及输入输出模式生成引脚对象，在通过对象调用对应的方法，如下图所示。

![image-20230822140633542](https://forum.sophgo.com/uploads/default/original/1X/757702784a22a7a10cf2fecad3d0f8723177a48c.png)

PWM：以pwm.py为例，也需要先生成对应的板子对象进行初始化，然后再生成所连接的引脚对象，再调用PWM()方法生成pwm对象，通过pwm对象执行对应的方法实现pwm功能，如下图所示。

![image-20230822141344499](https://forum.sophgo.com/uploads/default/original/1X/2e882edf79abfe9a44fdb9f448c5090341d8d6c8.png)

IIC:以sht31.py为例，生成对应的板子对象并初始化后，调用pinpong自带的sht31传感器库方法生成sht31对象，bus_num一般默认为0，需要根据所接的iic引脚对应的iic设备号传参。对象生成后可以调用库中对应的方法运行传感器。

![image-20230822141714720](https://forum.sophgo.com/uploads/default/original/1X/615bd227f69b1bb64d6b35cedea4bfd101b29f2b.png)

UART：以 nfc_uart_card.py为例，生成板子对象后并初始化后，调用pn532库的uart方法生成nfc对象，需要根据所连接的uart引脚设备号进行传参，再调用库中的方法操作传感器，如下图所示。

![image-20230822142520980](https://forum.sophgo.com/uploads/default/original/1X/d4d0d43d44b65406a4661939ac5270ed4416c20e.png)

ADC:以adc.py为例，传入A0代表使用ADC0引脚。生成ADC对象后则可以读取ADC的值。

![image-20230825103009113](https://forum.sophgo.com/uploads/default/original/1X/7023367dcbda07f6c73582de3c34592140855730.png)

SPI：以st7789.py为例，传入对应的spi设备号，可以通过ls /dev/查看，生成对应的对象后可以调用库中的方法实现功能。

![image-20230829164039190](https://forum.sophgo.com/uploads/default/original/1X/4624a0b219568ec2ce6b823787c983dfac9cb248.png)

### 5、查看板载资源

找到pinpong库extension文件夹中的milkvDuo.py文件并打开

![image-20230823183113579](https://forum.sophgo.com/uploads/default/original/1X/86a11bba050254802e08fa61b86a24f8b7c92840.png)

如上图，框选的部分表示硬件支持的资源，支持3路IIC，支持1路SPI，支持23路GPIO引脚，支持2路ADC，支持10路PWM。

### 6、引脚复用工具cvi_pinmux使用

[https://community.milkv.io/t/milk-v-duo-cvi-pinmux/292](https://community.milkv.io/t/milk-v-duo-cvi-pinmux/292)
