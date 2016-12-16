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

定时器的状态值可以在任意时间直接读取，以确定自上一次读取该状态值，定时器经历了多少个期满。   
读取定时器状态值的行为将清零状态值。   
定时器期满之前的剩余时间也是可读的，若值为0则表示该定时器已经停止。

某个线程可能会通过与定时器 **同步** 的方法来间接读取定时器的状态值。这将阻塞该线程直至该定时器的状态值为一个非零值（指示该定时器至少发生过期满）或该定时器被终止；如果改定时器的状态值已经是一个非零值或该定时器已经被终止，则该线程则继续运行而不再等待。同步操作将返回定时器的状态值并重置状态值为0。

.. note::
    因为在读取状态值（直接或间接）时将会改变其值，所以只能有一个用户可以检查指定定时器的状态值。类似的，在同一时刻只能有一个线程可以同步指定的定时器。因为中断服务程序不允许被阻塞，所以中断服务程序不允许同步定时器。

定时器的局限性
=================

因为定时器是基于系统时钟，所以在使用一个定时器时指定的延时时间都是 **最小** 值。
(详见 :ref:`clock_limitations`.)

实现
**************

定义一个定时器
================

通过使用类型为 :c:type:`struct k_timer` 的变量来定义一个定时器。
该定时器随后必须通过调用 :cpp:func:`k_timer_init()` 来初始化。

如下的代码定义并初始化了一个定时器：

.. code-block:: c

    struct k_timer my_timer;
    extern void my_expiry_function(struct k_timer *timer_id);

    k_timer_init(&my_timer, my_expiry_function, NULL);

Alternatively, a timer can be defined and initialized at compile time
by calling :c:macro:`K_TIMER_DEFINE`.

The following code has the same effect as the code segment above.

.. code-block:: c

    K_TIMER_DEFINE(my_timer, my_expiry_function, NULL);

使用定时器的期满函数
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

读取定时器状态值
====================

如下的代码直接读取了一个定时器的状态值，以确定该定时器是否期满。

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

使用定时器状态值同步
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

配置选项
*********************

相关的配置选项:

* 无。

APIs
****

:file:`kernel.h`:文件提供如下的定时器API：

* :c:macro:`K_TIMER_DEFINE`
* :cpp:func:`k_timer_init()`
* :cpp:func:`k_timer_start()`
* :cpp:func:`k_timer_stop()`
* :cpp:func:`k_timer_status_get()`
* :cpp:func:`k_timer_status_sync()`
* :cpp:func:`k_timer_remaining_get()`
