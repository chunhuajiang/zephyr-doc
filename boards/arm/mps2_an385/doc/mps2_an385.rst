.. _mps2_an385_board:

ARM V2M MPS2
############

概览
********

mps2_an385主板配置被Zephyr应用程序用于在V2M MPS2开发板上运行。它提供了对 ARM Cortex-M3 (AN385) CPU 及以下设备的支持：

- 嵌套向量中断控制器 (NVIC)
- System Tick System Clock (SYSTICK)
- Cortex-M System Design Kit UART

.. image:: img/mps2.png
     :width: 442px
     :align: center
     :height: 335px
     :alt: ARM V2M MPS2

有关此开发板的更多信息请参阅 `V2M MPS2 Website`_。

AN385操作说明请参阅 `Application Note AN385`_。

硬件
********

ARM V2M MPS2 提供了以下硬件:

- ARM Cortex-M3 (AN385)
- Cortex-M的ARM IoT 子系统
- 外形尺寸: 140x120cm
- SRAM: 8MB单周期SRAM, 16MB PSRAM
- Video: QSVG触屏面板, 4bit RGB VGA 连接器
- Audio: Audio Codec
- Debug:

  - ARM JTAG20 连接器
  - ARM 并行跟踪连接器 (MICTOR38)
  - 20 pin Cortex 调试连接器
  - 10 pin Cortex 调试连接器
  - 用于FPGA调试的ILA连接器

- 扩展

  - GPIO
  - SPI


支持的功能
==================

mps2_an385主板配置支持以下硬件功能:

+-----------+------------+-------------------------------------+
| 接口      | 控制器     | 驱动/元件                           |
+===========+============+=====================================+
| NVIC      | on-chip    | 嵌套向量中断控制器                  |
+-----------+------------+-------------------------------------+
| SYSTICK   | on-chip    | systick                             |
+-----------+------------+-------------------------------------+
| UART      | on-chip    | 串行端口轮询;                       |
|           |            | 串行端口中断                        |
+-----------+------------+-------------------------------------+
| GPIO      | on-chip    | gpio                                |
+-----------+------------+-------------------------------------+
| WATCHDOG  | on-chip    | 看门狗                              |
+-----------+------------+-------------------------------------+
| TIMER     | on-chip    | 计数器                              |
+-----------+------------+-------------------------------------+
| DUALTIMER | on-chip    | 计数器                              |
+-----------+------------+-------------------------------------+

本Zephyr端口还不支持其它硬件。
V2M MPS2开发板的完整硬件功能列表请参阅 `V2M MPS2 Website`_ 。

默认配置可在defconfig文件中找到:

.. code-block:: console

   boards/arm/mps2_an385/mps2_an385_defconfig

中断控制器
====================

MPS2是一块基于Cortex-M3的SoC，具有15个固定异常和45个IRQ。

基于Cortex-M3/4的开发板使用矢量异常，这意味着每个异常都从向量表直接调用处理程序（句柄）。

为异常提供的句柄为 1-6、11-12和14-15。下表标识了每个异常所使用的句柄。

+------+------------+----------------+--------------------------+
| Exc# | 名称       | 注释           | Zephyr内核用于           |
+======+============+================+==========================+
| 1    | Reset      |                | 系统初始化               |
+------+------------+----------------+--------------------------+
| 2    | NMI        |                | 系统致命错误             |
+------+------------+----------------+--------------------------+
| 3    | Hard fault |                | 系统致命错误             |
+------+------------+----------------+--------------------------+
| 4    | MemManage  | MPU 故障       | 系统致命错误             |
+------+------------+----------------+--------------------------+
| 5    | Bus        |                | 系统致命错误             |
+------+------------+----------------+--------------------------+
| 6    | Usage      | 未定义指令或试 | 系统致命错误             |
|      | fault      | 图切换至ARM模  |                          |
|      |            | 式             |                          |
+------+------------+----------------+--------------------------+
| 11   | SVC        |                | 上下文切换和软件中断     |
+------+------------+----------------+--------------------------+
| 12   | Debug      |                | 系统致命错误             |
|      | monitor    |                |                          |
+------+------------+----------------+--------------------------+
| 14   | PendSV     |                | 上下文切换               |
+------+------------+----------------+--------------------------+
| 15   | SYSTICK    |                | 系统时钟                 |
+------+------------+----------------+--------------------------+

引脚映射
===========

ARM V2M MPS2开发板有4个GPIO控制器。这些控制器负责引脚复用、输入/输出、上拉等等。

