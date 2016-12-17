.. _clocks_v2:

内核时钟
#############

内核时钟是所有时间相关服务的基础。

.. contents::
    :local:
    :depth: 2

概念
********

内核支持两种不同的时钟。

* 32位的 **硬时钟（hardware clock）** 是一个高精度的计数器，该计数器通过一种称为 **周期（cycles）** 的单位来度量时间。一个周期的长度取决于内核所使用的板卡硬件，其典型的时间长度为纳秒。

* 64位的 **系统时钟（system clock）** 是一个通过 **嘀嗒（ticks）** 来测量内核自初始化以来经历了多少时间的计数器，嘀嗒的时长是可配置的，其典型值为1~100毫秒。

内核同时提供了各种变量，可用于将时钟使用的时间单位转换为标准的时间单位（如秒，毫秒，纳秒等等），和可用于两种时钟的时间单位之间的转换。

系统时钟被内核中大部分时间相关的服务所使用，包括内核定时器对象和其它内核对象类型所支持的超时服务。为了方便使用，内核的API允许使用毫秒来定义时间长度，并自动将毫秒事件转换为对应的嘀嗒数。

硬件时钟可以用于更高精度的计时，精度高于基于系统时钟内核服务。


.. _clock_limitations:

时钟的局限性
=================

系统时钟的嘀嗒计数是从硬件时钟的周期数衍生出来的。由内核决定来多少个时钟周期等价于期望的嘀嗒频率，然后配置硬件在设定的周期后产生一个中断；每个中断对应一个嘀嗒。

.. note::
    配置一个较短的嘀嗒时间长度可以保证一个较小时间颗粒度，但同时增加也了大量的工作，让内核处理更高频率的嘀嗒中断。设置嘀嗒时间长度为0，则会关闭 *两个* 内核时钟及其相关的服务。
    
任何通过内核API指定的毫秒时间间隔会被视为可发生的 **最小** 延时，所以实际经历的时间可能比设置的要更长。

例如：当尝试获取一个信号量时，指定一个超时延时100ms，即内核在这100ms结束之前将不会终止该操作并报告错误。但是，该操作可能需要超过100ms的时间才能完成，并且可能在多出的时间里操作成功或失败。

在一个内核对象操作中，多出的额外时间的长度由如下因素决定：

* 在将毫秒转换为嘀嗒数时的舍入，将引入额外的时间。例如：如果使用了一个时长为10ms的嘀嗒，则25ms的延时将舍入为30ms。

* 因为在延时计时之前需要等待下一次的嘀嗒中断，所以这种情况将引入额外的事件。例如：如果采用了一个时长为10ms的嘀嗒，则设定20ms的延时需要内核等待3个嘀嗒发生（而不是2个），因为第一个嘀嗒可能在任何时刻，而计时点到嘀嗒中断很可能小于10ms；所以只有在第一个嘀嗒发生之后，内核可以通过后续的两个嘀嗒来确定延时了20ms。

实现
**************

标准精度的测量时间
====================================

这段代码采用系统时钟来确定两个时间点之间经历了多少时间。

.. code-block:: c

    int64_t time_stamp;
    int64_t milliseconds_spent;

    /* capture initial time stamp */
    time_stamp = k_uptime_get();

    /* do work for some (extended) period of time */
    ...

    /* compute how long the work took (also updates the time stamp) */
    milliseconds_spent = k_uptime_delta(&time_stamp);

高精度的时间测量
==================================

这段代码采用硬时钟来确定两个时间点之间经历了多少时间。

.. code-block:: c

    uint32_t start_time;
    uint32_t stop_time;
    uint32_t cycles_spent;
    uint32_t nanoseconds_spent;

    /* capture initial time stamp */
    start_time = k_cycle_get_32();

    /* do work for some (short) period of time */
    ...

    /* capture final time stamp */
    stop_time = k_cycle_get_32();

    /* compute how long the work took (assumes no counter rollover) */
    cycles_spent = stop_time - start_time;
    nanoseconds_spent = SYS_CLOCK_HW_CYCLES_TO_NS(cycles_spent);

建议的用法
**************

请使用基于系统时钟的服务来执行不需要高精度的时间相关处理，如 :ref:`timer objects <timers_v2>` or :ref:`thread_sleeping` 。

请使用基于硬时钟的服务来执行需要精度高于系统时钟的时间相关处理，如 :ref:`busy_waiting` ，或需要时间颗粒度更小的时间相关处理。

.. note::
    当硬时钟频率很高时，32位计数器更容易计数到最大值并从0开始。所以采用高精度的时间测量时，需要考虑这种超过一个时间周期的情况。
    
配置
*************

相关的配置选项：

* :option:`CONFIG_SYS_CLOCK_TICKS_PER_SEC`

APIs
****
:file:`kernel.h`文件提供了如下的内核时钟API:

* :cpp:func:`k_uptime_get()`
* :cpp:func:`k_uptime_get_32()`
* :cpp:func:`k_uptime_delta()`
* :cpp:func:`k_uptime_delta_32()`
* :cpp:func:`k_cycle_get_32()`
* :c:macro:`SYS_CLOCK_HW_CYCLES_TO_NS`
* :c:macro:`K_NO_WAIT`
* :c:macro:`K_MSEC`
* :c:macro:`K_SECONDS`
* :c:macro:`K_MINUTES`
* :c:macro:`K_HOURS`
* :c:macro:`K_FOREVER`
