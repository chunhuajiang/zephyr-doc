.. _quark_d2000_devboard:

Quark D2000开发板
#############################

概览
********

The Intel® Quark ™ 微控制器 D2000为40针QFN元件封装

.. image:: quark-d2000-developers-kit.png
   :width: 442px
   :align: center
   :alt: Quark D2000 Development Board

Intel™ Quark® 微控制器 D2000 包含以下部件:

- 板载元件:

  - 加速计/磁力计 传感器
  - USB调试端口的UART/JTAG与USB转换

- 扩展选项:

  - “Arduino Uno” 兼容 SIL sockets ( 仅3.3V IO )

- 其它连接器:

  - 1x USB 2.0 设备端口 – micro Type B
  - On-board coin cell battery holder
  - 5V 螺丝接线端/端口 输入端口 (外部电源或Li-ion)
  - EEMBC电源输入端口

硬件
********

主板的一般信息可在 `Intel Website`_找到，它包含了 `schematics`_ 以及 BRD 文件。

Intel® Quark™ 微处理器 D2000 开发平台支持常见的Arduino Uno Rev3.0硬件接口开放标准，以及与Uno Rev3.0物理兼容。它不支持6针ICSP端口。


支持功能
===================

+-----------+------------+-----------------------+
| Interface | Controller | Driver/Component      |
+===========+============+=======================+
| MVIC      | on-chip    | 中断控制器  |
+-----------+------------+-----------------------+
| UART      | on-chip    | 串口轮询 |
|           |            | 串口中断 |
+-----------+------------+-----------------------+
| SPI       | on-chip    | spi                   |
+-----------+------------+-----------------------+
| I2C       | on-chip    | i2c                   |
+-----------+------------+-----------------------+
| GPIO      | on-chip    | gpio                  |
+-----------+------------+-----------------------+
| PWM       | on-chip    | pwm                   |
+-----------+------------+-----------------------+


编程与调试
*************************

D2000主板配置详细信息可在:file:`boards/x86/quark_d2000_crb`.文件的项目树中找到。

编译此主板应用程序，需要调用以下命令：

.. code-block:: console

   $ make BOARD=quark_d2000_crb <make target>

烧写
========

#. 因为此主板已经内嵌JTAG；仅通过USB就可烧写设备。设置以下跳线以使能内嵌JTAG：

   +--------+------+--------+------+------+
   | Jumper | UART | Common | JTAG | Name |
   +========+======+========+======+======+
   | J9     | Open |   X    |  X   | TDO  |
   +--------+------+--------+------+------+
   | J10    | Open |   X    |  X   | TDI  |
   +--------+------+--------+------+------+
   | J11    | Open |   X    |  X   | TRST |
   +--------+------+--------+------+------+
   | J12    |  X   |  N/A   |  X   | TMS  |
   +--------+------+--------+------+------+
   | J17    |  X   |  N/A   |  X   | TCK  |
   +--------+------+--------+------+------+

#. 将D2000通过USB连接至主机。

#. 二进制文件编译完成后，可通过以下命令烧写：

   .. code-block:: console

      $ make BOARD=quark_d2000_crb flash

调试
=========

在Quark D2000主板上调试应用程序, 使用以下步骤。我们使用 :ref:`hello_world` 应用程序作为例子。

#. 进入应用程序目录:.

   .. code-block:: console

      $ cd $ZEPHYR_BASE/samples/hello_world

#.最终的二进制文件生成在 :file:`outdir/quark_d2000_crb/zephyr.elf`。

#. 要启动调试进程，请输入:

   .. code-block:: console

      $ make BOARD=quark_d2000_crb debug


.. _Intel Website:
   http://www.intel.com/content/www/us/en/embedded/products/quark/mcu/d2000/quark-d2000-crb-user-guide.html

.. _schematics:
   http://www.intel.com/content/www/us/en/embedded/products/quark/mcu/d2000/quark-d2000-crb-schematics.html

