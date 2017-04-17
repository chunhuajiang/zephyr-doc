.. _http-server-sample:

HTTP 服务器
###########

概述
********

HTTP 服务器示例程序基于 HTTP 解析器库实现了一个基本的 TCP 服务，能够接收并解析 HTTP 1.1 请求，并回送响应的响应消息。

本示例不会从文件系统上获取服务内容，而是动态地生成 HTTP 1.1 响应。源代码中的示例包括如何创建 HTTP 1.1 响应：
200 OK、400 错误的请求、403 禁止、404 Not Found 以及软 HTTP 错误，例如带有 404 Not Found HTML 消息的 200 OK。

本示例相关源码位于： :file:`samples/net/http_server`。

需求
************

- Linux 机器，可以使用 wget 命令，可以监视串口终端输出
- Freedom 开发板（FRDM-K64F）
- 用于测试的 LAN (Ethernet)

编译和运行
********************

HTTP 服务器当前所配置的监听端口是 80，该值定义在文件 :file:`samples/net/http_server/src/config.h` 中：

.. code-block:: c

	#define ZEPHYR_PORT		80


打开您的平台所对应的工程配置文件（例如 :ref:`frdm_k64f` 开发板对应的配置文件是 :file:`prj_frdm_k64f.conf`）。对于 IPv4 网络，设置如下变量：

.. code-block:: console

	CONFIG_NET_IPV4=y
	CONFIG_NET_IPV6=n

在本示例中，优先选择的路由技术的 IPv6。也就是说，如果 CONFIG_NET_IPV6=y 被设置，则 CONFIG_NET_IPV4=y 的值将会被忽略。、

本示例仅支持静态 IP 地址，这些地址在工程的配置文件中指定，例如：

.. code-block:: console

	CONFIG_NET_SAMPLES_MY_IPV6_ADDR="2001:db8::1"
	CONFIG_NET_SAMPLES_MY_IPV4_ADDR="192.168.1.101"

添加 URL
===========

如果要定义新的 URL 或者改变 HTTP 服务器对已有 URL 的处理方式，打开文件 :file:`samples/net/http_server/src/main.c` 并定位到如下代码：

.. code-block:: c

	http_url_default_handler(http_write_soft_404_not_found);
	http_url_add("/headers", HTTP_URL_STANDARD, http_write_header_fields);
	http_url_add("/index.html", HTTP_URL_STANDARD, http_write_it_works);

上面代码的第一行用于定义 Zephyr 如何处理未知 URL。在这种情形下，Zephyr 会响应一个软 HTTP 404 状态码，即一个 HTTP 200 OK 状态码，但是它的 body 是 404 Not Found HTML。

第二行必须按照如下的方式理解：对 /headers、/headers/index.html 以及更一般的 /headers/xxx 的请求将会触发例行程序 http_write_header_fields —— 打印所接收到的 HTTP 头部字段。在这种情形下，"xxx" 必须被理解为 /headers/ URL 下面的任何资源。

第三行将会触发另一个例行程序 —— 当找到 URL /index.html 或者 /index.html/xxx 时打印一个 HTML（It Works!）消息。

为了在您的 Linux 主机上编译这个示例程序，请打开一个终端窗口，进入示例程序所在目录并输入：

.. code-block:: console

	make BOARD=frdm_k64f

FRDM K64F 开发板会被主机识别成一个 USB 存储设备。烧写镜像文件前，开发板必须被挂在到某个目录（例如 /mnt）。烧写：

.. code-block:: console

    $ cp outdir/frdm_k64f/zephyr.bin /mnt

在 Linux 上，使用 `dmesg` 命令可以查看 FRDM 串行控制台的 USB 设备。假设该设备是 ttyACM0，打开中断查看并输入：

.. code-block:: console

    $ screen /dev/ttyACM0 115200

镜像文件被加载到 FRDM 开发板后，按下 RESET 按键。

关于 FRDM-K64F 的更多信息（以及如何在其它操作系统下访问 FRDM 串行控制台）请查看 Zephyr 中的开发板文档 :ref:`frdm_k64f`。

示例输出
=============

假设该 HTTP 服务器被配置用于监听 192.168.1.101 的 80 端口。在您的 Linux 主机上，打开一个终端窗口并输入：

.. code-block:: console

	wget 192.168.1.101/index.html

执行上面的 wget 命令后将会显示：

.. code-block:: console

	--2017-01-17 00:37:44--  http://192.168.1.101/
	Connecting to 192.168.1.101:80... connected.
	HTTP request sent, awaiting response... 200 OK
	Length: unspecified [text/html]
	Saving to: ‘index.html’

