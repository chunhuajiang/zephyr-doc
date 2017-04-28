.. _altera_max10:

Altera MAX10
############

概览
********


Zephyr内核支持 Altera MAX10 Rev C 开发板，它使用了Nios II Gen 2 soft CPU。

.. figure:: img/max_10_dev_kit_top_photo.jpg
   :width: 442px
   :align: center
   :alt: Altera’s MAX* 10

   Altera’s MAX* 10  (Credit: Altera)

硬件
********

DIP开关设置
===================

电路板背面有两套开关。尤其重要的是SW2：

* 开关2 (CONFIG_SEL) 应该在 OFF (up) 位置，这样第一启动镜像就是CFM0
* 开关3 (VTAP_BYPASS) 需要在 ON (down) 位置或者烧写脚本将不工作
* 开关4 (HSMC_BYPASSN) 应为 OFF (up)

.. image:: img/Altera_MAX10_switches.jpg
   :width: 442px
   :align: center
   :alt: Altera’s MAX* 10 Switches

其它开关为用户开关，它们的位置由应用程序指定。

必要的软件
==================

为了在这些设备上正常工作，你将需要Altera Quartus SDK。`Altera Lite Distribution`_ of Quartus 可免费获得。

为了方便起见，一旦安装，应将SDK所提供的二进制文件放入你所处的路径。下面是一个例子，将ALTERA_BASE改为你安装SDK的地方：

.. code-block:: console

   export ALTERA_BASE=/opt/altera_lite/16.0
   export PATH=$PATH:$ALTERA_BASE/quartus/bin:$ALTERA_BASE/nios2eds/bin

你可能需要调整udev规则，这样就可以告诉USB Blaster II外设，哪个是此设备的内置JTAG接口。

以下是Fedora 23中使用的命令:

.. code-block:: console

   # For Altera USB-Blaster permissions.
   SUBSYSTEM=="usb",\
   ENV{DEVTYPE}=="usb_device",\
   ATTR{idVendor}=="09fb",\
   ATTR{idProduct}=="6010",\
   MODE="0666",\
   NAME="bus/usb/$env{BUSNUM}/$env{DEVNUM}",\
   RUN+="/bin/chmod 0666 %c"
   SUBSYSTEM=="usb",\
   ENV{DEVTYPE}=="usb_device",\
   ATTR{idVendor}=="09fb",\
   ATTR{idProduct}=="6810",\
   MODE="0666",\
   NAME="bus/usb/$env{BUSNUM}/$env{DEVNUM}",\
   RUN+="/bin/chmod 0666 %c"

可使用SDK jtagconfig工具测试连通性, 你将看到类似如下信息：

.. code-block:: console

   $ jtagconfig
   1) USB-BlasterII [1-1.2]
     031050DD   10M50DA(.|ES)/10M50DC
     020D10DD   VTAP10


CPU相关
=============

Nios II/f 内核的CPU相关设计包含在Zephyr树中。可在 :file:`arch/nios2/soc/nios2f-zephyr/cpu` 目录中找到。

烧写此CPU，请使用 :file:`arch/nios2/soc/nios2f-zephyr/cpu/nios2-configure-sof`工具：

.. code-block:: console

   $ nios2-configure-sof ghrd_10m50da.sof

此CPU为Nios II/F内核，具有一个 16550 UART、JTAG UART、和Avalon定时器。对于 Nios II SOC 的定义，你可在SOC所包含的目录中查阅system.h来找到关于CPU配置的更详细信息。

控制台输出
==============

16550 UART
----------

默认情况下，内核被配置为向16550 UART发送控制台输出。
您可以通过连接到主板右上方迷你USB端口（它将作为ttyUSB节点出现在 /dev中）来监视工作站上的这一点。
然后运行minicom，并禁用流控制，参数设置为 115200-8N1 。

JTAG UART
---------

你还可以将控制台输出发送到JTAG UART。在你的项目配置中设置:

