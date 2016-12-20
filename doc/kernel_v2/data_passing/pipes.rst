.. _pipes_v2:

管道
#####

:dfn:`管道（pipe）` 是一个内核对象，它允许一个线程向另一个线程发送字节流。管道可用于同步或异步传递数据块（整部或部分）。

.. contents::
    :local:
    :depth: 2

概念
********

管道可以带环形缓冲（缓冲可以容纳已被添加且还未被接收的数据），也可以不带环形缓冲。

可以定义任意数量的管道。管道通过其内存地址进行引用。

管道的关键属性包括：

* **尺寸**：管道的环形缓冲的尺寸。注意，零表示无环形缓冲的管道。

管道必须先初始化再使用。初始化时会将管道置为空。

线程可以向管道中同步 **发送** （整体或部分）数据。如果所指定的最小字节数不能立即满足，则相关操作可以立即失败，或者可以发送尽可能多的数据并寄希望于在随后会完成发送。被接收到的数据既可以直接拷贝到管道的环形缓冲，也可以直接交给正在等待的读者。

线程可以使用内存块向管道中异步 **发送** （整体）数据。当管道接收到内存块中的所有数据后，它将会释放该内存块，（如果被要求）并给出信号量。

线程可以从管道中同步 **接收** 数据。如果所指定的最小字节数不能立即满足，则相关操作可以立即失败，或者可以接收尽可能多的数据并寄希望于在随后会完成接收。接收到的数据既可以直接拷贝到管道的环形缓冲中，也可以直接交给正在等待的读者。

.. note::
    
    内核 **不** 允许 ISR 向/从管道中发送/接收数据，即使它们不等待。

实现
**************

使用类型为 :c:type:`struct k_pipe` 的变量以及可选的类型为 :c:type:`unsigned char` 的字符缓冲可以定义管道。管道定义后必须使用函数 :cpp:func:`k_pipe_init()` 对其进行初始化。

下面的代码定义并初始化了一个空管道，它是 4 字节对其的，且带有一个能容纳 10 字节的环形缓冲。


.. code-block:: c

    unsigned char __aligned(4) my_ring_buffer[100];
    struct k_pipe my_pipe;

    k_pipe_init(&my_pipe, my_ring_buffer, sizeof(my_ring_buffer));

也可以使用宏 :c:macro:`K_PIPE_DEFINE` 在编译时定义并初始化一个管道。

下面的代码与上面的代码段具有相同的效果。注意到，该宏既定义了管道，又定义了环形缓冲。

.. code-block:: c

    K_PIPE_DEFINE(my_pipe, 100, 4);

向管道中写
=================

函数 :cpp:func:`k_pipe_put()` 可用于向管道中写数据。

下面的代码基于上面的例程之上，它使用管道从一个生产者线程向一个或多个消费者线程传递数据。如果由于消费者来不及取数据而导致管道的环形缓冲被填满，生产者线程可以等待一段指定的时间。

.. code-block:: c

    struct message_header {
        ...
    };

    void producer_thread(void)
    {
        unsigned char *data;
        size_t total_size;
        size_t bytes_written;
        int    rc;
        ...

        while (1) {
            /* Craft message to send in the pipe */
            data = ...;
            total_size = ...;

            /* send data to the consumers */
            rc = k_pipe_put(&my_pipe, data, total_size, &bytes_written,
                            sizeof(struct message_header), K_NO_WAIT);

            if (rc < 0) {
                /* Incomplete message header sent */
                ...
            } else if (bytes_written < total_size) {
                /* Some of the data was sent */
                ...
            } else {
                /* All data sent */
                ...
            }
        }
    }

从管道中读
===================

函数 :cpp:func:`k_pipe_get()` 可用于从管道中读取数据。

下面的代码基于上面的例程之上，它使用管道处理从一个或多个生产者线程产生的数据。

.. code-block:: c

    void consumer_thread(void)
    {
        unsigned char buffer[120];
        size_t   bytes_read;
        struct message_header  *header = (struct message_header *)buffer;

        while (1) {
            rc = k_pipe_get(&my_pipe, buffer, sizeof(buffer), &bytes_read,
                            sizeof(header), K_MSEC(100));

            if ((rc < 0) || (bytes_read < sizeof (header))) {
                /* Incomplete message header received */
                ...
            } else if (header->num_data_bytes + sizeof(header) > bytes_read) {
                /* Only some data was received */
                ...
            } else {
                /* All data was received */
                ...
            }
        }
    }

建议的用法
**************

使用管道在线程间发送字节流。

    如果有需要，消息队列也可用于传输大的数据项。不过，这将增加中断的延迟，因为向消息队列中写数据时会锁中断。传递大数据项的更优雅的做法是使用指向数据项的指针，而不是数据项本身。对这种情况，内核的内存映射和内存池对象更合适。
.. note::
    
    如果有需要，管道也可以用于传输长的字节流。不过，传输长字节流的更有效的做法是使用执行字节流的指针，从而避免拷贝数据。对这种情况，内核的内存映射和内存池对象类型更合适。

配置选项
*********************

相关的配置选项：

* :option:`CONFIG_NUM_PIPE_ASYNC_MSGS`

API
****


:file:`kernel.h` 中提供了与管道相关的 API：

* :c:macro:`K_PIPE_DEFINE`
* :cpp:func:`k_pipe_init()`
* :cpp:func:`k_pipe_put()`
* :cpp:func:`k_pipe_get()`
* :cpp:func:`k_pipe_block_put()`
