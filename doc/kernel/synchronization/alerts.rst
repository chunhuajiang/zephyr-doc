.. _alerts_v2:

告警
######

:dfn:`告警（alert）` 是一个内核对象，当用户感兴趣的条件发生时，它允许应用程序执行一个异步信号。

.. contents::
    :local:
    :depth: 2

概念
********


可以定义任意数量的告警。每个告警通过其内存地址进行引用。

告警的关键属性如下：

* **告警处理者**：用于指明当捕捉到告警信号时应采取的动作。这个动作可能会指示系统工作队列去执行一个处理函数，将告警标记为挂起，以使其随后能被线程处理或忽略。

* **挂起计数**：记录被挂起的、未被接收的告警数量。

* **计数界限**：挂起计数的最大值。

告警必须先初始化再使用。初始化时会建立一个告警处理者，并将挂机计数设为零。

告警的生命周期
===============

当某个感兴趣的但又不能被检测者处理的条件发生时，ISR 或者线程可以 **发送** 告警信号。

每次有告警被发出时，内核都会检查它的告警处理函数，以决定采取何种动作。

* :c:macro:`K_ALERT_IGNORE` 将导致告警被忽略。

* :c:macro:`K_ALERT_DEFAULT` 将导致挂起的告警计数递增（除非计数已达上限）。

* 其它任何值都会被认为是一个告警处理函数的地址，并会被系统工作队列线程调用。如果该函数返回零，则认为该信号已经被消费；否则，挂起的告警计数递增（除非计数已达上限）。

  内核假设，每次告警被发送时，告警处理函数会被执行一次。（即使在连续的时间内告警被多次发送）。

内核可以 **接收** 告警而接受一个挂起的告警。如果当前的挂起计数是零，线程可以等待该告警被挂起。多个线程可以同时等待一个挂起告警；当告警被挂起时，它会被优先级最高的、等待时间最久的线程所接受。

.. note::
   
    线程在同一个时刻只能处理一个挂起告警。线程在一个操作中不能接收多个挂起告警。

与 Unix 风格的信号的比较
================================

Zephyr 的告警在某种程度上类似于 Unix 风格的信号，但是也有一些显著的区别，最主要包括：

* Zephyr 告警不能被锁定；它总是立即被传递给告警处理者。

* Zephyr 告警被传递给告警处理者 *后* 会处于挂起状态，直到告警处理函数消费了该告警。

* Zephyr 没有预定义的告警或行为。所有的告警都是由应用程序定义的，其默认行为是挂起告警。

实现
**************

定义告警
=================

使用类型为 :c:type:`struct k_alert` 的变量可以定义告警。告警在被定义后必须使用函数 :cpp:func:`k_alert_init()` 进行初始化。

下面的代码定义并初始化了一个告警。该告警在开始忽略新的挂起告警前，最多能够允许 10 个未接收的告警信号被挂起。

.. code-block:: c

    extern int my_alert_handler(struct k_alert *alert);

    struct k_alert my_alert;

    k_alert_init(&my_alert, my_alert_handler, 10);

也可以使用宏 :c:macro:`K_ALERT_DEFINE` 在编译时定义并初始化一个告警。

下面的代码与上面的代码段具有系统的效果。

.. code-block:: c

    extern int my_alert_handler(struct k_alert *alert);

    K_ALERT_DEFINE(my_alert, my_alert_handler, 10);

发出告警
==================

函数 :cpp:func:`k_alert_send()` 可用于发出告警。

下面的代码展示了当有新的按键发生时 ISR 是如何发出告警信号的。

.. code-block:: c

    extern int my_alert_handler(struct k_alert *alert);

    K_ALERT_DEFINE(my_alert, my_alert_handler);

    void keypress_interrupt_handler(void *arg)
    {
        ...
        k_alert_send(&my_alert);
        ...
    }

处理告警
=================

当接收到的告警信号不能被忽略或者理解挂起时，内核会使用告警处理函数。告警处理函数的格式如下：


.. code-block:: c

    int <function_name>(struct k_alert *alert)
    {
        /* catch the alert signal; return zero if the signal is consumed, */
        /* or non-zero to let the alert pend                              */
        ...
    }

下面的代码描述了当 ISR 检测到按键被按下时的告警处理函数。

.. code-block:: c

    int my_alert_handler(struct k_alert *alert_id_is_unused)
    {
        /* determine what key was pressed */
        char c = get_keypress();

        /* do complex processing of the keystroke */
	...

        /* signalled alert has been consumed */
        return 0;
    }

接受告警
==================


函数 :cpp:func:`k_alert_recv()` 可用于让线程接受一个挂起的告警。


下面的代码是对上一节的功能的另一种实现形式。它使用一个专用的线程去做复杂的按键处理（否则会独占系统工作队列）。告警处理函数只用于过滤未知的按键告警，这样可以使专用线程去唤醒并处理已知按键的告警。

.. code-block:: c

    int my_alert_handler(struct k_alert *alert_id_is_unused)
    {
        /* determine what key was pressed */
        char c = get_keypress();

        /* signal thread only if key pressed was a digit */
        if ((c >= '0') && (c <= '9')) {
            /* save key press information */
            ...
            /* signalled alert should be pended */
            return 1;
        } else {
            /* signalled alert has been consumed */
            return 0;
        }
    }

    void keypress_thread(void *unused1, void *unused2, void *unused3)
    {
        /* consume numeric key presses */
        while (1) {

            /* wait for a key press alert to pend */
            k_alert_recv(&my_alert, K_FOREVER);

            /* process saved key press, which must be a digit */
            ...
        }
    }

建议的用法
**************

使用告警将 ISR 中中断相关的工作推迟到线程中，这样可以最简化 ISR 的处理工作，从而减小了中断被锁定的时间。

可以让内核的系统工作队列去处理告警，而不需要应用程序线程去处理。

可以让内核的系统工作队列去预处理告警，抢在应用程序线程处理之前。

配置选项
*********************

相关的配置选项：

* 无。

API
****


头文件 :file:`kernel.h` 提供了如下的告警 API：

* :c:macro:`K_ALERT_DEFINE`
* :cpp:func:`k_alert_init()`
* :cpp:func:`k_alert_send()`
* :cpp:func:`k_alert_recv()`
