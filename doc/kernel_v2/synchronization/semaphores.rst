.. _semaphores_v2:

信号量
##########

:dfn:`信号量（semaphore）` 是一个内核对象，用于实现传统的计数信号量。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的信号量。每个信号量通过其内存地址进行引用。

信号量的关键属性如下：

* **计数**： 信号量可以被获取的次数。计数为零表示该信号量不可用。

* **界限**： 信号量的计数器能达到的最大值。

信号量必须先初始化再使用。信号量的计数必须被初始化为非负值，且小于等于其界限。

线程或 ISR 可以 **释放（give）** 一个信号量。释放信号量时其计数会递增（除非计数已等于上限）。

线程可以 **获取（take）** 信号量。获取信号量时其计数会递减（除非信号量无效，例如为零）。当信号量不可用时，线程可以等待，直到获取到信号量。多个线程可以同时等待某个不可用的信号量。当信号量可用时，它会被优先级最高的、等待时间最久的线程获取到。

.. note::

    内核也允许 ISR 去获取信号量，不过如果信号量不可用时，ISR 不能等待。

实现
**************

定义信号量
====================

使用类型为 :c:type:`struct k_sem` 的变量可以定义一个信号量。信号量定义后必须使用函数 :cpp:func:`k_sem_init()` 进行初始化。

下面的代码定义了一个信号量，并通过将其计数设为 0 、界限设为 1，从而形成了一个二元信号量。

.. code-block:: c

    struct k_sem my_sem;

    k_sem_init(&my_sem, 0, 1);

也可以使用宏 :c:macro:`K_SEM_DEFINE` 在编译时定义并初始化一个信号量。

下面的代码与上面的代码段具有系统的效果。

.. code-block:: c

    K_SEM_DEFINE(my_sem, 0, 1);

释放信号量
==================

函数 :cpp:func:`k_sem_give()` 用于释放信号量。

下面的代码基于上面的例程之上释放了一个信号量，表面有可供消费者线程处理的数据单元。

.. code-block:: c

    void input_data_interrupt_handler(void *arg)
    {
        /* notify thread that data is available */
        k_sem_give(&my_sem);

        ...
    }

获取信号量
==================

函数 :cpp:func:`k_sem_take()` 用于获取信号量。

下面的代码基于上面的例程之上，并等待 50 毫秒以等待信号量被释放。如果在该时间内没有获取到信号量，则打印一条警告消息。

.. code-block:: c

    void consumer_thread(void)
    {
        ...

        if (k_sem_take(&my_sem, K_MSEC(50)) != 0) {
            printk("Input data not available!");
        } else {
            /* fetch available data */
            ...
        }
        ...
    }

建议的用法
**************

使用信号量控制对多个线程共有的资源的访问。

使用信号量在线程或 ISR 的生产者和消费者之间同步。

配置选项
*********************

相关的配置选项：

* 无。

API
****


:file:`kernel.h` 中提供了如下关于信号量的 API：

* :c:macro:`K_SEM_DEFINE`
* :cpp:func:`k_sem_init()`
* :cpp:func:`k_sem_give()`
* :cpp:func:`k_sem_take()`
* :cpp:func:`k_sem_reset()`
* :cpp:func:`k_sem_count_get()`
