.. _zperf-sample:

zperf: 网络流量发生器
################################

描述
***********

zperf是Zephyr的网络流量发生器，可用于评估网络带宽。

特征
*********

- 兼容iPerf_2.0.5.
- 客户端或服务器模式切换，无需修改源代码。
- 使用任务探测器（在编译zperf时设置PROFILER=1 ）

支持的开发板
****************

zperf是开发板无关的，尽管如此，要运行zperf应用示例，目标平台必须提供由Zephyr支持的网络接口。

此示例应用程序已经在以下平台经过测试:

- Freedom Board (FRDM K64F)
- Quark SE C1000 Development Board
- QEMU x86

需求
************

- 在主机安装iPerf 2.0.5
- 开发板支持

根据所选择的网络技术，可能需要额外的步骤来设置网络环境。

使用
*****

如果Zephyr作为一个客户端, iPerf必须运行在服务器模式下。以下命令行必须在UDP测试时使用:

.. code-block:: console

   $ iperf -s -l 1K -u -V -B 2001:db8::2

对于TCP测试, 命令行应该象这样:

.. code-block:: console

   $ iperf -s -l 1K -V -B 2001:db8::2


在Zephyr控制台, zperf可使用如下方法运行:

.. code-block:: console

   zperf> udp.upload 2001:db8::2 5001 10 1K 1M


对于TCP，zperf命令应该是这样的:

.. code-block:: console

   zperf> tcp.upload 2001:db8::2 5001 10 1K 1M


如果Zephyr和主机的IP地址在配置文件中指定，zperf可使用如下方法启动：

.. code-block:: console

   zperf> udp.upload2 v6 10 1K 1M


或者你希望测试TCP，可以这样:

.. code-block:: console

   zperf> tcp.upload2 v6 10 1K 1M


如果Zephyr作为服务器, 为UDP设置下载模式:

.. code-block:: console

   zperf> udp.download 5001


或者为TCP:

.. code-block:: console

   zperf> tcp.download 5001


在主机端, 如果你正在测试UDP，必须使用以下命令行执行iPerf:

.. code-block:: console

   $ iperf -l 1K -u -V -c 2001:db8::1 -p 5001


如果正在测试TCP，则:

.. code-block:: console

   $ iperf -l 1K -V -c 2001:db8::1 -p 5001


如果Zephyr不能以有序的方式接收所有数据包，可使用-b选项限制iPerf输出。
