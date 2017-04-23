.. _mbedtsl-delsserver-sample:

mbedTLS DTLS 服务器示例
############################

概览
********
本示例演示了在 Zephyr 下使用 mbed TLS 实现的简单的 DTLS（Datagram Transport Layer Security 数据包传输层安全协议）服务器。

编译和运行
********************

下列步骤用于测试  :ref:`使用 QEMU 网络仿真 <networking_with_qemu>`。

在应用程序目录下输入:

.. code-block:: console

   $make run

.. code-block:: console

   . Seeding the random number generator... ok
   . Setting up the DTLS structure... ok
   . Setting connection
   ok
   . Setting up ecjpake password ... ok
   . Performing the TLS handshake...
 
在另一终端窗口, 包含 mbed TLS 代码：

	https://tls.mbed.org/download/start/mbedtls-2.3.0-apache.tgz

将它放入 Linux 主机的众所周知的目录下, 作为客户端。

在你的主机上进入那个目录并编译 mbedTLS。

.. code-block:: console

   tar -xvzf mbedtls-2.3.0-apache.tgz
   cd mbedtls-2.3.0
   CFLAGS="-I$PWD/configs -DMBEDTLS_CONFIG_FILE='<config-thread.h>'" make

   ./programs/ssl/ssl_client2 server_addr=192.0.2.1 dtls=1 ecjpake_pw=passwd

将会输出如下内容:

.. code-block:: console

   . Seeding the random number generator... ok
   . Connecting to udp/192.0.2.1/4433... ok
   . Setting up the SSL/TLS structure... ok
   . Performing the SSL/TLS handshake... ok
   [ Protocol is DTLSv1.2 ]
   [ Ciphersuite is TLS-ECJPAKE-WITH-AES-128-CCM-8 ]
   [ Record expansion is 29 ]
   [ Maximum fragment length is 16384 ]
   > Write to server: 34 bytes written in 1 fragments

   GET / HTTP/1.0
   Extra-header:


   < Read from server: 34 bytes read

   GET / HTTP/1.0
   Extra-header:

   . Closing the connection... done

应用程序目录窗口会显示：

.. code-block:: console

   . Performing the TLS handshake... hello verification requested
   . Setting up ecjpake password ... ok
   . Performing the TLS handshake... ok
   < Read from client: 34 bytes read

   GET / HTTP/1.0
   Extra-header:


   > Write to client: 34 bytes written

   GET / HTTP/1.0
   Extra-header:

   < Read from client: connection was closed gracefully
   . Closing the connection... done
   . Setting up ecjpake password ... ok
   . Performing the TLS handshake...

如果要使用 IPv6，编辑文件 prj_qemu_x86.conf，并将 CONFIG_NET_IPV6=n 变为 CONFIG_NET_IPV6=y。

在 mbedTLS 上运行客户端：

.. code-block:: console

   ./programs/ssl/ssl_client2 server_addr=2001:db8::1 dtls=1 ecjpake_pw=passwd

如果服务器没有接收到信息, 重启应用程序，并再次尝试连接客户端。

参考
**********

* https://tls.mbed.org/
