.. _frdm_kw41z:

NXP FRDM-KW41Z
##############

概述
********



FRDM-KW41Z 是采用基于 ARM® Cortex®-M0+ 处理器的 Kinetis® W 系列 KW41Z/31Z/21Z (KW41Z) 系列支持的开发套件，具有集成的 2.4 GHz 收发器，支持 Bluetooth® Smart/Bluetooth®Low Energy (BLE) v4.2、Generic FSK、IEEE® 802.15.4 和 Thread 协议。

FRDM-KW41Z 套件包含两个 Freedom 电路板，可用作与主处理器连接的开发板或 Shield 扩展板。FRDM-KW41Z 的规格与 Arduino™ R3 引脚布局兼容，提供了更多的扩展选项。

FRDM-KW41Z 高灵敏度、优化的 2.4 GHz 无线电具有 PCB F 天线(可以绕过它，通过 SMA 连接进行测试)、多个电源选项、推拉式及电容式触摸按钮、开关、LED 和集成传感器。


.. image:: frdm_kw41z.jpg
   :width: 720px
   :align: center
   :alt: FRDM-KW41Z

硬件
********

- 可配置为与主处理器连接的主电路板或Shield扩展板
- 支持所有DC-DC配置(降压、升压和旁路)
- PCB反向F型天线
- SMA RF接头
- 获得射频监管认证
- OTA固件升级的串行闪存
- 板载恩智浦FXOS8700CQ数字传感器、3D加速度传感器 (±2g/±4g/±8g) + 3D磁力计
- OpenSDA和JTAG调试
- 全面的KSDK支持



关于 KW41Z SoC 和 FRDM-KW41Z 开发板的更多信息请参考：

- `KW41Z Website`_
- `KW41Z Datasheet`_
- `KW41Z Reference Manual`_
- `FRDM-KW41Z Website`_
- `FRDM-KW41Z User Guide`_
- `FRDM-KW41Z Schematics`_

支持的功能
==================

frdm_kw41z 开发板配置支持如下的硬件功能：

+-----------+------------+-------------------------------------+
| Interface | Controller | Driver/Component                    |
+===========+============+=====================================+
| NVIC      | on-chip    | nested vector interrupt controller  |
+-----------+------------+-------------------------------------+
| SYSTICK   | on-chip    | systick                             |
+-----------+------------+-------------------------------------+
| PINMUX    | on-chip    | pinmux                              |
+-----------+------------+-------------------------------------+
| GPIO      | on-chip    | gpio                                |
+-----------+------------+-------------------------------------+
| I2C       | on-chip    | i2c                                 |
+-----------+------------+-------------------------------------+
| UART      | on-chip    | serial port-polling;                |
|           |            | serial port-interrupt               |
+-----------+------------+-------------------------------------+
| FLASH     | on-chip    | soc flash                           |
+-----------+------------+-------------------------------------+
| SENSOR    | off-chip   | fxos8700 polling:                   |
|           |            | fxos8700 trigger                    |
+-----------+------------+-------------------------------------+

默认的配置可以在 defconfig 文件中找到：

	``boards/arm/frdm_kw41z/frdm_kw41z_defconfig``

当前还未支持其它硬件功能。

连接与 IO
===================

KW41Z SoC 有三对 pinmux/gpio 控制器，但是 FRDM-KW41Z 开发板当前只使能了其中两对（PORTA/GPIOA 和 PORTC/GPIOC）。

+-------+-------------+---------------------------+
| Name  | Function    | Usage                     |
+=======+=============+===========================+
| PTC1  | GPIO        | Red LED / FXOS8700 INT1   |
+-------+-------------+---------------------------+
| PTA19 | GPIO        | Green LED                 |
+-------+-------------+---------------------------+
| PTA18 | GPIO        | Blue LED                  |
+-------+-------------+---------------------------+
| PTC2  | I2C1_SCL    | I2C / FXOS8700            |
+-------+-------------+---------------------------+
| PTC3  | I2C1_SDA    | I2C / FXOS8700            |
+-------+-------------+---------------------------+
| PTC4  | GPIO        | SW3                       |
+-------+-------------+---------------------------+
| PTC5  | GPIO        | SW4                       |
+-------+-------------+---------------------------+
| PTC6  | LPUART0_RX  | UART Console              |
+-------+-------------+---------------------------+
| PTC7  | LPUART0_TX  | UART Console              |
+-------+-------------+---------------------------+

系统时钟
============

KW41Z SoC 使用开发板上的 32 MHz 外部晶振，并使用板载 FLL 产生一个 40 MHz的系统时钟。

串口
===========

KW41Z SoC 有一个 UART，用作控制台功能。

编程和调试
*************************

烧写
========

FRDM-KW41Z 包括一个 `OpenSDA`_ 串行和调试适配器，它提供了：

- 与主机 PC 的 USB 连接，暴露了一个大容量存储设备和一个 USB 串口。connection to the host computer, which exposes a Mass Storage and an
  USB Serial Port.
- 一个串行 Flash 设备，实现了 USB flash 磁盘设备存储。
- 一个物理 UART 连接，作为 USB 串口的中继。

烧写应用程序到 FRDM-KW41Z
-------------------------------------

这里以实例程序 :ref:`hello_world` 作为例子。编译 Zephyr 内核和应用程序：

.. code-block:: console

   $ cd $ZEPHYR_BASE
   $ . zephyr-env.sh
   $ cd $ZEPHYR_BASE/samples/hello_world/
   $ make BOARD=frdm_kw41z

使用 USB 口将 FRDM-KW41Z 连接到您的主机 PC 上，您将看到一个大容量存储设备（DAPLINK）和一个 USB 串口。然后，将生成的 zephyr.bin 拷贝到 DAPLINK 中。

复位开发板，您将在相应的串口上看到如下消息：

.. code-block:: console

   Hello World! arm


.. _FRDM-KW41Z Website:
   http://www.nxp.com/products/microcontrollers-and-processors/more-processors/application-specific-mcus-mpus/bluetooth-low-energy-ble/nxp-freedom-development-kit-for-kinetis-kw41z-31z-21z-mcus:FRDM-KW41Z

.. _FRDM-KW41Z User Guide:
   http://www.nxp.com/assets/documents/data/en/user-guides/FRDMKW41ZUG.pdf

.. _FRDM-KW41Z Schematics:
   http://www.nxp.com/assets/downloads/data/en/schematics/FRDM-KW41Z-SCH.pdf

.. _OpenSDA:
   http://www.nxp.com/products/software-and-tools/hardware-development-tools/startertrak-development-boards/opensda-serial-and-debug-adapter:OPENSDA#FRDM-KW41Z

.. _KW41Z Website:
   http://www.nxp.com/products/microcontrollers-and-processors/arm-processors/kinetis-cortex-m-mcus/w-series-wireless-m0-plus-m4/kinetis-kw41z-2.4-ghz-dual-mode-ble-and-802.15.4-wireless-radio-microcontroller-mcu-based-on-arm-cortex-m0-plus-core:KW41Z

.. _KW41Z Datasheet:
   http://www.nxp.com/assets/documents/data/en/data-sheets/MKW41Z512.pdf

.. _KW41Z Reference Manual:
   http://www.nxp.com/assets/documents/data/en/reference-manuals/MKW41Z512RM.pdf
