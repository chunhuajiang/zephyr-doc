.. _nucleo_l476rg_board:

ST Nucleo L476RG
################

概览
********

Nucleo L476RG是一块基于STM32L476RG MCU的ARM Cortex-M4开发板，具有广泛的连接支持和配置。以下是Nucleo L476RG开发板的亮点：

- QFP64包内的STM32微控制器
- 两种扩展资源类型:
       - Arduino Uno V3连通性
       - 可完全访问STM32 I/O的ST morpho扩展引脚接口
- 带SWD连接器的板载ST-LINK/V2-1 调试/编程
- 灵活的主板电源供应：
       - USB VBUS或外部电源(3.3V, 5V, 7 - 12V)
       - 电源管理接入点
- 三个LED: USB通信 (LD1), 用户LED (LD2), 电源LED(LD3)
- 两个按钮: 用户和重启

.. image:: img/nucleo64_ulp_logo_1024.jpg
     :width: 250px
     :align: center
     :height: 250px
     :alt: Nucleo L476RG

关于开发板的更多信息请查阅 `Nucleo L476RG website`_。

硬件
********

STM32L476RG SoC提供以下硬件IPs:

- FlexPowerControl下的超低功耗 (降至标准模式的130 nA和运行模式下的100 μA/MHz)
- 内核: 内置FPU的ARM® 32-bit Cortex®-M4 CPU，频率达到80 MHz, 100DMIPS/1.25DMIPS/MHz (Dhrystone 2.1)
- 时钟源:
        - 4 to 48 MHz 晶振
        - 32 kHz RTC (LSE)晶振
        - 内部16 MHz工厂校准RC (±1%)
        - 内部低功耗32 kHz RC (±5%)
        - 内部多速100 kHz至48 MHz振荡器, 自动LSE校准 (超过±0.25 % 精确率)
        - 用于系统时钟, USB, audio, ADC的3个PLL
- 带HW日历, 报警及校准的RTC
- 带升压转换器的8 × 40或4 × 44 LCD
- 高达24个电容传感通道：支持touchkey，线性和旋转触摸传感器
- 16x 定时器:
        - 2x 16-bit 高级电机控制
        - 2x 32-bit 和 5x 16-bit 通用目的
        - 2x 16-bit  基础
        - 2x 低功耗 16-bit 定时器 (停止模式下可用)
        - 2x 看门狗
        - SysTick 定时器
- 高达144个快速 I/Os, 最高5V耐压，多达14个I/O口可独立供电降至1.08 V
- 内存
        - 多达1 MB Flash，2路并发读写，专有代码读出保护
        - 多达128 KB SRAM，包括32 KB带硬件奇偶校验
        - 支持SRAM、PSRAM、NOR和NAND的静态存储器的外部存储器接口
        - Quad SPI内存接口
- 适用于sigma delta调制器的4x数字滤波器
- 丰富的模拟外设（独立电源）
        - 3× 12-bit ADC 5 MSPS, 多达16-bit硬件采样, 200 μA/MSPS
        - 2x 12-bit DAC, 低功耗采样和保持
        - 2x 内置PGA运算放大器
        - 2x 超低功耗比较器
- 18x 通信接口
        - 全速USB OTG 2.0, LPM 和 BCD
        - 2x SAIs (serial audio interface串行音频接口)
        - 3x I2C FM+(1 Mbit/s), SMBus/PMBus
        - 6x USARTs (ISO 7816, LIN, IrDA, modem)
        - 3x SPIs (4x SPIs with the Quad SPI)
        - CAN (2.0B Active) 和 SDMMC 接口
        - SWPMI single wire protocol master I/F
- 14-通道 DMA 控制器
- 真随机数发生器
- CRC计算单元，96-bit唯一ID
- 开发支持: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™


更多有关STM32L476RG的信息请参阅:
       - `STM32L476RG on www.st.com`_
       - `STM32L476 reference manual`_

支持功能
==================

Zephyr的nucleo_l476rg主板配置支持以下功能:

+-----------+------------+-------------------------------------+
| 接口 | 控制器 | 驱动/元件                    |
+===========+============+=====================================+
| NVIC      | on-chip    | 嵌套向量中断控制器  |
+-----------+------------+-------------------------------------+
| UART      | on-chip    | 串行端口轮询;                |
|           |            | 串行端口中断               |
+-----------+------------+-------------------------------------+
| PINMUX    | on-chip    | 引脚复用                              |
+-----------+------------+-------------------------------------+
| GPIO      | on-chip    | gpio                                |
+-----------+------------+-------------------------------------+
| I2C       | on-chip    | i2c                                 |
+-----------+------------+-------------------------------------+
| PWM       | on-chip    | pwm                                 |
+-----------+------------+-------------------------------------+

本Zephyr端口还不支持其它硬件

默认配置可在defconfig文件中找到:

	``boards/arm/nucleo_l476rg/nucleo_l476rg_defconfig``


连接和IO
===================

Nucleo L476RG开发板有8路GPIO控制器。这些控制器负责引脚利用、输入/输出、上拉等等。

可用引脚:
---------------
.. image:: img/nucleo_l476rg_arduino.png
     :width: 720px
     :align: center
     :height: 540px
     :alt: Nucleo L476RG Arduino connectors
.. image:: img/nucleo_l476rg_morpho.png
     :width: 720px
     :align: center
     :height: 540px
     :alt: Nucleo L476RG Morpho connectors

更多信息请参考 `STM32 Nucleo-64 board User Manual`_。

默认Zephyr外设映射：
----------------------------------

- UART_1_TX : PA9
- UART_1_RX : PA10
- UART_2_TX : PA2
- UART_2_RX : PA3
- UART_3_TX : PB10
- UART_3_RX : PB11
- I2C_0_SCL : PB6
- I2C_0_SDA : PB7
- PWM_2_CH1 : PA0
- USER_PB : PC13
- LD2 : PA5

系统时钟
------------

Nucleo L476RG系统时钟可由内部或外部晶振及主PLL时钟驱动。默认情况下，系统时钟由80MHz PLL时钟驱动，通过16MHz高速内部振荡器驱动。

串口
-----------

Nucleo L476RG开发板拥有6 U(S)ARTs。Zephyr控制台输出分配给UART2。默认设置为115200 8N1。

编程与调试
*************************

烧写
========

Nucleo L476RG开发板包括一个ST-LINK/V2-1 嵌入式调试工具接口。此接口不被Zephyr SDK 0.9的openocd 0.9版本支持，直到我们更新Zephyr SDK。使用来自GitHub上的openocd-stm32项目的openocd v0.10.0可以获取烧写及调试STM32开发板所需的最小脚本集。

.. code-block:: console

   $ git clone  https://github.com/erwango/openocd-stm32.git

以下说明来自README.md


在Nucleo L476RG中烧写应用程序
----------------------------------------

本说明使用示例应用程序 :ref:'hello_world` :

编译Zephyr内核及应用程序，输入:

.. code-block:: console

   $ cd <zephyr_root_path>
   $ source zephyr-env.sh
   $ cd $ZEPHYR_BASE/samples/hello_world/
   $ make BOARD=nucleo_l476rg

使用USB端口将Nucleo L476RG连接至你的计算机主机，然后输入如下命令：

.. code-block:: console

   $ cd <openocd-stm32_path>
   $ stm32_flsh l4 $ZEPHYR_BASE/samples/hello_world/outdir/nucleo_l476rg/zephyr.bin

在主机上运行串口程序并连接至Nucleo board。

.. code-block:: console

   $ minicom -D /dev/ttyACM0

你将看到以下信息:

.. code-block:: console

   $ Hello World! arm


调试
=========

使用以下make命令访问gdb:

.. code-block:: console

   $ cd <openocd-stm32_path>
   $ stm32_dbg l4 $ZEPHYR_BASE/samples/hello_world/outdir/nucleo_l476rg/zephyr.elf

.. _Nucleo L476RG website:
   http://www.st.com/en/evaluation-tools/nucleo-l476rg.html

.. _STM32 Nucleo-64 board User Manual:
   http://www.st.com/resource/en/user_manual/dm00105823.pdf

.. _STM32L476RG on www.st.com:
   http://www.st.com/en/microcontrollers/stm32l476rg.html

.. _STM32L476 reference manual:
   http://www.st.com/resource/en/reference_manual/DM00083560.pdf
