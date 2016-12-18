.. _stacks_v2:

栈
######

:dfn:`栈（stack）` 是一个内核对象，它实现了传统的后进先出（last in first out）队列，允许线程和 ISR 添加大小为 32 比特的数据值。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的栈。每个栈通过其内存地址进行引用。

栈的关键属性包括：

* **队列**： 它包含了已被添加但还未被移除的长度为 32 比特的数据值。队列使用整型数组实现，且必须在 4 字节边界上对齐。

* **最大数量**：栈的容量。

栈必须先初始化再使用。初始化时会将栈的队列设为空。

数据可以被线程或者 ISR **添加** 到栈中。如果有线程在该栈上等待数据，则该数据直接被传递该线程；否则，该数据会被添加到栈的队列中。内核在添加数据到栈时，不会检测该栈的队列值是否已达到最大数量。

.. note::

    向一个已满的栈添加数据会导致数组越界，最终会产生不可预料的行为。

数据项可以被线程从栈中 **移除**。如果该栈的队列为空，线程在这个栈上进行等待。多个线程可以同时在某个空栈上等待，当一个新的数据项被添加时，它会被给予优先级最高的、等待时间最久的线程。

.. note::
    
    ISR 虽然也可以从栈中移除数据，但是如果栈为空，ISR 不能进行等待。

实现
**************

定义栈
================

使用类型为 :c:type:`struct k_stack` 的变量可以定义一个栈。栈定义后必须使用函数 :cpp:func:`k_stack_init()` 对其进行初始化。

下面的代码定义并初始化了一个可以容纳 10 个值的空栈。

.. code-block:: c

    #define MAX_ITEMS 10

    uint32_t my_stack_array[MAX_ITEMS];
    struct k_stack my_stack;

    k_stack_init(&my_stack, my_stack_array, MAX_ITEMS);

也可以使用宏 :c:macro:`K_STACK_DEFINE` 在编译时定义并初始化一个栈。

下面的代码与上面的代码段具有相同的效果。注意，该宏既定义了栈又定义了数组。

.. code-block:: c

    K_STACK_DEFINE(my_stack, MAX_ITEMS);

压栈
==================

函数 :cpp:func:`k_stack_push()` 可用于将数据项压栈。

下面的代码基于上面的例程之上，它展示了线程是如何通过保存数据结构池的内存地址到栈中来创建数据结构池的过程。

.. code-block:: c

    /* define array of data structures */
    struct my_buffer_type {
        int field1;
        ...
	};
    struct my_buffer_type my_buffers[MAX_ITEMS];

    /* save address of each data structure in a stack */
    for (int i = 0; i < MAX_ITEMS; i++) {
        k_stack_push(&my_stack, (uint32_t)&my_buffers[i]);
    }

出栈
====================

函数 :cpp:func:`k_stack_pop()` 可以用于从栈中弹出一个数据项。

下面的代码基于上面的例程之上，它展示了线程是如何动态地分配一个未使用的数据结构的过程。当不再需要数据结构时，线程必须将它的地址压入到栈中，以允许该数据结构能被重复利用。

.. code-block:: c

    struct my_buffer_type *new_buffer;

    k_stack_pop(&buffer_stack, (uint32_t *)&new_buffer, K_FOREVER);
    new_buffer->field1 = ...

建议的用法
**************

当已知待存储的数据项的数量时，可以使用栈以后进先出的方式保存和恢复大小为 32 比特的数据。

配置选项
*********************

相关的配置学习：

* 无。

API
****

:file:`kernel.h` 中提供了如下与栈相关的 API：

* :c:macro:`K_STACK_DEFINE`
* :cpp:func:`k_stack_init()`
* :cpp:func:`k_stack_push()`
* :cpp:func:`k_stack_pop()`
