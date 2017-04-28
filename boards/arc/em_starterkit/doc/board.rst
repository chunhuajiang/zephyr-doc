.. _em_starterkit:

DesignWare(R) ARC(R) EM 入门套件
###################################

概览
********

The DesignWare(R) ARC(R) EM 入门套件是一款低成本、多功能的解决方案，可进行快速软件开发，软件调试，以及对ARC EM系列处理器进行学习分析。EM系列包括 EM4、EM6、EM5D、EM7D、EM9D和EM11D内核。Zephyr RTOS可用于EM入门套件。

.. image:: ARC_EM_Starter_Kit_Board_Photo.jpg
   :width: 442px
   :align: center
   :alt: DesignWare(R) ARC(R) EM Starter Kit (synopsys.com)

ARC EM 入门套件由一个硬件平台组成，包括不同外设的ARC EM处理器配置预安装FPGA镜像。此开发板文档可在以下URL中找到：
https://www.embarc.org.

也可阅读以下URL获取此开发板的详细信息:
https://www.synopsys.com/dw/ipdir.php?ds=arc_em_starter_kit

EM入门套件板的默认配置可在以下路径找到 :file:`boards/arc/em_starterkit/em_starterkit_defconfig`.

此开发板的默认SOC为 EM9D。它的配置为Harvard体系结构，具有单独的指令总线和数据总线。指令存储器称为ICCM，数据存储器称为DCCM。EM9D配置文件可在 :file:`arch/arc/soc/em9d/Kconfig.defconfig` 中找到。

如果使用更大的程序，可选择EM7D或EM11D，它可以访问到带i-cache和d-cache的128KB DRAM。EM7D配置文件在:file:`arch/arc/soc/em7d/Kconfig.defconfig`。EM11D的在:file:`arch/arc/soc/em11d/Kconfig.defconfig`。

硬件
********
主板布局
============

ARC EM 入门套件主板有6个Pmod连接器。它们可以被配置为支持I2C、GPIO、UART或SPI设备附件。

此主板配置了一个16MB SPI-FLASH 及一个SDCard存储器。还有9个LEDs，3个按钮及4个可用于GPIO的dip开关。

Xilinx Spartan(R)-6 LX150 FPGA可自动装载3个FPGA SOC二进制文件中的一个：EM7D、EM9D或EM11D SOC。

开发板的文档和一般信息可在`embARC-website`_中找到，其中还包含一些免费示例软件。

支持的功能
==================

Zephy内核通过设备驱动程序可支持EM入门套件的多个硬件功能。

EM入门套件支持 6个Digilent Pmod(TM) Interfaces，它使存储、通信、传感器、显示器等多种可插拔模块的使用成为可能。通过使用Pmod接口，你可使用Zephyr RTOS实现应用程序。

下表显示了对哪些驱动的支持，以及各功能所对应的体系：

+-----------+------------+-----+-------+-----------------------+
| 接口      | 控制器     |EM9D | EM11D | 驱动/元件             |
+===========+============+=====+=======+=======================+
| INT       | on-chip    | Y   | Y     | 中断控制器            |
+-----------+------------+-----+-------+-----------------------+
| UART      | usb +      | Y   | Y     | 串行端口轮询;         |
|           | 2 Pmods    |     |       | 串行端口中断          |
+-----------+------------+-----+-------+-----------------------+
| SPI       | 2 Pmods    | Y   | Y     | spi                   |
+-----------+------------+-----+-------+-----------------------+
| ADC       | n/a        | N   | N     | adc (can add via Pmod)|
+-----------+------------+-----+-------+-----------------------+
| I2C       | 2 Pmods    | Y   | Y     | i2c                   |
+-----------+------------+-----+-------+-----------------------+
| GPIO      | 6 Pmods    | Y   | Y     | gpio                  |
+-----------+------------+-----+-------+-----------------------+
| PWM       | n/a        | N   | N     | pwm                   |
+-----------+------------+-----+-------+-----------------------+

开发板有3个(消抖和中断)使用GPIO的按钮，4个dip开关，9个LED，使用SPI的SDCard和一个16MB SPI-Flash 闪存。

SPI-Flash还持有了3可4个单独的FPGA CPU二进制文件，可通过dip开关进行选择。

