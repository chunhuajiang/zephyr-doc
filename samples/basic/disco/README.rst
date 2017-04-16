.. _disco-sample:

Disco 示例
##########

概览
********

一个简单的 ‘disco’ 示例。此示例假定 2 个 LED 已经连接至主板 MCU 的 GPIO 输出引脚。


连线
******

在其它主板运行时，需要修改代码：按照主板的 GPIO 配置去设置 PORT、LED1 和 LED2。

Nucleo-64 F103RB/F401RE 开发板
==============================

将两个 LED 灯连接至 PB5 和 PB8 引脚。PB5 被映射至 Arduino 的 D4 引脚，PB8 对应 D15。有关此开发板的更详细信息请参考：

- https://developer.mbed.org/platforms/ST-Nucleo-F103RB/
- https://developer.mbed.org/platforms/ST-Nucleo-F401RE/

Arduino 101 (x86)
=================

将两个 LED 连接至 D4（IO4）和 D7（IO7）引脚。Arduino 101 开发板图表可参考：

https://www.arduino.cc/en/uploads/Main/Arduino101-REV4Schematic.pdf

Arduino 101 在 Zephyr 中的 pinmux（引脚复用）映射请参考： :file:`boards/x86/arduino_101/pinmux.c`

更改 src/main.c 文件并设置:

.. code-block:: c

   #define PORT	CONFIG_GPIO_QMSI_0_NAME
   /* GPIO_19 is Arduino's D4 */
   #define LED1	19
   /* GPIO_20 is Arduino's D7 */
   #define LED2	20

编译和运行
*********************

启动之后，程序寻找由 ‘PORT’ 定义的预定义 GPIO 设备，并将 ‘LED1’ 和 ‘LED2’ 引脚配置为输出状态。在主循环的每个迭代期间，更改 GPIO 状态，使得一个处于高电平状态时另一个处于低电平状态，从而在交替模式中切换 LED 的亮灭。

此项目不输出串口控制台，取而代之的是 GPIO 设备所连接的两个 LED 在交替模式中闪烁。

示例可在此目录中获取： :file:`samples/basic/disco`.

Nucleo F103RB
=============

.. code-block:: console

   $ make BOARD=nucleo_f103rb

Nucleo F401RE
=============

.. code-block:: console

   $ make BOARD=nucleo_f401re

Arduino 101
============

.. code-block:: console

   $ make BOARD=arduino_101

