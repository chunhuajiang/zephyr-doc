.. _lifecycle_v2:

生命周期
#########

:dfn:`线程` 是一个用于处理由于太复杂或耗时太长而不便于在 ISR 内完成的工作的内核对象。

.. contents::
    :local:
    :depth: 2

概念
********

应用程序可以定义任意数量的线程，且可以使用线程创建时分配给该线程的 :dfn:`线程标识符` 来引用该线程。

线程的注关键属性包括：

* **栈区域**：一段用于线程控制块（:c:type:`struct k_thread`）和线程栈的内存区域。
  栈空间的 **大小** 可以被裁剪，以适应线程处理的实际需求。

* **入口点函数**：线程启动时调用的函数。该函数最多能接收 3 个参数。

* **调度优先级**：指示内核的调度器如何给该线程分配 CPU 时间。（参考 :ref:`scheduling_v2`。）

* **线程选项**：允许内核在特定场景中对该线程做某种特殊处理。（参考 :ref:`thread_options_v2`。）

* **启动时延**： 指定线程在启动前需要等待的时间。

线程的创建
===============

线程必须先创建、再使用。创建线程时，内核将初始化线程栈区域的控制块区域以及栈的尾部。栈区域的其它部分通常都是未初始化的。

如果指定的启动时延是 :c:macro:`K_NO_WAIT`，内核将立即启动线程。您也可以指定一个超时时间，让内核延迟启动该线程。例如，让线程需要使用的设备就绪后再启动线程。

如果延迟启动的线程还未启动，内核可以取消该线程。如果线程已经启动了，则内核在尝试取消它时不会有如何效果。如果延迟启动的线程被成功地取消了，它必须被再次创建后才能再次使用。

线程的正常结束
==================

线程一旦启动，它通常会一直运行下去。不过，线程也可以从它的入口点函数中返回，从而同步结束执行。这种结束方式叫做 **正常结束（terminaltion）**。

正常结束的线程需要在返回前释放它所拥有的共享资源（例如互斥量、动态分配的内存）。内核 *不会* 自动回收这些资源。

.. note::
    当前内核不会做任何补偿。应用程序可以重新创建正常结束的线程。

线程的异常终止
===============

线程可以通过**异常终止 （aborting）**异步结束其执行。如果线程触发了一个致命错误（例如引用了空指针），内核将自动终止该线程。

其它线程（或线程自己）可以调用 :cpp:func:`k_thread_abort()` 终止一个线程。不过，更优雅的做法是向线程发送一个信号，让该线程自己结束执行。

线程终止时，内核不会自动回收该线程拥有的共享资源。

.. note::
    当前内核不会做任何补偿。应用程序可以重新创建异常终止的线程。

线程的挂起
=================

如果一个线程被挂起，它将在一段不确定的时间内暂停执行。函数 :cpp:func:`k_thread_suspend()` 可以用于挂起包括调用线程在内的所有线程。对已经挂起的线程再次挂起时不会产生任何效果。

线程一旦被挂起，它将一直不能被调度，除非另一个线程调用 :cpp:func:`k_thread_resume()` 取消挂起。

.. note::
   线程可以使用 :cpp:func:`k_sleep()` 睡眠一段指定的时间。不过，这与挂起不同，睡眠线程在睡眠时间完成后会自动运行。

.. _thread_options_v2:

线程的选项
==============

内核支持一系列 :dfn:`线程选项`，以允许线程在特殊情况下被特殊对待。这些与线程关联的选项在线程创建时就被指定了。

不需要任何线程选项的线程的选项值是零。如果线程需要选项，您可以通过选项名指定。如果需要多个选项，使用符号 :literal:`|` 作为分隔符。（即按位或操作符）。

支持如下选项：

:c:macro:`K_ESSENTIAL`
    该选项将线程标记为 :dfn:`必须线程`，表示当该线程正常结束或异常终止时，内核将认为产生了一个致命的系统错误。
    
    默认情况下，一般线程都不是必须线程。

:c:macro:`K_FP_REGS` and :c:macro:`K_SSE_REGS`
    这两个选项是 x86 相关的选项，分别表示线程使用 CPU 的浮点寄存器和 SSE 寄存器，指示内核在调度线程进行时需要采取额外的步骤来保存/恢复这些寄存器的上下文。（更多信息请参考 :ref:`float_v2`）。
    
    默认情况下，内核在调度线程时不会保存/恢复这些寄存器的上下文。

实现
**************

创建一个线程
=================

您可以通过定义线程的栈区域并调用 :cpp:func:`k_thread_spawn()` 创建一个线程。栈区域是一个由字节构成的数组，且其大小必须等于 :c:macro:`K_THREAD_SIZEOF` 加上线程栈大小之和。栈区域必须使用属性 :c:macro:`__stack` 进行定义，以确保被正确对齐。


创建线程的函数会返回该线程的标识符（ID），您可以使用该标识符来引用该线程。

下面的代码创建了一个立即启动的线程。

.. code-block:: c

    #define MY_STACK_SIZE 500
    #define MY_PRIORITY 5

    extern void my_entry_point(void *, void *, void *);

    char __noinit __stack my_stack_area[MY_STACK_SIZE];

    k_tid_t my_tid = k_thread_spawn(my_stack_area, MY_STACK_SIZE,
                                    my_entry_point, NULL, NULL, NULL,
                                    MY_PRIORITY, 0, K_NO_WAIT);

您也可以调用 :c:macro:`K_THREAD_DEFINE` 在编译时创建线程。需要注意的是，这个宏自动定义了一个栈区域以及一个线程标识符变量。

下面的代码与上面的代码具有系统的效果。

.. code-block:: c

    #define MY_STACK_SIZE 500
    #define MY_PRIORITY 5

    extern void my_entry_point(void *, void *, void *);

    K_THREAD_DEFINE(my_tid, MY_STACK_SIZE,
                    my_entry_point, NULL, NULL, NULL,
                    MY_PRIORITY, 0, K_NO_WAIT);

结束一个线程
====================

线程可以从它的入口点函数中返回，以正常结束其运行。

下面的代码描述了线程正常结束的方法。

.. code-block:: c

    void my_entry_point(int unused1, int unused2, int unused3)
    {
        while (1) {
            ...
	    if (<some condition>) {
	        return; /* thread terminates from mid-entry point function */
	    }
	    ...
        }

        /* thread terminates at end of entry point function */
    }


建议的用法
**************

建议使用线程来处理不便于在终端服务例程中处理的任务。

建议为每个在逻辑上有差异的任务创建一个独立的线程，让它们并行执行。

配置选项
*********************

相关的配置选项：

* 无。 

API
****

下面的 API 是在 :file:`kernel.h` 中提供的：

* :c:macro:`K_THREAD_DEFINE`
* :cpp:func:`k_thread_spawn()`
* :cpp:func:`k_thread_cancel()`
* :cpp:func:`k_thread_abort()`
* :cpp:func:`k_thread_suspend()`
* :cpp:func:`k_thread_resume()`