SPI-Flash还可通过bootloader进行编程。booloader可将程序镜像从SPI-Flash拷贝到可执行内存。如果设置了CONFIG_XIP，Zephyr在初始化时将拷贝初始数据段至数据存储器。


编程和调试
*************************

需要的硬件和软件
==============================

要在EM入门套件板中使用Zephyr RTOS应用程序，需要一些额外的硬件。

* USB线缆 (ARC EM入门套件的一部分)

* USB线缆向主板提供电源；尽管如此，如果主板独立运行，通用开关电源适配器(110-240V AC to 5V DC)也可给主板供电，它包含在套件内。

* :ref:`The Zephyr SDK <zephyr_sdk>`

* USB-UART终端模拟软件，建议使用： http://www.putty.org.

* (可选项) Pmods集合。参考 http://store.digilentinc.com/pmod-peripheral-modules 或开发自定义接口连接到Pmod连接器。

编译示例应用程序
==============================

你可尝试很多示例应用程序和测试，但我们只讨论其中的一个 :ref:`hello_world`。它可在 :file:`$ZEPHYR_BASE/samples/hello_world`中找到。

如果示例中没有，你可能需要写一个prj_arc.conf文件。接下来，你可以使用menuconfig规则配置目标
通过提供 "BOARD=em_starterkit"参数，你可以选择Zephyr所支持的ARC EM入门套件板。

.. code-block:: console

   $ make menuconfig BOARD=em_starterkit

对于这块开发板，你还需要考虑 "ARC SoC Selection"，将其设置为EM9D或EM11D。要在开发板中启动EM9D，除了开关1，所有dip开关都应处于UP状态。其它选项正常选择即可。要启动开发板上的EM11D，除了开关2，所有dip开关都应处于UP状态。接下来按下“ARC” logo中字母C上方的按钮。

编译应用程序，执行make命令:

.. code-block:: console

   $ make BOARD=em_starterkit

连接串口输出
=========================

在默认配置下，Zephyr的EM入门套件镜像支持通过主板上的UART1支持串口输出。要启用串口输出:

在开发环境中需要:

* 打开串口模拟器 (如Linux下的minicom, putty, screen等等)
* 指定tty驱动名称，例如在Linux下，可能为 :file:`/dev/ttyUSB1`
* 通信属性设置为:

========= =====
Parameter Value
========= =====
Baud:     115200
Data:     8 bits
Parity:    None
Stopbits:  1
========= =====

调试
==========
在调试之前，你需要下载并安装ARC GNU工具的Synopsys版本。不幸的是，当前Zephyr-SDK版本的openocd和gdb存在着一些功能性限制，在ARC EM入门套件中不能很好地工作。

Synopsys工具可在GITHUB中找到:

https://github.com/foss-for-synopsys-dwc-arc-processors/toolchain/releases/tag/arc-2016.03

在Linux中，你需要:

* arc_gnu_2016.03_ide_linux_install.tar.gz
* arc_gnu_2016.03_prebuilt_elf32_be_linux_install.tar.gz

可将它们解压至任意目录，建议: /usr/local/arc。接下来按照说明设置这些工具，你需要更改路径以找到它们的bin目录，这样就可以找到这些交叉开发工具了。

创建一个bash脚本来运行openock也是非常有用的，因为像我一样，很难记住这些参数。我所使用的放置在一个叫ocd的文件中。

.. code-block:: console

  #!/bin/bash
  openocd -c 'gdb_port 3333' -s $ARCGNU_IDE/share/openocd/scripts -f board/snps_em_sk_v2.2.cfg

  #where the environment variable ARCGNU_IDE refers to the install dir of the
  #openocd IDE

此命令让 openocd 使用gdb客户端的 3333 端口，并提供ARC EM入门套件的的主板cfg文件。

我还发现有个脚本非常有用，名字叫debug.sh，它提供了gdb的所有参数:

.. code-block:: console

   #!/bin/bash
   arc-elf32-gdb \
    -ex "target remote :3333" \
    -ex "load" \
    -ex "break __memory_error" \
    -ex "break _SysFatalErrorHandler" \
    -ex "set remotetimeout 2000" \
    outdir/em_starterkit/zephyr.elf

