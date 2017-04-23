.. _coap-server-sample:
 
基于 DTLS 的 CoAP 服务器端示例
############################

概览
********

此示例代码演示了在 Zephyr 中如何使用 mbedTLS 协议，也就是基于 DTLS（Datagram Transport Layer Security 数据包传输层安全协议）的 CoAP 服务器端的使用。

编译和运行
********************

以下步骤用于测试 :ref:`使用 QEMU 网络仿真 <networking_with_qemu>`。

在应用程序目录下键入:

.. code-block:: console

   $make run

在另一个终端窗口，通过以下命令获取 libcoap 代码:

.. code-block:: console

	git clone --recursive -b dtls https://github.com/obgm/libcoap.git

并将其放置在你的 Linux 机器中众所周知的目录当中，这将是你的客户端。为了编译 libcoap，你可能需要为 Ubuntu 安装以下类库。

.. code-block:: console

	sudo apt-get install libtool asciidoc

进入这个目录并在你的主机上编译 libcoap：

.. code-block:: console

	./autogen.sh
	./configure --disable-shared
	make all

现在你可以使用如下方法运行客户端：

.. code-block:: console

	cd examples
	./coap-client -m get coaps://[2001:db8::1]/test -u Client_identity -k passwd

你将获得如下输出：

.. code-block:: console

	v:1 t:CON c:GET i:7154 {} [ ]
	decrypt_verify(): found 24 bytes cleartext
	decrypt_verify(): found 123 bytes cleartext
	Type: 0
	Code: 1
	MID: 29012

应用程序目录将打印如下信息：

.. code-block:: console

	*******
	type: 0 code 1 id 29012
	*******
 	mbedtls_ssl_read returned -0x7780

如果服务器没有收到信息，重启应用程序，并再次尝试连接客户端。

参考
**********

* https://tls.mbed.org/
* https://libcoap.net/
