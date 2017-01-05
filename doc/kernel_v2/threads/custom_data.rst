.. _custom_data_v2:

自定义数据
###########

线程的 :dfn:`自定义数据（custom data）` 是由应用程序使用的 32 比特的线程相关的值，它可以用于任何目的。

.. contents::
    :local:
    :depth: 2

概念
********

每个线程都有一个 32 比特的自定义数据区域。只有线程自己能访问它的自定义数据。应用程序可以利用自定义数据实现任何目的。线程自定义数据的默认值是 0。

.. note::
   在 ISR 中没有自定义数据，因为 ISR 是一个单一的共享内核的中断处理上下文。

实现
**************

使用自定义数据
=================

默认情况下，线程自定义数据的功能是关闭的。配置选项 :option:`CONFIG_THREAD_CUSTOM_DATA` 用于使能自定义数据。

函数 :cpp:func:`k_thread_custom_data_set()` 和 :cpp:func:`k_thread_custom_data_get()` 分别用于写、读线程的自定义数据。线程只能访问它自己的自定义数据，不能访问其它线程的自定义数据。

下面的代码利用了自定义数据来记录各个线程访问某个例程的次数。

.. note::
    当然，只有一个例程能利用这种技巧，因为它独占了自定义数据。

.. code-block:: c

    int call_tracking_routine(void)
    {
        uint32_t call_count;

        if (k_is_in_isr()) {
	    /* 忽略所有的 ISR 调用 */
        } else {
            call_count = (uint32_t)k_thread_custom_data_get();
            call_count++;
            k_thread_custom_data_set((void *)call_count);
	}

        /* 其它操作... */
        ...
    }

建议的用法
**************

要使用线程自定义数据时，最好将自定义数据作为一个指向线程的某个数据结构的指针。

配置选项
*********************

相关的配置选项：

* :option:`CONFIG_THREAD_CUSTOM_DATA`

API
****

:file:`kernel.h` 中提供了如下关于线程自定义数据的 API：

* :cpp:func:`k_thread_custom_data_set()`
* :cpp:func:`k_thread_custom_data_get()`
