开发蓝牙应用
#################################

初始化
**************

函数 :c:func:`bt_init()` 用于初始化蓝牙子系统。调用者应当通过返回的错误代码判断初始化是否成功。如果一个函数指针被传递给 :c:func:`bt_init()` 了，初始化会同步发生，且会通过所给函数通知其完成。

蓝牙应用例程
*****************************

下面演示了一个蓝牙信标应用例程。该程序初始化了蓝牙子系统，使能了非连接广告，并高效地扮演了低功耗蓝牙广播者的身份。

.. literalinclude:: ../../../samples/bluetooth/beacon/src/main.c
   :language: c
   :lines: 19-
   :linenos:

信标应用中比较关键的 API 是 :c:func:`bt_enable()` 和 :c:func:`bt_le_adv_start()` 。:c:func:`bt_enable()` 用于初始化蓝牙协议栈；:c:func:`bt_le_adv_start()` 用于启动一个广播和扫描响应数据。

使用 QEMU 测试 
*****************

可以在 QEMU 中测试蓝牙应用程序。要达到此目的，需要将蓝牙控制器从主机操作系统（Linux）导出到模拟器。

在 QEMU 中使用主机系统蓝牙控制器
==============================================

主机操作系统的蓝牙控制器被 UNIX 套接字连接到第二个 QEMU 串行线。这个套接字使用 QEMU 选项 :literal:`-serial unix:/tmp/bt-server-bredr` 。在大多数蓝牙例程的 Makefile 文件中已经将使用 :makevar:`QEMU_EXTRA_FLAGS` 将其添加到 QEMU 中了，因此您可以在 make 时使用 'qemu' 目标。

在主机侧，BlueZ 允许通过一个叫做用户通道的方式将它的蓝牙控制器导出：

#. 确保蓝牙控制器已关闭。

#. 使用 btproxy 工具打开正在监听的 UNIX 套接字，输入：

   .. code-block:: console

      $ sudo tools/btproxy -u
      Listening on /tmp/bt-server-bredr

#. 选择位于 :literal:`samples/bluetooth` 中的某个例程。

#. 在 QEMU 中允许蓝牙用于，输入：

   .. code-block:: console

      $ make qemu

正在运行的 QEMU 将引起第二串行线与 :literal:`bt-server-bredr` UNIX 套接字进行连接，让应用程序能够访问蓝牙控制器。
