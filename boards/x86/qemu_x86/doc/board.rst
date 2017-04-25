.. _qemu_x86:

X86仿真(QEMU)
####################

概览
********

Zephyr内核使用qemu_x86主板配置以在QEMU上模拟运行奔腾级系统。此主板配置提供了对一个x86 Minute IA CPU及以下设备的支持：

* HPET（高精度定时器）
* Advanced Programmable Interrupt Controller (APIC高级可编程中断控制器)
* NS16550 UART


硬件
********

支持功能
==================

qemu_x86主板配置支持以下硬件功能:

+--------------+------------+-----------------------+
| Interface    | Controller | Driver/Component      |
+==============+============+=======================+
| HPET         | on-chip    | 系统时钟         |
+--------------+------------+-----------------------+
| APIC         | on-chip    | 中断控制器  |
+--------------+------------+-----------------------+
| NS16550      | on-chip    | 串口           |
| UART         |            |                       |
+--------------+------------+-----------------------+

设备
=======

HPET系统时钟支持
-------------------------

qemu_x86主板配置使用25 MHz的HPET时钟频率。

串口
-----------

qemu_x86主板配置使用了单个串口通信信道，它使用了轮询模式下的NS16550串口驱动。要重写，请打开UART_INTERRUPT_DRIVEN Kconfig选项，它允许系统的中断驱动。

已知问题或限制
=============================

不支持以下平台功能：

* 隔离存储区
* 串口的Direct Memory Access (DMA)模式
* Serial Peripheral Interface (SPI)闪存
* General-Purpose Input/Output (GPIO)
* Inter-Integrated Circuit (I2C)
* 以太网
* Supervisor Mode Execution Protection (SMEP)
