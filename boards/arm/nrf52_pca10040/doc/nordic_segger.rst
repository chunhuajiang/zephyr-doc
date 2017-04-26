.. _nordic_segger:

Nordic nRF5x Segger J-Link
##########################

概览
********

所有 Nordic nRF5x 开发板、预览板及软件狗都装备了一块Debug IC (Atmel ATSAM3U2C)，它提供了以下功能：

* Segger J-Link 固件及桌面工具
* nRF5x IC的SWD debug
* 可拖放烧写镜像文件的大容量存储器
* USB CDC ACM 串口桥接的 nRF5x UART 外设
* Segger RTT 控制台
* Segger Ozone Debugger

Segger J-Link 软件安装
***********************************

请照下面步骤安装J-Link软件及文件包：

#. 从 `J-Link Software and documentation pack`_ 网站下载适当的安装包
#. 根据你的平台，安装包或运行安装程序
#. 当连接到一个J-Link用开发板，如nRF5x DK、PDK或电子狗，应该会出现一个对应于大容量USB存储设备及串口的驱动器

nRF5x命令行工具安装
*************************************

nRF5x命令行工具使得你可以使用命令行来控制nRF5x设备，包括重启、擦除或对flash闪存进行编程以及更多功能。

要安装此工具，根据你的操作系统使用适当的链接：

* `nRF5x Command-Line Tools for Windows`_
* `nRF5x Command-Line Tools for Linux 32-bit`_
* `nRF5x Command-Line Tools for Linux 64-bit`_
* `nRF5x Command-Line Tools for macOS`_

安装完成后，确保 ``nrfjprog`` 在某个可执行路径，以方便在任何地方调用它。
.. _nordic_segger_flashing:

烧写
********

在根据以上指南安装完Segger J-Link软件及nRF5x命令行工具后，请根据以下步骤将已编译Zephyr镜像烧写进flash：

* 使用micro-USB线缆将nRF5x开发板和你的计算机相连
* 擦除nRF5x IC的flash闪存：

.. code-block:: console

   $ nrfjprog --eraseall -f nrf5<x>

``<x>``：开发板基于nRF51时为1，基于nRF52时为2。

* 从你所写的sample文件夹烧写Zephyr镜像:

.. code-block:: console

   $ nrfjprog --program outdir/<board>/zephyr.hex -f nrf5<x>

``<board>``： 在编译时用于指向主板的开始板名称 (例如nrf52_pca10040)
``<x>``： 开发板基于nRF51时为1，基于nRF52时为2。

* 重启Zephyr

.. code-block:: console

   $ nrfjprog --reset -f nrf5<x>

``<x>``：开发板基于nRF51时为1，基于nRF52时为2。

USB CDC ACM串口安装
*****************************

**Important note**: Segger J-Link固件在nRF5x开发板上会出现一个问题，在某些机器上使用USB CDC ACM串口会导致数据丢失或损坏。要避免此错误请禁用开发板上的大容量存储设备，具体步骤请参考:ref:`nordic_segger_msd`。

Windows
=======

串口将显示为 ``COMxx``。在设备管理器中检查“Ports (COM & LPT)”项即可。

GNU/Linux
=========

串口将显示为 ``/dev/ttyACMx``。默认情况下，端口对所有用户不可访问。输入以下命令将用户添加到dialout组以让它可以访问串口。注意，需要重新登录才能生效。

.. code-block:: console

   $ sudo usermod -a -G dialout <username>

当你将开发板插入时，为避免它被Modem Manage占用几秒：

.. code-block:: console

   systemctl stop ModemManager.service
   systemctl disable ModemManager.service

Apple macOS (OS X)
==================

串口将显示为 ``/dev/tty.usbmodemXXXX``。

.. _nordic_segger_msd:

禁用大容量存储设备功能
***********************************************

由于Segger J-Link固件的已知问题，在使用USB CDC ACM串口时如果数据包大于64字节，根据不同的操作系统和版本，可能会遇到数据损坏或丢失。这已经在GNU/Linux和macOS (OS X)出现过。

