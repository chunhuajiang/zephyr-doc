.. _frdm_k64f:

NXP FRDM-K64F
##############

概述
********

Freedom-K64F 是一款面向 Kinetis K64、K63 和 K24 MCU 设计的超低成本的开发平台。

- 规格与 Arduino™ R3 引脚布局兼容 。
- 配备丰富的外设，包括用于开发完整电子罗盘功能的 6 轴数字加速度传感器和磁力计，用于直接交互与反馈的 3 色 LED 和两个用户按钮，microSD 卡插槽，以及板载以太网端口，面向 Bluetooth 和 2.4 GHz 无线电附加模块的接头等连接选项，可实现快速原型设计。 。
- 包含 OpenSDAv2 接口。 OpenSDAv2 是 NXP 开源硬件嵌入式串行接口和调试适配器，它运行了一个开源的 bootloader，提供了串口通信、flash 编程和运行时的控制调试功能。

.. image:: frdm_k64f.jpg
   :width: 720px
   :align: center
   :alt: FRDM-K64F

硬件
********

- MK64FN1M0VLL12 MCU (120 MHz，1 MB 闪存，256 KB RAM，低功耗，无晶振 USB 和 100 引脚薄型四方扁平封装(LQFP))
- 两用 USB 接口，带 Micro-B USB 接头
- RGB LED
- FXOS8700CQ 加速度传感器和磁力计
- 两个用户按钮
- 灵活的供电选项 - OpenSDAv2 USB、Kinetis K64 USB和外部电源
- 可通过兼容Arduino™ R3的I/O接头轻松访问MCU输入/输出
- 可编程 OpenSDAv2 调试电路，支持 CMSIS-DAP 接口软件，提供以下功能： 

  - 大容量存储设备(MSD)闪存编程接口
  - CMSIS-DAP 调试接口可通过免驱动的 USB HID 连接提供运行控制调试功能，兼容 IDE 工具
  - 虚拟串行端口
  - 开源 CMSIS-DAP 软件项目

- 以太网
- SDHC

关于 K64F SoC 和 FRDM-K64F 开发板的更多信息请参考：

- `K64F Website`_
- `K64F Datasheet`_
- `K64F Reference Manual`_
- `FRDM-K64F Website`_
- `FRDM-K64F User Guide`_
- `FRDM-K64F Schematics`_

支持的功能
==================

frdm_k64f 开发板配置支持如下的硬件特性：

+-----------+------------+-------------------------------------+
| Interface | Controller | Driver/Component                    |
+===========+============+=====================================+
| NVIC      | on-chip    | nested vector interrupt controller  |
+-----------+------------+-------------------------------------+
| SYSTICK   | on-chip    | systick                             |
+-----------+------------+-------------------------------------+
| PINMUX    | on-chip    | pinmux                              |
+-----------+------------+-------------------------------------+
| GPIO      | on-chip    | gpio                                |
+-----------+------------+-------------------------------------+
| I2C       | on-chip    | i2c                                 |
+-----------+------------+-------------------------------------+
| SPI       | on-chip    | spi                                 |
+-----------+------------+-------------------------------------+
| ETHERNET  | on-chip    | ethernet                            |
+-----------+------------+-------------------------------------+
| UART      | on-chip    | serial port-polling;                |
|           |            | serial port-interrupt               |
+-----------+------------+-------------------------------------+
| FLASH     | on-chip    | soc flash                           |
+-----------+------------+-------------------------------------+
| SENSOR    | off-chip   | fxos8700 polling;                   |
|           |            | fxos8700 trigger                    |
+-----------+------------+-------------------------------------+

默认的配置文件为：

	``boards/arm/frdm_k64f/frdm_k64f_defconfig``

当前还未支持其它的硬件特性。

连接与 IO
===================

K64F SoC 有五对 pinmux/gpio 控制器。

