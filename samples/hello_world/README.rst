.. _hello_world:

Hello World
###########

概述
********
Hello World 示例非常简单，它可以运行在任何所支持的开发板上面，用于向控制台打印“Hello World”消息。该应用程序可以被编译成：

* 单线程模式
* 多线程模式

编译和运行
********************

该示例于向控制台打印“Hello World”消息。您可以按照下面的方法编译它，并在 QEMU 中运行它：

.. code-block:: console

   $ cd samples/hello_world
   $ make run


如果要编译成单线程版本，需要使用所提供的另一个配置文件：:file:`prj_single.conf`:

.. code-block:: console

   $ make CONF_FILE=prj_single.conf run

示例的输出
=============

.. code-block:: console

    Hello World! x86
