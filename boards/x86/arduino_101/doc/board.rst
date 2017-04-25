.. _arduino_101:

Arduino/Genuino 101
###################

概述
********

Arduino/Genuino 101 是一个基于 Intel® Curie™ 模组的开发板。 开发板设计整合了低功耗、高性能核心且具备 Arduino 的易用性。Arduino 101 增加了低耗蓝牙功能以及一个板载 6 轴加速计/陀螺仪，为连接世界的创造性项目提供令人兴奋的机会。

.. figure:: img/arduino_101.jpg
   :width: 442px
   :align: center
   :alt: Arduino/Genuino 101

   Arduino/Genuino 101 (来源: Intel)

Curie 模组中的 Intel Quark* SE SoC 包含一个单核 32 MHz x86(Intel Quark* 处理器)以及 32 MHz Argonaut RISC Core (ARC)* EM 处理器。两个处理器同时运行并共享内存。ARC 处理器也被当作数字信号处理器（DSP）的传感器集线器或传感器子系统，这取决于你看的文档。理论上，DSP 可使用最小功率运行，理想状态下，它可以在 x86 处理器在低功耗模式等待时收集和处理传感器数据。

Zephyr 可被烧写进 Arduino 101 以用于实验和测试目的。注意，在 Arduino 101 上运行 Zephyr OS 不被 Arduino LLC 支持。

硬件
********

主板布局
============

主板的一般信息可在 `Arduino 101 website <https://www.arduino.cc/en/Main/ArduinoBoard101>`_ 找到，其中包含主板原理图及 BRD 文件。

Arduino 101 引脚
==================

在使用 Zephyr 内核时，对于 Arduino 101 的引脚映射变得稍微复杂。下表详述了 Zephyr 对 Arduino 101 开发板控制引脚的映射。关于引脚复用详情、可配置的有效选项、以及在何处映射可参阅 :file:`boards/x86/arduino_101/pinmux.c` 文件。


+-------------+----------+------------+
| Arduino Pin | Function | Zephyr Pin |
+=============+==========+============+
| IO-0        | UART1-RX | 17         |
+-------------+----------+------------+
| IO-1        | UART1-TX | 16         |
+-------------+----------+------------+
| IO-2        | GPIO     | 52         |
+-------------+----------+------------+
| IO-3        | GPIO     | 51         |
|             |          | 63         |
+-------------+----------+------------+
| IO-4        | GPIO     | 53         |
+-------------+----------+------------+
| IO-5        | GPIO     | 49         |
|             |          | 64         |
+-------------+----------+------------+
| IO-6        | PWM2     | 65         |
+-------------+----------+------------+
| IO-7        | GPIO     | 54         |
+-------------+----------+------------+
| IO-8        | GPIO     | 50         |
+-------------+----------+------------+
| IO-9        | PWM3     | 66         |
+-------------+----------+------------+
| IO-10       | AIN0     | 0          |
+-------------+----------+------------+
| IO-11       | AIN3     | 3          |
+-------------+----------+------------+
| IO-12       | AIN1     | 1          |
+-------------+----------+------------+
| IO-13       | AIN2     | 2          |
+-------------+----------+------------+
| ADC0        | GPIO SS  | 10         |
+-------------+----------+------------+
| ADC1        | GPIO SS  | 11         |
+-------------+----------+------------+
| ADC2        | GPIO SS  | 12         |
+-------------+----------+------------+
| ADC3        | GPIO SS  | 13         |
+-------------+----------+------------+
| ADC4        | AIN14    | 14         |
+-------------+----------+------------+
| ADC5        | AIN9     | 9          |
+-------------+----------+------------+

.. node::

   IO-3 and IO-5 需要同时设置以适应功能改变。

支持功能
==================

通过驱动程序的使用，Zephyr 内核可在 Arduino 101 上支持多种硬件功能。某些驱动程序仅支持 x86,另一些仅支持 ARC，有少数两者都支持。下表显示了驱动程序和功能所对应的架构：

+-----------+------------+-----+-----+-----------------------+
| 接口      | 控制器     | ARC | x86 | 驱动/元件             |
+===========+============+=====+=====+=======================+
| APIC      | on-chip    | N   | Y   | 中断控制器            |
+-----------+------------+-----+-----+-----------------------+
| UART      | on-chip    | N   | Y   | 串行端口轮询;         |
|           |            |     |     | 串行端口中断          |
+-----------+------------+-----+-----+-----------------------+
| SPI       | on-chip    | Y   | Y   | spi                   |
+-----------+------------+-----+-----+-----------------------+
| ADC       | on-chip    | Y   | N   | adc                   |
+-----------+------------+-----+-----+-----------------------+
| I2C       | on-chip    | Y   | Y   | i2c                   |
+-----------+------------+-----+-----+-----------------------+
| GPIO      | on-chip    | Y   | Y   | gpio                  |
+-----------+------------+-----+-----+-----------------------+
| PWM       | on-chip    | Y   | Y   | pwm                   |
+-----------+------------+-----+-----+-----------------------+
| mailbox   | on-chip    | Y   | Y   | ipm                   |
+-----------+------------+-----+-----+-----------------------+

