.. _kernel_event_logger_v2:

内核事件日志器
###################

内核事件日志器记录了指定类型的内核事件的发生情况，这样的好处是可以在随后抽取并检查这些事件。这种功能有助于概括应用程序的所有操作，既可以用于调试目的，又可以用于优化应用程序的性能。

.. contents::
    :local:
    :depth: 2

概念
********

内核事件日志器的功能是可配置的，默认未开启。在默认情况下，它包括一个最多可以容纳 128 个 32 比特字的环形缓冲。每一个 32 比特字可以代表一个事件信息。

内核事件日志器具有记录如下事件类型的能力：

* 中断。
* 线程的上下文切换。
* 内核睡眠事件（进入、退出低功耗状态）。

内核事件日志器只能记录所配置的预定义事件类型。每种事件类型可以被单独使能。

应用程序也可以定义并记录自定义的事件类型。应用程序必须实现用于记录自定义事件的信息和被记录的事件。

内核事件日志器记录的所有事件都驻留在日志器的环形缓冲中，直到被应用程序恢复出来检查和分析。应用程序必须实现恢复和分析逻辑。

.. important::
    
    应用程序必须及时地抽恢复并分析内核所记录的事件，否则当事件日志器的环形缓冲满时会丢弃新事件。推荐的做法是使用一个协作式线程周期性地恢复事件。
    
默认情况下，内核事件日志器会记录被使能的所有事件类型的发生情况。不过这要是可配置的，可以让应用程序在任何时间开始或者结束记录事件，以及控制记录哪些事件。这样能够让应用程序只在感兴趣的时间段内采集感兴趣的事件，减小了分析事件的工作量。

.. note::

    内核事件日志器也可被指示去忽略调用某个指定线程的上下文切换，这样可以避免记录从内核事件日志器恢复事件的线程的上下文切换。

事件的格式
=============

内核事件日志器记录的每个事件都由一到多个用于描述事件的 32 比特字的数据组成。


**中断事件** 具有如下格式：

.. code-block:: c

    struct {
        uint32_t timestamp;        /* time of interrupt */
        uint32_t interrupt_id;     /* ID of interrupt */
    };

**上下文切换事件** 具有如下格式：

.. code-block:: c

    struct {
        uint32_t timestamp;        /* time of context switch */
        uint32_t context_id;       /* ID of thread that was switched out */
    };

**睡眠事件** 具有如下格式：

.. code-block:: c

    struct {
        uint32_t sleep_timestamp;  /* time when CPU entered sleep mode */
        uint32_t wake_timestamp;   /* time when CPU exited sleep mode */
        uint32_t interrupt_id;     /* ID of interrupt that woke CPU */
    };

**自定义事件** 必须具有一个与已存在的预定义事件的类型 ID 不冲突的类型 ID。自定义事件的格式由应用程序定义，但是它必须至少包含一个 32 比特数据字。自定义事件可以利用可变尺寸来让单一类型的不同事件记录消息的不同数量。

时间戳
==========

默认情况下，每个预定义事件的时间戳由内核的 :ref:`hardware clock <clocks_v2>` 中获取。这个 32 比特的始终计数非常快，也就是说时间戳的值会快速地溢出。（例如， Quark SE 的 Lakemont APIC 定时器每隔 134 秒就会溢出一次。）当分析内核事件日志器的时候必须将这个溢出考虑在内。此外，在无滴答空转被使能时也需要当心，在这种情况下，一个睡眠时期超过了 2^32 个时钟周期。

如果有需要，可以通过配置让内核事件日志器使用自定义的时间戳，而不使用默认时间戳。应用程序通过调用函数 :cpp:func:`sys_k_event_logger_set_timer()` 在运行时产生自定义的 32 比特的时间戳。

实现
**************

恢复事件
===================

可以使用下列 API 以阻塞方式或者非阻塞方式从内核事件日志器中恢复事件：

* :cpp:func:`sys_k_event_logger_get()`
* :cpp:func:`sys_k_event_logger_get_wait()`
* :cpp:func:`sys_k_event_logger_get_wait_timeout()`

在每种情形下，API 都会返回事件的类型和尺寸，以及事件信息本身。API 也可以指示在先前的事件也被恢复的事件之间有多少个事件被丢弃了。