由 Zephyr 所产生并被 wget 所下载的 HTML 文件的内容是：

.. code-block:: html

	<html>
	<head>
	<title>Zephyr HTTP Server</title>
	</head>
	<body><h1><center>It Works!</center></h1></body>
	</html>

串口监视终端将显示打印如下消息：

.. code-block:: console

	[dev/eth_mcux] [INF] eth_0_init: Enabled 100M full-duplex mode.
	[dev/eth_mcux] [DBG] eth_0_init: MAC 00:04:9f:c9:29:6e
	Zephyr HTTP Server
	Address: 192.168.1.101, port: 80

	----------------------------------------------------
	[print_client_banner:42] Connection accepted
	Address: 192.168.1.10, port: 54327
	[http_ctx_get:268] Free ctx found, index: 0
	[http_write:59] net_nbuf_get_tx, rc: 0 <OK>
	[http_write:82] net_context_send: 0 <OK>
	[http_rx_tx:86] Connection closed by peer


要获取 HTTP 头部字段的 web 页面，使用下面的命令：

.. code-block:: console

	wget 192.168.1.101/headers -O index.html

执行上面的 wget 命令后将会显示：

.. code-block:: console

	--2017-01-19 22:09:55--  http://192.168.1.101/headers
	Connecting to 192.168.1.101:80... connected.
	HTTP request sent, awaiting response... 200 OK
	Length: unspecified [text/html]
	Saving to: ‘index.html’

由 Zephyr 所产生并被 wget 所下载的 HTML 文件的内容是：

.. code-block:: html

	<html>
	<head>
	<title>Zephyr HTTP Server</title>
	</head>
	<body>
	<h1>Zephyr HTTP server</h1>
	<h2>HTTP Header Fields</h2>
	<ul>
	<li>User-Agent: Wget/1.16 (linux-gnu)</li>
	<li>Accept: */*</li>
	<li>Host: 192.168.1.101</li>
	<li>Connection: Keep-Alive</li>
	</ul>
	<h2>HTTP Method: GET</h2>
	<h2>URL: /headers</h2>
	<h2>Server: arm</h2>
	</body>
	</html>

要测试 404 Not Found 软错误，使用下面的命令：

.. code-block:: console

	wget 192.168.1.101/not_found -O index.html

Zephyr 将会将生成一个具有如下头部的 HTTP 响应：

.. code-block:: console

	HTTP/1.1 200 OK
	Content-Type: text/html
	Transfer-Encoding: chunked

wget 将会保存的 HTML 文件的内容是：

.. code-block:: html

	<html>
	<head>
	<title>Zephyr HTTP Server</title>
	</head>
	<body><h1><center>404 Not Found</center></h1></body>
	</html>

HTTPS 服务器
============

本示例还包含一个 HTTPS（(HTTP over TLS） 服务器，它与 HTTP 服务器并行运行。在 qemu 中运行该示例：

.. code-block:: console

        make BOARD=qemu_x86 run

本示例仅支持一个 Hard-coded 的 URL（index.html）。如果接收到其它请求，服务器将会返回 404 代码。

示例的输出
=============

程序会在屏幕上显示如下消息：

.. code-block:: console

	Zephyr HTTP Server
	Address: 192.0.2.1, port: 80
	Zephyr HTTPS Server
	Address: 192.0.2.1, port: 443
	failed
	! mbedtls_ssl_handshake returned -29312

在另一个终端窗口执行如下的命令：

.. code-block:: console

	wget https://192.0.2.1 --no-check-certificate

屏幕上将显示如下消息：

.. code-block:: console

	Connecting to 192.0.2.1:443... connected.
	WARNING: cannot verify 192.0.2.1's certificate
	Unable to locally verify the issuer's authority.
	HTTP request sent, awaiting response... 200 OK
	Length: unspecified [text/html]
	Saving to: ‘index.html’

	index.html                                            [ <=> ]

检查文件 index.html 将会显示：

.. code-block:: console

	<h2>Zephyr TLS Test Server</h2>
	<p>Successful connection</p>

已知问题和限制
============================

- 本示例当前只能以块差（chunk）传输模式产生 HTTP 响应。
- 客户端必须先关闭连接，以允许 HTTP 服务器释放网络上下文，然后 HTTP 服务器才能接受另一连接。
- 使用 mbedTLS 和 IPv6 所需资源超过仿真平台的可用 ram，因此当前 QEMU 仅支持 IPv4。
