.. _kbuild_project:

开发应用程序和编译系统
**********************************************

编译系统是应用程序的中心系统。应用程序将驱动内核二进制文件的配置和编译过程。

应用程序开发包括三个独立的目录：内核基本目录、工程目录、工程源码目录。

Zephyr 内核的基本目录包含内核源码、配置选项以及内核编译定义。

应用程序目录用于将内核与开发者的应用程序组合在一起，它包含应用程序的相关定义，例如应用程序相关的配置选项和应用程序源码。

应用程序工程
=======================

应用程序工程通常由如下文件组成：

* **Makefile**： 定义应用程序的编译过程，并将开发者的应用程序集成到内核的编译系统中。

* **配置文件**： 开发者可以使用配置文件覆盖开发板默认配置。

* **:file:`src/` 目录**: 默认情况下，该目录包含应用程序的源代码。不过您也可以将应用程序的源码定义在其它目录中。

   * **Makefile**: 将开发者的源代码添加到编译系统的递归模型中。

应用程序的源代码可以以子目录的形式进行组织，每个目录必须遵循 Kbuild Makefile 的约定；请参考 :ref:`kbuild_makefiles`。

应用程序定义
======================

开发者通过 Makefile 将相关的应用程序定义到编译系统中：包含内核提供的 Makefile.inc。

.. code-block:: make

   include $(ZEPHYR_BASE)/Makefile.inc

下列预定义变量可以用来配置开发工程：
The following predefined variables configure the development project:

* :makevar:`ARCH`： 指定内核的编译架构。当前支持的架构包括 x86、arm 和 arc。编译系统会设置 C 标志，选择默认配置，并使用合适的工具链。默认值是 x86。

* :makevar:`ZEPHYR_BASE`： 设置内核基本目录的路径。该变量通常是由脚本 :file:`zephyr_env.sh` 设置的。它可以用于获取内核的基本目录（Makefile.inc 中就是这样使用的）。您也可以指定一个其它的内核实例将其覆盖。

* :makevar:`PROJECT_BASE`： 提供开发者的应用程序工程的目录路径。它由 :file:`Makefile.inc` 进行设置。

* :makevar:`SOURCE_DIR`： 覆盖应用程序源代码目录的默认值。开发者的源代码目录默认被设置为 :file:`$(PROJECT_BASE/)src/`。这个目录的名字应当以斜线 **'/'** 结束。

* :makevar:`BOARD`： 为默认配置选择开发板，应用程序编译时将使用这个开发板。

* :makevar:`CONF_FILE`： 指定应用程序碎片文件的名字。该文件包含的 kconfig 配置值会覆盖默认值。

* :makevar:`O`： 可选。指示 Kconfig 所使用的输出目录。该目录会存储在编译期间产生的所有文件。输出文件的默认路径是 :file:`$(PROJECT_BASE)/outdir`。

调试应用程序
=====================

本节是使用 QEMU 调试应用程序的快速上手指南。本节中的大多数内容在 `QEMU`_ 和 `GNU_Debugger`_ 的参考手册中都有说明。

.. _QEMU: http://wiki.qemu.org/Main_Page

.. _GNU_Debugger: http://www.gnu.org/software/gdb


在这个快速指南中，您可以找到捷径，指定有助于快速设置您的调试环境的环境变量和参数。

调试运行在 QEMU 中的应用程序的最简单的办法是使用 GNU 调试器，通过 QEMU 在您的开发环境中设置一个本地 GDB Server。

调试时，您需要一个 ELF 格式的二进制镜像文件。编译系统会自动在输出目录中产生这个镜像。该镜像默认的名字是 :file:`zephyr.elf`，但是您也可以使用 Kconfig 进行修改。

.. note::

   我们将使用标准的 TCP 端口 1234 来打开 :abbr:`GDB (GNU Debugger)` 服务实例。您也可以使用一个适合于您的开发系统的其它端口。

QEMU 是内核支持的仿真系统。调用 QEMU 时必须加上 -s 和 -S 选项。

* ``-S`` 不会在 QEMU 启动时启动 CPU；相反，您必须在监视器中输入 'c' 来启动 CPU。
* ``-s`` 是 :literal:`-gdb tcp::1234`的简短写法：在 TCP 端口 1234 上打开一个 GDB Server。

编译系统可以通过 :makevar:`qemu` 目标直接编译 elf 镜像并调用 QEMU。QEMU 的调试选项可以使用环境变量 nvvar:`QEMU_EXTRA_FLAGS` 进行设置，例如：

.. code-block:: bash

    export QEMU_EXTRA_FLAGS="-s -S"

编译和仿真过程由 Makefile 的 ``qemu`` 对象进行调用：

.. code-block:: bash

   make qemu

编译系统会启动一个 QEMU 实例，该实例会让 CPU 在启动时暂停。此外，该实例还会创建一个监听 TCP 端口 1234 的 GDB Server。

:file:`.gdbinit` 用于帮助您在每次运行时初始化 GDB 实例。在这里例子里面，初始化文件执行 GDB Server 实例：它在本地主机上的 TCP 端口 1234 上配置了一个连接到远程目标的连接。初始化时会设置内核的根目录。:file:`.gdbinit` 中的内容如下：

.. code-block:: bash

   target remote localhost:1234
   dir ZEPHYR_BASE

.. note::

   ZEPHYR_BASE 指的是当前内核的根目录。

从与 :file:`gdbinit` 所在的同一目录启动启动并调试应用程序。命令行选项 ``--tui`` 用于使能终端用户接口。下面的命令会使用 :file:`gdb` 链接到 GDB Server。在这个例子里面，elf 二进制镜像的名字是 :file:`zephyr.elf`：

.. code-block:: bash

   gdb --tui zephyr.elf

.. note::

   开发系统的 GDB 版本可能部支持 --tui 选项。

最后，使用数据显示器调试器（Data Displayer Debugger，:file:`ddd` ）连接到 GDB Server。该命令会从 elf 二进制文件 :file:`zephyr.elf` 中加载符号表。

.. note::

   您的开发系统中可能默认没有安装 :abbr:`DDD (Data Displayer Debugger)` 。请根据系统提示的指令进行安装。

.. code-block:: bash

   ddd --gdb --debugger "gdb zephyr.elf"

.. note::

   两个命令都会执行 :abbr:`gdb (GNU Debugger)`。不同的工具链和交叉开发工具的命令名字可能不一样。
