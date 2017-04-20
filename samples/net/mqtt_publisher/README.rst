.. _mqtt-publisher-sample:

MQTT 发布机
##############

概述
********

`MQTT <http://mqtt.org/>`_ (Message Queuing  Telemetry Transport 消息队列遥测传输) 是一个轻量级发布/订阅信息协议，为小型传感器及移动设备而优化。

Zephyr MQTT 发布机示例应用程序是一个 MQTT v3.1.1 客户端，它向 MQTT 代理传送 MQTT PUBLISH 消息。参考 `MQTT V3.1.1 spec`_ 获取更多信息。

.. _MQTT V3.1.1 spec: http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html

此示例应用源码位于：:file:`samples/net/mqtt_publisher`.

需求
************

- Linux 机器
- 自由板 (FRDM-K64F)
- Mosquitto 服务器: 支持 MQTT v3.1.1 的任意版本。 此例在 mosquitto 1.3.4上经过测试。
- Mosquitto 订阅者
- 用于测试目的的 LAN (以太网)

编译和运行
*****************

当前，此示例仅支持静态 IP 地址。打开 :file:`src/config.h` 文件， 并依照局域网环境设置 IP 地址。或者在 :file:`prj_frdm_k64f.conf` 文件中设置 IP 地址。

:file:`src/config.h` 文件也包含了一些需要设置的变量:

MQTT 代理的 TCP 端口：

.. code-block:: c

	#define SERVER_PORT		1883

应用程序睡眠时间：

.. code-block:: c

	#define APP_SLEEP_MSECS		500

应用程序的接收和发送超时：

.. code-block:: c

	#define APP_TX_RX_TIMEOUT       300

最大尝试连接次数：

.. code-block:: c

	#define APP_CONNECT_TRIES	10

MQTT PUBLISH 最大迭代次数：

.. code-block:: c

	#define APP_MAX_ITERATIONS	5

MQTT 客户端标识：

.. code-block:: c

	#define MQTT_CLIENTID		"zephyr_publisher"

此示例应用支持 IBM Bluemix Watson 主题格式，可将 APP_BLUEMIX_TOPIC 默认值由 0 变为 1:

.. code block:: c

	#define APP_BLUEMIX_TOPIC	1

Bluemix 主题可以包含一些参数如设备类型、设备标识符、事件类型和消息格式。此应用使用以下宏来指定这些值：

.. code block:: c

	#define BLUEMIX_DEVTYPE		"sensor"
	#define BLUEMIX_DEVID		"carbon"
	#define BLUEMIX_EVENT		"status"
	#define BLUEMIX_FORMAT		"json"

在你的 Linux 主机上, 打开终端窗口, 定位到此应用程序的源码 (即 :file:`samples/net/mqtt_publisher`) 并输入：

.. code-block:: console

	make BOARD=frdm_k64f

打开另一个终端窗口并输入:

.. code-block:: console

	sudo mosquitto -v -p 1883

打开另一个终端窗口并输入:

.. code-block:: console

	mosquito_sub -t sensors

示例输出
=============

以下是输出来自 FRDM UART 控制台，参数设置为:

.. code-block:: c

	#define APP_MAX_ITERATIONS     5

.. code-block:: console

	[dev/eth_mcux] [INF] eth_0_init: Enabled 100M full-duplex mode.
	[dev/eth_mcux] [DBG] eth_0_init: MAC 00:04:9f:3e:1a:0a
	[publisher:233] network_setup: 0 <OK>
	[publisher:258] mqtt_init: 0 <OK>
	[connect_cb:81] user_data: CONNECTED
	[try_to_connect:212] mqtt_tx_connect: 0 <OK>
	[publisher:276] try_to_connect: 0 <OK>
	[publisher:285] mqtt_tx_pingreq: 0 <OK>
	[publisher:290] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBACK> packet id: 1888, user_data: PUBLISH
	[publisher:295] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBREC> packet id: 16356, user_data: PUBLISH
	[publish_cb:149] <MQTT_PUBCOMP> packet id: 16356, user_data: PUBLISH
	[publisher:300] mqtt_tx_publish: 0 <OK>
	[publisher:285] mqtt_tx_pingreq: 0 <OK>
	[publisher:290] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBACK> packet id: 45861, user_data: PUBLISH
	[publisher:295] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBREC> packet id: 53870, user_data: PUBLISH
	[publish_cb:149] <MQTT_PUBCOMP> packet id: 53870, user_data: PUBLISH
	[publisher:300] mqtt_tx_publish: 0 <OK>
	[publisher:285] mqtt_tx_pingreq: 0 <OK>
	[publisher:290] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBACK> packet id: 60144, user_data: PUBLISH
	[publisher:295] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBREC> packet id: 6561, user_data: PUBLISH
	[publish_cb:149] <MQTT_PUBCOMP> packet id: 6561, user_data: PUBLISH
	[publisher:300] mqtt_tx_publish: 0 <OK>
	[publisher:285] mqtt_tx_pingreq: 0 <OK>
	[publisher:290] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBACK> packet id: 38355, user_data: PUBLISH
	[publisher:295] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBREC> packet id: 60656, user_data: PUBLISH
	[publish_cb:149] <MQTT_PUBCOMP> packet id: 60656, user_data: PUBLISH
	[publisher:300] mqtt_tx_publish: 0 <OK>
	[publisher:285] mqtt_tx_pingreq: 0 <OK>
	[publisher:290] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBACK> packet id: 28420, user_data: PUBLISH
	[publisher:295] mqtt_tx_publish: 0 <OK>
	[publish_cb:149] <MQTT_PUBREC> packet id: 49829, user_data: PUBLISH
	[publish_cb:149] <MQTT_PUBCOMP> packet id: 49829, user_data: PUBLISH
	[publisher:300] mqtt_tx_publish: 0 <OK>
	[disconnect_cb:101] user_data: DISCONNECTED
	[publisher:304] mqtt_tx_disconnect: 0 <OK>

	Bye!

