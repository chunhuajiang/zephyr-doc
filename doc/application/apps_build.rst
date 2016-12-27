.. _apps_build:

编译应用程序
####################

Zephyr 编译系统将应用程序的所有组件编译并链接为一个可在仿真硬件和真实硬件上运行的单一应用程序镜像。

.. contents:: Procedures
   :local:
   :depth: 1

编译应用程序
=======================

编译系统允许您使用应用程序已存在的配置轻松地编译应用程序。不过，如果有需要，您也可以使用不同的配置设置进行编译。

开始前
----------------

* 确保您已将所有应用程序相关的代码添加到应用程序目录，如  :ref:`apps_code_dev` 所述。确保每个源代码目录和子目录都有它自己的 :file:`Makefile` 。

* 确保您已按照 :ref:`apps_kernel_conf` 所述的方法为应用程序配置了内核。

* 确保为每个控制台终端都设置了 Zephyr 环境变量。参考 :ref:`apps_common_procedures` 。

步骤
-----

#. 进入应用程序目录 :file:`~/appDir` 。

#. 输入下面的目录编译应用程序的 :file:`zephyr.elf` 镜像，它会使用应用程序的 :file:`Makefile` 中所指定的板子典型配置设置。

   .. code-block:: console

       $ make

   如果有需要，您可以使用参数 :code:`CONF_FILE` 指定一个 :file:`.conf` 文件，并在其中给出编译应用程序时的配置。这些配置设置会覆盖应用程序的 :file:`.config` 文件或者默认的 :file:`.conf` 文件中的内容。例如：

   .. code-block:: console

       $ make CONF_FILE=prj.alternate.conf

   如果有需要，您可以使用参数 :code:`BOARD` 为其它类型的开发板编译应用程序，例如：

   .. code-block:: console

       $ make BOARD=arduino_101

   当编译应用程序是，可以同时指定参数 :code:`CONF_FILE` 和 :code:`BOARD` 。

重新编译应用程序
=========================

应用程序开发的过程通常是高速的。高频率地编译应用程序能减轻您调试的痛苦，因为应用程序总是会变得越来越复杂。当应用程序的源文件、Makefile 或者配置设置有任何主要改动时，重新编译和测试总是一个好的行为。

.. important::

    Zephyr 的编译系统只会编译可能对应用程序镜像造成影响的那部分。因此，重新编译应用程序总是比第一次编译快很多。

步骤
-----

#. 按照上面的 `Building an Application`_ 中指定的步骤。

从编译失败中恢复
===============================

有时候当一个或多个必须的文件编译失败后，编译系统可能不能再正确地编译应用程序。您可以按照下面的步骤强制编译系统重新编译整个应用程序：

步骤
-----

#. 进入应用程序目录 :file:`~/appDir`.

#. 输入如下命令，删除应用程序为指定开发板类型生成的文件（不包括 :file:`.config` ，因为它包含应用程序的当前配置信息）：

   .. code-block:: console

       $ make [BOARD=<type>] clean

   您也可以输入如下命令删除应用程序生成的包括 :file:`.config` 在内的所有文件：

   .. code-block:: console

       $ make pristine

#. 按照上面的 `Building an Application`_ 中所指定的步骤重新编译应用程序。
