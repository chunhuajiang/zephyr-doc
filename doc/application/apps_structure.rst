.. _apps_structure:

创建应用程序目录
###############################

每个应用程序都位于一个由开发者创建的唯一命名的应用程序目录下。应用程序开发者也为应用程序的源代码创建了一个 :file:`src` 目录。


.. contents:: Procedures
   :local:
   :depth: 1

创建应用程序和源代码目录
=================================================

为您的应用程序创建一个目录，为应用程序的源代码创建一个子目录。这样能更简单地按照内核所期待的形式组织目录和文件。

开始前
----------------

* 确保为每个控制台终端都设置了 Zephyr 环境变量。参考 :ref:`apps_common_procedures` 。

步骤
-----

1. 在内核的安装目录树外创建一个应用程序目录结构。这通常就是您的工作目录。

 a) 从一个控制台终端进入您创建的用于存放应用程序的目录。

 b) 创建应用程序目录，输入：

   .. code-block:: console

      $ mkdir application_name

   .. note::

      这个目录在本文当中叫做 :file:`~/appDir` 。

2. 在 :file:`~/appDir` 下创建源码目录，输入：

   .. code-block:: console

      $ mkdir src

   The source code directory :file:`~/appDir/src` is created.

   .. code-block:: console

      -- appDir
         |-- src

创建应用程序的 Makefile
================================

您需要为应用程序创建一个 Makefile 来定义一些基本信息，例如应用程序使用的板级配置。此外，编译系统还需要利用 Makefile 编译一个包含应用程序和内核库的 :file:`zephyr.elf` 镜像文件。

开始前
----------------

* 熟悉标志 GNU Make 语法

* 熟悉用于您的应用程序的板级配置。

* 确保为每个控制台终端都设置了 Zephyr 环境变量。参考 :ref:`apps_common_procedures` 。

步骤
-----

1. 在 :file:`appDir` 目录下创建一个 Makefile 文件，输入：

   .. code-block:: bash

      $ touch Makefile

2. 使用文本编辑器打开 :file:`Makefile` 并添加下面的命令条目。

   .. note::

      确保在每个 ``=`` 后有一个空格。

   a) 在新的一行为您的应用程序添加一个默认板级配置：

      .. code-block:: make

         BOARD ?= board_configuration_name

      所支持的开发板位于 :ref:`board` 。

   b) 在新的一行为您的应用程序添加默认内核配置的名字：

      .. code-block:: make

         CONF_FILE ?= kernel_configuration_name

      如果默认的内核配置文件的名字叫做 :file:`prj.conf` ，则该条目可以忽略。如果您的默认板级配置的内核设置足够用于您的应用程序，该条目也可以忽略。

   c) 在新的一行包含顶层的 :file:`Makefile` 碎片：

      .. code-block:: make

         include ${ZEPHYR_BASE}/Makefile.inc

3. 保存、关闭 :file:`Makefile`.

Makefile 举例
----------------

.. code-block:: make

   BOARD ?= qemu_x86
   CONF_FILE ?= prj.conf
   include ${ZEPHYR_BASE}/Makefile.inc

支持编译第三方库
=============================================

当编译库文件时需要牢记一点，即库文件和应用程序最终会被编译到同一个镜像（应用程序二进制接口，ABI）中。大多数架构的编译器中都有用于控制 ABI 的编译标志。同时需要注意的是，库文件和应用程序应当具有相同的编译器标志。

为了更方便地集成第三方组件，Zephyr 项目的编译系统包含了一个特殊的编译目标 —— ``outputexports``，它会从 Zephyr 项目的编译系统中拿取很多关键变量，并将它们拷贝到 :file:`Makefile.export` 中。这样可以让关键变量很方便地封装到第三方的编译系统中。


推荐将下列变量用于第三方的编译中（参考 :file:`Makefile.export` 查看所导出的变量的完整列表）：

* ``CROSS_COMPILE`` 以及相关的调用交叉编译器的变量（包括 ``AR``, ``AS``, ``CC``, ``CXX``, ``CPP``
  and ``LD``）。

* ``ARCH``，``BOARD`` 以及一些标识 Zephyr 内核版本的变量。

* ``KBUILD_CFLAGS``, ``NOSTDINC_FLAGS``， ``ZEPHYRINCLUDE`` 应当按顺序添加到 ``CFLAGS`` 或者 ``CXXFLAGS`` 中。

* 所有的 Kconfig 变量，允许基于 Zephyr 内核版本的库代码的功能被自动使能/禁止。

:file:`samples/static_lib` 是一个用于演示这些特性的例程项目。
