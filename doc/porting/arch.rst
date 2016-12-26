.. _architecture_porting_guide:

架构移植指导
##########################

.. Hint::
   
   译注：这部分很多内容都过时了，因此并未翻译。

Zephyr 目前不支持某些 :abbr:`ISA(instruction set architecture)` 和 :abbr:`ABI (
Application Binary Interface)` 架构。如果您希望在这些架构上运行 Zephyr，需要
做一些架构相关的移植工作。

Zephyr 目前支持的 ISA 和 ABI 架构包括：

* x86_32 ISA with System V ABI
* x86_32 ISA with IAMCU ABI
* ARMv7-M ISA with Thumb2 instruction set and ARM Embedded ABI (aeabi)
* ARCv2 ISA

架构相关的移植主要集中在 nanokernel。这是因为 microkernel 在概念上只是一个用 C 语言写的、运行在 nanokernel 之上的应用程序。在架构移植过程中，与 microkernel 唯一相关的部分是系统时钟定时器驱动。

架构相关的移植可以划分为几个部分，其中一部分是必须的，另一些是可选的：

* **早期的启动过程**: 必须的。当 CPU 复位后，每种架构都需要做不同的处理。

* **中断和异常处理**: 必须的。每种架构以特定的方式处理异步和未请求事件。

* **线程上下文切换**: 必须的。 Zephyr 的上下文切换依赖于 ABI。不同的 ISA 需要保存不同的寄存器集合。

* **线程的创建和结束**: 必须的。线程的初始化帧依赖于 ABI 和架构。线程的终止也类似。

* **设备驱动程序**: 部分是必须的，部分是可选的。大多数情况下，系统的时钟定时器和中断控制器都是与架构绑定在一起的。

* **工具库**: 必须的。由于性能问题，内核的一些通用 API 依赖于架构相关的实现。

* **CPU 空转/电源管理**: 可选的。大多数架构都实现了让 CPU 睡眠的指令。

* **Fault 处理**: 可选的。 主要与架构相关的调试、处理线程致命错误相关。

* **链接脚本和工具链**: 必须的。 编译系统在链接镜像时，极有可能需要一些架构相关
  的细节。

早期的启动过程
*******************

早起的启动过程是为了让系统从复位状态切换到能运行 C 代码的状态。大多数情况下都只需要很少的步骤，只有个别架构需要略多的处理。

所有架构的通用步骤：

* 设置初始化栈。 
* 如果运行的是 :abbr:`XIP (eXecute-In-Place)` 内核，将初始化代码从 ROM 拷贝到 RAM。
* 如果没有使用 ELF 加载器，初始化 BSS 段。
* 跳转到 :code:`_Cstart()` 去初始化内核。

  * :code:`_Cstart()` 负责从系统启动时的虚拟上下文切换到后台/空转任务。

一些架构相关的步骤可能包括：

* 如果处于 x86_32 实模式，则需要切换到 32 位的保护模式。
* 设置 x86_32 的段寄存器，以处理 boot loader。
* 处理 Cortex-M3/4 的开发板相关的看门狗。
* 将 Cortex-M3/4 的栈由 MSP 切换到 PSP。

中断和异常处理
********************************

每种架构的中断和异常处理都是不同的。

当设备希望向处理器发送信号时，*它的内部需要完成一些额外的工作*，然后再发出一个中断。当线程需要执行一个不能由软件自身按照串行流程的方式处理的操作时，它会发出一个异常。中断和异常都会将控制权限传递给处理者。对于中断，这个处理者被叫做 :abbr:`ISR (Interrupt Service Routine)`。处理者执行中断或异常请求的工作。对于中断，这些工作是与设备相关的。对于异常，这些工作依赖于异常，但是大多数时候内核的核心都会自己提供处理者。

除处理者需要执行相关工作外，内核还必须执行一些额外的工作。

* 在将控制器交给处理者之前：

  * 保存当前的执行上下文。

* 从处理者收回控制器后：

  * 决定是否执行上下文切换。
  * 当需要执行上下文切换时，恢复被切换的上下文。

从概念上讲，所有的架构都是做这些工作，但是具体细节是不同的：

* 需要保存和恢复的寄存器。
* 执行相关工作的处理器指令。
* 异常数量。
* 等等。

因此，它的实现是架构相关的，叫做中断/异常桩。

另一个问题是内核将 ISR 的签名定义为：

.. code-block:: C

    void (*isr)(void *parameter)

