.. _bluetooth:

蓝牙
#########

Zephyr 集成了功能丰富的、高度可配置的蓝牙协议栈：

* 兼容蓝牙 4.2

* 支持蓝牙控制器（LE 链路层）

  * 当前支持 Nordic 半导体的 nRF51 and nRF52

* 带有各种角色的通用访问配置文件（Generic Access Profile，GAP）

  * Peripheral & Central
  * Observer & Broadcaster

* GATT (Generic Attribute Profile)

  * 服务端（一个传感器）
  * 客户端（连接到一个传感器）

* 配对支持，包括来自蓝牙 4.2 的安全连接特性

* IPSP/6LoWPAN for IPv6 connectivity over Bluetooth LE

  * IPSP 节点例程应用程序位于 ``samples/bluetooth/ipsp``

* Clean HCI driver abstraction

  * 3-线 (H:5) & 5-线 (H:4) 驱动程序
  * 支持本地控制器作为 HCI 驱动程序

* Raw HCI interface to run Zephyr as a Controller instead of a full Host stack

  * Possible to export HCI over a physical transport
  * ``samples/bluetooth/hci_uart`` sample for HCI over UART
  * ``samples/bluetooth/hci_usb`` sample for HCI over USB

* Verified with multiple popular controllers

* 高度可配置

  * 功能、缓冲尺寸/数量、栈尺寸等。

源码树分布
==================

协议栈分配在如下的源码数中：

``subsys/bluetooth/host``

  主机协议栈。这里包括 HCI 命令 & 事件处理、连接跟踪。这里也实现了例如 L2CAP、ATT & SMP 等核心协议。

``subsys/bluetooth/controller``

  蓝牙控制器的实现。实现了 HCI 的控制侧，链路层以及对无线收发器的访问。

``include/bluetooth/``

  共用 API 头文件。这些头文件是应用程序在使用蓝牙功能时需要包含的文件。

``drivers/bluetooth/``

  HCI 传输驱动程序。每个 HCI 传输都需要它自己的驱动程序。例如，两种类型的 UART 传输协议（3 线 & 5 线）都有它们自己的驱动程序。

``samples/bluetooth/``

  蓝牙例程代码。这是开发蓝牙应用程序的一个入口点。

``tests/bluetooth/``
  
  测试程序。这些程序用于校验蓝牙协议栈的功能，但是它不是最好的例程代码（ ``samples/bluetooth`` 才是最好的例程）。

``doc/subsystems/bluetooth/``
  
  附加文档，例如 PICS 文档。

深入阅读
===============

您可以在 `wiki <http://wiki.zephyrproject.org/view/Arduino_101#Bluetooth_firmware_for_the_Arduino_101>`_ 和下面的子章节里查看原语蓝牙协议栈及其使用方法的更多信息。

.. toctree::
   :maxdepth: 1

   ../../api/bluetooth.rst
   devel.rst
   qualification.rst
