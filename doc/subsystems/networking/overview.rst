.. _ip_stack_overview:

概述
########

支持的功能
******************

网络 IP 协议栈是模块化的、高度可配置的，它可以在编译时通过配置选项进行配置。您可以只使能那些您的应用程序所需要的功能，以达到最小化系统内存消耗的目的。几乎所有的功能都可以在不需要时被禁止。

* **IPv6** 默认开启了对 IPv6 的支持。各种 IPv6 子选项可以根据具体的网络需求进行使能和禁止。

  * 开发者可以同时设置可用单播、组播 IPv6 地址的数量。
  * 设备的 IPv6 地址既可以静态设置，又可以使用 SLAAC（无状态地址自动配置）（RFC 4862） 动态设置。
  * 支持多个 IPv6 前缀，且最大的 IPv6 前缀数量是可以在编译时配置的。
  * IPv6 邻居 cache 可以在不需要时被禁止，且 cache 大小也是可以在编译时配置的。
  * IPv6 邻居发现（RFC 4861）默认未被开启。
  * 多播侦听发现 v2（RFC 3810）默认开启。
  * IPv6 头部压缩（6lo）可用于 Bluetooth IPSP（RFC 7668）和 IEEE 802.15.4（RFC 4944）的 IPv6 连接。

* **IPv4** 协议栈支持传统的 IPv4。它不能用于 IEEE 802.15.4 或 Bluetooth IPSP，因为这些网络技术仅支持 IPv6。IPv4 可以用于基于以太网的网络中。默认未被开启。

  * 支持 DHCP（动态主机配置协议）（RFC 2131）。
  * IPv4 地址可以手工配置。默认开启了静态 IPv4 地址。

* **双协议栈支持。** 网络协议栈运行开发者同时使用 IPv6 和 IPv4。

* **UDP** 支持用户数据报协议（RFC 768）。开发者既可以发送 UDP 数据报（客户端侧支持），又可以创建监听者来自某个端口的 UDP 报文（服务器侧支持）。

* **TCP** 支持传输控制协议（RFC 793），包括客户端角色和服务端角色。应用程序可用 TCP 套接字的数量可以在编译时配置。

* **HTTP** 支持超文本传输协议（RFC 2116）。应用程序可以使用协议栈提供的简单库代码。提供了示例程序 :ref:`http-client-sample` 和 :ref:`http-server-sample`。:ref:`http-client-sample` 和 :ref:`http-server-sample` 均可以使用 TLS （Transport Layer Security） v1.2 (RFC 5246) 或 SSL (Secure Sockets Layer) v3.0 (RFC 6101) 功能来加密网路流量。安全连接由 mebe 库提供。

* **MQTT** 支持消息队列遥测传输（ISO/IEC PRF 20922）提供了一个 MQTT v3.1.1 的客户端示例程序 :ref:`mqtt-publisher-sample`。

* **CoAP** 支持受限应用协议（RFC 7252）。提供了客户端例程 :ref:`zoap-client-sample` 和服务端例程 :ref:`zoap-server-sample`。
还提供了使用 DTLS（Datagram Transport Layer Security） 的例程 :ref:`coap-client-sample` 和 :ref:`coap-server-sample`。 ) is supported. Both

* **RPL** 支持用于低功耗有损网络的 IPv6 路由协议（RFC 6550）。RPL 是基于 IPv6 的 mesh 路由协议。

* **DNS** 支持域名服务（RFC 1035）客户端功能。应用程序可以使用一个 API 来查询域名信息，或从 DNS 服务器查询 IP 地址。

* **网络管理 API。** 应用程序可以使用网络管理 API 连监听由协议栈核心产生的管理事件（例如，IP 地址被添加到设备上，或者网络接口即将启动）。

* **多种网络技术。** Zephyr OS 可以被配置为同时至此多种网络技术，这只需要在 Kconfig 文件中将其使能即可：例如，支持 Ethernet 和 802.15.4。
注意，这些技术不提供自动 IP 路由功能。应用程序可以根据自己的需求向指定的网络接口发送数据。

* **最小化拷贝网络缓冲管理。** 可以最小化拷贝网络数据路径，这意味着系统可以在将数据发送到网络前可以进行尝试。对于某些技术，甚至可以实现从应用程序到设备驱动程序的零拷贝数据路径。
  
Zephyr OS v1.7 及其以后的版本至此这些额外的网络技术：

* IEEE 802.15.4
* Bluetooth
* Ethernet

  * SLIP (IP over serial line) 用于 QEMU 测试。它在主机系统（例如 Linux）与测试程序之间提供了一个以太网接口，可以运行在 Linux 主机上，并将网络数据发送到 Zephyr OS 设备中。

源码树分布
******************

IP 协议栈的源码树的组织结构如下：

``subsys/net/ip/``
  
  IP 协议栈代码所在路径。

``include/net/``
  
  公用的 API 头文件。应用程序在使用 IP 网络的功能时会根据需要包含这些头文件。

``samples/net/``

  网络的例程代码。这是开始开发网络应用程序的参考指南。

``tests/net/``

  用于测试的应用程序。这些应用程序被用于测试 IP 协议栈的功能，但是它不是最佳的例程代码（参考 ``samples/net``）。
