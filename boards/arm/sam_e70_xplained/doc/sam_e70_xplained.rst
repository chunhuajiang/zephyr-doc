.. _sam_e70_xplained:

SAM E70 Xplained
################

概览
********

SAM E70 Xplained评估套件是用于评估Atmel SAM E70系列微控制器的开发平台。

硬件
********

- ATSAME70Q21 ARM Cortex-M7 处理器
- 12 MHz 晶振
- 32.768 kHz 晶振 (未插入)
- AT24MAC402 EEPROM
- IS42S16100E 16 Mb SDRAM
- SD card 连接器
- 以太网端口
- Micro-AB USB 设备
- 支持CMSIS-DAP的Micro-AB USB debug 接口 , 虚拟COM口及Data Gateway Interface (DGI数据网关接口)
- JTAG 接口连接器
- 一个重启按钮及一个用户按钮
- 一个绿色用户LED

支持功能
==================

sam_e70_xplained 开发板配置支持以下硬件功能：

+-----------+------------+-------------------------------------+
| Interface | Controller | Driver/Component                    |
+===========+============+=====================================+
| NVIC      | on-chip    | 嵌套向量中断控制器  |
+-----------+------------+-------------------------------------+
| SYSTICK   | on-chip    | systick                             |
+-----------+------------+-------------------------------------+
| USART     | on-chip    | 串口                         |
+-----------+------------+-------------------------------------+
| ETHERNET  | on-chip    | 以太网                            |
+-----------+------------+-------------------------------------+
| WATCHDOG  | on-chip    | 看门狗                            |
+-----------+------------+-------------------------------------+

当前Zephyr还未支持其它的硬件功能。

默认配置可在Kconfig文件中找到
:file:`boards/arm/sam_e70_xplained/sam_e70_xplained_defconfig`.

连线及IOs
===================

`SAME70-XPLD User Guide`_ 详细描述了主板连线信息

系统时钟
============

SAM E70 MCU 在主板上配置使用12 MHz外部晶振，配合芯片内的PLL产生300MHz系统时钟。

串口
===========

ATSAME70Q21 MCU 有5个UART和3个USART。其中一个USART配置用于控制台，还可以通过EDBG USB芯片当成虚拟COM口使用。

编程与调试
*************************

烧写
========

将Zephyr项目烧写进SAM E70 MCU需要 `OpenOCD tool`_ 工具。OpenOCD release 0.10.0加入了对Atmel SAM E系列微控制器的支持。而当前Zephyr SDK中使用的OpenOCD版本是0.9。很不幸，它并不支持Atmel SAM E系列微控制器。当前主要的Linux发行版本很少提供OpenOCD 0.10.0版本包，你需要自行编译和安装它。务必打开对CMSIS-DAP的支持，因为这是主板EDBG芯片所使用的调试接口。

默认情况下，新出厂的SAM E70芯片将从位于ROM的SAM-BA boot loader而非flash镜像启动。可使用Atmel的系统程序SAM Boot Assistant (`SAM-BA`_) 对GPNVM1（General-Purpose NVM的第一个位）重新编程以进行改变。这个操作只需进行一次，如果不需要对固件进行调试，也可以使用SAM-BA而不是OpenOCD来烧写项目。

#. 编译Zephyr内核及应用程序：

   .. code-block:: console

      $ cd $ZEPHYR_BASE/samples/hello_world/
      $ make BOARD=sam_e70_xplained

#. 使用USB debug接口将SAM E70 Xplained开发板连接至你的电脑主机。

#. 运行你喜欢的终端程序监听输出。Linux下终端应为 :code:`/dev/ttyACM0`。例如：

   .. code-block:: console

      $ minicom -D /dev/ttyACM0 -o

   -o选项让minicom不发送modem的初始化字串。连接配置如下：

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1

#. 烧写镜像，假设OpenOCD工具已经安装，输入：

   .. code-block:: console

      $ openocd -f board/atmel_same70_xplained.cfg -c "program outdir/sam_e70_xplained/zephyr.elf verify reset exit"

   该命令还将验证镜像是否被正确编程，重启开发板并运行Zephyr应用程序。

   你将在终端看到“Hello World!”

调试
=========

#. 使用USB debug接口将SAM E70 Xplained开发板连接至你的电脑主机。

#. 在电脑主机上启动GDB服务

   .. code-block:: console

      $ openocd -f board/atmel_same70_xplained.cfg&

#. 现在你可以使用GDB对目标板进行远程连接及调试。GDB服务默认监听3333端口。

参考
**********

SAM E70 产品页:
    http://www.atmel.com/products/microcontrollers/arm/sam-e.aspx

.. _SAME70-XPLD User Guide:
    http://www.atmel.com/Images/Atmel-44050-Cortex-M7-Microcontroller-SAM-E70-XPLD-Xplained_User-guide.pdf

.. _OpenOCD tool:
    http://openocd.org/

.. _SAM-BA:
    http://www.atmel.com/tools/ATMELSAM-BAIN-SYSTEMPROGRAMMER.aspx
