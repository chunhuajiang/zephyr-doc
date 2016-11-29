.. _architecture_porting_guide:

架构移植指导
##########################

Zephyr 目前不支持某些 :abbr:`ISA(instruction set architecture)` 和 :abbr:`ABI (
Application Binary Interface)` 架构。如果您希望在这些架构上运行 Zephyr，需要
做一些架构相关的移植工作。

Zephyr 目前支持的 ISA 和 ABI 架构包括：

* x86_32 ISA with System V ABI
* x86_32 ISA with IAMCU ABI
* ARMv7-M ISA with Thumb2 instruction set and ARM Embedded ABI (aeabi)
* ARCv2 ISA

架构相关的移植主要集中在 nanokernel。这是因为 microkernel 在概念上只是一个用
 C 语言写的、运行在 nanokernel 之上的应用程序。在架构移植过程中，与 microkernel 
唯一相关的部分是系统时钟定时器驱动。

架构相关的移植可以划分为几个部分，其中一部分是必须的，另一些是可选的：

* **早期的启动过程**: 必须的。当 CPU 复位后，每种架构都需要做不同的处理。

* **中断和异常处理**: 必须的。每种架构以特定的方式处理异步和未请求事件。

* **线程上下文切换**: 必须的。 Zephyr 的上下文切换依赖于 ABI。不同的 ISA 
  需要保存不同的寄存器集合。

* **线程的创建和结束**: 必须的。线程的初始化帧依赖于 ABI 和架构。线程的终止
  也类似。

* **设备驱动程序**: 部分是必须的，部分是可选的。大多数情况下，系统的时钟定时器
  和中断控制器都是与架构绑定在一起的。

* **工具库**: 必须的。由于性能问题，内核的一些通用 API 依赖于架构相关的实现。

* **CPU 空转/电源管理**: 可选的。大多数架构都实现了让 CPU 睡眠的指令。

* **Fault 处理**: 可选的。 主要与架构相关的调试、处理线程致命错误相关。

* **链接脚本和工具链**: 必须的。 编译系统在链接镜像时，极有可能需要一些架构相关
  的细节。

早期的启动过程
*******************

早起的启动过程是为了让系统从复位状态切换到能运行 C 代码的状态。大多数情况下都只需要
很少的步骤，只有个别架构需要略多的处理。

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

Each architecture defines interrupt and exception handling differently.

When a device wants to signal the processor that there is some work to be done
on its behalf, it raises an interrupt. When a thread does an operation that is
not handled by the serial flow of the software itself, it raises an exception.
Both, interrupts and exceptions, pass control to a handler. The handler is
knowns as an :abbr:`ISR (Interrupt Service Routine)` in the case of
interrupts. Handler perform the work required the exception or the interrupt.
For interrupts, that work is device-specific. For exceptions, it depends on the
exception, but most often the core kernel itself is responsible for providing
the handler.

The kernel has to perform some work in addition to the work the handler itself
performs. For example:

* Prior to handing control to the handler:

  * Save the currently executing context.

* After getting control back from the handler:

  * Decide whether to perform a context switch.
  * When performing a context switch, restore the context being context
    switched in.

This work is conceptually the same across architectures, but the details are
completely different:

* The registers to save and restore.
* The processor instructions to perform the work.
* The numbering of the exceptions.
* etc.

It thus needs an architecture-specific implementation, called the
interrupt/exception stub.

Another issue is that the kernel defines the signature of ISRs as:

.. code-block:: C

    void (*isr)(void *parameter)

Architectures do not have a consistent or native way of handling parameters to
an ISR. As such there are two commonly used methods for handling the
parameter.

* Using some architecture defined mechanism, the parameter value is forced in
  the stub. This is commonly found in X86-based architectures.

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

Thread Context Switching
************************

Multi-threading is the basic purpose to have a kernel at all. Zephyr supports
two types of threads: preemptive tasks and cooperative fibers.

Two crucial concepts when writing an architecture port are the following:

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

Thread Creation and Termination
*******************************

To start a new thread, a stack frame must be constructed so that the context
switch can pop it the same way it would pop one from a thread that had been
context switched out. This is to be implemented in an architecture-specific
:code:`_new_thread` internal routine.

The thread entry point is also not to be called directly, i.e. it should not be
set as the :abbr:`PC (program counter)` for the new thread. Rather it must be
wrapped in :code:`_thread_entry`. This means that the PC in the stack
frame shall be set to :code:`_thread_entry`, and the thread entry point shall
be passed as the first parameter to :code:`_thread_entry`. The specifics of
this depend on the ABI.

The need for an architecture-specific thread termination implementation depends
on the architecture. There is a generic implementation, but it might not work
for a given architecture.

