.. _timers_v2:

定时器
######

:dfn:`定时器（Timer）` 是一个使用内核系统时钟来计时的内核对象。当一个定时器指定的时间计时结束，它将执行一个应用层面已定义的行为，或简单地记录下这个“期满”事件，并等待应用层读取该状态。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的定时器，每个定时使用各自独立的内存地址资源。

每个定时器有以下关键属性：:

* :dfn:`时限（Duration）` 是指从启动到定时器第一次期满之间的时间间隔，单位为毫秒。该值必须大于0。

* :dfn:`周期（Period）` 是指在定时器第一次期满之后，后续每次期满之间的时间间隔，单位为毫秒。该值不能为负数，若该值为0，则该定时器为一次性计时，并会在单次期满后停止工作。

* :dfn:`期满函数（Expiry function）` 是在定时器每次期满时所执行的函数，该函数由系统时钟中断处理函数来执行。若在期满时无函数需要执行，则该期满函数需要指定为:c:macro:`NULL` 。

* :dfn:`终止函数（Stop function）` 是在定时器运行期间提前终止时所执行的函数。该函数由终止定时器的线程来执行。若在提前终止时无函数需要执行，则该终止函数需要指定为:c:macro:`NULL` 。

* :dfn:`状态值（status）` 指示了自最后一次读取该状态值后，定时器经历了多少次期满。 

定时器在使用前必须先初始化。初始化时将设置期满函数和终止函数，清零定时器状态值，并设置定时器为 **停止** 状态。

定时器将在指定时限和周期后 **启动**。在定时器状态值清零后，定时器进入 **运行** 状态并开始计时。

当一个运行中的定时器发生期满时：其状态值将自增，并执行期满函数（若已设置期满函数）。若某线程正在等待该定时器计时结束，该线程将不再被阻塞。如果定时器的周期为0，则此时定期进入停止状态；否则定时器将重启一个新的与周期时间相等的时限时间。

如果有需要，运行中的定时器可以在中途被终止，此时：定时器的状态值将保持不变，然后定时器进入停止状态并执行终止函数（若已设置中值函数）。若某线程正在等待该定时器计时结束，该线程将不再被阻塞。   
尝试终止一个非运行的定时器是允许的，但这不产生任何效果，因为其已经停止了。

如果有需要，运行中的定时器可以在中途被重启，此时：定时器的状态值复位为0，然后定时器以调用者指定的时限和周期继续运行。若某线程正在等待该定时器计时结束，该线程将继续等待。

定时器的状态值可以在任意时间直接读取，以确定自上一次读取该状态值，定时器经历了多少个期满。读取定时器状态值的行为将清零状态值。
A timer's status can be read directly at any time to determine how many times
the timer has expired since its status was last read.
Reading a timer's status resets its value to zero.
The amount of time remaining before the timer expires can also be read;
a value of zero indicates that the timer is stopped.

A thread may read a timer's status indirectly by **synchronizing**
with the timer. This blocks the thread until the timer's status is non-zero
(indicating that it has expired at least once) or the timer is stopped;
if the timer status is already non-zero or the timer is already stopped
the thread continues without waiting. The synchronization operation
returns the timer's status and resets it to zero.

.. note::
    Only a single user should examine the status of any given timer,
    since reading the status (directly or indirectly) changes its value.
    Similarly, only a single thread at a time should synchronize
    with a given timer. ISRs are not permitted to synchronize with timers,
    since ISRs are not allowed to block.

Timer Limitations
=================

Since timers are based on the system clock, the delay values specified
when using a timer are **minimum** values.
(See :ref:`clock_limitations`.)

实现
**************

定义一个定时器
================

A timer is defined using a variable of type :c:type:`struct k_timer`.
It must then be initialized by calling :cpp:func:`k_timer_init()`.

The following code defines and initializes a timer.

.. code-block:: c

    struct k_timer my_timer;
    extern void my_expiry_function(struct k_timer *timer_id);

    k_timer_init(&my_timer, my_expiry_function, NULL);

Alternatively, a timer can be defined and initialized at compile time
by calling :c:macro:`K_TIMER_DEFINE`.

The following code has the same effect as the code segment above.

.. code-block:: c

    K_TIMER_DEFINE(my_timer, my_expiry_function, NULL);

使用定时器的“期满函数”Using a Timer Expiry Function
=============================

The following code uses a timer to perform a non-trivial action on a periodic
basis. Since the required work cannot be done at interrupt level,
the timer's expiry function submits a work item to the
:ref:`system workqueue <workqueues_v2>`, whose thread performs the work.

.. code-block:: c

    void my_work_handler(struct k_work *work)
    {
        /* do the processing that needs to be done periodically */
        ...
    }

    struct k_work my_work = K_WORK_INITIALIZER(my_work_handler);

    void my_timer_handler(struct k_timer *dummy)
    {
        k_work_submit(&my_work);
    }

    K_TIMER_DEFINE(my_timer, my_timer_handler, NULL);

    ...

    /* start periodic timer that expires once every second */
    k_timer_start(&my_timer, K_SECONDS(1), K_SECONDS(1));

Reading Timer Status
====================

The following code reads a timer's status directly to determine
if the timer has expired on not.

.. code-block:: c

    K_TIMER_DEFINE(my_status_timer, NULL, NULL);

    ...

    /* start one shot timer that expires after 200 ms */
    k_timer_start(&my_status_timer, K_MSEC(200), 0);

    /* do work */
    ...

    /* check timer status */
    if (k_timer_status_get(&my_status_timer) > 0) {
        /* timer has expired */
    } else if (k_timer_remaining_get(&my_status_timer) == 0) {
        /* timer was stopped (by someone else) before expiring */
    } else {
        /* timer is still running */
    }

Using Timer Status Synchronization
==================================

The following code performs timer status synchronization to allow a thread
to do useful work while ensuring that a pair of protocol operations
are separated by the specified time interval.

.. code-block:: c

    K_TIMER_DEFINE(my_sync_timer, NULL, NULL);

    ...

    /* do first protocol operation */
    ...

    /* start one shot timer that expires after 500 ms */
    k_timer_start(&my_sync_timer, K_MSEC(500), 0);

    /* do other work */
    ...

    /* ensure timer has expired (waiting for expiry, if necessary) */
    k_timer_status_sync(&my_sync_timer);

    /* do second protocol operation */
    ...

.. note::
    If the thread had no other work to do it could simply sleep
    between the two protocol operations, without using a timer.

建议的用法
**************

Use a timer to initiate an asynchronous operation after a specified
amount of time.

Use a timer to determine whether or not a specified amount of time
has elapsed.

Use a timer to perform other work while carrying out operations
involving time limits.

.. note::
   If a thread has no other work to perform while waiting for time to pass
   it should call :cpp:func:`k_sleep()`.
   If a thread needs to measure the time required to perform an operation
   it can read the :ref:`system clock or the hardware clock <clocks_v2>`
   directly, rather than using a timer.

Configuration Options
*********************

Related configuration options:

* None.

APIs
****

The following timer APIs are provided by :file:`kernel.h`:

* :c:macro:`K_TIMER_DEFINE`
* :cpp:func:`k_timer_init()`
* :cpp:func:`k_timer_start()`
* :cpp:func:`k_timer_stop()`
* :cpp:func:`k_timer_status_get()`
* :cpp:func:`k_timer_status_sync()`
* :cpp:func:`k_timer_remaining_get()`