架构没有处理传递给 ISR 的参数的一致性方法或者本地方法。处理这些参数一般有两种方法：

* 使用一些架构定义的机制，参数值被强迫在桩中。这种方法通常出现在基于 x86 的架构中。

* The parameters to the ISR are inserted and tracked via a separate table
  requiring the architecture to discover at runtime which interrupt is
  executing. A common interrupt handler demuxer is installed for all entries of
  the real interrupt vector table, which then fetches the device's ISR and
  parameter from the separate table. This approach is commonly used in the ARC
  and ARM architectures via the :option:`CONFIG_SW_ISR_TABLE` implementation.
  You can find examples of the stubs by looking at :code:`_interrupt_enter()` in
  x86, :code:`_IntExit()` in ARM, :code:`_isr_wrapper()` in ARM, or the full
  implementation description for ARC in :file:`arch/arc/core/isr_wrapper.S`.

Each architecture also has to implement primitives for interrupt control:

* locking interrupts: :c:func:`irq_lock`, :c:func:`irq_unlock`.
* registering interrupts: :c:func:`irq_connect`.
* programming the priority if possible :c:func:`irq_priority_set`.
* enabling/disabling interrupts: :c:func:`irq_enable`, :c:func:`irq_disable`.

.. note::

  :c:macro:`IRQ_CONNECT` is a macro that uses assembler and/or linker script
  tricks to connect interrupts at build time, saving boot time and text size.

The vector table should contain a handler for each interrupt and exception that
can possibly occur. The handler can be as simple as a spinning loop. However,
we strongly suggest that handlers at least print some debug information. The
information helps figuring out what went wrong when hitting an exception that
is a fault, like divide-by-zero or invalid memory access, or an interrupt that
is not expected (:dfn:`spurious interrupt`). See the ARM implementation in
:file:`arch/arm/core/fault.c` for an example.

线程的上下文切换
************************

使用多线程是使用内核的基本目的。Zephyr 支持两种类型的线程：抢占式线程和协作式线程。


当写架构相关的移植代码时，有两个关键性概念：

.. note::
  
  译注：这部分的内容已过时，故未翻译。

* Fibers run at a higher priority than tasks, and always preempt them.
* The nanokernel has knowledge of only one task at a time.

  * When running a nanokernel-only system, there is only one task.
  * When running a microkernel, the microkernel tells the nanokernel which
    task it should be aware of at a given moment.

.. note::

  When talking about "the task" in this document, it refers to the task the
  nanokernel is currently aware of.

A context switch can happen in several circumstances:

* When a thread executes a blocking operation, such as taking a semaphore that
  is currently unavailable.

* When a thread unblocks a thread of higher priority by releasing the object on
  which it was blocked.

* When an interrupt unblocks a thread of higher priority than the one currently
  executing.

* When a thread runs to completion.

* When a thread causes a fatal exception and is removed from the running
  threads. For example, referencing invalid memory,

Therefore, the context switching must thus be able to handle all these cases.

The microkernel handles conditions that cause task-to-task transitions. Recall
that the microkernel is architecture-agnostic. Thus, these transitions are of
no concern to an architecture port. One example of these is a task blocking on
a microkernel mutex object.

Mechanically, there is never any direct task-to-task context switching anyway.
A context switch from the running task to the kernel server fiber is always
involved when switching from one task to another.

So, the transitions of interest for an architecture port are:

* task-to-fiber
* fiber-to-task
* thread-to-ISR
* ISR-to-thread

There are two types of context switches: :dfn:`cooperative` and :dfn:`preemptive`.

* A *cooperative* context switch happens when a thread willfully gives the
  control to another thread. There are two cases where this happens

  * When a thread explicitly yields.
  * When a thread tries to take an object that is currently unavailable and is
    willing to wait until the object becomes available.

* A *preemptive* context switch happens either because an ISR or a
  task causes an operation that schedules a thread of higher priority than the
  one currently running, if the currently running thread is a task.
  An example of such an operation is releasing an object on which the thread
  of higher priority was waiting.

.. note::

  Since fibers are non-preemptible, control is not taken from them if one of
  them is the running thread.

A cooperative context switch is always done by having a thread call the
:code:`_Swap()` kernel internal symbol. When :code:`_Swap` is called, the
kernel logic knows that a context switch has to happen: :code:`_Swap` does not
check to see if a context switch must happen. Rather, :code:`_Swap` decides
what thread to context switch in. :code:`_Swap` is called by a very select set
of nanokernel functions, basically nanokernel objects (fifo, lifo, stack,
semaphore) primitives when the object being operated on is unavailable, and
some fiber/task yielding/sleeping primitives.

