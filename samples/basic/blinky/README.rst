.. _blinky-sample:

Blinky
##################

概览
********

Blinky 示例演示了如何将 GPIO 配置为输出引脚，从而驱动 LED，它们通常在 Zephyr 支持的众多开发板中也被当成 “User LEDs”。

需求
************

此示例假设某个 LED 已经连上一个 GPIO 引脚。此示例代码的运行需要用户在 :file:`board.h` 中为开发板定义按钮以及 LED0_* 变量。

:file:`board.h` 必须定义以下变量：

- LED0_GPIO_PORT
- LED0_GPIO_PIN


编译并运行
********************

此示例不在控制台输出任何内容。可通过以下命令将其编译并烧写进开发板：

.. code-block:: console

   $ cd samples/basic/blinky
   $ make BOARD=arduino_101
   $ make BOARD=arduino_101 flash

将镜像烧写进开发板之后，开发板上的用户 LED 开始闪烁。
