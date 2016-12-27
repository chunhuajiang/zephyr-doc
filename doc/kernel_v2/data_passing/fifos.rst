.. _fifos_v2:

Fifo
#####

:dfn:`fifo` 是一个内核对象，它实现了传统的先进先出（first in first  out）队列，允许线程 和 ISR 添加、移除任意尺寸的数据项。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的 fifo。每个 fifo 通过其内存地址进行引用。

fifo 的关键属性包括：

* **队列**：它里面包含了已被添加但还未被移除的数据项。队列是使用一个简单的单链表实现的。

fifo 必须初始化加再使用。初始化时会将队列设为空。

fifo 的数据项必须在 4 字节边界上对齐，这是因为每个数据项的前 32 比特是内核保留的，它（被当做指针）用来指向队列中的下一个数据项。因此，如果应用程序需要 N 字节的数据项时，实际需要 N+4 字节的内存。

数据项可以被线程或者 ISR **添加** 到 fifo 中。如果有线程在等待从这个 fifo 中取数据，这个数据项则直接被给予这个线程；否则，该项会被直接添加到 fifo 的队列中去。对可入队的数据项的数量没有任何限制。

数据项可以被线程从 fifo 中 **移除**。如果该 fifo 的队列为空，线程在这个 fifo 上进行等待。多个线程可以同时在某个空 fifo 上等待，当一个新的数据项被添加时，它会被给予优先级最高的、等待时间最久的线程。

.. note::
    
    ISR 虽然也可以从 fifo 中移除数据，但是如果 fifo 为空，ISR 不能进行等待。

如果有需要，链接为单链表的 **多个数据项** 可以一次性添加到 fifo 中。当多个写者正在添加一系列相关的数据项（集合）到 fifo 中时，能体现处这种做法的好处，因为这能确保每个被添加到 fifo 中的同一个集合中的数据项不能被其它集合的数据项交错开。一个性添加多个数据项比每次添加一个数据项的效率更高，且能保证移除集合中第一个数据项的线程或者 ISR 不需要等待就能移除该集合中剩余的数据项。

实现
**************

定义 fifo
===============

使用类型为 :c:type:`struct k_fifo` 的变量可以定义一个 fifo。fifo 定义后必须使用函数 :cpp:func:`k_fifo_init()` 进行初始化。

下面的代码定义并初始化了一个空 fifo。

.. code-block:: c

    struct k_fifo my_fifo;

    k_fifo_init(&my_fifo);

也可以使用宏 :c:macro:`K_FIFO_DEFINE` 在编译时定义并初始化一个 fifo。

下面的代码与上面的代码段具有相同的效果。

.. code-block:: c

    K_FIFO_DEFINE(my_fifo);

向 fifo 中写
=================

函数 :cpp:func:`k_fifo_put()` 可用于向 fifo 中写数据。

下面的代码基于上面的例程之上，它使用 fifo 给一个或多个消费者线程发送数据。

.. code-block:: c

    struct data_item_t {
        void *fifo_reserved;   /* 1st word reserved for use by fifo */
        ...
    };

    struct data_item_t tx_data;

    void producer_thread(int unused1, int unused2, int unused3)
    {
        while (1) {
            /* create data item to send */
            tx_data = ...

            /* send data to consumers */
            k_fifo_put(&my_fifo, &tx_data);

            ...
        }
    }

函数 :cpp:func:`k_fifo_put_list()` 或者 :cpp:func:`k_fifo_put_slist()` 可用于将一个单链表数据项添加到 fifo 中。

从 fifo 中读
===================

函数 :cpp:func:`k_fifo_get()` 可用于从 fifo 中读取数据。

下面的代码基于上面的例程之上，它使用 fifo 从一个消费者线程获取数据项。

.. code-block:: c

    void consumer_thread(int unused1, int unused2, int unused3)
    {
        struct data_item_t  *rx_data;

        while (1) {
            rx_data = k_fifo_get(&my_fifo, K_FOREVER);

            /* process fifo data item */
            ...
        }
    }

建议的用法
**************

使用 fifo 以先进先出的方式异步传输任意大小的数据项。

配置选项
*********************

相关的配置选项：

* 无。

API
****

:file:`kernel.h` 中提供了如下关于 fifo 的 API：

* :c:macro:`K_FIFO_DEFINE`
* :cpp:func:`k_fifo_init()`
* :cpp:func:`k_fifo_put()`
* :cpp:func:`k_fifo_put_list()`
* :cpp:func:`k_fifo_put_slist()`
* :cpp:func:`k_fifo_get()`
