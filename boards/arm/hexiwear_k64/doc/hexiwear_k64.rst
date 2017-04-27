.. _hexiwear_k64:

Hexiwear
########

概览
********

Hexiwear由基于ARM Cortex-M4内核的Kinetis K64微处理器驱动。另一块Kinetis无线MCU，提供低功耗蓝牙的连通性。Hexiwear还集成了多种传感器，一个由1.1寸 96px x 96px全彩OLED显示屏组成的用户界面，以及6个触控式电容按钮。

- 智能手表拥有引人注目的外形，强大的低功耗Kinetis K6x MCU以及6个板载传感器。
- 专为可穿戴应用设计的板载可充电电池，OLED屏幕以及板载传感器，如光学心率传感器、加速计、磁力计及陀螺仪。
- 专为IoT终端结点应用设计的板载传感器，如温度、压力、湿度及环境光度传感器。
- 高度的灵活性，可通过点击面板在近200个额外传感器中选择添加。

.. image:: hexiwear_k64.jpg
   :width: 442px
   :align: center
   :alt: Hexiwear

硬件
********

- 主MCU: NXP Kinetis K64x (ARM Cortex-M4, 120 MHz, 1M Flash, 256K SRAM)
- 无线MCU: NXP Kinetis KW4x (ARM Cortex-M0+, 低功耗蓝牙 & 802.15.4无线电)
- 6轴组合式加速计及NXP FXOS8700磁力计
- 3轴陀螺仪: NXP FXAS21002
- 绝对压力传感器 NXP MPL3115
- Li-Ion/Li-Po 电池充电器 NXP MC34671
-光学心率传感器 Maxim MAX30101
- 环境光度传感器, 温湿度传感器
- 1.1寸全彩OLED显示屏
- 触觉反馈引擎
- 190 mAh 2C Li-Po 电池
- 电容式触摸界面
- RGB LED

有关 K64F SoC 及 Hexiwear 开发板的更多信息请参阅:

- `K64F Website`_
- `K64F Datasheet`_
- `K64F Reference Manual`_
- `Hexiwear Website`_
- `Hexiwear Fact Sheet`_
- `Hexiwear Schematics`_

支持的功能
==================

hexiwear_k64主板配置支持以下硬件功能:

+-----------+------------+-------------------------------------+
| 接口      | 控制器     | 驱动/元件                           |
+===========+============+=====================================+
| NVIC      | on-chip    | 嵌套向量中断控制器                  |
+-----------+------------+-------------------------------------+
| SYSTICK   | on-chip    | systick                             |
+-----------+------------+-------------------------------------+
| PINMUX    | on-chip    | 引脚复用                            |
+-----------+------------+-------------------------------------+
| GPIO      | on-chip    | gpio                                |
+-----------+------------+-------------------------------------+
| I2C       | on-chip    | i2c                                 |
+-----------+------------+-------------------------------------+
| UART      | on-chip    | 串行端口轮询;                       |
|           |            | 串行端口中断                        |
+-----------+------------+-------------------------------------+
| FLASH     | on-chip    | soc flash                           |
+-----------+------------+-------------------------------------+
| SENSOR    | off-chip   | fxos8700 轮询;                      |
|           |            | fxos8700 触发器                     |
+-----------+------------+-------------------------------------+

默认配置可在defconfig文件中找到:

	``boards/arm/hexiwear_k64/hexiwear_k64_defconfig``

暂不支持其它硬件功能。

连接和IO
===================

K64F SoC 有5对 pinmux/gpio 控制器。

+-------+-----------------+---------------------------+
| 名称  | 功能            | 应用                      |
+=======+=================+===========================+
| PTC8  | GPIO            | 红色LED                   |
+-------+-----------------+---------------------------+
| PTC9  | GPIO            | 绿色 LED                  |
+-------+-----------------+---------------------------+
| PTD0  | GPIO            | 蓝色 LED                  |
+-------+-----------------+---------------------------+
| PTD13 | GPIO            | FXOS8700 INT2             |
+-------+-----------------+---------------------------+
| PTB16 | UART0_RX        | UART 控制台               |
+-------+-----------------+---------------------------+
| PTB17 | UART0_TX        | UART 控制台               |
+-------+-----------------+---------------------------+
| PTE24 | UART4_RX        | UART BT HCI               |
+-------+-----------------+---------------------------+
| PTE25 | UART4_TX        | UART BT HCI               |
+-------+-----------------+---------------------------+
| PTC10 | I2C1_SCL        | I2C / FXOS8700            |
+-------+-----------------+---------------------------+
| PTC11 | I2C1_SDA        | I2C / FXOS8700            |
+-------+-----------------+---------------------------+

系统时钟
============

K64F SoC 配置为使用12 MHz板载外部振荡器，通过片内PLL产生120 MHz系统时钟。

串口
===========

K64F SoC拥有6个UARTs，一个配置为控制台使用，一个用于BT HCI，剩余的没有使用。

编程与调试
*************************

烧写
========

Hexiwear扩展坞包含了一个 `OpenSDA`_ 串口及内置debug适配器。适配器提供了:

- 一个连接计算机主机的USB接口，显示为大容量存储器及USB串口。
- 一个USB Flash设备，实现了USB flash存储器文件存储。
- 一个物理UART连接器，它是USB串口的中继接口。