下行:

.. code-block:: console

	[try_to_connect:220] mqtt_connect: -5 <ERROR>

表示检测到一个错误，并准备发送一个新的连接信息。

MQTT API 是异步的, 所以消息在回调函数执行时显示。

以下为订阅者收到的信息:

.. code-block:: console

	mosquitto_sub -t sensors
	DOORS:OPEN_QoS0
	DOORS:OPEN_QoS1
	DOORS:OPEN_QoS2
	DOORS:OPEN_QoS0
	DOORS:OPEN_QoS1
	DOORS:OPEN_QoS2
	DOORS:OPEN_QoS0
	DOORS:OPEN_QoS1
	DOORS:OPEN_QoS2
	DOORS:OPEN_QoS0
	DOORS:OPEN_QoS1
	DOORS:OPEN_QoS2
	DOORS:OPEN_QoS0
	DOORS:OPEN_QoS1
	DOORS:OPEN_QoS2

以下为 MQTT 代理输出信息:

.. code-block:: console

	sudo mosquitto -v
	1485663791: mosquitto version 1.3.4 (build date 2014-08-17 00:14:52-0300) starting
	1485663791: Using default config.
	1485663791: Opening ipv4 listen socket on port 1883.
	1485663791: Opening ipv6 listen socket on port 1883.
	1485663797: New connection from 192.168.1.101 on port 1883.
	1485663797: New client connected from 192.168.1.101 as zephyr_publisher (c1, k0).
	1485663797: Sending CONNACK to zephyr_publisher (0)
	1485663798: Received PINGREQ from zephyr_publisher
	1485663798: Sending PINGRESP to zephyr_publisher
	1485663798: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
	1485663799: Received PUBLISH from zephyr_publisher (d0, q1, r0, m1888, 'sensors', ... (15 bytes))
	1485663799: Sending PUBACK to zephyr_publisher (Mid: 1888)
	1485663799: Received PUBLISH from zephyr_publisher (d0, q2, r0, m16356, 'sensors', ... (15 bytes))
	1485663799: Sending PUBREC to zephyr_publisher (Mid: 16356)
	1485663799: Received PUBREL from zephyr_publisher (Mid: 16356)
	1485663799: Sending PUBCOMP to zephyr_publisher (Mid: 16356)
	1485663800: Received PINGREQ from zephyr_publisher
	1485663800: Sending PINGRESP to zephyr_publisher
	1485663800: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
	1485663801: Received PUBLISH from zephyr_publisher (d0, q1, r0, m45861, 'sensors', ... (15 bytes))
	1485663801: Sending PUBACK to zephyr_publisher (Mid: 45861)
	1485663801: Received PUBLISH from zephyr_publisher (d0, q2, r0, m53870, 'sensors', ... (15 bytes))
	1485663801: Sending PUBREC to zephyr_publisher (Mid: 53870)
	1485663801: Received PUBREL from zephyr_publisher (Mid: 53870)
	1485663801: Sending PUBCOMP to zephyr_publisher (Mid: 53870)
	1485663802: Received PINGREQ from zephyr_publisher
	1485663802: Sending PINGRESP to zephyr_publisher
	1485663802: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
	1485663803: Received PUBLISH from zephyr_publisher (d0, q1, r0, m60144, 'sensors', ... (15 bytes))
	1485663803: Sending PUBACK to zephyr_publisher (Mid: 60144)
	1485663803: Received PUBLISH from zephyr_publisher (d0, q2, r0, m6561, 'sensors', ... (15 bytes))
	1485663803: Sending PUBREC to zephyr_publisher (Mid: 6561)
	1485663803: Received PUBREL from zephyr_publisher (Mid: 6561)
	1485663803: Sending PUBCOMP to zephyr_publisher (Mid: 6561)
	1485663804: Received PINGREQ from zephyr_publisher
	1485663804: Sending PINGRESP to zephyr_publisher
	1485663804: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
	1485663805: Received PUBLISH from zephyr_publisher (d0, q1, r0, m38355, 'sensors', ... (15 bytes))
	1485663805: Sending PUBACK to zephyr_publisher (Mid: 38355)
	1485663805: Received PUBLISH from zephyr_publisher (d0, q2, r0, m60656, 'sensors', ... (15 bytes))
	1485663805: Sending PUBREC to zephyr_publisher (Mid: 60656)
	1485663805: Received PUBREL from zephyr_publisher (Mid: 60656)
	1485663805: Sending PUBCOMP to zephyr_publisher (Mid: 60656)
	1485663806: Received PINGREQ from zephyr_publisher
	1485663806: Sending PINGRESP to zephyr_publisher
	1485663806: Received PUBLISH from zephyr_publisher (d0, q0, r0, m0, 'sensors', ... (15 bytes))
	1485663807: Received PUBLISH from zephyr_publisher (d0, q1, r0, m28420, 'sensors', ... (15 bytes))
	1485663807: Sending PUBACK to zephyr_publisher (Mid: 28420)
	1485663807: Received PUBLISH from zephyr_publisher (d0, q2, r0, m49829, 'sensors', ... (15 bytes))
	1485663807: Sending PUBREC to zephyr_publisher (Mid: 49829)
	1485663807: Received PUBREL from zephyr_publisher (Mid: 49829)
	1485663807: Sending PUBCOMP to zephyr_publisher (Mid: 49829)
	1485663808: Received DISCONNECT from zephyr_publisher
