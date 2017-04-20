.. _zoap-server-sample:

CoAP服务器
###########

概览
********

一个简单的CoAP服务器，演示了如何公开一个简单资源。

本示例假定你所选的平台支持网络，可能需要对配置进行一些调整。

示例将监听为Coap节点所保留的站点本地IPv6组播地址的CoAP UDP端口（5683）的请求。

示例导出以下资源:

.. code-block:: none

   /test
   /seg1/seg2/seg3
   /query
   /separate
   /large
   /location-query
   /large-update

这些资源使得ETSI测试用例的一大部分可以运行于zoap-server。

编译和运行
********************

此项目在运行成功的情况下没有输出，可使用某些外部工具如tcpdump或wireshark来验证其功能性是否正确。

参考 `net-tools`_ 项目获取更多细节。

它可以使用以下方法编译并运行在QEMU上:

.. code-block:: console

    make run


在主机上使用以下命令来运行ETSI测试用例实现`libcoap`_ ：

.. code-block:: console

   sudo ./examples/etsi_coaptest.sh -i tap0 2001:db8::1

创建对TI CC2520射频的版本支持，请使用所提供的配置文件以使能IEEE 802.15.4:

.. code-block:: console

    make CONF_FILE=prj_cc2520.conf run


.. _`net-tools`: https://gerrit.zephyrproject.org/r/gitweb?p=net-tools.git;a=tree

.. _`libcoap`: https://github.com/obgm/libcoap
