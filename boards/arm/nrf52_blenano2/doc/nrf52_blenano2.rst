.. _nrf52_blenano2:

Redbear Labs Nano v2
####################

概览
********
Nano V2是一块装备了Nordic的下一代nRF52832蓝牙低功耗SOC的开发板。此开发板设计作为BLE Nano的直接替代者，它们拥有相同的外形。Kickstart支持者在2017年2月可获取此开发板，也可以在Redbear商店买到。
https://redbear.cc/product/ble/ble-nano-kit-2.html

硬件
********
- nRF52832 SoC 在 32-bit ARM Cortex-M4F CPU 中集成了 512kB flash + 64kB RAM
- 11 x 数字 I/0
- 1 带硬件流控制的UART  ( 4 I/O pins 占用 )
- 1 I2C ( 2 I/O pins 占用 )



支持的功能
==================
BLE Nano v2主板配置支持以下硬件功能:

+-----------+------------+--------------------------------------+
| 接口      | 控制器     |      驱动/元件                       |
+===========+============+======================================+
| NVIC      | on-chip    | 嵌套向量中断控制器                   |
+-----------+------------+--------------------------------------+
| UART      | on-chip    | 串口                                 |
+-----------+------------+--------------------------------------+
| GPIO      | on-chip    | gpio                                 |
+-----------+------------+--------------------------------------+
| FLASH     | on-chip    | flash                                |
+-----------+------------+--------------------------------------+
| RADIO     | on-chip    | 蓝牙                                 |
+-----------+------------+--------------------------------------+
| I2C       | on-chip    | i2c                                  |
+-----------+------------+--------------------------------------+

连接与IOs
====================

BLE nano v2 引脚输出

.. image:: nano2.png
   :width: 680px
   :align: center
   :alt: NANO2

DAPLink 主板

.. image:: dap.jpg
   :width: 680px
   :align: center
   :alt: DAP

DAPLink USB 主板为一个电子狗。DAPLink调试探针在主机上显示为一个USB硬盘。还可通过板载LDO将USB的5V切换为3.3V以给Nano v2供电。


编程与调试
*************************

烧写
========

编译Zephyr内核与BLE示例应用程序:

.. code-block:: console

   $ cd $ZEPHYR_BASE
   $ . zephyr-env.sh
   $ make -C samples/bluetooth/beacon BOARD=nrf52_blenano2

- 将BLE Nano v2正确装入DAPLink USB电子狗。
- DAPLink USB电子狗插入你的计算机。
- PC会提示一个新的大容量存储器。
- 在文件夹samples/bluetooth/beacon/outdir/nrf52_blenano2中将生成文件zephyr.bin on folder samples/bluetooth/beacon/outdir/nrf52_blenano2 拷贝到DAPLink驱动器。
- 打开nRF连接应用以检查公告包。

参考
**********

.. target-notes::

.. _Kickstarter: https://www.kickstarter.com/projects/redbearinc/bluetooth-5-ready-ble-module-nano-2-and-blend-2
.. _Github: https://github.com/redbear/nRF5x
.. _RedBear Forum: discuss.redbear.cc
