.. _nucleo_f401re_board:

ST Nucleo F401RE
################

概览
********

Nucleo F401RE是一块基于STM32F401RE MCU的ARM Cortex-M4开发板，具有广泛的连接支持和配置。以下是Nucleo F401RE开发板的亮点：:


- QFP64包内的STM32微控制器
- 两种扩展资源类型:
       - Arduino Uno V3连通性
       - 可完全访问STM32 I/O的ST morpho扩展引脚接口
- 带SWD连接器的板载ST-LINK/V2-1 调试/编程
- 灵活的主板电源供应:
       - USB VBUS或外部电源(3.3V, 5V, 7 - 12V)
       - 电源管理接入点
- 三个LED: USB通信 (LD1), 用户LED (LD2), 电源LED(LD3)
- 两个按钮: 用户和重启

.. image:: img/nucleo64_perf_logo_1024.png
     :width: 720px
     :align: center
     :height: 720px
     :alt: Nucleo F401RE

关于开发板的更多信息请查阅 `Nucleo F401RE website`_。

硬件
********

Nucleo F401RE提供以下硬件:

- LQFP64包内STM32F411RET6
- 内置FPU的ARM® 32-bit Cortex®-M4 CPU
- 84 MHz 的最高CPU频率
- 1.7 V 至 3.6 V VDD
- 512 KB Flash
- 96 KB SRAM
- 具有外部中断功能的GPIO
- 16通道12-bit ADC with 16 channels
- RTC
- 高级控制定时器
- 通用目的定时器 (7)
- 看门狗定时器 (2)
- USART/UART (3)
- I2C (3)
- SPI (4)
- SDIO
- USB 2.0 OTG FS
- DMA 控制器

更多有关 STM32F401RE 的信息请参阅:
       - `STM32F401RE on www.st.com`_
       - `STM32F401 reference manual`_

支持的功能
==================

Zephyr的nucleo_401re主板配置支持以下硬件功能:

+-----------+------------+-------------------------------------+
| 接口      | 控制器      | 驱动/元件                          |
+===========+============+=====================================+
| NVIC      | on-chip    | 嵌套向量中断控制器                  |
+-----------+------------+-------------------------------------+
| UART      | on-chip    | 串行端口轮询;                       |
|           |            | 串行端口中断                        |
+-----------+------------+-------------------------------------+
| PINMUX    | on-chip    | 引脚复用                            |
+-----------+------------+-------------------------------------+
| GPIO      | on-chip    | gpio                                |
+-----------+------------+-------------------------------------+
| PWM       | on-chip    | pwm                                 |
+-----------+------------+-------------------------------------+

本Zephyr端口还不支持其它硬件。

默认配置可在defconfig文件中找到:

	``boards/arm/nucleo_f401re/nucleo_f401re_defconfig``


引脚映射
===========

Nucleo F401RE开发板有6路GPIO控制器。这些控制器负责引脚利用、输入/输出、上拉等等。

可用引脚:
---------------
.. image:: img/nucleo_f401re_arduino.png
     :width: 720px
     :align: center
     :height: 540px
     :alt: Nucleo F401RE Arduino connectors
.. image:: img/nucleo_f401re_morpho.png
     :width: 720px
     :align: center
     :height: 540px
     :alt: Nucleo F401RE Morpho connectors

更多信息请参考 `STM32 Nucleo-64 board User Manual`_。

默认Zephyr外设映射:
----------------------------------
- UART_1_TX : PB6
- UART_1_RX : PB7
- UART_2_TX : PA2
- UART_2_RX : PA3
- PWM_2_CH1 : PA0
- USER_PB : PC13
- LD2 : PA5

系统时钟
============

Nucleo F401RE 系统时钟可由内部或外部晶振及主PLL时钟驱动。默认情况下，系统时钟由84MHz PLL时钟驱动，通过8MHz高速内部振荡器驱动。

串口
===========

Nucleo F401RE 开发板拥有3个UART。Zephyr控制台输出分配给UART2。默认设置为115200 8N1。


编程与调试
*************************

烧写
========

Nucleo F401RE 开发板包括一个ST-LINK/V2-1 嵌入式调试工具接口。此接口被Zephyr SDK中的openocd所支持。

在Nucleo F401RE中烧写应用程序
----------------------------------------

本说明使用示例应用程序 :ref:`hello_world` :

.. code-block:: console

   $<zephyr_root_path>/samples/hello_world

编译Zephyr内核及应用程序，输入:

.. code-block:: console

   $ cd <zephyr_root_path>
   $ source zephyr-env.sh
   $ cd $ZEPHYR_BASE/samples/hello_world/
   $ make BOARD=nucleo_f401re

使用USB端口将 Nucleo F401RE 连接至你的计算机主机，然后输入如下命令：

.. code-block:: console

   $ make BOARD=nucleo_f401re flash

在主机上运行串口程序并连接至Nucleo board。

.. code-block:: console

   $ minicom -D /dev/ttyACM0

你将看到以下信息:

.. code-block:: console

   Hello World! arm


调试
=========

使用以下make命令访问gdb:

.. code-block:: console

   $ make BOARD=nucleo_f411re debug


.. _Nucleo F401RE website:
   http://www.st.com/en/evaluation-tools/nucleo-f401re.html

.. _STM32 Nucleo-64 board User Manual:
   http://www.st.com/resource/en/user_manual/dm00105823.pdf

.. _STM32F401RE on www.st.com:
   http://www.st.com/en/microcontrollers/stm32f401re.html

.. _STM32F401 reference manual:
   http://www.st.com/resource/en/reference_manual/dm00096844.pdf
