.. _rgb-led-sample:

PWM: RGB LED
############

概览
********

这是一个简单的示例，它使用 PWM 驱动一个 RGB LED。

在一个 RGB LED 中有三个单色 LED。每个单色 LED 都需要一个 PWM 端口驱动。每个 PWM 端口的脉宽都将从 0 变至特定周期。从而使得每个 LED 的亮度在 11 步内从全黑渐变为最亮。三个 “for” 循环（每个 LED 一个 for）将产生 1331 种组合，也就是 1331 种不同的颜色。整个过程将持续重复。

接线
******

Arduino 101
===========

在 arduino 101 中你需要通过扩展板将 LED 接至 PWM0、PWM1、PWM2，这依赖于你所使用的是哪种类型的 RGB LED。请将共阴极接地或共阳极接 Vcc，还需要为每个单色 LED 接限流电阻。

此示例需要三个 PWM 端口，所以不能工作于 Quark D2000 平台。

编译和运行
********************

此示例不在控制台输出任何东西，可使用以下语句编译并烧写至开发板。

.. code-block:: console

   $ cd samples/basic/rgb_led
   $ make BOARD=arduino_101
   $ make BOARD=arduino_101 flash
