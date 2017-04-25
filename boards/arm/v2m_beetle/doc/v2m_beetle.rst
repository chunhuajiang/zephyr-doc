.. _v2m_beetle_board:

ARM V2M Beetle
##############

概览
********

v2m_beetle板配置被用于在V2M Beetle开发板上运行Zephyr应用程序。它提供了对Beetle ARM Cortex-M3 CPU及以下设备的支持：

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Cortex-M System Design Kit GPIO
- Cortex-M System Design Kit UART

.. image:: img/v2m_beetle.png
     :width: 442px
     :align: center
     :height: 335px
     :alt: ARM V2M Beetle

更多有关此开发板的信息可在 `V2M Beetle Website`_中找到。

硬件
********

ARM V2M BEETLE提供了以下硬件：

- ARM Cortex-M3
- Cortex-M ARM物联网子系统
- CORDIO蓝牙智能无线
- 内存

  - 256KB内嵌flash
  - 128KB SRAM
  - 2MB外部QSPI flash.

- 调试

  - JTAG, SWD & 4 bit TRACE
  - 带UART虚拟端口的CMSIS-DAP

- Arduino接口

  - GPIO, UART, SPI, I2C
  - 模拟信号


支持的功能
===================

v2m_beetle板配置支持以下硬件功能：

+-----------+------------+-------------------------------------+
| Interface | Controller | Driver/Component                    |
+===========+============+=====================================+
| NVIC      | on-chip    | 嵌套中断向量控制器 |
+-----------+------------+-------------------------------------+
| SYSTICK   | on-chip    | systick                             |
+-----------+------------+-------------------------------------+
| UART      | on-chip    | 串口轮询               |
|           |            | 串口中断               |
+-----------+------------+-------------------------------------+
| PINMUX    | on-chip    | 引脚复用                              |
+-----------+------------+-------------------------------------+
| GPIO      | on-chip    | gpio                                |
+-----------+------------+-------------------------------------+
| WATCHDOG  | on-chip    | 看门狗                            |
+-----------+------------+-------------------------------------+
| TIMER     | on-chip    | 定时器                               |
+-----------+------------+-------------------------------------+

暂不支持其它硬件功能，参考 `V2M Beetle Website`_ 获取V2M Beetle开发板的硬件功能完整列表。

默认配置可在以下defconfig文件中找到：

.. code-block:: console

   boards/arm/v2m_beetle/v2m_beetle_defconfig

中断控制器
====================

Beetle是一款基于Cortex-M3的SOC，拥有15个固定异常和45个IRQ。

基于Cortex-M3/4的主板使用矢量异常，这意味着每个异常直接从向量表调用句柄。

为异常提供的句柄号为1-6、11-12和14-15。下表列出了每个异常所对应的句柄。

+------+------------+----------------+--------------------------+
| Exc# | 名称       | 注释        | Zephyr内核使用    |
+======+============+================+==========================+
| 1    | Reset      |                | 系统初始化    |
+------+------------+----------------+--------------------------+
| 2    | NMI        |                | 系统致命错误       |
+------+------------+----------------+--------------------------+
| 3    | Hard fault |                | 系统致命错误        |
+------+------------+----------------+--------------------------+
| 4    | MemManage  | MPU 错误       | 系统致命错误        |
+------+------------+----------------+--------------------------+
| 5    | Bus        |                | 系统致命错误        |
+------+------------+----------------+--------------------------+
| 6    | Usage      | 未定义指令或    | 系统致命错误        |
|      | fault      | 尝试切换到      |                          |
|      |            | ARM模式        |                          |
+------+------------+----------------+--------------------------+
| 11   | SVC        |                | 上下文切换和软件中断       |
+------+------------+----------------+--------------------------+
| 12   | Debug      |                | 系统致命错误       |
|      | monitor    |                |                          |
+------+------------+----------------+--------------------------+
| 14   | PendSV     |                | 上下文切换           |
+------+------------+----------------+--------------------------+
| 15   | SYSTICK    |                | 系统时钟             |
+------+------------+----------------+--------------------------+