.. note::

  On x86, :code:`_Swap` is generic enough and the architecture flexible enough
  that :code:`_Swap` can be called when exiting an interrupt to provoke the
  context switch. This should not be taken as a rule, since neither the ARM
  Cortex-M or ARCv2 port do this.

Since :code:`_Swap` is cooperative, the caller-saved registers from the ABI are
already on the stack. There is no need to save them in the TCS.

A context switch can also be performed preemptively. This happens upon exiting
an ISR, in the kernel interrupt exit stub:

* :code:`_interrupt_enter` on x86 after the handler is called.
* :code:`_IntExit` on ARM.
* :code:`_firq_exit` and :code:`_rirq_exit` on ARCv2.

In this case, the context switch must only be invoked when the interrupted
thread was the task, not when it was a fiber, and only when the current
interrupt is not nested.

So, the decision logic to invoke the context switch when exiting an interrupt
is extremely simple

* If the interrupted thread is a fiber, do not invoke it.
* Else, if there is a fiber ready, invoke it.
* Else, do not invoke it.

This is simple, but crucial: if this is not implemented correctly, the kernel,
specifically the microkernel, will not function as intended and will experience
bizarre crashes, mostly due to stack corruption.

线程的创建和终止
*******************************

要开始一个新线程，必须构建一个栈帧，然后在进行上下文切换时弹出它。对于一个已经切换出去的线程，它也需要以类似的方式弹出栈帧。这一点是在架构相关的内部函数 :code:`_new_thread` 中实现的。

线程的入口点不能被直接调用，也就是说，不能直接为新线程设置 :abbr:`PC (程序计数器)`。相反，它必须封装在 :code:`_thread_entry` 内。这意味着栈帧中的 PC 应该被设置到 :code:`_thread_entry` 中，且线程入口点应该作为 :code:`_thread_entry` 的第一个参数。它的具体细节依赖于 ABI。

线程的终止是架构相关的，因此它的实现也依赖于架构。我们给出了一个通用实现，但是它可能在您的架构下不能正常工作。

由于线程可能是优雅地终止，也可能由于异常而终止，所以将线程终止实现为架构相关的方案是合理的。对于 Cortex-M 架构，当线程触发了致命错误时，它的 CPU 必须从进入处理者模式；但是当线程自己从入口函数优雅地推出时，则无需进入处理者模式。

因此，我们可以根据架构的需要（:file:`arch/arm//core/cortex_m/Kconfig`）设置 Kconfig 选项 :option:`CONFIG_ARCH_HAS_TASK_ABORT` 和 :option:`CONFIG_ARCH_HAS_NANO_FIBER_ABORT`，并实现架构相关的 :c:func:`fiber_abort` 和 :code:`_TaskAbort`。

设备驱动程序
**************

内核只需要少量的硬件设备就能正常工作。理论上，唯一需要实现的设备是中断控制器，因为内核在无系统时钟下一可以运行。在实际中，为了能够访问大多数健全检测测试套件，通常也需要系统时钟。由于二者通常都是与架构绑定在一起的，所以它们也属于架构相关移植的一部分。

中断控制器
=====================

不同的架构在中断控制器和中断的概念之间存在巨大的差异。

例如，x86 架构有 :abbr:`IDT (中断描述符表)` 和中断控制器的概念，且某些基于 Quark 的系统使用 :abbr:`MVIC (微控制器向量中断控制器)`。此外，中断在 IDT 中的位置决定了它们的优先级。

另一方面，Cortex-M3/M4 在架构中有 :abbr:`NVIC (嵌套向量中断控制器)` 的概念，因此除 NVIC 向量表外不再需要单独的类似于 IDT 的表格。中断在向量表中的位置与 IRQ 的优先级无关：每个中断的优先级是可编程的。

ARCv2 有它自己的控制单元，它在某种程度上与 NVIC 类似。ARC 定义的中断在异常号和中断号（例如 1 号异常是 IRQ1，设备的 IRQ 从 16 开始）之间存在一对一的映射，而 ARM 的 IRC0 等同于 16 号异常（且不可思议的是，1 号异常可以被看做 IRQ-15）。

所有的这些意味着，对于控制控制器来说，在不同架构间只有很少的一部分代码能够共享。

系统时钟
============

x86 架构有 APIC 定时器和 HPET。ARM Cortex-M 有 SYSTIKC 异常，ARCv2 有 0/1 定时器设备。

