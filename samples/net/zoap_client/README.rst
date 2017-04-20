.. _zoap-client-sample:

CoAP客户端
###########

概览
********

一个简单的CoAP服务器，演示了如何从一个资源中获取信息。

本示例假定你所选的平台支持网络，可能需要对配置进行一些调整。

本示例将向为CoAP节点所保留的IPv6组播地址发起一个带‘test’路径的GET请求，所以URL可表现为：

.. code-block:: none

    coap://[ff02::fd]:5683/test

编译和运行
********************

此项目将以字节方式打印出所有接收到的响应，更多的内容可以通过使用像tcpdump或wireshark类似的工具获得。

参考 `net-tools`_ 项目以获取更详细信息。

可使用如下方法在QEMU上编译并运行：

.. code-block:: console

    make run

示例输出
=============

.. code-block:: console

  reply: 60 00 00 00 00 24 11 40 fe 80 00 00 00 00 00 00 5c 25 e2 ff fe
  15 01 01 fe 80 00 00 00 00 00 00 5c 25 e2 ff fe 15 01 01 16 33 16 33
  00 24 3d 86 60 40 00 01 ff 54 79 70 65 3a 20 30 0a 43 6f 64 65 3a 20
  31 0a 4d 49 44 3a 20 31 0a (76 bytes)

.. 注意: 以上所显示的值可能会有所不同。

.. _`net-tools`: https://gerrit.zephyrproject.org/r/gitweb?p=net-tools.git;a=tree