引脚复用
===========

ARM V2M Beetle开发板有4个GPIO控制器。这些控制器负责引脚复用、输入/输出、上拉等等。

以下为每个GPIO控制器所对应的引脚号：

- Pins 0 - 15 对应 GPIO 0
- Pins 16 - 31 对应 GPIO 1

从ARM V2M Beetle开发板引脚到GPIO控制器的映射：

.. hlist::
   :columns: 3

   - D0 : P0_0
   - D1 : P0_1
   - D2 : P0_2
   - D3 : P0_3
   - D4 : P0_4
   - D5 : P0_5
   - D6 : P0_6
   - D7 : P0_7
   - D8 : P0_8
   - D9 : P0_9
   - D10 : P0_10
   - D11 : P0_11
   - D12 : P0_12
   - D13 : P0_13
   - D14 : P0_14
   - D15 : P0_15
   - D16 : P1_0
   - D17 : P1_1
   - D18 : P1_2
   - D19 : P1_3
   - D20 : P1_4
   - D21 : P1_5
   - D22 : P1_6
   - D23 : P1_7
   - D24 : P1_8
   - D25 : P1_9
   - D26 : P1_10
   - D27 : P1_11
   - D28 : P1_12
   - D29 : P1_13
   - D30 : P1_14
   - D31 : P1_15

Peripheral Mapping:

.. hlist::
   :columns: 3

   - UART_0_RX : D0
   - UART_0_TX : D1
   - SPI_0_CS : D10
   - SPI_0_MOSI : D11
   - SPI_0_MISO : D12
   - SPI_0_SCLK : D13
   - I2C_0_SCL : D14
   - I2C_0_SDA : D15
   - UART_1_RX : D16
   - UART_1_TX : D17
   - SPI_1_CS : D18
   - SPI_1_MOSI : D19
   - SPI_1_MISO : D20
   - SPI_1_SCK : D21
   - I2C_1_SDA : D22
   - I2C_1_SCL : D23

更多详细信息请参考： `Beetle Technical Reference Manual (TRM)`_.

系统时钟
============

V2M Beetle拥有一个外部晶振和两个片内晶振。慢时钟为32.768KHz，主时钟为24MHz。处理器可设置PLL来驱动主时钟。

串口
===========

ARM Beetle处理器有两个UART。两个UART都仅为两根线RX/TX，无流控制（CTS/RTS）或FIFO。Zephyr控制台输出，默认使用UART1。

编程与调试
*************************

烧写
========

CMSIS DAP
---------

V2M Beetle提供：

- 一个到计算机主机的USB连接器，它可用于大容量存储器和USB串口。
- 一个串行Flash设备，可实现USB闪存盘文件存储。
- 一个物理UART连接器，是USB串口的中继接口。

此接口通过CMSIS DAP暴露。获取更详细信息请参考`CMSIS-DAP Website`_。

将应用程序烧写进V2M Beetle
-------------------------------------

此说明讲解如何使用示例应用程序 :ref:`hello_world`:

.. code-block:: console

   $ZEPHYR_BASE/samples/hello_world

编译Zephyr内核及应用程序，输入：

.. code-block:: console

   $ cd $ZEPHYR_BASE
   $ . zephyr-env.sh
   $ cd $ZEPHYR_BASE/samples/hello_world/
   $ make BOARD=v2m_beetle

使用USB接口将V2M Beetle连接至你的计算机主机，你将看到一个大容量存储器的USB连接器以及一个USB串口。拷贝生成的zephyr.bin至MBED驱动器。重启开发板，你将在相应的串口看到以下信息：

.. code-block:: console

   Hello World! arm


.. _V2M Beetle Website:
   https://www.arm.com/products/tools/development-boards/versatile-express/beetle_iot_evaluation_platform.php

.. _Beetle Technical Reference Manual (TRM):
   https://developer.arm.com/-/media/developer/products/system-design-tools/versatile-express-family/V2M-Beetle_TRM_draft.pdf?la=en

.. _CMSIS-DAP Website:
   https://github.com/mbedmicro/CMSIS-DAP
