.. _interrupts_v2:

中断
##########

:dfn:`中断服务例程` (ISR) 是一个异步响应硬件或者软件中断的函数。ISR 通常会抢占当前正在执行的线程，以达到快速响应的目的。只有当所有的 ISR 工作都完成后，线程才能得以恢复执行。

.. contents::
    :local:
    :depth: 2

概念
********

理论上，您可以定义任意数量的 ISR，但是它的实际个数受到硬件的限制。

ISR 的关键属性如下：

* **中断请求（IRQ）信号**：触发 ISR 的信号。
* **优先级**：与 IRQ 绑定在一起的优先级。
* **中断处理函数**：用于处理中断的函数。
* **参数值**：传递给函数的参数。

:abbr:`IDT（中断描述符表）`或者向量表用于将一个给定的 ISR 与一个给定的中断源关联在一起。在任意时刻，一个 IRQ 只能与一个 ISR 关联。

多个 ISR 可以利用同一个函数来处理中断，这样的好处是允许一个函数可以同时服务于某个设备产生的多种不同类型中断，或者甚至服务于多个设备（通常是同种类型的）产生的中断。传递给 ISR 的参数值可以用于判断是具体哪一个中断源产生了信号。

内核为所有未使用的 IDT 入口提供了一个默认的 ISR。如果发生了意外的中断，改 ISR 将产生一个致命系统错误。

内核支持 **中断嵌套**，即高优先级的中断可以抢占正在执行的低优先级中断。当高优先级的 ISR 处理完成后，低优先级的 ISR 将恢复执行。

ISR 的中断处理函数在内核的 **中断上下文** 中执行。这个上下文有自己专用的栈区。如果中断嵌套被使能了，必须保证中断上下文栈的大小能够容纳多个 ISR 并发执行。

.. important::
    很多 API 只能被线程使用，不能被 ISR 使用。如果某个函数既可以被线程调用，也可以被 ISR 调用，内核会使用 API  cpp:func:`k_is_in_isr()` 来让该函数判断当前的上下文是线程还是 ISR，然后再做对应的处理。
	
阻止中断
========================

在某些特殊情况下，例如当前线程正在执行时间敏感的任务或者进行临界区的操作，则可能需要阻止 ISR 运行。

线程可以使用 **IRQ 锁** 临时阻止系统处理所有 IRQ。IRQ 锁可以嵌套使用。内核如果要再次正常处理 IRQ，则必须保证 IRQ 解锁的次数等于 IRQ 锁的次数。

.. important::

    IRQ 锁是与线程相关的。如果线程 A 锁定了中断，然后执行了某个操作（例如释放了一个信号量，或者睡眠 N 毫秒）导致线程 B 开始运行，则当线程 A 被交换出去后，这个线程锁将（暂时）失效。也就是说，当线程 B 运行后，除非它使用了自己的 IRQ 锁锁定了中断，否则它将能正常处理中断。（当内核正在在使用了 IRQ 锁的两个线程间切换时，其是否可以处理中断依赖于具体的架构。）
	

    当线程 A 再次变为当前线程后，内核会重新建立线程 A 的 IRQ 锁。这意味着，线程 A 在明确解除 IRQ 锁前都不会被中断。

或者，线程也可以临时 **禁止** 某一个 IRQ。当接收到该 IRQ 的信号时，其关联的 ISR 不会被执行。在随后，该 IRQ 必须被 **使能**，以允许其 ISR 能够执行。

.. important::
    禁止一个 IRQ 后，不仅仅是禁止该 IRQ  的线程不会被对应的 ISR 抢占，而是系统中的 *所有* 线程都不会被这个 IRQ 对应的 ISR 抢占。

分担 ISR 工作
===================
   
ISR 应当快速执行，以确保可预见的系统行为。如果需要执行耗时的处理，ISR 应当将部分或者全部处理都移交给线程，以此恢复内核响应其它中断的功能。

内核支持多种将中断相关处理移交给线程的机制。


* ISR 可以利用内核对象，例如 fifo、lifo 或者信号量，给帮助线程发送信号，让它们做中断相关的处理。


* ISR 可以发送一个告警，让系统的工作队列线程执行一个相关的告警处理函数。（参考 :ref:`alerts_v2`。）


* ISR 可以指示系统工作队列线程执行一个工作项。（参考 TBD。）

当 ISR 将工作移交给线程后，内核通常会在 ISR 完成后切换到该线程，以使中断相关的处理能够立即执行。不过，这依赖于处理移交工作的线程的优先级，即当前正在执行的协作式线程或者其它高优先级线程可能比该线程先执行。

实现
**************

定义一个 ISR
===============

在运行时，可以先调用 :c:macro:`IRQ_CONNECT` 来定义一个 ISR，然后调用 :cpp:func:`irq_enable()` 来使能该 ISR。 

.. important::
    IRQ_CONNECT() 不是 C 函数，其它内部其实是一个内敛汇编。它的所有参数都必须在编译时确定。如果一个驱动程序有多个实例，它可以为该驱动的每个实例定义一个配置函数。

下面的代码定义并使能了一个 ISR。

.. code-block:: c

    #define MY_DEV_IRQ  24       /* device uses IRQ 24 */
    #define MY_DEV_PRIO  2       /* device uses interrupt priority 2 */
    /* argument passed to my_isr(), in this case a pointer to the device */
    #define MY_ISR_ARG  DEVICE_GET(my_device)
    #define MY_IRQ_FLAGS 0       /* IRQ flags. Unused on non-x86 */

    void my_isr(void *arg)
    {
       ... /* ISR code */
    }

    void my_isr_installer(void)
    {
       ...
       IRQ_CONNECT(MY_DEV_IRQ, MY_DEV_PRIO, my_isr, MY_ISR_ARG, MY_IRQ_FLAGS);
       irq_enable(MY_DEV_IRQ);
       ...
    }

建议的用法
**************

在 ISR 执行需要快速响应、能够快速完成、不会阻塞的中断处理。

.. note::
    对于那些比较耗时的，或者会阻塞的中断处理，应当将它们的工作移交给一个线程。您可以阅读 `Offloading ISR Work`_ 查看可以在应用程序中使用的各种技术。

配置选项
*********************

相关的配置选项：

* :option:`CONFIG_ISR_STACK_SIZE`

此外，还有一些与架构相关的或者与设备相关的配置选项。

API
****

:file:`irq.h` 中提供的关于中断的 API 如下：

* :c:macro:`IRQ_CONNECT`
* :cpp:func:`irq_lock()`
* :cpp:func:`irq_unlock()`
* :cpp:func:`irq_enable()`
* :cpp:func:`irq_disable()`
* :cpp:func:`irq_is_enabled()`

:file:`kernel.h` 中提供的关于中断的 API 如下：

* :cpp:func:`k_is_in_isr()`
* :cpp:func:`k_is_preempt_thread`
