.. _mbedtls-dtls-client-sample:

mbedTLS DTLS 客户端
####################

概览
********
本示例演示了在 Zephyr 下使用 mbed TLS 实现的简单 DTLS（Datagram Transport Layer Security 数据包传输层安全协议）客户端。

编译和运行
********************

下列步骤用于测试 :ref:`使用 QEMU 网络仿真 <networking_with_qemu>`。

从以下链接包含 mbed TLS 代码:

https://tls.mbed.org/download/start/mbedtls-2.3.0-apache.tgz

将它放入 Linux 主机的众所周知的目录下, 作为服务器。

在你的主机上进入那个目录并编译 mbedTLS:

.. code-block:: console

   $ tar -xvzf mbedtls-2.3.0-apache.tgz
   $ cd mbedtls-2.3.0
   $ CFLAGS="-I$PWD/configs -DMBEDTLS_CONFIG_FILE='<config-thread.h>'" make

赋予服务器 IP 地址并启动 DTLS 服务。

.. code-block:: console

   $ sudo ip addr add 192.0.2.2/24 dev tap0
   $ ./programs/ssl/ssl_server2 dtls=1 ecjpake_pw=passwd

.. code-block:: console

   . Seeding the random number generator... ok
   . Bind on udp://*:4433/ ... ok
   . Setting up the SSL/TLS structure... ok
   . Waiting for a remote connection ...

使用 Ctrl-C 停止服务，在每次 QEMU 终止时由于网络接口（tap）被重启，请重复上面步骤，。

在应用程序目录下输入：

.. code-block:: console

   $ make run

在运行 Qemu 时会导致如下输出:

.. code-block:: console

	. Seeding the random number generator... ok
	. Setting up the DTLS structure... ok
	. Connecting to udp 192.0.2.2:4433... ok
	. Setting up ecjpake password ... ok
	. Performing the SSL/TLS handshake... ok
	> Write to server: ok
	. Closing the connection... done

服务端会看到以下内容：

.. code-block:: console

	. Performing the SSL/TLS handshake... hello verification requested
	. Waiting for a remote connection ... ok
	. Performing the SSL/TLS handshake... ok
	[ Protocol is DTLSv1.2 ]
	[ Ciphersuite is TLS-ECJPAKE-WITH-AES-128-CCM-8 ]
	[ Record expansion is 29 ]
	[ Maximum fragment length is 16384 ]
	< Read from client: 18 bytes read

	GET / HTTP/1.0

	> Write to client: 143 bytes written in 1 fragments


	HTTP/1.0 200 OK
	Content-Type: text/html

	<h2>mbed TLS Test Server</h2>
	<p>Successful connection using: TLS-ECJPAKE-WITH-AES-128-CCM-8</p>

	. Closing the connection... done
	. Waiting for a remote connection ... ok
	. Performing the SSL/TLS handshake... failed
	! mbedtls_ssl_handshake returned -0x7900

	. Waiting for a remote connection ...

由于关闭了连接，忽略最后的握手失败信息。

如果服务器没有接收到信息，使用网络流量分析器，如 Wireshark。

重启开发板。

参考
**********

- https://tls.mbed.org/
