.. _atomic_v2:

原子服务
###############

:dfn:`原子变量` 是一个 32 比特的变量。线程或者 ISR 可以以不可打断的方式对其进行读取和修改。

.. contents::
    :local:
    :depth: 2

概念
********

您可以定义任意数量的原子变量。

对原子变量的操作需要使用内核提供的原子相关的 API，这样才能保证所需要的操作能正确执行（即使高优先级的上下文也操作了同一变量）。

内核也支持在一个原子变量数组中对单一比特进行原子操作。

实现
**************

定义原子变量
===========================

原子变量使用类型 :c:type:`atomic_t` 进行定义。

默认情况下，原子变量被初始化为 0。不过，您也可以使用宏 :c:macro:`ATOMIC_INIT` 将其初始化为其它值：

.. code-block:: c

    atomic_t flags = ATOMIC_INIT(0xFF);

操作原子变量
===============================

您可以使用本节后面列举的 API 操作原子变量。

下面的代码向您展示了如何利用原子变量记录某个函数被调用的次数。由于 count 是原子递增的，因此可以避免这样的风险：当线程正在调用该函数时，对递增操作只进行了一半，此时有一个更高优先级的上下文抢占了该线程，且也调用了这个函数，从而导致递增值的错误。

.. code-block:: c

    atomic_t call_count;

    int call_counting_routine(void)
    {
        /* increment invocation counter */
        atomic_inc(&call_count);

        /* do rest of routine's processing */
        ...
    }

操作原子变量数组
=========================================

您可以以常规的方式定义一个原子变量数组（每个元素 32 比特）。不过，您也可以使用宏 :c:macro:`ATOMIC_DEFINE` 来定义一个 N 比特的原子数组。

本节最后面以 :cpp:func:`_bit` 结尾的 API 可以用来操作原子数组中的某一个比特。

下面的代码展示了如何通过原子数组的方式实现设置 200 个标志比特的方法。

.. code-block:: c

    #define NUM_FLAG_BITS 200

    ATOMIC_DEFINE(flag_bits, NUM_FLAG_BITS);

    /* set specified flag bit & return its previous value */
    int set_flag_bit(int bit_position)
    {
        return (int)atomic_set_bit(flag_bits, bit_position);
    }

建议的用法
**************

当只需要操作一个 32 比特的值时，使用一个原子变量即可。

当需要操作的标志比特位数超过 32 比特时，使用多个原子变量。

.. note::
    相对于其它方法，例如互斥量或者锁中断，原子变量通常更高效。

配置选项
*********************

相关配置选项：

* :option:`CONFIG_ATOMIC_OPERATIONS_BUILTIN`
* :option:`CONFIG_ATOMIC_OPERATIONS_CUSTOM`
* :option:`CONFIG_ATOMIC_OPERATIONS_C`

APIs
****

文件 :file:`atomic.h` 中提供了如下关于原子操作的 API：

* :c:macro:`ATOMIC_INIT`
* :c:macro:`ATOMIC_DEFINE`
* :cpp:func:`atomic_get()`
* :cpp:func:`atomic_set()`
* :cpp:func:`atomic_clear()`
* :cpp:func:`atomic_add()`
* :cpp:func:`atomic_sub()`
* :cpp:func:`atomic_inc()`
* :cpp:func:`atomic_dec()`
* :cpp:func:`atomic_and()`
* :cpp:func:`atomic_or()`
* :cpp:func:`atomic_xor()`
* :cpp:func:`atomic_nand()`
* :cpp:func:`atomic_cas()`
* :cpp:func:`atomic_set_bit()`
* :cpp:func:`atomic_clear_bit()`
* :cpp:func:`atomic_test_bit()`
* :cpp:func:`atomic_test_and_set_bit()`
* :cpp:func:`atomic_test_and_clear_bit()`
