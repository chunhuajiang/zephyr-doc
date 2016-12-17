.. _memory_slabs_v2:

内存片
############

:dfn:`内存片（memory slab）` 是一个内核对象，它允许从指定的内存区域上动态地分配内存块（memory block）。同一个内存片上面的所有内存块的尺寸是固定（相同）的，这样做的好处是可以高效地分配和释放，避免了内存碎片问题。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的内存片。每个内存片通过其内存地址进行引用。

内存片的关键属性包括：

* **块大小**： 每个块的尺寸，单位是字节。它必须大于 4N 字节，其中 N 大于 0。

* **块数量**：该内存片上可分配的块的数量。它必须大于 0。

* **buffer**：内存片的块的实际内存区域。它必须大于 “块大小” x “块数量”。

内存片的 buffer 必须 N 字节对齐，其中 N 是大于 2 的 2 的整数次幂（例如 4,8,16...）。为了保证 buffer 中的所有内存块都对齐到这个边界，块的大小必须是 N 的整数倍。

内存片必须先初始化再使用。初始化时会将所有的块标记为未使用。


当线程需要内存块时，它只需要从一个内存片中申请。当线程使用完内存块后，它必须将其释放给原内存片，让其可以重复利用。


如果当前所有的内存块都在使用中，线程可以等待，直到某个块可用。多个线程可以同时等待某个空的内存片；当某个内存块可用时，它会被某个优先级最高的、等待时间最久的线程使用。

与堆不同的是，如果有需要，可以定义多个内存片。这样的好处是可以定义块大小不同的内存片。也可以使用内存池对象。

内部操作
==================

内存片的 buffer 是一个数组，数组的元素则是大小固定的块，这样能保证在块与块之间没有空间被浪费。

内存片使用一个链表来跟踪未使用的块。每个未使用块的前 4 个字节用于提供链接信息。

实现
**************

定义内存片
======================

使用类型为 :c:type:`struct k_mem_slab` 的变量可以定义内存片。内存片定义后必须使用函数 :cpp:func:`k_mem_slab_init()` 进行初始化。

下面的代码定义并初始化了一个内存片，该内存片具有 6 大小为 400 字节的块，每个块都对齐到 4 字节边界。

.. code-block:: c

    struct k_mem_slab my_slab;
    char __aligned(4) my_slab_buffer[6 * 400];

    k_mem_slab_init(&my_slab, my_slab_buffer, 400, 6);

另外，也可以调用宏 :c:macro:`K_MEM_SLAB_DEFINE` 在编译期间就定义并初始化一个内存片。

下面的代码与上面的代码片段具有相同的作用。注意到，该宏即定义了它的内存片，也定义了它的 buffer。

.. code-block:: c

    K_MEM_SLAB_DEFINE(my_slab, 400, 6, 4);

分配内存块
=========================

函数 :cpp:func:`k_mem_slab_alloc()` 用于分配内存块。

下面的代码基于上面的例程，它会先等待 100 毫秒，以拿到一个可以的内存块，然后将其填充为零。如果没有获得合适的内存块，代码会打印一个警告信息。

.. code-block:: c

    char *block_ptr;

    if (k_mem_slab_alloc(&my_slab, &block_ptr, 100) == 0)) {
        memset(block_ptr, 0, 400);
	...
    } else {
        printf("Memory allocation time-out");
    }

释放内存块
========================

调用函数 :cpp:func:`k_mem_slab_free()` 可以释放内存块。

下面的代码基于上面的例程，先分配了一个内存块，并在不再需要使用时将其释放。

.. code-block:: c

    char *block_ptr;

    k_mem_slab_alloc(&my_slab, &block_ptr, K_FOREVER);
    ... /* use memory block pointed at by block_ptr */
    k_mem_slab_free(&my_slab, &block_ptr);

建议的用法
**************

当需要分配、释放大小固定的内存块时，可以使用内存片。

当一个线程需要给另一个线程发送大量的数据时，可以使用内存片，这样可以避免不必要的数据拷贝。

配置选项
*********************

相关的配置选项：

* 无。

API
****

:file:`kernel.h` 中提供了下列内存片相关的 API：

* :c:macro:`K_MEM_SLAB_DEFINE`
* :cpp:func:`k_mem_slab_init()`
* :cpp:func:`k_mem_slab_alloc()`
* :cpp:func:`k_mem_slab_free()`
* :cpp:func:`k_mem_slab_num_used_get()`
* :cpp:func:`k_mem_slab_num_free_get()`
