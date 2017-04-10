.. _echo-server-sample:

Echo 服务端
#############

概述
********

示例程序 echo-client 是 Zephyr 实现的一个 UDP/TCP 服务端程序，它会监听接收到的（由 echo 客户端发送的） IPv4 或者 IPv6 报文，并简单地将其送回。


该示例程序的源代码位于：:file:`samples/net/echo_server`。

编译和运行
********************

运行该程序的方法多种多样，其中一种最常见的方式是在 QEMU 中运行 echo-server。详细信息请参考 :ref:`networking with QEMU <networking_with_qemu>`.

echo-server 的目录下包含多个配置文件，它们可用于不同的开发板和设置：


- :file:`prj_arduino_101_cc2520.conf`
  
  用于带有外部 IEEE 802.15.4 cc2520 的 Arduino 101 开发板。

- :file:`prj_arduino_101.conf`

  用于带有外部 enc28j60 的 Arduino 101 开发板。

- :file:`prj_bt.conf`

  用于蓝牙 Bluetooth IPSP 连接。

- :file:`prj_cc2520.conf`
  
  用于那些支持 IEEE 802.15.4 cc2520 芯片的设备。

- :file:`prj_frdm_k64f_cc2520.conf`
  
  用于带有外部 IEEE 802.15.4 cc2520 的 FRDM-K64F 开发板。

- :file:`prj_frdm_k64f.conf`
  
  用于带有内置以太网的 FRDM-K64F 开发板。

- :file:`prj_frdm_k64f_mcr20a.conf`
  
  用于带有 IEEE 802.15.4 mcr20a 开发板的 FRDM-K64F 开发板。

- :file:`prj_qemu_802154.conf`
  
  用于使用两个连接在一起的 QEMU 进行的 IEEE 802.15.4 网络的仿真中。

- :file:`prj_qemu_cortex_m3.conf`
  
  用于 ARM QEMU。

- :file:`prj_qemu_x86.conf`
  
  用于 x86 QEMU。

- :file:`prj_sam_e70_xplained.conf`
  
  用于带有以太网的 Atmel SMART SAM E70 Xplained 开发板。

编译 echo-server 的方法：

.. code-block:: console

    $ cd $ZEPHYR_BASE/samples/net/echo_server
    $ make pristine && make CONF_FILE=<your desired conf file> \
      BOARD=<board to use>

make 命令会根据你指定的 BOARD 参数来选择一个默认的配置文件，因此您可能不需要指定 CONF_FILE 选项。

在 Linux 主机中运行 echo-client
=================================

一个比较好的测试场景是在 Linux 主机上面运行 echo-client，在 QEMU 中运行 echo-server。

在 Linux 主机上进入 net-tools 所在目录，然后运行脚本 'loop_socat' 和 'loop-slip-tap'：

.. code-block:: console

    $ ./loop_socat.sh

在另一个窗口：

.. code-block:: console

    $ sudo ./loop-slip-tap.sh

在 QEMU 中运行 echo-server：

.. code-block:: console

    $ cd $ZEPHYR_BASE/samples/net/echo-server
    $ make pristine && make qemu

在第三个窗口中：

.. code-block:: console

    $ sudo ./echo-client -i tap0 2001:db8::1

需要注意的是，在运行 echo-client 程序前，您必须先在 QEMU 中运行 echo-server。