+-------+-----------------+---------------------------+
| Name  | Function        | Usage                     |
+=======+=================+===========================+
| PTB22 | GPIO            | Red LED                   |
+-------+-----------------+---------------------------+
| PTE26 | GPIO            | Green LED                 |
+-------+-----------------+---------------------------+
| PTB21 | GPIO            | Blue LED                  |
+-------+-----------------+---------------------------+
| PTC6  | GPIO            | SW2 / FXOS8700 INT1       |
+-------+-----------------+---------------------------+
| PTC13 | GPIO            | FXOS8700 INT2             |
+-------+-----------------+---------------------------+
| PTA4  | GPIO            | SW3                       |
+-------+-----------------+---------------------------+
| PTB16 | UART0_RX        | UART Console              |
+-------+-----------------+---------------------------+
| PTB17 | UART0_TX        | UART Console              |
+-------+-----------------+---------------------------+
| PTC16 | UART3_RX        | UART BT HCI               |
+-------+-----------------+---------------------------+
| PTC17 | UART3_TX        | UART BT HCI               |
+-------+-----------------+---------------------------+
| PTCD0 | SPI0_PCS0       | SPI                       |
+-------+-----------------+---------------------------+
| PTCD1 | SPI0_SCK        | SPI                       |
+-------+-----------------+---------------------------+
| PTCD2 | SPI0_SOUT       | SPI                       |
+-------+-----------------+---------------------------+
| PTCD3 | SPI0_SIN        | SPI                       |
+-------+-----------------+---------------------------+
| PTE24 | I2C0_SCL        | I2C / FXOS8700            |
+-------+-----------------+---------------------------+
| PTE25 | I2C0_SDA        | I2C / FXOS8700            |
+-------+-----------------+---------------------------+
| PTA5  | MII0_RXER       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA12 | MII0_RXD1       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA13 | MII0_RXD0       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA14 | MII0_RXDV       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA15 | MII0_TXEN       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA16 | MII0_TXD0       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA17 | MII0_TXD1       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA28 | MII0_TXER       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTB0  | MII0_MDIO       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTB1  | MII0_MDC        | Ethernet                  |
+-------+-----------------+---------------------------+
| PTC16 | ENET0_1588_TMR0 | Ethernet                  |
+-------+-----------------+---------------------------+
| PTC17 | ENET0_1588_TMR1 | Ethernet                  |
+-------+-----------------+---------------------------+
| PTC18 | ENET0_1588_TMR2 | Ethernet                  |
+-------+-----------------+---------------------------+
| PTC19 | ENET0_1588_TMR3 | Ethernet                  |
+-------+-----------------+---------------------------+

.. note::
   由于 PTC16-17 的冲突，不要同时使能以太网和串行蓝牙 HCI。

系统时钟
============

K64F SoC 利用开发板上的 50 MHz 的外部振荡器以及板载的 PLL 产生了一个 120 MHz 的系统时钟。 

串行端口
===========

K64F SoC 有六个 UART，其中一个用于控制台，另一个用于 BT HCI，剩余四个未被使用。 

编程和调试
*************************

烧写
========

FRDM-K64F 开发板上包括一个 `OpenSDA`_ 串行和调试适配器，这个适配器提供了：

- 与主机 PC 的 USB 连接，包括一个大型存储设备和一个 USB 串行端口。
- 一个串行 Flash 设备，实现了 USB flash 磁盘文件存储。
- 一个物理 UART 连接，它以接口 USB 串行端口为中继。

烧写应用程序到 FRDM-K64F
-------------------------------------

此处使用的示例程序是 :ref:`hello_world` 。按照下面的方法编译 Zephyr 内核和应用程序：

.. code-block:: console

   $ cd $ZEPHYR_BASE
   $ . zephyr-env.sh
   $ cd $ZEPHYR_BASE/samples/hello_world/
   $ make BOARD=frdm_k64f

使用 micro-USB 线将 FRDM-K64F 连接到您的主机 PC 后，您应当能看到一个大型存储器（MBED）和一个 USB 串行端口。将编译生成的 zephyr.bin 拷贝到 MBED 驱动器中。

打开一个串行终端（minicom、putty等），并进行如下设置：

- 波特率： 115200
- 数据位： 8
- 奇偶位： 无
- 停止位： 1

然后将开发板进行复位，您就能在相应的串行端口上看到如下的输出：

.. code-block:: console

   Hello World! arm


.. _FRDM-K64F Website:
   http://www.nxp.com/products/software-and-tools/hardware-development-tools/freedom-development-boards/freedom-development-platform-for-kinetis-k64-k63-and-k24-mcus:FRDM-K64F

.. _FRDM-K64F User Guide:
   http://www.nxp.com/assets/documents/data/en/user-guides/FRDMK64FUG.pdf

.. _FRDM-K64F Schematics:
   http://www.nxp.com/assets/downloads/data/en/schematics/FRDM-K64F-SCH-E4.pdf

.. _OpenSDA:
   http://www.nxp.com/products/software-and-tools/hardware-development-tools/startertrak-development-boards/opensda-serial-and-debug-adapter:OPENSDA#FRDM-K64F

.. _K64F Website:
   http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/kinetis-cortex-m-mcus/k-series-performance-m4/k6x-ethernet/kinetis-k64-120-mhz-256kb-sram-microcontrollers-mcus-based-on-arm-cortex-m4-core:K64_120

.. _K64F Datasheet:
   http://www.nxp.com/assets/documents/data/en/data-sheets/K64P144M120SF5.pdf

.. _K64F Reference Manual:
   http://www.nxp.com/assets/documents/data/en/reference-manuals/K64P144M120SF5RM.pdf
