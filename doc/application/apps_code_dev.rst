.. _apps_code_dev:

添加应用程序相关的代码
#############################

应用程序相关的源代码一般都放到应用程序的自己的目录中（:file:`~/appDir` ）。不过，某些时候应用程序也需要修改或者增加内核代码。

.. contents:: Procedures
   :local:
   :depth: 1

添加源代码到应用程序目录
**********************************************

理解源代码需求
======================================

应用程序相关的源代码文件通常被添加到应用程序的 :file:`src` 目录。如果应用程序需要添加大量的文件，可以将它们分组放到 :file:`src` 下面的子目录里，且路径的深入可以根据实际需求决定。开发者必须为 :file:`src` 目录极其下面的每个子目录各提供一个 :file:`Makefile` 文件。

.. note::

   这些 Makefile 文件与应用程序顶层目录 :file:`~/appDir` 下面的 Makefile 文件有一定的区别。

应用程序相关的源代码不应该使用内核所保留的符号名前缀。更多信息请参考 `Naming Conventions <https://wiki.zephyrproject.org/view/Coding_conventions#Naming_Conventions>`_ 。

理解 Makefile 需求
===================================

下面的需求适用于 :file:`src` 及其子目录下面的所有 Makefile。

* 在编译的过程中，Kconfig 文件通过匹配应用程序的 makefile 中的文件名将源文件编译到目标文件中。

  .. important::

    没有被任何 Makefile 引用的源文件不会被编译。

* Makefile 不能直接引用源代码。它只能引用由源码文件产生的目标文件（:file:`.o` 文件）。

* Makefile 只能引用它自己目录及其子目录下的文件。

* Makefiel 可以在在一行引用多个文件，不过引用每个目录时必须使用新行。

开始前
-----------------

* 确保您已经创建了应用程序目录。参考 :ref:`apps_structure` 。

* 确保为每个控制台终端都设置了 Zephyr 环境变量。参考 :ref:`apps_common_procedures` 。

* 您可以在 :file:`\$ZEPHYR_BASE/samples` 下面查找很多有用的例程代码。

步骤
-----

#. 在 :file:`src` 下面创建您的目录结构，并添加源码。

#. 在 :file:`src` 及其每个子目录下面（如果）创建一个 :file:`Makefile` 文件。

   a) 使用下面的语法添加对文件的引用：

      .. code-block:: make

         obj-y += file1.o file2.o

   b) 使用下面的语法添加对目录的引用：

      .. code-block:: make

         obj-y += directory_name/**

例程 src Makefile
--------------------

这个例程来源于哲学家例程。要在上下文中检查这个文件，先进入 :file:`\$ZEPHYR_BASE/samples/philosophers/src` 。

.. code-block:: make

   obj-y = main.o


修改和增加内核
**********************************

子系统命令规范
============================

当需要修改一个已经存在的内核子系统时，请按照已经存在的命名规范。更多信息请参考 `Naming Conventions <https://wiki.zephyrproject.org/view/Coding_conventions#Naming_Conventions>`_ 。

当创建一个新的子系统时，在该子系统中可以为符号定义它自己的命名规范。不过，命名规范应当以一个唯一的命名前缀实现（例如蓝牙是 bt\_，IP 是 net\_），以最大限度地减小与应用程序冲突的可能性。子系统内的命名应当继续按照前缀前面的前缀规范；这样能为所有用户提供一致性的接口。

包含路径使用指南
==============================

不要向系统中添加不必要的包含（include）路径或者默认包含路径，因为当两个或多个目录下包含同名文件时会导致有歧义的引用。唯一能添加到 :file:`\$ZEPHYR_BASE/include`  下面的包含路径应当是 :file:`\$ZEPHYR_BASE/include`  自身。

源文件在使用 :code:`#include` 时应该指定相对包含目录的完整路径。例如，使用的形式应该是 :code:`#include <path/to/[header].h>` 而不是 :code:`#include <[header].h>` 。

当指定了非必要的默认包含路径可能引起的各种问题。

* 注意，内核既包含 :file:`include/pci.h` 和 :file:`include/drivers/pci.h` 。

* 如果 :file:`include` 和 :file:`include/drivers` 都被添加到包含路径（例如 :code:`gcc -Iinclude/drivers -Iinclude [...]` ），当使用 :code:`#include <pci.h>` 时会造成歧义。

解决办法是避免将 :file:`include/drivers` 添加到默认包含路径，然后源文件可以引用 :code:`#include <pci.h>` 或者 :code:`#include <drivers/pci.h>` 。