.. code-block:: console

   CONFIG_UART_ALTERA_JTAG=y
   CONFIG_UART_CONSOLE_ON_DEV_NAME="jtag_uart0"

要在本地工作站看到这些信息，在SDK中运行终端应用程序：

.. code-block:: console

   $ nios2-terminal

编程和调试
*************************

烧写
========

将内核烧入 UFM
------------------------
这一步很简单:

.. code-block:: console

   $ make flash

使用 scripts/support/quartus-flash.py 脚本，将向主板提供Zephyr内核以及CPU配置。完成后内核将立即重启。


直接通过JTAG将内核烧写进RAM
-------------------------------------------

SDK所包含的nios2-download工具可让你将内核直接烧写进RAM，并从 __start 标记启动。

为了让它工作，整个内核都必须位于RAM之中。确保禁用以下配置选项：

.. code-block:: console

   CONFIG_XIP=n
   CONFIG_INCLUDE_RESET_VECTOR=n

内核编译完成后，将它压入设备的RAM内：

.. code-block:: console

   $ nios2-download --go outdir/zephyr.elf

如果在运行一个控制台会话minicom或nios2-terminal) ，你将会看到应用程序输出。你可以向nios2-download传递额外参数从而启动GDB服务并连接它，如下所述，仅仅使用nios2-gdb-server是非常简单的。

调试
=========

Altera SDK包含了一个GDB服务器，它可用于调试MAX10主板。你还可以调试已经烧入User Flash Memory (UFM)的设备的正在运行的镜像，或使用GDB通过JTAG加载镜像。

使用UFM Flashed镜像进行调试
--------------------------------

可通过"make debug"编译目标来完成此功能：