.. note::
   OpenSDA通过开关在K64和KW40Z间共用，因此，同一时间只有一块Soc可被烧写、调试或拥有一个打开的控制台。

在Hexiwear中烧 写应用程序
-----------------------------------

#. 编译Zephyr内核及应用程序:

   .. code-block:: console

      $ cd $ZEPHYR_BASE
      $ . zephyr-env.sh
      $ cd $ZEPHYR_BASE/samples/hello_world/
      $ make BOARD=hexiwear_k64

#. 确保扩展坞中的USB线缆已经拔出。
#. 将Hexiwear开发板连接至扩展坞。
#. 配置扩展坞开关以向OpenSDA电路发送希望的SoC信号：

   +--------+-------------+-------+-----+
   | 开关   | 信号        | KW40Z | K64 |
   +========+=============+=======+=====+
   | 1      | MK64 SWDIO  | OFF   | ON  |
   +--------+-------------+-------+-----+
   | 2      | MK64 RST    | OFF   | ON  |
   +--------+-------------+-------+-----+
   | 3      | MKW40 RST   | ON    | OFF |
   +--------+-------------+-------+-----+
   | 4      | MKW40 SWDIO | ON    | OFF |
   +--------+-------------+-------+-----+
   | 5      | OSDA        | ON    | ON  |
   +--------+-------------+-------+-----+
   | 6      | LED1        | OFF   | OFF |
   +--------+-------------+-------+-----+
   | 7      | LED2        | OFF   | OFF |
   +--------+-------------+-------+-----+
   | 8      | LED3        | OFF   | OFF |
   +--------+-------------+-------+-----+

#. 连接USB线缆并确保电源开关处于开状态，此时显示了一个叫DAPLINK的USB大容量存储设备。
#. 将应用程序的二进制文件``zephyr.bin``拷贝到DAPLINK驱动器。驱动器将暂时消失，并在几秒后重新显示。
#. 打开一个串口终端 (minicom, putty等等) ，使用以下设置:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1

#. 重启SoC。扩展坞中每个SoC都有一个重启按钮，你将在串口中看到以下信息:

  .. code-block:: console

     Hello World! arm

使用蓝牙
***************

配置KW40Z为蓝牙控制器
=============================================

当配置KW40Z为蓝牙控制器时，K64可支持Zephyr蓝牙主机应用。

#. 下载并安装 `KW40Z Connectivity Software`_。这个安装包包含了KW40Z的蓝牙控制器应用。
#. 将 ``tools/binaries/BLE_HCI_Modem.bin`` 文件烧写至KW40Z。

现在可以在K64上编译并运行Zephyr蓝牙主机应用示例了。下次把新的蓝牙主机应用烧写至K64时无需重复此步骤。

心率传感器外设
============================
导航到Zephyr示例应用并为Hexiwear K64编译它。

.. code-block:: console

   $ cd samples/bluetooth/peripheral_hr
   $ make BOARD=hexiwear_k64

向Hexiwear K64烧写应用程序，请确保扩展坞上的OpenSDA开关配置用于K64。

使用扩展坞上的按钮重启KW40Z和K64。

在你的智能手机上安装Kinetis BLE Toolbox:

- `Kinetis BLE Toolbox for iOS`_
- `Kinetis BLE Toolbox for Android`_

打开app, 点击the **Heart Rate** 功能，你将会看到一个 **Zephyr
Heartrate Sensor** 设备。点击 **Zephyr Heartrate Sensor** 设备，你将会看到每秒更新一次的心率数据。

.. _Hexiwear Website:
   http://www.nxp.com/hexiwear

.. _Hexiwear Fact Sheet:
   http://www.nxp.com/assets/documents/data/en/fact-sheets/HEXIWEAR-FS.pdf

.. _Hexiwear Schematics:
   http://cdn-docs.mikroe.com/images/c/c0/Sch_Hexiwear_MainBoard_v106c.pdf

.. _OpenSDA:
   http://www.nxp.com/products/software-and-tools/hardware-development-tools/startertrak-development-boards/opensda-serial-and-debug-adapter:OPENSDA

.. _K64F Website:
   http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/kinetis-cortex-m-mcus/k-series-performance-m4/k6x-ethernet/kinetis-k64-120-mhz-256kb-sram-microcontrollers-mcus-based-on-arm-cortex-m4-core:K64_120

.. _K64F Datasheet:
   http://www.nxp.com/assets/documents/data/en/data-sheets/K64P144M120SF5.pdf

.. _K64F Reference Manual:
   http://www.nxp.com/assets/documents/data/en/reference-manuals/K64P144M120SF5RM.pdf

.. _KW40Z Connectivity Software:
   https://www.nxp.com/webapp/Download?colCode=KW40Z-CONNECTIVITY-SOFTWARE&appType=license&location=null&fpsp=1&WT_TYPE=Protocol%20Stacks&WT_VENDOR=FREESCALE&WT_FILE_FORMAT=exe&WT_ASSET=Downloads&fileExt=.exe&Parent_nodeId=1432854896956716810497&Parent_pageType=product

.. _Kinetis BLE Toolbox for iOS:
   https://itunes.apple.com/us/app/kinetis-ble-toolbox/id1049036961?mt=8

.. _Kinetis BLE Toolbox for Android:
   https://play.google.com/store/apps/details?id=com.freescale.kinetisbletoolbox
