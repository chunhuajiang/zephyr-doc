.. _synchronization_sample:

同步
######################

概述
********

这个简单的应用程序用于演示内核的基本功能。两个线程（A 和 B）轮流向控制台打印问候消息，在程序内部使用睡眠请求和信号量来控制消息的产生速率。这个示例说明内核调度、通信和时序都正确运行。

编译和运行
********************

该示例会向控制台打印消息。您可以按照下面的方法编译它，并在 QEMU 中运行它：

.. code-block:: console

   $ cd samples/synchronization
   $ make run

示例的输出
=============

.. code-block:: console

   threadA: Hello World!
   threadB: Hello World!
   threadA: Hello World!
   threadB: Hello World!
   threadA: Hello World!
   threadB: Hello World!
   threadA: Hello World!
   threadB: Hello World!
   threadA: Hello World!
   threadB: Hello World!

   <repeats endlessly>
