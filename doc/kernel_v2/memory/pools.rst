.. _memory_pools_v2:

内存池
############

:dfn:`内存池（memory pool）` 是一个内核对象，它允许从指定的内存区域上动态地分配内存块（memory block）。同一个内存池中的内存块的大小是不固定的，这样可以减小由于不同的应用程序需要为大小不同的数据结构分配不同的存储空间所造成的浪费。内存池使用“伙伴（buddy）内存分配”算法，它可以高效地将大块内存分割为小块内存。此外，它还可以在最大限度减小内存碎片的前提下，高效地分配和释放不小不同的内存块。

.. contents::
    :local:
    :depth: 2

概念
********

Any number of memory pools can be defined. Each memory pool is referenced
by its memory address.

A memory pool has the following key properties:

* A **minimum block size**, measured in bytes.
  It must be at least 4X bytes long, where X is greater than 0.

* A **maximum block size**, measured in bytes.
  This should be a power of 4 times larger than the minimum block size.
  That is, "maximum block size" must equal "minimum block size" times 4^Y,
  where Y is greater than or equal to zero.

* The **number of maximum-size blocks** initially available.
  This must be greater than zero.

* A **buffer** that provides the memory for the memory pool's blocks.
  This must be at least "maximum block size" times
  "number of maximum-size blocks" bytes long.

The memory pool's buffer must be aligned to an N-byte boundary, where
N is a power of 2 larger than 2 (i.e. 4, 8, 16, ...). To ensure that
all memory blocks in the buffer are similarly aligned to this boundary,
the minimum block size must also be a multiple of N.

A thread that needs to use a memory block simply allocates it from a memory
pool. Following a successful allocation, the :c:data:`data` field
of the block descriptor supplied by the thread indicates the starting address
of the memory block. When the thread is finished with a memory block,
it must release the block back to the memory pool so the block can be reused.

If a block of the desired size is unavailable, a thread can optionally wait
for one to become available.
Any number of threads may wait on a memory pool simultaneously;
when a suitable memory block becomes available, it is given to
the highest-priority thread that has waited the longest.

Unlike a heap, more than one memory pool can be defined, if needed. For
example, different applications can utilize different memory pools; this
can help prevent one application from hijacking resources to allocate all
of the available blocks.

Internal Operation
==================

A memory pool's buffer is an array of maximum-size blocks,
with no wasted space between the blocks.
Each of these "level 0" blocks is a *quad-block* that can be
partitioned into four smaller "level 1" blocks of equal size, if needed.
Likewise, each level 1 block is itself a quad-block that can be partitioned
into four smaller "level 2" blocks in a similar way, and so on.
Thus, memory pool blocks can be recursively partitioned into quarters
until blocks of the minimum size are obtained,
at which point no further partitioning can occur.

A memory pool keeps track of how its buffer space has been partitioned
using an array of *block set* data structures. There is one block set
for each partitioning level supported by the pool, or (to put it another way)
for each block size. A block set keeps track of all free blocks of its
associated size using an array of *quad-block status* data structures.

When an application issues a request for a memory block,
the memory pool first determines the size of the smallest block
that will satisfy the request, and examines the corresponding block set.
If the block set contains a free block, the block is marked as used
and the allocation process is complete.
If the block set does not contain a free block,
the memory pool attempts to create one automatically by splitting a free block
of a larger size or by merging free blocks of smaller sizes;
if a suitable block can't be created, the allocation request fails.

.. note::
    By default, memory pools will attempt to split a larger block
    before trying to merge smaller blocks. However, they can also
    be configured to merge smaller blocks first, or to skip
    the merging step entirely. In the latter case, merging of smaller
    blocks only occurs when the application explicitly issues
    a request to defragment the entire memory pool.

The memory pool's block merging and splitting process is done efficiently,
but it is a recursive algorithm that may incur significant overhead.
In addition, the merging algorithm cannot combine adjacent free blocks
of different sizes, nor can it merge adjacent free blocks of the same size
if they belong to different parent quad-blocks. As a consequence,
memory fragmentation issues can still be encountered when using a memory pool.

When an application releases a previously allocated memory block
it is simply marked as a free block in its associated block set.
The memory pool does not attempt to merge the newly freed block,
allowing it to be easily reallocated in its existing form.

实现
**************

定义内存池
======================

使用类型为 :c:type:`struct k_mem_pool` 的变量可以定义一个内存池。不过，由于内存池也需要大量的尺寸可变的数据结构来代表它的块集合和它的 quad-block 的状态，内核不支持在运行时动态地定义内存池。内存池只能使用 :c:macro:`K_MEM_POOL_DEFINE` 在编译时进行定义和初始化。

下面的代码定义并初始化了一个内存池，这个内存池有三个大小为 4096 字节的块。这些块也可以被划分为最小为 64 字节的 4 字节对齐的子块。（也就是说，内存池支持的块大小是 4096、1024、256 和 64 字节。）注意，该宏定义了内存池的所有数据结构和它的 buffer。

.. code-block:: c

    K_MEM_POOL_DEFINE(my_pool, 64, 4096, 3, 4);

分配内存块
=========================

函数 :cpp:func:`k_mem_pool_alloc()` 用于分配内存块。

下面的代码会先等待 100 毫秒，以拿到一个 200 字节的可以内存块，然后将其填充为零。如果没有获得合适的内存块，代码会打印一个警告信息。

注意，应用程序实际会接收到一个大小为 256 字节的内存块，因为这是内存池所支持的最接近的尺寸。

.. code-block:: c

    struct k_mem_block block;

    if (k_mem_pool_alloc(&my_pool, &block, 200, 100) == 0)) {
        memset(block.data, 0, 200);
	...
    } else {
        printf("Memory allocation time-out");
    }

释放内存块
========================

函数 :cpp:func:`k_mem_pool_free()` 用于释放内存块。

下面的代码基于上面的例程之上，它申请了 75 字节的内存块，并在不再使用时释放。（基于安全考虑，实际上会从堆内存池使用 256 字节的内存块。）

.. code-block:: c

    struct k_mem_block block;

    k_mem_pool_alloc(&my_pool, &block, 75, K_FOREVER);
    ... /* use memory block */
    k_mem_pool_free(&block);

内存池手工去碎片
====================================

This code instructs the memory pool to concatenate unused memory blocks
into their parent quad-blocks wherever possible. Doing a full defragmentation
of the entire memory pool before allocating a number of memory blocks
may be more efficient than relying on the partial defragmentation that can
occur automatically each time a memory block allocation is requested.

.. code-block:: c

    k_mem_pool_defragment(&my_pool);

建议的用法
**************

当需要分配大小不固定的内存时，可以使用内存池。

当一个线程需要给另一个线程发送大量的数据时，可以使用内存池，这样可以避免不必要的数据拷贝。

配置选项
*********************

相关的配置选项：

* :option:`CONFIG_MEM_POOL_SPLIT_BEFORE_DEFRAG`
* :option:`CONFIG_MEM_POOL_DEFRAG_BEFORE_SPLIT`
* :option:`CONFIG_MEM_POOL_SPLIT_ONLY`


API
****

:file:`kernel.h` 中提供了下列内存池相关的 API：

* :c:macro:`K_MEM_POOL_DEFINE`
* :cpp:func:`k_mem_pool_alloc()`
* :cpp:func:`k_mem_pool_free()`
* :cpp:func:`k_mem_pool_defrag()`