..Hint::
  
   译注：这部分内容已过时，故未翻译。

The system clock driver is divided between a nanokernel and a microkernel
implementations. All nanokernel timers and timeouts are supported in a
microkernel system, but the context in which they are handled is different. In
a nanokernel system, the timers are handled in the system clock ISR since there
is no other guaranteed context where to handle them. In a microkernel, time
advances in the kernel server fiber: the system timer ISR sends a microkernel
event to the kernel to signal the passage of time.

无滴答空转
-------------

The kernel has support for tickless idle. Tickless idle is the concept where no
system clock timer interrupt is to be delivered to the CPU when the kernel is
about to go idle and the closest timeout expiry is passed a certain threshold.
When this condition happens, the system clock is reprogrammed far in the future
instead of for a periodic tick. For this to work, the system clock timer driver
must support it.

Tickless idle is optional but strongly recommended to achieve low-power
consumption.

The microkernel has built-in support for going into tickless idle. However, in
nanokernel-only systems, part of the support has to be built in the
architecture (:c:func:`nano_cpu_idle` and :c:func:`nano_cpu_atomic_idle`).

The interrupt entry stub (:code:`_interrupt_enter`, :code:`_isr_wrapper`) needs
to be adapted to handle exiting tickless idle. See examples in the code for
existing architectures.

Console Over Serial Line
========================

There is one other device that is almost a requirement for an architecture
port, since it is so useful for debugging. It is a simple polling, output-only,
serial port driver on which to send the console (:code:`printk`,
:code:`printf`) output.

It is not required, and a RAM console (:option:`CONFIG_RAM_CONSOLE`)
can be used to send all output to a circular buffer that can be read
by a debugger instead.

工具库
*****************

内核依赖于少量的特殊函数，这些函数由非常少的指令实现，或者以现代处理去无锁的方式实现。这也是属于架构相关的移植的一部分。

* 原子操作。

  * If instructions do not exist for a give architecture, it is possible to
    create a generic version that wraps :c:func:`irq_lock` or :c:func:`irq_unlock`
    around non-atomic operations. It is trivial to implement, but does not currently exist.

* Find-least-significant-bit-set and find-most-significant-bit-set.

  * If instructions do not exist for a given architecture, it is always
    possible to implement these functions as generic C functions.

CPU 空转/电源管理
***************************

内核对 CPU 电源管理提供了两个函数：:c:func:`nano_cpu_idle` 和 :c:func:`nano_cpu_atomic_idle`。

:c:func:`nano_cpu_idle` 只是简单地在调用架构相关的指令（以及保持中断未被锁定），例如 x86 的 :code:`hlt`、ARM 的 :code:`wfe`、ARC 的:code:`sleep`。在一个不关心是否会被中断的循环上下文中可以调用该函数。正确使用它的两种基本场景：

.. Hint:: 

   译注：已过时，未翻译。

* In a nanokernel system, in the task when the task is not used for
  doing real work after initialization, i.e. it is sitting in a loop doing
  nothing for the duration of the application.

* In a microkernel system, in the idle task.

:c:func:`nano_cpu_atomic_idle`, on the other hand, must be able to atomically
re-enable interrupts and invoke the power saving instruction. It can thus be
used in real application code. For example, it is used in the implementation of
nanokernel objects when the task is polling an object, waiting for the object
to be available. Since the task is the lowest-priority thread, and it cannot
block, the only thing to do for the CPU is to sleep and wait for an interrupt
to release the object.

Both functions must exist for a given architecture. However, the implementation
can be simply the following steps, if desired:

#. unlock interrupts
#. NOP

However, a real implementation is strongly recommended.

错误管理
****************

每种架构都提供了两个致命错误处理者：

* :code:`_NanoFatalErrorHandler`，由软件和不可恢复的错误调用。
* :code:`_SysFatalErrorHandler`, 用于决定如何处理产生错误的线程，通常是终止它。

相关例子请参考当前架构的实现。

工具链和链接
*********************

工具链的支持已经被添加到编译系统中了。

:file:`toolchain/gcc.h` 中需要一些架构相关的定义。请参考该文件查看所支持的架构存在哪些定义。

每种架构都需要它自己的链接脚本，但是大多数段可以从其它结构的链接脚本中推断出来。在不同的架构中可能需要指定不同的段，例如 AMR 架构需要指定 SCB 段，x86 架构需哟啊指定 IDT 段。