One reason that has been encountered for having an architecture-specific
implementation of thread termination is that aborting a thread might be
different if aborting because of a graceful exit or because of an exception.
This is the case for ARM Cortex-M, where the CPU has to be taken out of handler
mode if the thread triggered a fatal exception, but not if the thread
gracefully exits its entry point function.

This means implementing an architecture-specific version of
:c:func:`fiber_abort` and :code:`_TaskAbort`, and setting the two
Kconfig options :option:`CONFIG_ARCH_HAS_TASK_ABORT` and
:option:`CONFIG_ARCH_HAS_NANO_FIBER_ABORT` as needed for the
architecture (e.g. see :file:`arch/arm//core/cortex_m/Kconfig`).

Device Drivers
**************

The kernel requires very few hardware devices to function. In theory, the only
required device is the interrupt controller, since the kernel can run without a
system clock. In practice, to get access to most, if not all, of the sanity
check test suite, a system clock is needed as well. Since these two are usually
tied to the architecture, they are part of the architecture port.

Interrupt Controllers
=====================

There can be significant differences between the interrupt controllers and the
interrupt concepts across architectures.

For example, x86 has the concept of an :abbr:`IDT (Interrupt Descriptor Table)`
and different interrupt controllers. Although modern systems mostly
standardized on the :abbr:`APIC (Advanced Programmable Interrupt Controller)`,
some small Quark-based systems use the :abbr:`MVIC (Micro-controller Vectored
Interrupt Controller)`. Also, the position of an interrupt in the IDT
determines its priority.

On the other hand, the Cortex-M3/4 has the :abbr:`NVIC (Nested Vectored
Interrupt Controller)` as part of the architecture definition. There is no need
for an IDT-like table that is separate from the NVIC vector table. The position
in the table has nothing to do with priority of an IRQ: priorities are
programmable per-entry.

The ARCv2 has its interrupt unit as part of the architecture definition, which
is somewhat similar to the NVIC. However, where ARC defines interrupts has
having a one-to-one mapping between exception and interrupt numbers (i.e.
exception 1 is IRQ1, and device IRQs start at 16), ARM has IRQ0 being
equivalent to exception 16 (and weirdly enough, exception 1 can be seen as
IRQ-15).

All these differences mean that very little, if anything, can be shared between
architectures with regards to interrupt controllers.

System Clock
============

x86 has APIC timers and the HPET as part of its architecture definition. ARM
Cortex-M has the SYSTICK exception. Finally, ARCv2 has the timer0/1 device.

The system clock driver is divided between a nanokernel and a microkernel
implementations. All nanokernel timers and timeouts are supported in a
microkernel system, but the context in which they are handled is different. In
a nanokernel system, the timers are handled in the system clock ISR since there
is no other guaranteed context where to handle them. In a microkernel, time
advances in the kernel server fiber: the system timer ISR sends a microkernel
event to the kernel to signal the passage of time.

Tickless Idle
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

Utility Libraries
*****************

The kernel depends on a few functions that can be implemented with very few
instructions or in a lock-less manner in modern processors. Those are thus
expected to be implemented as part of an architecture port.

* Atomic operators.

  * If instructions do not exist for a give architecture, it is possible to
    create a generic version that wraps :c:func:`irq_lock` or :c:func:`irq_unlock`
    around non-atomic operations. It is trivial to implement, but does not currently exist.

* Find-least-significant-bit-set and find-most-significant-bit-set.

  * If instructions do not exist for a given architecture, it is always
    possible to implement these functions as generic C functions.

CPU Idling/Power Management
***************************

The kernel provides support for CPU power management with two functions:
:c:func:`nano_cpu_idle` and :c:func:`nano_cpu_atomic_idle`.

:c:func:`nano_cpu_idle` can be as simple as calling the power saving
instruction for the architecture with interrupts unlocked, for example :code:`hlt` on
x86, :code:`wfi` or :code:`wfe` on ARM, :code:`sleep` on ARC. This function can be called in a
loop within a context that does not care if it get interrupted or not by an interrupt
before going to sleep. There are basically two scenarios when it is correct to
use this function:

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

Fault Management
****************

Each architecture provides two fatal error handlers:

* :code:`_NanoFatalErrorHandler`, called by software for unrecoverable errors.
* :code:`_SysFatalErrorHandler`, which makes the decision on how to handle
  the thread where the error is generated, most likely by terminating it.

See the current architecture implementations for examples.

Toolchain and Linking
*********************

Toolchain support has to be added to the build system.

Some architecture-specific definitions are needed in :file:`toolchain/gcc.h`.
See what exists in that file for currently supported architectures.

Each architecture also needs its own linker script, even if most sections can
be derived from the linker scripts of other architectures. Some sections might
be specific to the new architecture, for example the SCB section on ARM and the
IDT section on x86.
