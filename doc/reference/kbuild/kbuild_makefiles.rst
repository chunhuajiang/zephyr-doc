.. _kbuild_makefiles:

Makefile 
*************

概述
========

为了正确使用内核源码目录中的 Makefile，编译系统做了一系列的约定。Makefile 的核心概念是递归。

在递归模型中，目录中的每个 Makefile 都包含需要编译的源码和子目录。对于每个子目录也遵循这个原则。开发者可以专注于它们自己的工作。如果需要将某个模块集成到编译系统中，只需要按照递归模型的原则添加一个简单的 Makefle 文件。

.. _makefile_conventions:

Makefile 规则
====================

下面的约定限定了如何向编译系统中添加模块和 Makefile。这些约定保证了递归模型的正确性。

* 每个源代码目录必须包含一个 Makefile。没有包含 Makefile 的目录不被认为是源代码目录。

* 每个 Makefile 的范围仅限于该目录中的内容，且只能直接引用它自己的文件及其子目录。该目录外的其它任何文件必须只能被主目录 Makefile 引用。

* Makefile 中列举了链接时需要包含的目标文件。编译系统通过文件名查找、匹配该目标文件的源文件。

* 父目录将它们的子目录添加到递归模型中。

* 根 Makefile 将内核基本目录中的目录添加到递归模型中。


添加源文件
===================
源代码通过其主目录的 Makefile 文件添加到编译系统中。Makefile 通过变量 :literal:`obj-y` 间接地引用目标文件。例如，如果要被添加的 C 文件的文件名是 :file:`<file>.c`，您需要将如下几行添加到 Makefile 中：

.. code-block:: make

   obj-y += <file>.o

.. note::

   以 .s 作为扩展名的汇编文件也采用这种方法。

您也可以使用配置选项对源文件进行条件添加。例如，如果选项 ``CONFIG_VAR`` 被设置时表示需要编译一个源文件，您需要将如下几行添加到 Makefile 中：

.. code-block:: none

   obj-$(CONFIG_VAR) += <file>.o

添加目录
==================

如果您需要将某个子目录添加到编译系统中，您需要编辑 Makefile 中。通过变量 :literal:`obj-y` 可以添加子目录，其语法是：

.. code-block:: make

   obj-y += <directory_name>/

目录名后面的斜线用于给编译系统提供指示，表示需要添加到递归模型中的是一个目录而不是文件。

约定，每一行只能添加一个目录，且单个 :literal:`obj-y` 中不能有文件和目录的混合。这样能增加 Makefile 的可读性，尤其是能看到它的递归层级。

目录也可以进行条件添加：

.. code-block:: none

   obj-y-$(CONFIG_VAR) += <directory_name>/

子目录必须包含它自己的 Makefile，且其必须遵循 :ref:`makefile_conventions` 中描述的规则。
