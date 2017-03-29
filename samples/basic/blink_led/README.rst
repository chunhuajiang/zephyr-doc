PWM: LED 闪烁
##############

概述
********
本示例将会使用 PWM 让 LED 灯闪烁。

The LED will start at a blinking frequency of 0.5Hz. Every 4 seconds,
the blinking frequency will double. When the blinking frequency
reaches 500Hz, the blinking frequency will be halved every 4 seconds
until the blinking frequency reaches 0.5Hz. This completes a whole
blinking cycle. From now on, the LED will repeat the blinking cycle
for ever.

连线
******

Arduino 101 和 Quark D2000 CRB
===============================
You will need to connect the LED to ground and PWM0 via the shield.
You may need a current limiting resistor. See your LED datasheet.

Nucleo_F401RE 和 Nucleo_L476RG
===============================
将 PWM2(PA0) 与 LED 连接。

Nucleo_F103RB
=============
将 PWM1(PA8) 与 LED 连接。

编译和运行
********************

本示例可以用于多个开发板，这里以 arduino_101 为例：

.. code-block:: console

   $ cd samples/basic/blink_led
   $ make BOARD=arduino_101
   $ make BOARD=arduino_101 flash

镜像被烧写到板子上后，开发板上的 LED 会按照概述中所讨论的那样开始闪烁。


