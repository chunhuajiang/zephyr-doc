.. _coap-client-sample:

基于 DTLS 的 CoAP 客户端示例
############################

概览
********
此示例代码演示了在 Zephyr 中如何使用 mbedTLS 协议，也就是基于 DTLS（Datagram Transport Layer Security 数据包传输层安全协议）的 CoAP 客户端的使用。

编译和运行
********************

以下步骤用于测试 :ref:`使用 QEMU 网络仿真 <networking_with_qemu>`。

运行位于 samples/net/coaps_server 的服务端应用程序, 使用以下命令：

.. code-block:: console

	make server

在另一个终端窗口,运行位于 samples/net/coaps_client 的本客户端应用程序：

.. code-block:: console

	make client

你将获得以下输出:

.. code-block:: console

	reply: 60 45 00 01 ff 54 79 70 65 3a 20 30 0a 43 6f 64 65 3a 20 31 0a 4d
	49 44 3a 20 31 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 (123 bytes)

在服务端应用程序目录中，屏幕将显示以下内容：

.. code-block:: console

	*******
	type: 0 code 1 id 1
	*******
	connection was closed gracefully
	done

如果服务器没有收到信息，重启应用程序，并再次尝试连接客户端。

