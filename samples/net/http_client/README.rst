.. _http-client-sample:

HTTP 客户端
###########

概述
********

本示例用于演示如何创建并向 HTTP 服务器发送一个 HTTP 1.1 请求，以及如何解析接收到的响应消息。当前支持的 HTTP 1.1 方法包括： GET、HEAD、OPTIONS 和 POST。

相关源代码位于： :file:`samples/net/http_client`。

需求
************

- Freedom 开发板（FRDM-K64F）
- 用于测试的局域网（LAN）—— Ethernet
- 终端仿真软件
- HTTP 服务器

编译和运行
********************

打开您的平台所对应的工程配置文件（例如 :ref:`frdm_k64f` 开发板对应的配置文件是 :file:`prj_frdm_k64f.conf`）。对于 IPv4 网络，设置如下变量：

.. code-block:: console

	CONFIG_NET_IPV4=y
	CONFIG_NET_IPV6=n

在本示例中，优先选择的路由技术的 IPv6。也就是说，如果 CONFIG_NET_IPV6=y 被设置，则 CONFIG_NET_IPV4=y 的值将会被忽略。、

本示例仅支持静态 IP 地址，这些地址在工程的配置文件中指定，例如：

.. code-block:: console

	CONFIG_NET_SAMPLES_MY_IPV6_ADDR="2001:db8::1"
	CONFIG_NET_SAMPLES_PEER_IPV6_ADDR="2001:db8::2"

分别是 HTTP 服务器和 HTTP 客户端的 IPv6 地址。

可选的，IP 地址也可以在 :file:`src/config.h` 文件中指定。

打开文件 :file:`src/config.h`，并设置一个与 HTTP 服务器设置相匹配的服务器端口，例如：

.. code-block:: c

   #define SERVER_PORT		80

表示 HTTP 服务器正在监听 TCP 端口 80。

HTTP 服务器
===========

在主机上设置 HTTP 服务器超出了本文档的讨论范围。我们使用 `Apache 2 <http://httpd.apache.org/docs/2.4/getting-started.html>`_ 测试本例程。

我们假设服务器的资源能够处理 HTTP 1.1 POST 请求。

例如，假设使用的服务器是支持 PHP 的 Apache 2，并假设发送一个内容包含 "Content-Type = application/x-www-form-urlencoded" 的 POST 请求，则客户端将会收到类似下面的由服务器发送回来的包含载荷长度 PHP 脚本：

.. code-block:: html

	<html>
	<head>
		<title>HTTP Server POST test</title>
	</head>
	<body>
		<?php
			echo '<p>POST key/values:</p>';
			foreach ($_POST as $key => $value) {
				echo "<p> {$key} : {$value} </p>";
			}
		?>
	</body>
	</html>

在运行 HTTP 服务器的那台机器上面，php 脚本位于 :file:`/var/www/html/post_test.php`。不过，您的测试机器. However, for your test machine
this path can be different, but should be at your server's root folder.

HTTP 响应
==============

接收到的服务器响应消息由文件 :file:`src/http_client_rcv.c` 中所定义的函数 http_receive_cb 进行处理。

本示例通过 HTTP 解析器库（参考 :file:`include/net/http_parser.h`）解析了 HTTP 头部字段，并将其打印到控制台。要处理 HTTP 响应的 body 字段，请使用 HTTP 解析器的回调来判断 body 是从何处开始的。如果载荷太长，解析器可能需要遍历网络缓冲的碎片链。示例代码 :file:`src/http_client_rcv.c` 的第 70 行演示了如何遍历碎片链。

FRDM K64F
=========

打开一个终端窗口并输出：

.. code-block:: console

    $ make BOARD=frdm_k64f

FRDM K64F 开发板会被主机识别成一个 USB 存储设备。烧写镜像文件前，开发板必须被挂在到某个目录（例如 /mnt）。烧写：

.. code-block:: console

    $ cp outdir/frdm_k64f/zephyr.bin /mnt

在 Linux 上，使用 `dmesg` 命令可以查看 FRDM 串行控制台的 USB 设备。假设该设备是 ttyACM0，打开中断查看并输入：

.. code-block:: console

    $ screen /dev/ttyACM0 115200

镜像文件被加载到 FRDM 开发板后，按下 RESET 按键。

关于 FRDM-K64F 的更多信息（以及如何在其它操作系统下访问 FRDM 串行控制台）请查看 Zephyr 中的开发板文档 :ref:`frdm_k64f`。

示例的输出
=============

本示例在指定的时间段内循环发送四个 HTTP 1.1 请求，并显示由接收到的来自服务器的响应中抽取出来的头部字段。这四个请求是：

- GET "/index.html"
- HEAD "/"
- OPTIONS "/"
- POST "/post_test.php"

中断窗口将会显示类似于下面的消息：

.. code-block:: console

	*******************************************
	HTTP Client: 2001:db8::1
	Connecting to: 2001:db8::2 port 80
	Hostname: 2001:db8::2
	HTTP Request: GET

	--------- HTTP response (headers) ---------
	Date: Thu, 02 Feb 2017 00:51:31 GMT
	Server: Apache/2.4.10 (Debian)
	Last-Modified: Sat, 28 Jan 2017 02:55:09 GMT
	ETag: "3c-5471eb5db3c73"
	Accept-Ranges: bytes
	Content-Length: 60
	Connection: close
	Content-Type: text/html

	HTTP server response status: OK
	HTTP parser status: success
	HTTP body: 60 bytes, expected: 60 bytes

	*******************************************
	HTTP Client: 2001:db8::1
	Connecting to: 2001:db8::2 port 80
	Hostname: 2001:db8::2
	HTTP Request: HEAD

	--------- HTTP response (headers) ---------
	Date: Thu, 02 Feb 2017 00:51:37 GMT
	Server: Apache/2.4.10 (Debian)
	Last-Modified: Sat, 28 Jan 2017 02:55:09 GMT
	ETag: "3c-5471eb5db3c73"
	Accept-Ranges: bytes
	Content-Length: 60
	Connection: close
	Content-Type: text/html

	HTTP server response status: OK
	HTTP parser status: success

	*******************************************
	HTTP Client: 2001:db8::1
	Connecting to: 2001:db8::2 port 80
	Hostname: 2001:db8::2
	HTTP Request: OPTIONS

	--------- HTTP response (headers) ---------
	Date: Thu, 02 Feb 2017 00:51:43 GMT
	Server: Apache/2.4.10 (Debian)
	Allow: GET,HEAD,POST,OPTIONS
	Content-Length: 0
	Connection: close
	Content-Type: text/html

	HTTP server response status: OK
	HTTP parser status: success

	*******************************************
	HTTP Client: 2001:db8::1
	Connecting to: 2001:db8::2 port 80
	Hostname: 2001:db8::2
	HTTP Request: POST

	--------- HTTP response (headers) ---------
	Date: Thu, 02 Feb 2017 00:51:49 GMT
	Server: Apache/2.4.10 (Debian)
	Vary: Accept-Encoding
	Content-Length: 231
	Connection: close
	Content-Type: text/html; charset=UTF-8

	HTTP server response status: OK
	HTTP parser status: success
