.. _networking_with_qemu:

QEMU 网络环境
####################

本节描述了如何在一个（Linux）主机与运行在 QEMU 虚拟机中的 Zephyr 应用程序之间设置一个“虚拟”网络环境。在这个例子中，我们将 Zephyr 源码中的例程 ``echo_server`` 运行在 QEMU 中。QEMU 实例通过串行端口连接到 Linux 主机。通过 SLIP 在 Zephyr 与 Linux 之间传递数据（通过虚拟连接链）。

前提
*************

在 Linux 主机上，您需要获取 Zephyr net-tools 工程。该工程位于一个独立的 git 仓库中：

.. code-block:: console

   $ git clone https://gerrit.zephyrproject.org/r/net-tools
   $ cd net-tools
   $ make

.. note::

   如果您碰到关于 AX_CHECK_COMPILE_FLAG 的错误，请在 Debain/Ubuntu 上面安装软件包 autoconf-archive。、

基本设置
***********

在下面的过程中，您至少需要四个终端窗口：

* 终端 #1 是你平常所使用的 Zephyr 开发终端
* 终端 #2、#3、#4 - 新的终端窗口，且当前路径是 net-tools 所在路径

Step 1 - 创建助手 socket
=============================

在开始使用 QEMU 仿真前，需要创建已给 unix socket。

在终端 #2，输入：

.. code-block:: console

   $ ./loop-socat.sh

Step 2 - 启动 TAP 设备路由守护进程
========================================

在终端 #3，输入：

.. code-block:: console

   $ sudo ./loop-slip-tap.sh


Step 3 - 在 QEMU 中启动 app
==========================

编译并启动例程 ``echo_server``。

在终端 #1，输入：

.. code-block:: console

   $ cd samples/net/echo_server
   $ make pristine && make qemu

如果您在 QEMU 中看到类似于 unix:/tmp/slip.sock 的错误，说明您遗漏了上面的第 1 步。

Step 4 - 在主机上运行 app
=========================

现在，在终端 #4，您可以运行各种工具与 QEMU 中的应用程序通信。

您可以使用 ping：

.. code-block:: console

   $ ping 192.0.2.1
   $ ping6 2001:db8::1

例如，使用 netcat（“nc”）工具连接一个 UDP 连接：

.. code-block:: console

   $ echo foobar | nc -6 -u 2001:db8::1 4242
   foobar

.. code-block:: console

   $ echo foobar | nc -u 192.0.2.1 4242
   foobar

如果 echo_server 在编译时使能了对 TCP 的支持（当前默认是支持的，CONFIG_NET_TCP=y）：

.. code-block:: console

   $ echo foobar | nc -6 -q2 2001:db8::1 4242
   foobar

.. note::

   您需要手动过输入 Ctrl+C 。

您也可以使用 telnet 命令实现上面的功能。

Step 5 - 停止守护进程
================================

当您使用 QEMU 完成网络测试后，需要停止在初始化步骤中启动的守护进程和助手，以避免在本地网络接口发生地址冲突之类的网络或路由问题。例如，当您从使用 QEMU 测试网络切换到使用真实硬件测试网络时，您就需要停止这些守护进程和助手。否则，您将接收到一个由于地址冲突而报告的一个错误 —— 空中 WiFi 连接无法工作。

要停止守护例程，只需要在响应的终端窗口按下 Ctrl+C（您需要同时停止 ``loop-slip-tap.sh`` 和 ``loop-socat.sh``）。 


设置 NAT/masquerading 以访问 Internet
**********************************************

要使运行在 QEMU 中的应用程序能够访问 Internet，需要为 QEMU 的源地址设置 NAT（masquerading）。假设使用的地址是 192.0.2.1，则需要以 root 权限运行下面的命令：

.. code-block:: console

   $ iptables -t nat -A POSTROUTING -j MASQUERADE -s 192.0.2.1

此外，还需要在主机上使能 IPv4 转发，并确保其它防火墙（iptables）规则不与 masquerading 相互干扰。

在两个 QEMU VM 之间的网络连接
***************************************

与上面所描述的 VM-Host 设置不同的是，VM-VM 设置是自动的。对于那些支持 echo_server 和 echo_client 这种模式的应用程序，您需要 2 个终端窗口来设置 Zephyr 开发环境。

终端 #1:
============

.. code-block:: console

   $ cd samples/net/echo_server
   $ make server

这将会启动一个 QEMU，并等待来自客户端 QEMU 的连接。

终端 #2:
============

.. code-block:: console

   $ cd samples/net/echo_client
   $ make client

这将会启动第 2 个 QEMU 实例，同时您会看到数据收发的日志。
