.. _kernel_apis:

内核 API
###########

本节包含内核核心服务（参考 :ref:`kernel_v2` ）的 API。

.. important::
    除非特别注释，这些 API 只能被线程使用，不能被 ISR 使用。

.. contents::
   :depth: 1
   :local:
   :backlinks: top

线程
*******

线程是用于实现应用程序部分功能的独立可调度指令的集合。线程用于处理由于执行时间太长或者太复杂而不能在 ISR 内执行的任务。（参考 :ref:`threads_v2` ）

.. doxygengroup:: thread_apis
   :project: Zephyr
   :content-only:

工作队列
**********

工作队列通过执行一个专有线程里的相关函数来处理一系列的工作项。工作队列通常用于将 ISR 或者高优先级线程的非紧急任务移交到低优先级线程。（参考 :ref:`threads_v2` ）

.. doxygengroup:: workqueue_apis
   :project: Zephyr
   :content-only:

时钟
******

内核时钟使线程或者 ISR 能够用常规精度和高精度来测量经过了多少时间。（参考 :ref:`clocks_v2` ）

.. doxygengroup:: clock_apis
   :project: Zephyr
   :content-only:

定时器
******

定时器时线程能够测量经过了多少时间，并在时间到期后执行某个动作（可选）。（参考 :ref:`timers_v2` ）

.. doxygengroup:: timer_apis
   :project: Zephyr
   :content-only:

内存片
************

内存片能够用来动态地分配和释放固定尺寸的内存块。（参考 :ref:`memory_slabs_v2` ）

.. doxygengroup:: mem_slab_apis
   :project: Zephyr
   :content-only:

内存池
************

内存池能够用来动态地分配和释放可变尺寸的内存块。（参考 :ref:`memory_pools_v2` ）

.. doxygengroup:: mem_pool_apis
   :project: Zephyr
   :content-only:

堆内存池
****************

堆内存池能够用来像 :cpp:func:`malloc` 那样动态地分配和释放内存块。（参考 :ref:`heap_v2` ）

.. doxygengroup:: heap_apis
   :project: Zephyr
   :content-only:

信号量
**********

信号量提供了传统的计数信号量功能。（参考 :ref:`semaphores_v2` ）

.. doxygengroup:: semaphore_apis
   :project: Zephyr
   :content-only:

互斥量
*******

互斥量提供了带有基础优先级继承的传统可重入互斥量功能。（参考 :ref:`mutexs_v2` ）

.. doxygengroup:: mutex_apis
   :project: Zephyr
   :content-only:

告警
******

告警使应用程序能够执行异步信号，在这某种程度上类似于 Unix 风格的信号。（参考 :ref:`alerts_v2` ）

.. doxygengroup:: alert_apis
   :project: Zephyr
   :content-only:

FIFO
*****

FIFO 提供了传统的适用于任意尺寸数据的先进先出的功能。（参考 :ref:`fifos_v2` ）

.. doxygengroup:: fifo_apis
   :project: Zephyr
   :content-only:

LIFO
*****

LIFO 提供了传统的适用于任意尺寸数据的后进先出的功能。（参考 :ref:`lifos_v2` ）

.. doxygengroup:: lifo_apis
   :project: Zephyr
   :content-only:

栈
******

栈提供了传统的以 32 比特为单位的数据项的后进线程的功能。（参考 :ref:`stacks_v2` ）

.. doxygengroup:: stack_apis
   :project: Zephyr
   :content-only:

消息队列
**************

消息队列提供了一个简单的适用于尺寸固定的数据项的消息队列机制。（参考 :ref:`message_queues_v2` ）

.. doxygengroup:: msgq_apis
   :project: Zephyr
   :content-only:

邮筒
*********

邮筒提供了一个适用于尺寸可变的消息的消息排队机制。（参考 :ref:`mailboxes_v2` ）

.. doxygengroup:: mailbox_apis
   :project: Zephyr
   :content-only:

管道
*****

管道提供了可发送尺寸可变的数据块的匿名管道机制。（参考 :ref:`pipes_v2` ）

.. doxygengroup:: pipe_apis
   :project: Zephyr
   :content-only:

中断服务例程（ISR）
*********************************

ISR 是为响应硬件或者软件中断而异步执行的一些列指令。（参考 :ref:`interrupts_v2` ）

.. doxygengroup:: isr_apis
   :project: Zephyr
   :content-only:

原子服务
***************

原子服务使多个线程和 ISR 能够以不可中断的方式读取和修改 32 比特的变量。（参考 :ref:`atomic_v2` ）

.. important::
    All atomic services APIs can be used by both threads and ISRs.

.. doxygengroup:: atomic_apis
   :project: Zephyr
   :content-only:

浮点服务
***********************

浮点服务使线程能够利用开发板的浮点寄存器。（参考 :ref:`float_v2` ）

.. doxygengroup:: float_apis
   :project: Zephyr
   :content-only:

环形缓冲
************

缓冲缓冲使尺寸可变的数据项能够以先进先出的方式进行排队。（参考 :ref:`ring_buffers_v2` ）

.. doxygengroup:: ring_buffer_apis
   :project: Zephyr
   :content-only:
