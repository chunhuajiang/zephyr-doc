.. _qemu_cortex_m3:

ARM Cortex-M3 模拟器 (QEMU)
##############################

概览
********

Zephyr内核使用qemu_cortex_m3主板配置来模拟在QEMU上运行TI LM3S6965平台。它提供对ARM Cortex-M3 CPU和以下设备的支持：

* 嵌套向量中断控制器
* System Tick System Clock
* Stellaris UART

.. note::
   此主板配置对使用实际ti_lm3s6965硬件系统及其它硬件系统没有适用性要求。

硬件
********
支持功能
==================

qemu_cortex_m3主板配置支持以下硬件功能：

+--------------+------------+----------------------+
| 接口         | 控制器     | 驱动/元件            |
+==============+============+======================+
| NVIC         | on-chip    | 嵌套向量中断控制器   |
+--------------+------------+----------------------+
| Stellaris    | on-chip    | 串口                 |
| UART         |            |                      |
+--------------+------------+----------------------+
| SYSTICK      | on-chip    | 系统时钟             |
+--------------+------------+----------------------+

此平台内核当前不支持上的其它硬件功能

设备
========
系统时钟
------------

qemu_cortex_m3主板配置所使用的系统时钟为12 MHz。

串口
-----------

qemu_cortex_m3主板配置使用单个CPU UART0串口通信信道。

已知问题和限制
==============================

不支持以下平台功能:

* 可选MPU内存保护。但是可在ROM内使用XIP内核有效提供TEXT/RODATA写保护。
* 地址为0x1FFF0000-0x1FFFFFFF的SRAM
* 写硬件flash闪存

参考
**********

1. The Definitive Guide to the ARM Cortex-M3, Second Edition by Joseph Yiu (ISBN
   978-0-12-382090-7)
2. ARMv7-M Architecture Technical Reference Manual (ARM DDI 0403D ID021310)
3. Procedure Call Standard for the ARM Architecture (ARM IHI 0042E, current
   through ABI release 2.09, 2012/11/30)
4. Cortex-M3 Revision r2p1 Technical Reference Manual (ARM DDI 0337I ID072410)
5. Cortex-M3 Devices Generic User Guide (ARM DUI 0052A ID121610)