为避免这些，你可以简单地禁用大容量存储器：

* 在GNU/Linux和macOS (OS X)中打开终端
* 在Microsoft Windows中打开“JLink Commander”应用程序

输入：

.. code-block:: console

   MSDDisable

最终，拔掉并重插开发板，大容量存储器将不再出现，你现在可以通过虚拟串口发送长数据包了。有关Segger的进一步信息请参阅 `Segger SAM3U Wiki`_.

RTT 控制台
***********

Segger的J-Link支持 `Real-Time Tracing (RTT)`_，此技术允许在目标板（nRF5x）和开发电脑间建立一个终端连接（输入和输出）。Zephyr支持nRF5x目标板的RTT,当UART（通过 USB CDC ACM）已经被用于不同目的（如hci_uart应用中的HCI通信）时，此技术会非常有用。要使用RTT，你首先要通过在 ``.conf`` 文件中添加以下行来启用它:

.. code-block:: console

   CONFIG_HAS_SEGGER_RTT=y
   CONFIG_RTT_CONSOLE=y

RTT启用被编译并烧写后，你可以通过以下步骤来显示RTT控制台信息：

Windows
=======

* 打开“J-Link RTT Viewer”应用程序
* 选择以下选项

  * Connection: USB
  * Target Device: Select your IC from the list
  * Target Interface and Speed: SWD, 4000 KHz
  * RTT Control Block: Auto Detection

GNU/Linux and macOS (OS X)
==========================

* 从终端打开``JLinkRTTLogger``
* 选择以下选项：

  * Device Name: Use the fully qualified device name for your IC
  * Target Interface: SWD
  * Interface Speed: 4000 KHz
  * RTT Control Block address: auto-detection
  * RTT Channel name or index: 0
  * Output file: filename or ``/dev/stdout`` to display on the terminal directly

Segger Ozone
************

Segger J-Link兼容 `Segger Ozone`_, 一个虚拟调试器，可在以下地址获取：

* `Segger Ozone Download`_

下载后，你可以安装它并进行如下配置：

* Target Device: Select your IC from the list
* Target Interface: SWD
* Target Interface Speed: 4 MHz
* Host Interface: USB

配置完成后，你可以使用 File->Open 菜单打开 ``zephyr.elf``文件，此文件可以 ``outdir/<board>/`` 目录下找到。

参考
**********

.. target-notes::

.. _nRF5x Command-Line Tools for Windows: https://www.nordicsemi.com/eng/nordic/Products/nRF51822/nRF5x-Command-Line-Tools-Win32/33444
.. _nRF5x Command-Line Tools for Linux 32-bit: https://www.nordicsemi.com/eng/nordic/Products/nRF51822/nRF5x-Command-Line-Tools-Linux32/52615
.. _nRF5x Command-Line Tools for Linux 64-bit: https://www.nordicsemi.com/eng/nordic/Products/nRF51822/nRF5x-Command-Line-Tools-Linux64/51386
.. _nRF5x Command-Line Tools for macOS: https://www.nordicsemi.com/eng/nordic/Products/nRF51822/nRF5x-Command-Line-Tools-OSX/53402

.. _Segger SAM3U Wiki: https://wiki.segger.com/index.php?title=J-Link-OB_SAM3U
.. _Real-Time Tracing (RTT): https://www.segger.com/jlink-rtt.html
.. _Segger Ozone: https://www.segger.com/ozone.htm
.. _Segger Ozone Download: https://www.segger.com/downloads/jlink#Ozone

.. _nRF52 DK website: http://www.nordicsemi.com/eng/Products/Bluetooth-Smart-Bluetooth-low-energy/nRF52-DK
.. _Nordic Semiconductor Infocenter: http://infocenter.nordicsemi.com/
.. _J-Link Software and documentation pack: https://www.segger.com/jlink-software.html

