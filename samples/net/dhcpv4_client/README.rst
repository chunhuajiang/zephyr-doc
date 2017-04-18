.. _dhcpv4-client-sample:

DHCPv4 客户端应用示例
################################

概览
********

此应用程序启动一个 DHCPv4 客户端，从 DHCPv4 服务器端获取一个 IPv4 地址，并向串口控制台打印地址、租用期、掩码以及路由器信息。

需求
************

- :ref:`使用 QEMU 网络仿真 <networking_with_qemu>`

编译和运行
********************

QEMU x86
========

本操作指南用于在 Linux 主机中通过 QEMU 使用此示例应用程序，以从 Linux 主机中的 DHCPv4 服务器协商 IP 地址。

以下为自述文件:

    从 net-tools 运行 'loop_socat' 和 'loop-slip-tap' 脚本。

    https://gerrit.zephyrproject.org/r/gitweb?p=net-tools.git;a=blob;f=README

.. code-block:: console

    $ ./loop_socat.sh

在另一窗口:

.. code-block:: console

    $ sudo ./loop-slip-tap.sh

'/etc/dhcpd/dhcp.conf' 为服务器配置文件示例，它用于配置 DHCPv4 服务器：

.. code-block:: console

   log-facility local7;
   default-lease-time 600;
   max-lease-time 7200;

   subnet 192.0.2.0 netmask 255.255.255.0 {
     range 192.0.2.10 192.0.2.100;
   }

在 Linux 主机中使用另一终端窗口启动一个 DHCPv4 服务器，使用以下 conf 文件：

.. code-block:: console

    $ sudo dhcpd -d -4 -cf /etc/dhcp/dhcpd.conf -lf /var/lib/dhcp/dhcpd.leases tap0

在 QEMU 中运行 samples/net/dhcpv4_client 应用示例:

.. code-block:: console

    $ cd $ZEPHYR_BASE/samples/net/dhcpv4_client
    $ make pristine && make qemu

一旦与服务器完成协商 DHCPv4 客户端地址，将显示如下信息:

.. code-block:: console

    [dhcpv4] [INF] main: In main
    [dhcpv4] [INF] main_thread: Run dhcpv4 client
    [dhcpv4] [INF] handler: Your address: 192.0.2.10
    [dhcpv4] [INF] handler: Lease time: 600
    [dhcpv4] [INF] handler: Subnet: 255.255.255.0
    [dhcpv4] [INF] handler: Router: 0.0.0.0

为证明 Zephyr 应用客户端正在运行，并已经接收到一个 IP 地址，请键入:

.. code-block:: console

    $ ping -I tap0 192.0.2.10


FRDM_K64F
=========

本操作指南用于在 :ref:`frdm_k64f` 开发板运行此示例应用程序，以从 Linux 主机中的 DHCPv4 服务器协商 IP 地址。

使用以太网电缆将 :ref:`Freedom-K64F 开发板 <frdm_k64f>` 开发板连接至 Linux 主机，并检查新接口：

.. code-block:: console

    $ ifconfig

为接口添加 ip 地址及路由信息：

.. code-block:: console

    $ sudo ip addr add 192.0.2.2 dev eth1
    $ sudo ip route add 192.0.2.0/24 dev eth1

'/etc/dhcpd/dhcp.conf' 为服务器配置文件示例，用于配置 DHCPv4 服务：

.. code-block:: console

   log-facility local7;
   default-lease-time 600;
   max-lease-time 7200;

   subnet 192.0.2.0 netmask 255.255.255.0 {
     range 192.0.2.10 192.0.2.100;
   }

在 Linux 主机使用另一个终端窗口启动 DHCPv4 服务，使用以下 conf 文件:

.. code-block:: console

    $ sudo dhcpd -d -4 -cf /etc/dhcp/dhcpd.conf -lf /var/lib/dhcp/dhcpd.leases eth1

创建 samples/net/dhcpv4_client Zephyr 应用程序:

.. code-block:: console

    $ cd $ZEPHYR_BASE/samples/net/dhcpv4_client
    $ make pristine && make BOARD=frdm_k64f
    $ cp outdir/frdm_k64f/zephyr.bin /media/rveerama/MBED/

一旦与服务器完成协商 DHCPv4 客户端地址，将显示如下信息:

.. code-block:: console

    $ sudo screen /dev/ttyACM0 115200
    [dhcpv4] [INF] main: In main
    [dhcpv4] [INF] main_thread: Run dhcpv4 client
    [dhcpv4] [INF] handler: Your address: 192.0.2.10
    [dhcpv4] [INF] handler: Lease time: 600
    [dhcpv4] [INF] handler: Subnet: 255.255.255.0
    [dhcpv4] [INF] handler: Router: 0.0.0.0

为证明 Zephyr 应用客户端正在运行，并已经接收到一个 IP 地址，请键入:

.. code-block:: console

    $ ping -I eth1 192.0.2.10
