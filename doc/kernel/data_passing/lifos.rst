.. _lifos_v2:

Lifo
#####

:dfn:`lifo` 是一个内核对象，它实现了传统的后进先出（last in first  out）队列，允许线程 和 ISR 添加、移除任意尺寸的数据项。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的 lifo。每个 lifo 通过其内存地址进行引用。

lifo 的关键属性包括：

* **队列**：它里面包含了已被添加但还未被移除的数据项。队列是使用一个简单的单链表实现的。

lifo 必须先初始化再使用。初始化时会将队列设为空。

lifo 的数据项必须在 4 字节边界上对齐，这是因为每个数据项的前 32 比特是内核保留的，它（被当做指针）用来指向队列中的下一个数据项。因此，如果应用程序需要 N 字节的数据项时，实际需要 N+4 字节的内存。

数据项可以被线程或者 ISR **添加** 到 lifo 中。如果有线程在等待从这个 lifo 中取数据，这个数据项则直接被给予这个线程；否则，该项会被直接添加到 lifo 的队列中去。对可入队的数据项的数量没有任何限制。

数据项可以被线程从 lifo 中 **移除**。如果该 lifo 的队列为空，线程在这个 lifo 上进行等待。多个线程可以同时在某个空 lifo 上等待，当一个新的数据项被添加时，它会被给予优先级最高的、等待时间最久的线程。

.. note::
    
    ISR 虽然也可以从 lifo 中移除数据，但是如果 lifo 为空，ISR 不能进行等待。

实现
**************

定义 lifo
===============

使用类型为 :c:type:`struct k_lifo` 的变量可以定义一个 lifo。lifo 定义后必须使用函数 :cpp:func:`k_lifo_init()` 进行初始化。

下面的代码定义并初始化了一个空 lifo。

.. code-block:: c

    struct k_lifo my_lifo;

    k_lifo_init(&my_lifo);

也可以使用宏 :c:macro:`K_lifo_DEFINE` 在编译时定义并初始化一个 lifo。

下面的代码与上面的代码段具有相同的效果。

.. code-block:: c

    K_LIFO_DEFINE(my_lifo);

向 lifo 中写
=================

函数 :cpp:func:`k_lifo_put()` 可用于向 lifo 中写数据。

下面的代码基于上面的例程之上，它使用 lifo 给一个或多个消费者线程发送数据。

.. code-block:: c

    struct data_item_t {
        void *lifo_reserved;   /* 1st word reserved for use by lifo */
        ...
    };

    struct data_item_t tx data;

    void producer_thread(int unused1, int unused2, int unused3)
    {
        while (1) {
            /* create data item to send */
            tx_data = ...

            /* send data to consumers */
            k_lifo_put(&my_lifo, &tx_data);

            ...
        }
    }

从 lifo 中读
===================


函数 :cpp:func:`k_lifo_get()` 可用于从 lifo 中读取数据。

下面的代码基于上面的例程之上，它使用 lifo 从一个消费者线程获取数据项。


.. code-block:: c

    void consumer_thread(int unused1, int unused2, int unused3)
    {
        struct data_item_t  *rx_data;

        while (1) {
            rx_data = k_lifo_get(&my_lifo, K_FOREVER);

            /* process lifo data item */
            ...
        }
    }

建议的用法
**************


使用 lifo 以后进先出的方式异步传输任意大小的数据项。

配置选项
*********************

相关的配置选项：

* 无。

API
****

头文件 :file:`kernel.h` 中提供了如下的 lifo API：

* :c:macro:`K_LIFO_DEFINE`
* :cpp:func:`k_lifo_init()`
* :cpp:func:`k_lifo_put()`
* :cpp:func:`k_lifo_get()`
