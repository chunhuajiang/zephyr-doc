.. _dns-client-sample:

DNS 客户端应用
######################

概览
********

本例为 DNS 解析器或 DNS 客户端应用示例，按照 RFC 1035 实现了一个基本 DNS 的解析器。支持的 DNS 应答有：IPv4/IPv6 地址和 CNAME。

如果接收到一个 CNAME，DNS 解析器将创建另一个 DN 查询。此附加查询的编号由D NS_RESOLVER_ADDITIONAL_QUERIES 这个 kconfig 变量控制。

获取更多有关 DNS 配置变量的信息请参考:
:file:`subsys/net/lib/dns/Kconfig`。

DNS 解析 API 可查看：
:file:`include/net/dns_client.h`。

示例代码请查看：
:file:`samples/net/dns_client`。

下表描述了此示例应用的返回值编码。

=======		=====	================================================
Macro		Value	Description
-------		-----	------------------------------------------------
-EINVAL		-22	如果检测到无效参数
-EIO		-5	网络错误
-ENOMEM		-12	内存错误，可能与网络缓冲有关
=======		=====	================================================

返回值 0 必须被中断，表示成功。

需求
************

- :ref:`使用 QEMU 网络仿真 <networking_with_qemu>`

- 屏幕终端仿真或类似设备

- 对于 Arduino 101 开发板, 需要 ENC28J60 以太网模块.

- dnsmasq 应用。 此示例所使用的 dnsmasq 版本为:

.. code-block:: console

    dnsmasq -v
    Dnsmasq version 2.76  Copyright (c) 2000-2016 Simon Kelley

接线
******

ENC28J60 模块是一个 SPI 接口以太网设备。以下引脚必须从 ENC28J60 设备连接至 Arduino 101 开发板

===========	===================================
Arduino 101	ENC28J60 (主板上的引脚号)
-----------	-----------------------------------
D13		SCK  (1)
D12		SO   (3)
D11		SI   (2)
D10		CS   (7)
D04		INT  (5)
3.3V		VCC  (10)
GDN		GND  (9)
===========	===================================


编译和运行
********************

网络配置
=====================

打开你的平台所对应的项目配置文件，例如: :file:`prj_frdm_k64f.conf` 是针对 :ref:`frdm_k64f` 开发板的配置文件。 对于 IPv4 网络，设置以下变量：

.. code-block:: console

	CONFIG_NET_IPV4=y
	CONFIG_NET_IPV6=n

对此示例来说，IPv6 是首选路由技术,如果设置了 CONFIG_NET_IPV6=y， CONFIG_NET_IPV4 的值将被忽略。

本示例仅支持静态 IP 地址，这些 IP 地址在项目配置文件中指定，例如:

.. code-block:: console

	CONFIG_NET_SAMPLES_MY_IPV6_ADDR="2001:db8::1"
	CONFIG_NET_SAMPLES_PEER_IPV6_ADDR="2001:db8::2"

分别是运行于 Zephyr 的 DNS 客户端以及 DNS 服务器的 IPv6 地址。

或者，IP 地址也可在:file:`samples/net/dns_client/src/config.h` 文件中指定。

打开 :file:`samples/net/dns_client/src/config.h` 文件，并服务端口设置为与 DNS 服务器匹配，例如：

.. code-block:: c

   #define REMOTE_PORT		5353

假设 DNS 服务正在监听 UDP 端口 5353.

DNS 服务
==========

dnsmasq 工具可用于测试。打开终端窗口并输入:

.. code-block:: console

    $ dnsmasq -p 5353 -d

注意： 一些系统可能需要根权限来运行 dnsmasq，则使用 sudo 或 su。

如果 dnsmasq 启动出现如下错误：

.. code-block:: console

    dnsmasq: failed to create listening socket for port 5353: Address already in use

打开终端窗口并输入:

.. code-block:: console

    $ killall -s KILL dnsmasq

再次启动 dnsmasq 应用。


QEMU x86
========

打开终端窗口并输入:

.. code-block:: console

    $ make


按照以下链接指示运行 'loop_socat.sh' 和 'loop-slip-tap.sh':

    https://gerrit.zephyrproject.org/r/gitweb?p=net-tools.git;a=blob;f=README

设置 IPv4 ip 地址:

.. code-block:: console

    $ ip addr add 192.0.2.2/24 dev tap0

在项目创建处打开一个终端 (如 :file:`samples/net/dns_client`)并输入:

.. code-block:: console

    $ make run

FRDM K64F
=========

打开终端窗口并输入:

.. code-block:: console

    $ make BOARD=frdm_k64f


FRDM K64F 开发板被检测为一个 USB 存储设备。 开发板必须被挂接（如到 /mnt）以烧写二进制文件：

.. code-block:: console

    $ cp outdir/frdm_k64f/zephyr.bin /mnt


获取此开发板的更多信息请访问 :ref:`Freedom-K64F board documentation <frdm_k64f>` 。

打开终端窗口并输入:

.. code-block:: console

    $ screen /dev/ttyACM0 115200


使用 'dmesg' 来寻找正确的 USB 设备。

一旦二进制文件加载到 FRDM 开发板，按下 RESET 按钮。

Arduino 101
===========

打开终端窗口并输入:

.. code-block:: console

	$ make BOARD=arduino_101

使用以下步骤向开发板载入二进制文件 :ref:`arduino_101`.

打开终端窗口并输入:

.. code-block:: console

    $ screen /dev/ttyUSB0 115200

使用 'dmesg' 来寻找正确的USB设备。

一旦二进制文件加载到 Arduino 101 开发板, 按下RESET按钮。

示例输出
=============

IPv4 (CONFIG_NET_IPV6=n, CONFIG_NET_IPV4=y)

.. literalinclude:: sample_output_IPv4.txt


IPv6 (CONFIG_NET_IPV6=y, CONFIG_NET_IPV4=n)

.. literalinclude:: sample_output_IPv6.txt


注意: IPv6 地址通过 dnsmasq 被包含并且 :file:`/etc/hosts`.

已知问题
============

- 以上示例包含一个 rc: -22 (-EINVAL)。这是该域名的预期行为。

- 如果很多 rc: -5 (-EIO) 错误充满屏幕, 增加 APP_SLEEP_MSECS 值到 500 甚至 1000。请参考 :file:`samples/net/dns_client/src/config.h`。

- IPv4: 仍然有一个问题尚未解决，它导致应用程序在前两个查询期间失败。这个问题位于 L2（ARP）和 UDP 之间，只在应用程序启动时出现。

