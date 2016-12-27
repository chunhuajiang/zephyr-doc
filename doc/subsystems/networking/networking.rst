.. _networking:

网络
###########

本节介绍 Zephyr 内核中的网络协议栈相关的信息，您可以利用这些信息理解协议栈操作时的具体行为，以及理解协议栈是如何实现的。

协议栈支持如下特性：

* IPv6

  * IPv6 头部压缩。这也是 6LoWPAN 的部分功能。

* UDP
* IPv4

  * 在这一步的 IP 协议栈中，不能同时使用 IPv4 和 IPv6。
  * IPv4 的 DHCP 客户端。

* TCP

  * 同时支持客户端和服务端。

* RPL (Ripple) IPv6 mesh 路由
* CoAP
* MQTT
* 高度可配置

  * 特性，缓冲尺寸/计数，栈尺寸等。

此外，还支持这些网络技术：

* IEEE 802.15.4
* Bluetooth
* Ethernet
* SLIP (仅在 Qemu 中测试)

源码树结构
==================

IP 协议栈的源码树的组织结构如下：

``net/ip/``
  核心协议栈。Contiki 的 uIP 协议栈就在这里。

``include/net/``
  公用 API 头文件。应用程序在使用 IP 网络的功能时会根据需要包含这些头文件。

``samples/net/``
  网络的例程代码。这是开始开发网络应用程序的参考指南。

``tests/net/``
  用于测试的应用程序。这些应用程序被用于测试 IP 协议栈的功能，但是它不是最好的例程代码（参考 ``samples/net`` ）。

.. toctree::
   :maxdepth: 1

   buffers.rst