硬件及软件需求
==============================

在将 Zephyr 内核烧写进 Arduino 101 之前，需要一些额外的硬件。

* 可使用 USB 端口电源；但还是推荐使用 7V-12V 电池电源与 JTAG 连接器。
* 如果希望从串口抓取任何数据，需要使用 TTL 转 USB 适配器。以下适配器在连接 Arduino 101 开发板时需要使用雄跨电缆。 

  * USB 转 3.3V TTL 串行线
  * FTDI USB 转 TTL 串口部分 #TTL-232R-3V3 http://www.ftdichip.com/Products/Cables/USBTTLSerial.htm

我们推荐使用 ``dfu-util`` 工具来烧写 Arduino 101 开发板。对于 Linux 环境来说，可验证 ``udev`` 在 DFU 模式下是否有适当规则以允许你访问 Arduino 101 开发板。使用为Arduino桌面IDE的`Intel Curie Boards package`_ 所提供的``create_dfu_udev_rule`` 脚本，你可以很方便地添加规则。你可以使用以下命令获取并运行此脚本：

.. code-block:: console

   $ wget https://github.com/01org/intel-arduino-tools/raw/linux64/scripts/create_dfu_udev_rule
   $ chmod +x create_dfu_udev_rule
   $ sudo ./create_dfu_udev_rule
   $ rm create_dfu_udev_rule

如果你希望使用 JTAG 进行烧写，需要以下额外硬件:

* Flyswatter2 JTAG debugger
* ARM Micro JTAG Connector, Model: ARM-JTAG-20-10

连接串口输出
========================

Zephyr 内核配置中，默认支持串口通过开发板的 UART1 口输出。你需要使用 USB 转 3.3V TTL 串口线来接收串口输出：

* 将串口线 RX 引脚连接至 Arduino 101 的 TX->1 引脚。
* 将串口线 TX 引脚连接至 Arduino 101 的 RX<-0 引脚。
* 将串口线 GND 引脚连接至 Arduino 101 的 GND 引脚。

一旦连接，你需要在开发环境中：

* 打开一个串口模拟器 (如 Linux 下的 minicom, screen, 等等)
* 将 USB 附加到 TTL 串口线，例如，在 Linux 中它可能是 /dev/ttyUSB0
* 参数设置为:

  * Speed: 115200
  * Data: 8 bits
  * Parity: None
  * Stopbits: 1

编程与调试
*************************

Arduino 101 由 Quark CPU 供电，传感器子系统由 ARC 处理器供电。在创建应用程序时，根据使用情况, 需要编译和烧写两个Zephyr镜像。

Arduino 101 自带的 bootloarder 支持通过 USB 使用 DFU 协议进行烧写。此外，工厂安装的引导程序支持 Curie 模组的蓝牙设备的固件烧写。

创建 Quark 内核时使用 ``arduino_101`` 定义，目标为传感器子系统时使用 ``arduino_101_sss`` 定义。

当应用程序目标仅为Quark处理器时，一定要使用 ``CONFIG_ARC_INIT=n`` 选项来禁用传感器子系统处理器。否则将出现开发板挂起等待传感器子系统处理器启动的情况。

Bootloader (Boot ROM)
=====================

从Zephyr 1.4.0开始，已经移除了对 `QMSI Bootloader`_ 的支持。因此，出厂的启动ROM可确保通过DFU烧写开发板，并烧写蓝牙固件。

如果你之前已经安装了一个不同的启动ROM，推荐使用 `Flashpack Utility`_ 恢复出厂启动ROM镜像。 参阅 `Flashpack Utility`_ 包中的README，根据你的环境进行使用。

烧写
========

使用 ``dfu-util`` 烧写应用程序 会在按下开发板的主重启按钮后的 5 秒钟内将 Arduino 101 识别为 DFU-capable 设备。你可以使用手动或者``make`` 来运行应用程序:

* 手动方法: 键入 ``dfu-util`` 命令行，按下主重启按钮，并快速按下回车键以执行 deu-util 命令。如果 dfu-util 命令执行失败并显示 "No DFU capable USB device available"，请尝试在按下主重启按钮后操作更快些。
* Make 方法: 定义环境变量 ``ZEPHYR_FLASH_OVER_DFU=y`` 并执行 ``make flash``。在make命令准备进行烧写时，将提示重启开发板。如果你经常使用这个方法，可在 ``~/.zephyrrc`` 文件中添加以下命令行：

