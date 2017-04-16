.. _blink-led-sample:

PWM: LED 闪烁
##############

概述
********
本示例将会使用 PWM 让 LED 灯闪烁。

LED 将以 0.5Hz 的频率开始闪烁。每隔 4 秒，闪烁频率翻倍。当闪烁频率到达 500Hz 后，每隔 4 秒减半，直到到达 0.5Hz。这是一个完整的闪烁周期。然后，LED 将持续重复闪烁周期。

连线
******

Arduino 101 和 Quark D2000 CRB
===============================
You will need to connect the LED to ground and PWM0 via the shield.
你可能需要一个限流电阻，请参考数据手册中的 LED 部分。

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