.. code-block:: console

   $ make debug
   make[1]: Entering directory '/projects/zephyr2'
   make[2]: Entering directory '/projects/zephyr2/tests/crypto/test_sha256/outdir'
     Using /projects/zephyr2 as source for kernel
     GEN     ./Makefile
     CHK     include/generated/version.h
     CHK     misc/generated/configs.c
     CHK     include/generated/offsets.h
     CHK     misc/generated/sysgen/prj.mdef
   Nios II GDB server running on port 14777
   Ignoring --stop option because --tcpport also specified
   Python Exception <type 'exceptions.ImportError'> No module named gdb:
   /opt/zephyr-sdk/sysroots/i686-pokysdk-linux/usr/bin/nios2-poky-elf/nios2-poky-elf-gdb: warning:
   Could not load the Python gdb module from `/opt/zephyr-sdk/2.0.1/sysroots/i686-pokysdk-linux/usr/share/gdb/python'.
   Limited Python support is available from the _gdb module.
   Suggest passing --data-directory=/path/to/gdb/data-directory.

   GNU gdb (GDB) 7.9.1
   Copyright (C) 2015 Free Software Foundation, Inc.
   License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
   This is free software: you are free to change and redistribute it.
   There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
   and "show warranty" for details.
   This GDB was configured as "--host=i686-pokysdk-linux --target=nios2-poky-elf".
   Type "show configuration" for configuration details.
   For bug reporting instructions, please see:
   <http://www.gnu.org/software/gdb/bugs/>.
   Find the GDB manual and other documentation resources online at:
   <http://www.gnu.org/software/gdb/documentation/>.
   For help, type "help".
   Type "apropos word" to search for commands related to "word"...
   Reading symbols from /projects/zephyr2/tests/crypto/test_sha256/outdir/zephyr.elf...done.
   Remote debugging using :14777
   Using cable "USB-BlasterII [1-1.6.1]", device 1, instance 0x00
   Resetting and pausing target processor: OK
   Listening on port 14777 for connection from GDB: accepted
   vprintf (format=<optimized out>, vargs=<optimized out>)
       at /projects/zephyr2/lib/libc/minimal/source/stdout/fprintf.c:61
   61 {
   (gdb) b nano_init
   Breakpoint 1 at 0x1de8: file /projects/zephyr2/kernel/nanokernel/nano_init.c, line 207.
   (gdb) c
   Continuing.

   Breakpoint 1, _Cstart () at /projects/zephyr2/kernel/nanokernel/nano_init.c:323
   323      nano_init((struct tcs *)&dummyTCS);
   (gdb) bt
   Python Exception <type 'exceptions.ImportError'> No module named gdb.frames:
   #0  _Cstart () at /projects/zephyr2/kernel/nanokernel/nano_init.c:323
   #1  0x00003ca4 in _PrepC () at /projects/zephyr2/arch/nios2/core/prep_c.c:61
   #2  0x00003ccc in __start () at /projects/zephyr2/arch/nios2/core/crt0.S:155
   (gdb)

手动启动调试：


.. code-block:: console

   nios2-gdb-server --tcpport 1234 --stop --reset-target

然后连接至GDB:


.. code-block:: console

   nios2-poky-elf-gdb  outdir/zephyr.elf -ex "target remote :1234"

使用JTAG Flashed镜像进行调试
---------------------------------

为进行此项工作，execute-in-place必须禁用，因为GDB的'load'命令仅能将文本和数据压入RAM。确保它在你的配置中：

.. code-block:: console

   CONFIG_XIP=n

此程序可以离开复位向量启用，不同于nios2-download (如果发现SRAM之外的部分出错,则会出错)，它将被忽略。

在终端内运行nios2 GDB服务器，它并不关心设备上使用的内核（如果有的话），但你至少应该使用nios2-configure-sof烧写CPU，你可以离开这个进程运行。

.. code-block:: console

   $ nios2-gdb-server --tcpport 1234 --tcppersist --init-cache --reset-target

编译你的zephyr内核，并将其载入为Nios II(在Zephyr SDK中)所创建的GDB中：

.. code-block:: console

   $ nios2-poky-elf-gdb outdir/zephyr.elf

然后连接至GDB服务器：

.. code-block:: console

   (gdb) target remote :1234

然后通过线缆载入内核镜像。CPU将不再从复位向量启动，转而从__start标记启动。


.. code-block:: console

   (gdb) load
   Loading section reset, size 0xc lma 0x0
   Loading section exceptions, size 0x1b0 lma 0x400020
   Loading section text, size 0x8df0 lma 0x4001d0
   Loading section devconfig, size 0x30 lma 0x408fc0
   Loading section rodata, size 0x3f4 lma 0x408ff0
   Loading section datas, size 0x888 lma 0x4093e4
   Loading section initlevel, size 0x30 lma 0x409c6c
   Loading section _k_task_list, size 0x58 lma 0x409c9c
   Loading section _k_task_ptr, size 0x8 lma 0x409cf4
   Loading section _k_event_list, size 0x10 lma 0x409cfc
   Start address 0x408f54, load size 40184
   Transfer rate: 417 KB/sec, 368 bytes/write.
   After this is done you may set breakpoints and continue execution. If you ever want to reset the CPU, issue the 'load' command again.



参考
**********

* `CPU Documentation <https://www.altera.com/en_US/pdfs/literature/hb/nios2/n2cpu-nii5v1gen2.pdf>`_
* `Nios II Processor Booting Methods in MAX 10 FPGA Devices <https://www.altera.com/en_US/pdfs/literature/an/an730.pdf>`_
* `Embedded Peripherals IP User Guide <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/ug/ug_embedded_ip.pdf>`_
* `MAX 10 FPGA Configuration User Guide <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/hb/max-10/ug_m10_config.pdf>`_
* `MAX 10 FPGA Development Kit User Guide <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/ug/ug-max10m50-fpga-dev-kit.pdf>`_
* `Nios II Command-Line Tools <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/hb/nios2/edh_ed51004.pdf>`_
* `Quartus II Scripting Reference Manual <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/manual/tclscriptrefmnl.pdf>`_


.. _Altera Lite Distribution: http://dl.altera.com/?edition=lite
