.. _button-sample:

Button 示例
###########

概览
********

一个简单的按钮示例，展示了 GPIO 输入中断的使用。

需求
************

此示例假定按钮连接至一个GPIO引脚。示例代码的运行需要用户定义了按钮，并在 board.h 文件中定义了 SW0_* 变量。

使用此示例，你需要在开发板的头文件中定义用户开关。:file:`board.h` 中必须定义以下变量:

- SW0_GPIO_NAME
- SW0_GPIO_PIN

以下开发板已经定义了上述变量:

- bbc_microbit
- cc3200_launchxl
- frdm_k64f
- nrf51_pca10028
- nrf52840_pca10056
- nrf52_pca10040
- nucleo_f103rb
- :ref:`quark_d2000_devboard`
- quark_se_c1000_devboard
- quark_se_c1000_ss_devboard


编译和运行
********************

此示例可为多块开发板编译，此处以 nucleo_f103rb 为例:

.. code-block:: console

   $ cd samples/basic/button
   $ make BOARD=nucleo_f103rb


启动之后，程序寻找一个预定义 GPIO 设备，并将引脚配置为输入模式，使用下降沿中断触发模式。在主循环的每个迭代期间，监视 GPIO 引脚状态并打印至串口控制台。当输入按钮按下，中断处理函数将打印一个携带时间戳事件信息。
