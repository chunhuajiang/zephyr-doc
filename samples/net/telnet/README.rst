.. _telnet-console-sample:

TELNET控制台应用示例
#################################

概览
********

此应用程序将在默认网络接口安装IPv4/IPv6地址。telnet控制台服务由内核透明启动，伴随shell和双shell模块：net和内核。一旦启动和运行，你可以通过连接到目标，使用Telnet客户端。

需求
************

- :ref:`Networking with Qemu <networking_with_qemu>`


编译和运行
********************

QEMU x86
========

这是使用此示例应用程序的指南，讲解了在Linux主机如何使用QEMU通过DHCP服务器连接至网络。

使用QEMU进行测试，请参考 :ref:`Networking with Qemu
<networking_with_qemu>` 指南。

在net-tools中运行 'loop_socat' 和 'loop-slip-tap' 脚本。

.. code-block:: console

    $ ./loop_socat.sh

在另一窗口:

.. code-block:: console

    $ sudo ./loop-slip-tap.sh

在QEMU中运行 samples/net/telnet 应用程序:

.. code-block:: console

    $ cd $ZEPHYR_BASE/samples/net/telnet
    $ make pristine && make run

一旦启动，你将看到IP地址细节，如:

.. code-block:: console

    [Setup] [INF] main: Starting Telnet sample
    [Setup] [INF] setup_ipv4: IPv4 address: 192.0.2.1
    [Setup] [INF] setup_ipv6: IPv6 address: 2001:db8::1

此时，你的QEMU guest启动并运行。通过以下方法从你的Linux主机连接到telnet控制台：

.. code-block:: console

    $ telnet 192.0.2.1
    Telnet escape character is '^]'.
    Trying 192.0.2.1...
    Connected to 192.0.2.1.
    Escape character is '^]'.

现在键入回车，将显示shell提示，你可以开始键入命令，如 ``help``。


Freedom-K64F Board
===================

这是讲解如何在Freedom-K64F开发板上运行此示例应用程序的指南。与在QEMU上运行不同， :ref:`Freedom-K64F board <frdm_k64f>` 的网络配置将依靠DHCPv4。如果实在需要，你可以更改 :file:`prj_frdm_k64f.conf` 文件以设置静态IPv4地址。

有关创建、烧写和使用串口控制台日志的详细指令，请参考 :ref:`Freedom-K64F board <frdm_k64f>` 的文档部分。

把:ref:`Freedom-K64F <frdm_k64f>` 开发板通过网线连接至本地网络，将通过DHCPv4来提供IPv4地址配置。在本地网络创建你自己的DHCP服务器不在本文讨论范围内。

创建 samples/net/telnet Zephyr应用程序:

.. code-block:: console

    $ cd $ZEPHYR_BASE/samples/net/dhcpv4_client
    $ make pristine && make BOARD=frdm_k64f

根据 :ref:`Freedom-K64F <frdm_k64f>`开发板文档烧写生成的Zephyr二进制文件。

在电脑主机中为你的开发板打开串口控制台:

.. code-block:: console

    $ sudo screen /dev/ttyACM0 115200

将以太网线缆插入 :ref:`Freedom-K64F <frdm_k64f>` 开发板。重启开发板，首先会在控制台上看到:

.. code-block:: console

    [dev/eth_mcux] [INF] eth_0_init: Enabled 100M full-duplex mode.
    [dev/eth_mcux] [DBG] eth_0_init: MAC 00:04:9f:69:c7:36
    shell> [Setup] [INF] main: Starting Telnet sample
    [Setup] [INF] setup_dhcpv4: Running dhcpv4 client...
    [Setup] [INF] setup_ipv6: IPv6 address: 2001:db8::1

如果DHCPv4客户端成功，将很快看到和以下类似的文字:

.. code-block:: console

   [Setup] [INF] ipv4_addr_add_handler: IPv4 address: 192.168.0.21
   [Setup] [INF] ipv4_addr_add_handler: Lease time: 86400 seconds
   [Setup] [INF] ipv4_addr_add_handler: Subnet: 255.255.255.0
   [Setup] [INF] ipv4_addr_add_handler: Router: 192.168.0.1

以上结果依赖于你的网络。此时你应当已经使用telnet通过网络连接至你的Linux主机：

.. code-block:: console

    $ telnet 192.168.0.21
    Telnet escape character is '^]'.
    Trying 192.168.0.21...
    Connected to 192.168.0.1.
    Escape character is '^]'.

现在已经连接成功，使用UART控制台，你可以输入命令并通过telnet客户端获得输出。