远程目标将附加到openocd上，并将elf文件加载到内存。你也可以在CPU异常处理程序或致命错误处理程序中设置断点。

现在使用这两个脚本变得非常容易。按下“C”按钮启动SOC，确保digilent线缆已从EM入门套件板连接至你的主机。

在任意终端窗口，首先调用"ocd"脚本。它将跟开发板建立关联并输出很多信息，例如：

.. code-block:: console

   Open On-Chip Debugger 0.9.0-dev-g90a4ff5 (2016-05-04-15:37)
   Licensed under GNU GPL v2
   For bug reports, read
   http://openocd.sourceforge.net/doc/doxygen/bugs.html
   adapter speed: 5000 kHz
   Info : clock speed 5000 kHz
   Info : JTAG tap: arc-em.cpu tap/device found: 0x200044b1 (mfg: 0x258, part: 0x0004, ver: 0x2)
   Info : JTAG tap: arc-em.cpu tap/device found: 0x200044b1 (mfg: 0x258, part: 0x0004, ver: 0x2)
   target state: halted
   target state: halted

在第二个控制台窗口，导航到你的示例应用程序的目录，并调用debug.sh脚本:

.. code-block:: console

   GNU gdb (ARCompact/ARCv2 ISA elf32 toolchain 2016.03) 7.10
   Copyright (C) 2015 Free Software Foundation, Inc.
   License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
   This is free software: you are free to change and redistribute it.
   There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
   and "show warranty" for details.
   This GDB was configured as "--host=x86_64-unknown-linux-gnu --target=arc-elf32".
   Type "show configuration" for configuration details.
   For bug reporting instructions, please see:
   <https://github.com/foss-for-synopsys-dwc-arc-processors/toolchain/issues>.
   Find the GDB manual and other documentation resources online at:
   <http://www.gnu.org/software/gdb/documentation/>.
   For help, type "help".
   Type "apropos word" to search for commands related to "word"...
   Reading symbols from outdir/zephyr.elf...done.
   Remote debugging using :3333
   0x000077b4 in ?? ()
   Loading section text, size 0x3714 lma 0x0
   Loading section devconfig, size 0x78 lma 0x3714
   Loading section gpio_compat, size 0x20 lma 0x378c
   Loading section rodata, size 0x244 lma 0x37ac
   Loading section datas, size 0x714 lma 0x80000000
   Loading section initlevel, size 0x78 lma 0x80000714
   Loading section _k_task_list, size 0x58 lma 0x8000078c
   Loading section _k_task_ptr, size 0x8 lma 0x800007e4
   Loading section _k_event_list, size 0x10 lma 0x800007ec
   Start address 0x36f4, load size 16876
   Transfer rate: 122 KB/sec, 1406 bytes/write.
   Breakpoint 1 at 0x3264: file /home/johndoe/repository/zephyr/arch/arc/core/fault_s.S, line 81.
   Breakpoint 2 at 0x3628: file /home/johndoe/repository/zephyr/arch/arc/core/sys_fatal_error_handler.c, line 73.
   (gdb)

此时，你可以执行正常的debug对话。设置断点并按‘c’继续执行程序。

烧写
========

大多数时候，你无需烧写应用程序，而是使用openocd和gdb进行调试。程序可通过USB线缆下载至代码和数据内存。

当你准备好布署应用程序，以便它开机自动复位或上电，你可以依据步骤来将程序放置在SPI-FLASH。


关于如何将程序写入SPI-FLASH，可参考`embARC-website`_中有关ARC EM入门套件的文档，它包含了如何将可执行镜像文件以bootloader可理解的方式放入SPI-FLASH的说明。


发行说明
*************

以下是待办事项列表：

* :jira:`ZEP-1153`: Zephyr所需的i-cache API (所有目标)
* :jira:`ZEP-713`: Zephyr ARC端口还不支持嵌套规则中断。
* 引脚复用驱动: 可能在配置PMod时需要写它。

参考
**********

.. _embARC-website: https://www.embarc.org

.. _emstarterkit-website: https://www.synopsys.com/dw/ipdir.php?ds=arc_em_starter_kit

.. _digilent-website: http://store.digilentinc.com

.. _putty-website: http://www.putty.org