GPIO 控制器引脚所对应的引脚号为： 

- GPIO 0：Pins 0 - 15  
- GPIO 1：Pins 16 - 31  
- GPIO 2：Pins 32 -  47  
- GPIO 3：Pins 48 -  51 

ARM MPS2开发板引脚到GPIO控制器的映射：

.. hlist::
   :columns: 3

   - D0 : EXT_0
   - D1 : EXT_4
   - D2 : EXT_2
   - D3 : EXT_3
   - D4 : EXT_1
   - D5 : EXT_6
   - D6 : EXT_7
   - D7 : EXT_8
   - D8 : EXT_9
   - D9 : EXT_10
   - D10 : EXT_12
   - D11 : EXT_13
   - D12 : EXT_14
   - D13 : EXT_11
   - D14 : EXT_15
   - D15 : EXT_5
   - D16 : EXT_16
   - D17 : EXT_17
   - D18 : EXT_18
   - D19 : EXT_19
   - D20 : EXT_20
   - D21 : EXT_21
   - D22 : EXT_22
   - D23 : EXT_23
   - D24 : EXT_24
   - D25 : EXT_25
   - D26 : EXT_26
   - D27 : EXT_30
   - D28 : EXT_28
   - D29 : EXT_29
   - D30 : EXT_27
   - D31 : EXT_32
   - D32 : EXT_33
   - D33 : EXT_34
   - D34 : EXT_35
   - D35 : EXT_36
   - D36 : EXT_38
   - D37 : EXT_39
   - D38 : EXT_40
   - D39 : EXT_44
   - D40 : EXT_41
   - D41 : EXT_31
   - D42 : EXT_37
   - D43 : EXT_42
   - D44 : EXT_43
   - D45 : EXT_45
   - D46 : EXT_46
   - D47 : EXT_47
   - D48 : EXT_48
   - D49 : EXT_49
   - D50 : EXT_50
   - D51 : EXT_51

外设映射：

.. hlist::
   :columns: 3

   - UART_3_RX : D0
   - UART_3_TX : D1
   - SPI_3_CS : D10
   - SPI_3_MOSI : D11
   - SPI_3_MISO : D12
   - SPI_3_SCLK : D13
   - I2C_3_SDA : D14
   - I2C_3_SCL : D15
   - UART_4_RX : D26
   - UART_4_TX : D30
   - SPI_4_CS : D36
   - SPI_4_MOSI : D37
   - SPI_4_MISO : D38
   - SPI_4_SCK : D39
   - I2C_4_SDA : D40
   - I2C_4_SCL : D41

获取更多详细信息请参阅 `MPS2 Technical Reference Manual (TRM)`_。

系统时钟
============

V2M MPS2 主时钟为 24 MHz。

串口
===========

V2M MPS2有5个UARTs。所有UART仅有两根线用于发送/接收，而且无流控制(CTS/RTS)或FIFO。Zephyr控制台输出默认使用UART0。

编程与调试
*************************

烧写
========

V2M MPS2 提供:

- 一个连接至电脑主机的USB连接器，显示为大容量存储器及USB串口。
- 一个串行Flash设备，实现了USB flash存储器文件存储。
- 一个物理UART连接器， 它是USB串口的中继接口。

在V2M MPS2中烧写应用程序
-----------------------------------

本指南使用了示例应用程序 :ref:`hello_world` :

.. code-block:: console

   $ZEPHYR_BASE/samples/hello_world

编译Zephyr内核及应用程序，请输入:

.. code-block:: console

   $ cd $ZEPHYR_BASE
   $ . zephyr-env.sh
   $ cd $ZEPHYR_BASE/samples/hello_world/
   $ make BOARD=mps2_an385

将V2M MPS2通过USB口连接至你的电脑主机，你将看到一个USB连接器，显示为大容量存储器及一个USB串口。拷贝生成的zephyr.bin到所显示的驱动器。重启开发板，你将看到相应的串口信息：

.. code-block:: console

   Hello World! arm


.. _V2M MPS2 Website:
   https://developer.mbed.org/platforms/ARM-MPS2/

.. _MPS2 Technical Reference Manual (TRM):
   http://infocenter.arm.com/help/topic/com.arm.doc.100112_0200_05_en/versatile_express_cortex_m_prototyping_systems_v2m_mps2_and_v2m_mps2plus_technical_reference_100112_0200_05_en.pdf

.. _Application Note AN385:
   http://infocenter.arm.com/help/topic/com.arm.doc.dai0385c/DAI0385C_cortex_m3_on_v2m_mps2.pdf
