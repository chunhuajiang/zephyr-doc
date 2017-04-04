.. _dining-philosophers-sample:

哲学家进餐
###################

概述
********

该示例为哲学家进餐问题（一个经典的多线程同步问题）提供了一个解决方案。这个特殊的实现演示了具有不同优先级的多个抢占式线程和协作式线程的使用方法，以及动态互斥量、线程睡眠的使用方法。

哲学家总是先尝试拿取编号最小的叉子（先拿 f1 再拿 f2）。用完后，它会按照相反的顺序放回叉子（先放 f2 再放 f1）。如果他拿到两个叉子，他就会*进餐*；否则，他会*思考*。如果哲学家处于饥饿状态但是没有叉子，则他处于*挨饿*状态；如果他拿有一根叉子正在等待另一根叉子，则处于*等待另一根叉子*的状态。

每个哲学家都会在*进餐*与*思考*两个状态间随机交替。

本示例既可以运行在仅协作式模式下，也可以运行在仅抢占式模式下。为此，您需要在 prj.conf 中设置 CONFIG_NUM_COOP_PRIORITIES 和 CONFIG_NUM_PREEMPT_PRIORITIES 的值：

仅抢占式：

  CONFIG_NUM_PREEMPT_PRIORITIES 6
  CONFIG_NUM_COOP_PRIORITIES 0

仅协作式:

  CONFIG_NUM_PREEMPT_PRIORITIES 0
  CONFIG_NUM_COOP_PRIORITIES 6

在这两种情形下，哲学家线程的优先级是 0 到 5（仅抢占式）和 -7 到 -1（仅协作式）。

编译和运行
********************

该示例于会向控制台打印消息。您可以按照下面的方法编译它，并在 QEMU 中运行它：

.. code-block:: console

   $ cd samples/philosophers
   $ make run

示例的输出
=============

.. code-block:: console

   Philosopher 0 [P: 3]  HOLDING ONE FORK
   Philosopher 1 [P: 2]  HOLDING ONE FORK
   Philosopher 2 [P: 1]  EATING  [ 1900 ms ]
   Philosopher 3 [P: 0]  THINKING [ 2500 ms ]
   Philosopher 4 [C:-1]  THINKING [ 2200 ms ]
   Philosopher 5 [C:-2]  THINKING [ 1700 ms ]


