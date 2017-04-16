.. _fade-led-sample:

PWM: LED 亮度渐变
###################

概述
********

此示例使用 PWM 控制 LED 亮度渐变。

LED 将从全黑开始，并在 10 秒内逐渐增加其亮度。然后在 10 秒内逐渐减少亮度，最终 LED 再次全黑。LED 将持续重复这个周期。

接线
******

Arduino 101 和 Quark D2000 CRB
===============================

需要将 LED 接地，并通过扩展板接至 PWM0。 你可能需要一个限流电阻，请参考数据手册中的 LED 部分。

Nucleo_F401RE 和 Nucleo_L476RG
===============================

将 PWM2(PA0) 连接至 LED。

Nucleo_F103RB
=============

将 PWM1(PA8) 连接至 LED。

编译和运行
********************

本示例可以用于多个开发板，这里以 arduino_101 为例：

.. code-block:: console

   $ cd samples/basic/fade_led
   $ make BOARD=arduino_101
   $ make BOARD=arduino_101 flash
