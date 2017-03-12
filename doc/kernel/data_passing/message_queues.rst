.. _message_queues_v2:

消息队列
##############

:dfn:`消息队列（message queue）` 是一个内核对象，它实现了一个简单的消息队列，允许线程和 ISR 异步地发送和接收大小固定的数据项。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的消息队列。消息队列通过其内存地址进行引用。

消息队列的关键属性包括：

* **环形 buffer**：它包含已经发送但还未接收的数据项。

* **数据项尺寸**：以字节为单位。

* **最大数量**：环形 buffer 中可排队的数据项的最大数量。

消息队列的环形 buffer 必须对齐到 N 字节边界，其中 N 是 2 的整数次幂（即1,2,4,8，...）。为确保存放到环形 buffer 中的消息都对齐到这个边界，数据项的尺寸必须是 N 的整数倍。

消息队列必须先初始化再使用。初始化时会将环形 buffer 设为空。

数据项可以被线程或 ISR **发送** 到消息队列中。如果有线程在这个消息队列上等待，数据项会直接被拷贝给等待线程；否则，数据项会被拷贝到消息队列的环形 buffe 中（如果 buffer 还有剩余空间）。在这两种情况下，被发送的数据项的尺寸 *必须* 等于消息队列的数据项的尺寸。

如果线程发送数据项时环形 buffer 已满，它可以选择等待。当环形 buffer 已满时，多个发送线程可以同时等待；当 buffe 空间可用时，它会被分配给优先级最高的、等待时间最久的线程。


线程可以从消息队列中 **接收** 数据项。数据项会被拷贝至接收线程所指定的区域；接收区域的尺寸 **必须** 等于消息队列的数据项的尺寸。

如果接收线程接收数据时环形 buffer 为空，它可以选择等待。当环形 buffer 为空时，多个接收线程可以同时等待；当数据项可用时，它会被分配给优先级最高的、等待时间最久的线程。

.. note::

    ISR 虽然也可以从消息队列中接收数据项，但是如果消息队列为空，ISR 不能进行等待。

实现
**************

定义消息队列
========================

使用类型为 :c:type:`struct k_msgq` 的变量可以定义消息队列。消息队列定义后必须使用函数 :cpp:func:`k_msgq_init()` 对其进行初始化。

下面的代码定义并初始化了一个空的消息队列，这个消息队列能容纳 10 个数据项，每个数据项的长度是 12 字节。

.. code-block:: c

    struct data_item_type {
        uint32_t field1;
	uint32_t field2;
	uint32_t field3;
    };

    char __aligned(4) my_msgq_buffer[10 * sizeof(data_item_type)];
    struct k_msgq my_msgq;

    k_msgq_init(&my_msgq, my_msgq_buffer, sizeof(data_item_type), 10);

也可以使用宏 :c:macro:`K_MSGQ_DEFINE` 在编译时定义并初始化一个消息队列。

下面的代码与上面的代码段具有相同的效果。注意，该宏既定义了消息队列，也定义了 buffer。

.. code-block:: c

    K_MSGQ_DEFINE(my_msgq, sizeof(data_item_type), 10, 4);

向消息队列中写
==========================

函数 :cpp:func:`k_msgq_put()` 可用于将数据项添加到消息队列中。

下面的代码基于上面的例程之上，它使用消息队列将数据项从一个生产者线程传递给一个或多个消费者线程。如果由于消费者线程不能消耗而导致消息队列被填满，生产者线程会丢弃所有已存在的数据，以存储更新的数据。

.. code-block:: c

    void producer_thread(void)
    {
        struct data_item_t data;

        while (1) {
            /* create data item to send (e.g. measurement, timestamp, ...) */
            data = ...

            /* send data to consumers */
            while (k_msgq_put(&my_msgq, &data, K_NO_WAIT) != 0) {
                /* message queue is full: purge old data & try again */
                k_msgq_purge(&my_msgq);
            }

            /* data item was successfully added to message queue */
        }
    }

从消息队列中读
============================

函数 :cpp:func:`k_msgq_get()` 可用于从消息队列中获取一个数据项。

下面的代码基于上面的例程之上，它使用消息队列来处理由一个或者多个消费者线程产生的数据项。

.. code-block:: c

    void consumer_thread(void)
    {
        struct data_item_t data;

        while (1) {
            /* get a data item */
            k_msgq_get(&my_msgq, &data, K_FOREVER);

            /* process data item */
            ...
        }
    }

建议的用法
**************

使用消息队列以异步的方式在线程间传递小的数据项。

.. note::
    
    如果有需要，消息队列也可用于传输大的数据项。不过，这将增加中断的延迟，因为向消息队列中写数据时会锁中断。传递大数据项的更优雅的做法是使用指向数据项的指针，而不是数据项本身。对这种情况，内核的内存映射和内存池对象更合适。

    使用内核的邮箱对象类型可以实现同步传递。

配置选项
*********************

相关的配置选项：

* 无。

API
****

头文件 :file:`kernel.h` 提供了如下的消息队列 API：

* :c:macro:`K_MSGQ_DEFINE`
* :cpp:func:`k_msgq_init()`
* :cpp:func:`k_msgq_put()`
* :cpp:func:`k_msgq_get()`
* :cpp:func:`k_msgq_purge()`
* :cpp:func:`k_msgq_num_used_get()`
* :cpp:func:`k_msgq_num_free_get()`
