.. _ring_buffers_v2:

环形缓冲
############

:dfn:`环形缓冲（ring buffer）` 是一个以 32 比特字为单位的、以先进先出的顺序进行存储的环形缓冲。从环形缓冲中入队/出队的单个数据项的最多能达到 1020 字节。每个数据项有两个相关联的元数据值：类型标识符和 16 比特的整数值，二者都由应用程序指定。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的环形缓冲。每个环形缓冲通过其地址进行引用。

环形缓冲的关键属性包括：

* **数据缓冲区**： 以 32 比特字为单位。它包含已被添加到环形缓冲区但还未被移除的数据项。

* **数据缓冲区的大小**：以 32 比特字为单位。它表示环形缓冲所能容纳的最大数据（包括元数据值）数量。

环形缓冲必须先初始化再使用。初始化时会将其数据缓冲设为空。


环形缓冲的 **数据项** 是一个以 32 比特字为单位的数组，该数组范围是 0 到 1020 字节。当数据项 **入队** 时，它的内容以及所关联的元数据值（需要额外的 32 比特字空间）会被拷贝到数据缓冲中。如果环形缓冲没有足够的空间来容纳新的数据项，则入队操作失败。

数据项的 **出队** 操作指的是移除已入队时间最久的项。待出队的数据项的内容以及所关联的元数据值会被拷贝到所指定的区域。如果环形缓冲为空，或者所指定的区域不够容难数据项的数据，则出队操作失败。


并发性
===========

环形缓冲的 API 没有提供任何的并发控制。依赖于具体的使用方法（尤其是有多个并发的读者/写者），应用程序可以使用信号量/互斥量来通知消费者有新数据到达，这样能够保护环形缓冲。

对于只有一个生产者和一个消费者的情况，不需要使用并发控制。

内部操作
==================

环形缓冲总是在其数据缓冲区中维护了一个空的 32 比特字，用于区分空/满状态。

如果数据缓冲区的大小是 2 的整数次幂，则当数据项在入队/出队操作时会使用高效的位掩操作，而不是昂贵的取模操作。

实现
**************

定义环形缓冲
======================

使用类型为 :c:type:`struct ring_buf` 的变量可以定义环形缓冲。缓冲缓冲定后必须使用函数 :cpp:func:`sys_ring_buf_init()` 对其进行初始化。

下面的代码定义并初始化了一个空的环形缓冲（是一个更大的数据结构的一部分）。环形缓冲的数据 buffer 可以容纳 64 字的数据和元数据（metadata）信息。

.. code-block:: c

    #define MY_RING_BUF_SIZE 64

    struct my_struct {
        struct ring_buf rb;
        uint32_t buffer[MY_RING_BUF_SIZE];
        ...
    };
    struct my_struct ms;

    void init_my_struct {
        sys_ring_buf_init(&ms.rb, sizeof(ms.buffer), ms.buffer);
        ...
    }

也可以使用文件中的两个宏在编译时定义并初始化一个互斥量。每个宏都会既定义环形缓冲又会定义其数据缓冲区。

下面的代码定义了一个数据缓冲区大小为 2 的整数次幂的环形缓冲，它可以通过位掩操作进行高效地访问。

.. code-block:: c

    /* Buffer with 2^8 (or 256) words */
    SYS_RING_BUF_DECLARE_POW2(my_ring_buf, 8);

下面的代码定义了一个数据缓冲区大小任意的环形缓冲，它可以通过取模操作进行低效率地访问。

.. code-block:: c

    #define MY_RING_BUF_WORDS 93
    SYS_RING_BUF_DECLARE_SIZE(my_ring_buf, MY_RING_BUF_WORDS);

数据入队
==============

函数 :cpp:func:`sys_ring_buf_put()` 可用于往环形缓冲中添加一个数据项。

.. code-block:: c

    uint32_t my_data[MY_DATA_WORDS];
    int ret;

    ret = sys_ring_buf_put(&ring_buf, TYPE_FOO, 0, my_data, SIZE32_OF(my_data));
    if (ret == -EMSGSIZE) {
        /* not enough room for the data item */
	...
    }

如果该数据项只需要类型或者应用程序指定的整数值（即它没有数据数组），可以将其 size 设为 0、其数据指针指向 :c:macro:`NULL`。

.. code-block:: c

    int ret;

    ret = sys_ring_buf_put(&ring_buf, TYPE_BAR, 17, NULL, 0);
    if (ret == -EMSGSIZE) {
        /* not enough room for the data item */
	...
    }

重入数据
===============

函数 :cpp:func:`sys_ring_buf_get()` 可用于从环形缓冲中移除一个数据项。

.. code-block:: c

    uint32_t my_data[MY_DATA_WORDS];
    uint16_t my_type;
    uint8_t  my_value;
    uint8_t  my_size;
    int ret;

    my_size = SIZE32_OF(my_data);
    ret = sys_ring_buf_get(&ring_buf, &my_type, &my_value, my_data, &my_size);
    if (ret == -EMSGSIZE) {
        printk("Buffer is too small, need %d uint32_t\n", my_size);
    } else if (ret == -EAGAIN) {
        printk("Ring buffer is empty\n");
    } else {
        printk("Got item of type %u value &u of size %u dwords\n",
               my_type, my_value, my_size);
        ...
    }

API
****

:file:`misc/ring_buffer.h` 中提供了如下关于环形缓冲的 API：

* :cpp:func:`SYS_RING_BUF_DECLARE_POW2()`
* :cpp:func:`SYS_RING_BUF_DECLARE_SIZE()`
* :cpp:func:`sys_ring_buf_init()`
* :cpp:func:`sys_ring_buf_is_empty()`
* :cpp:func:`sys_ring_buf_space_get()`
* :cpp:func:`sys_ring_buf_put()`
* :cpp:func:`sys_ring_buf_get()`
