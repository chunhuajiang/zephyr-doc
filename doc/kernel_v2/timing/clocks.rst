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

例如：当尝试获取一个信号量时，指定一个超时延时100ms，即内核在这100ms结束之前将不会终止该操作并报告错误
For example, specifying a timeout delay of 100 ms when attempting to take
a semaphore means that the kernel will never terminate the operation
and report failure before at least 100 ms have elapsed. However,
it is possible that the operation may take longer than 100 ms to complete,
and may either complete successfully during the additional time
or fail at the end of the added time.

The amount of added time that occurs during a kernel object operation
depends on the following factors.

* The added time introduced by rounding up the specified time interval
  when converting from milliseconds to ticks. For example, if a tick duration
  of 10 ms is being used, a specified delay of 25 ms will be rounded up
  to 30 ms.

* The added time introduced by having to wait for the next tick interrupt
  before a delay can be properly tracked. For example, if a tick duration
  of 10 ms is being used, a specified delay of 20 ms requires the kernel
  to wait for 3 ticks to occur (rather than only 2), since the first tick
  can occur at any time from the next fraction of a millisecond to just
  slightly less than 10 ms; only after the first tick has occurred does
  the kernel know the next 2 ticks will take 20 ms.

Implementation
**************

Measuring Time with Normal Precision
====================================

This code uses the system clock to determine how much time has elapsed
between two points in time.

.. code-block:: c

    int64_t time_stamp;
    int64_t milliseconds_spent;

    /* capture initial time stamp */
    time_stamp = k_uptime_get();

    /* do work for some (extended) period of time */
    ...

    /* compute how long the work took (also updates the time stamp) */
    milliseconds_spent = k_uptime_delta(&time_stamp);

Measuring Time with High Precision
==================================

This code uses the hardware clock to determine how much time has elapsed
between two points in time.

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

Use services based on the system clock for time-based processing
that does not require high precision,
such as :ref:`timer objects <timers_v2>` or :ref:`thread_sleeping`.

Use services based on the hardware clock for time-based processing
that requires higher precision than the system clock can provide,
such as :ref:`busy_waiting` or fine-grained time measurements.

.. note::
    The high frequency of the hardware clock, combined with its 32-bit size,
    means that counter rollover must be taken into account when taking
    high-precision measurements over an extended period of time.

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