下面的代码演示了线程时如何恢复内核事件日志器所记录的事件的。例程 :file:`samples/kernel_event_logger` 也演示了如何收集内核事件数据。

.. code-block:: c

    uint16_t event_id;
    uint8_t  dropped_count;
    uint32_t data[3];
    uint8_t  data_size;

    while(1) {
        /* retrieve an event */
        data_size = SIZE32_OF(data);
        res = sys_k_event_logger_get_wait(&event_id, &dropped_count, data,
                                          &data_size);

        if (dropped_count > 0) {
            /* ... Process the dropped events count ... */
        }

        if (res > 0) {
            /* process the event */
            switch (event_id) {
            case KERNEL_EVENT_CONTEXT_SWITCH_EVENT_ID:
                /* ... Process the context switch event ... */
                break;
            case KERNEL_EVENT_INTERRUPT_EVENT_ID:
                /* ... Process the interrupt event ... */
                break;
            case KERNEL_EVENT_SLEEP_EVENT_ID:
                /* ... Process the sleep event ... */
                break;
            default:
                printf("unrecognized event id %d\n", event_id);
            }
        } else if (res == -EMSGSIZE) {
            /* ... Data array is too small to hold the event! ... */
        }
    }

添加自定义事件类型
==========================

A custom event type must use an integer type ID that does not duplicate
an existing type ID. The type IDs for the pre-defined events can be found
in :file:`include/misc/kernel_event_logger.h`. If dynamic recording of
events is enabled, the event type ID must not exceed 32.

Custom events can be written to the kernel event logger using the following
APIs:

* :cpp:func:`sys_k_event_logger_put()`
* :cpp:func:`sys_k_event_logger_put_timed()`

Both of these APIs record an event as long as there is room in the kernel
event logger's ring buffer. To enable dynamic recording of a custom event type,
the application must first call :cpp:func:`sys_k_must_log_event()` to determine
if event recording is currently active for that event type.

The following code illustrates how an application can write a custom
event consisting of two 32-bit words to the kernel event logger.

.. code-block:: c

    #define MY_CUSTOM_EVENT_ID 8

    /* record custom event only if recording is currently wanted */
    if (sys_k_must_log_event(MY_CUSTOM_EVENT_ID)) {
        uint32_t data[2];

        data[0] = custom_data_1;
        data[1] = custom_data_2;

        sys_k_event_logger_put(MY_CUSTOM_EVENT_ID, data, ARRAY_SIZE(data));
    }

The following code illustrates how an application can write a custom event
that records just a timestamp using a single 32-bit word.

.. code-block:: c

    #define MY_CUSTOM_TIME_ONLY_EVENT_ID 9

    if (sys_k_must_log_event(MY_CUSTOM_TIME_ONLY_EVENT_ID)) {
        sys_k_event_logger_put_timed(MY_CUSTOM_TIME_ONLY_EVENT_ID);
    }

配置选项
*********************

相关的配置选项：

* :option:`CONFIG_KERNEL_EVENT_LOGGER`
* :option:`CONFIG_KERNEL_EVENT_LOGGER_CONTEXT_SWITCH`
* :option:`CONFIG_KERNEL_EVENT_LOGGER_INTERRUPT`
* :option:`CONFIG_KERNEL_EVENT_LOGGER_SLEEP`
* :option:`CONFIG_KERNEL_EVENT_LOGGER_BUFFER_SIZE`
* :option:`CONFIG_KERNEL_EVENT_LOGGER_DYNAMIC`
* :option:`CONFIG_KERNEL_EVENT_LOGGER_CUSTOM_TIMESTAMP`

API
****

:file:`kernel_event_logger.h` 中提供了如下与内核事件日志器相关的 API：

* :cpp:func:`sys_k_event_logger_register_as_collector()`
* :cpp:func:`sys_k_event_logger_get()`
* :cpp:func:`sys_k_event_logger_get_wait()`
* :cpp:func:`sys_k_event_logger_get_wait_timeout()`
* :cpp:func:`sys_k_must_log_event()`
* :cpp:func:`sys_k_event_logger_put()`
* :cpp:func:`sys_k_event_logger_put_timed()`
* :cpp:func:`sys_k_event_logger_get_mask()`
* :cpp:func:`sys_k_event_logger_set_mask()`
* :cpp:func:`sys_k_event_logger_set_timer()`