.. code-block:: console

   export ZEPHYR_FLASH_OVER_DFU=y

烧写传感器子系统内核
----------------------------------
创建ARC处理器时，开发板类型显示为 ``arduino_101_sss``。

示例应用程序 :ref:`hello_world` 用于此教程。
切换到Zephyr本地校验副本目录，并运行：

.. code-block:: console

   $ cd $ZEPHYR_BASE/samples/hello_world
   $ make BOARD=arduino_101_sss

一旦镜像被创建，即可使用手动方法烧写：

.. code-block:: console

   $ dfu-util -a sensor_core -D outdir/arduino_101_sss/zephyr.bin

也可使用 make-assisted 方法烧写:

.. code-block:: console

   $ ZEPHYR_FLASH_OVER_DFU=y make BOARD=arduino_101_sss flash

烧写x86应用程序内核
---------------------------------

创建x86处理器时, 开发板类型显示为``arduino_101``。

切换到Zephyr本地校验副本目录，并运行：

.. code-block:: console

   $ cd $ZEPHYR_BASE/samples/hello_world
   $ make BOARD=arduino_101

一旦镜像被创建，即可使用手动方法烧写：

.. code-block:: console

   $ dfu-util -a x86_app -D outdir/arduino_101/zephyr.bin

也可使用 make-assisted 方法烧写:

.. code-block:: console

   $ ZEPHYR_FLASH_OVER_DFU=y make BOARD=arduino_101 flash

.. _bluetooth_firmware_arduino_101:

烧写蓝牙内核
---------------------------

要让Zephyr蓝牙栈和Arduino 101蓝牙控制器（Nordic Semiconductor nRF51）协同工作，需要烧写一个兼容的固件。

此控制器上的Arduino 101出厂固件不支持Zephyr项目，所以需要烧写一个新的。

幸运的是，从Zephyr 1.6开始，Zephyr本身可以作为控制器的固件。你需要的应用程序是 ``samples/bluetooth/hci_uart`` ，目标开发板是 ``arduino_101_ble``。

创建蓝牙控制器镜像，请按照以下说明进行操作:

.. code-block:: console

   $ cd $ZEPHYR_BASE/samples/bluetooth/hci_uart
   $ make BOARD=arduino_101_ble

一旦镜像被创建，即可使用手动方法烧写：

.. code-block:: console

   $ dfu-util -a ble_core -D outdir/arduino_101_ble/zephyr.bin

也可使用 make-assisted 方法烧写:

.. code-block:: console

   $ ZEPHYR_FLASH_OVER_DFU=y make BOARD=arduino_101_ble flash

在成功完成这些步骤后，你的Arduino 101现在已拥有一个HCI兼容BLE固件。


使用JTAG适配器烧写
---------------------------

一般的开发工作，我们推荐使用 ``dfu-util`` 工具烧写Arduino 101开发板。JTAG用于高级开发与调试。

* 将ARM Micro JTAG Connector连接至Flyswatter2.

* 观察Arduino 101开发板的微JTAG接口。Arduino接口连接了SCL和SDA引脚，如下图红色方框所示：

  .. figure:: img/arduino_101_flat.jpg
     :width: 442px
     :align: center
     :alt: Arduino/Genuino 101 JTAG

* 微JTAG接口旁的小白点指示接口pin 1所在位置。图中绿色键头所指。

* 将ARM Micro JTAG连接器连接至Arduino 101微JTAG接口.

确保线缆和接口的pin 1定位准确。来自ARM Micro JTAG连接器的线缆使用红色线指示哪个接头连接pin 1。

对于Linux环境来说，要控制Flyswatter2，你的Linux账户需要授予硬件抽像层交互权限，这由'plugdev'组实现。可使用usermod命令实现组存在验证以及添加用户名：

.. code-block:: console

   $ sudo usermod -a -G plugdev $LOGNAME

如果组不存在，可以运行以下命令进行添加：


.. code-block:: console

   $ sudo groupadd -r plugdev

对于Linux开发环境，需要验证Flyswatter2设备所指定用户控制的 ``udev`` 的规则是否正确。添加以下规则将给予plugdev组成员以Flyswatter2控制权。

.. code-block:: console

   $ sudo su
   $ cat <<EOF > /etc/udev/rules.d/99-openocd.rules
   # TinCanTools Flyswatter2
   ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6010", MODE="664", GROUP="plugdev"
   EOF
   $ exit

udev规则安装完毕后，需要重载规则：

.. code-block:: console

   $ sudo udevadm control --reload-rules

使用USB B型线缆连接Flyswatter2和你的电脑。在Linux中，你将在dmesg中看到类似下面的信息:

.. code-block:: console

   usb 1-2.1.1: new high-speed USB device number 13 using xhci_hcd
   usb 1-2.1.1: New USB device found, idVendor=0403, idProduct=6010
   usb 1-2.1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
   usb 1-2.1.1: Product: Flyswatter2
   usb 1-2.1.1: Manufacturer: TinCanTools
   usb 1-2.1.1: SerialNumber: FS20000
   ftdi_sio 1-2.1.1:1.0: FTDI USB Serial Device converter detected
   usb 1-2.1.1: Detected FT2232H
   usb 1-2.1.1: FTDI USB Serial Device converter now attached to ttyUSB0
   ftdi_sio 1-2.1.1:1.1: FTDI USB Serial Device converter detected
   usb 1-2.1.1: Detected FT2232H
   usb 1-2.1.1: FTDI USB Serial Device converter now attached to ttyUSB1


调试
=========

以下指南将帮助你分别调试Arduino 101上的x86核心或ARC核心。

Core (x86)应用程序
----------------------

使用以下命令编译和烧写x86应用程序：

.. code-block:: console

   $ cd <my x86 app>
   $ make BOARD=arduino_101 flash

在x86核心上启动debug server:

.. code-block:: console

   $ make BOARD=arduino_101 debugserver

在第二个控制台将debug server连接至x86核心：

.. code-block:: console

   $ cd <my x86 app>
   $ $ZEPHYR_SDK_INSTALL_DIR/sysroots/x86_64-pokysdk-linux/usr/bin/i586-zephyr-elfiamcu/i586-zephyr-elfiamcu-gdb outdir/arduino_101/zephyr.elf
   (gdb) target remote localhost:3333
   (gdb) b main
   (gdb) c

传感器子系统Core (ARC)
---------------------------

使能x86核心的ARC INIT。这可以通过烧写设置了 ``CONFIG_ARC_INIT=y`` 选项的x86应用程序来完成，例如Zephyr测试框架所提供的booting stub。

.. code-block:: console

   $ cd $ZEPHYR_BASE/tests/booting/stub
   $ make BOARD=arduino_101 flash

使用以下命令编译和烧写ARC应用程序：

.. code-block:: console

   $ cd <my arc app>
   $ make BOARD=arduino_101_sss flash

在ARC核心上启动debug server:

.. code-block:: console

   $ make BOARD=arduino_101_sss debugserver

在第二个控制台将debug server连接至ARC核心：

.. code-block:: console

   $ cd <my arc app>
   $ $ZEPHYR_SDK_INSTALL_DIR/sysroots/x86_64-pokysdk-linux/usr/bin/arc-zephyr-elf/arc-zephyr-elf-gdb outdir/arduino_101_sss/zephyr.elf
   (gdb) target remote localhost:3334
   (gdb) b main
   (gdb) c


蓝牙固件
------------------

你仅能在控制台上看到普通日志信息，默认情况下无任何途径访问Zephyr和nRF51控制器间的人机交互信息。尽管如此，还是有一个专门的蓝牙日志模式将控制台转换为二进制协议，可插入普通日志信息及人机交互信息。在编译应用程序前，设置以下Kconfig选项以使用这个协议：

.. code-block:: console

   CONFIG_BLUETOOTH_DEBUG_MONITOR=y
   CONFIG_UART_CONSOLE=n
   CONFIG_UART_QMSI_1_BAUDRATE=1000000

第一项重置了BLUETOOTH_DEBUG_LOG选项，第二项禁用了默认的printk/printf钩子，为了不产生瓶颈，第三项匹配与nRF51通信所使用的控制台波特率。

为将发送至控制台UART的二进制协议译码，你将使用BlueZ 5.40及之后版本的btmon工具：


.. code-block:: console

   $ btmon --tty <console TTY> --tty-speed 1000000

发行说明
*************
在调试ARC时，切记，试图调试ARC前必须首先启动并运行x86核心。这是因为IPM控制台调用会挂起并等待x86核心清除通信。

参考
**********

.. _QMSI Bootloader: https://github.com/quark-mcu/qm-bootloader

.. _Flashpack Utility: https://downloadcenter.intel.com/downloads/eula/25470/Arduino-101-software-package?httpDown=https%3A%2F%2Fdownloadmirror.intel.com%2F25470%2Feng%2Farduino101-factory_recovery-flashpack.tar.bz2

.. _Intel Curie Boards package: https://www.arduino.cc/en/Guide/Arduino101#toc2
