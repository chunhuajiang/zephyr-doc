.. _makefile:

Makefile
##############################

概述
========

为了在内核源码目录中正确地使用 Makefile 文件，编译系统定义了一系列的约定。递归概念是正确使用 Makefile 文件的核心。

在递归模型中，目录中的每个 Makefile 包含该目录的源代码以及子目录。每个子目录也遵循同样的规则。开发者只需要按照递归模型简单地添加一个 Makefile 文件就能将他们自己的模块集成到编译系统中去，从而可以专心地将精力集中在本身的工作上。

.. _makefile_conventions:

Makefile 的约定
====================

下面的约定规定了如何将模块和 Makefile 添加到编译系统中去。这些约定能确保正确地实现递归模型。

* 每个源代码目录必须包含一个 Makefile。不包含 Makefile 的目录将不被当做源代码目录。

* 每个 Makefile 的范围被限制为该目录的内容。Makefile 只能直接引用同级或下级目录的文件和子目录。

* 在 Makefile 中列举出需要在链接过程中包含的目标文件。编译系统通过对目标文件名的匹配来查找源文件。

* 父目录将它们的子目录添加到递归模型中去。

* 根 Makefile 将内核目录树中的目录添加到递归模型中去。

添加源文件
===================

Makefile 必须间接地引用源文件，即使用 :literal:`obj-y` 变量指定目标文件。例如，如果我们需要添加的 C 文件叫做 :file:`<file>.c`，则我们需要在 Makefile 中按照下面的方式进行引用：


.. code-block:: make

   obj-y += <file>.o

.. note::

   该方法同样适用于以 .S 作为扩展名的汇编文件。

您也可以通过使用配置选项来按条件添加源文件。例如，如果需要在选项 ``CONFIG_VAR`` 被设置时添加某个源文件，则可以在 Makefile 中按如下形式添加一行代码：

.. code-block:: none

   obj-$(CONFIG_VAR) += <file>.o

添加目录 
==================

您也可以通过编辑某个目录下的 Makefile 来将该目录下的子目录添加到编译系统中。子目录的添加也是通过变量 :literal:`obj-y` 来完成的。添加子目录的正确语法是： 

.. code-block:: make

   obj-y += <directory_name>/

目录名后面的反斜线用于告诉编译系统需要添加到编译系统中的是一个目录，而不是文件。

约定还要求我们在一行只能添加一个目录，且不要在一行 :literal:`obj-y` 中同时包括源代码和目录。这样能保持 Makefile 文件的可读性。

目录也可以被条件添加：

.. code-block:: none

   obj-y-$(CONFIG_VAR) += <directory_name>/

子目录也可以按照 :ref:`makefile_conventions` 中所描述的规则添加它自己的 Makefile。

应用程序的 Makefile
********************

创建一个 Makefile 来定义一些基本信息，例如应用程序所使用的开发板配置。编译系统使用 Makefile 来编译并生成一个既包含应用程序又包含内核库的镜像文件 :file:`zephry.elf`。

#. 使用任何文本编辑器打开 :file:`Makefile` 并添加下面这些强制性条目。

   .. note::

      确保在每个 ``=`` 前后都存在一个空格。

#. 在新的一行为您的应用程序添加默认的开发板配置：

   .. code-block:: make

      BOARD = board_configuration_name

   所支持的开发板可以在 :ref:`boards` 找到。

#. 在新的一行为您的应用程序添加默认的内核配置：

   .. code-block:: make

      CONF_FILE ?= kernel_configuration_name

#. 在新的一行添加一条强制性条目：

   .. code-block:: make

      include ${ZEPHYR_BASE}/Makefile.inc

#. 保存并关闭 :file:`Makefile`。


下面是一个 Makefile 的例子：

.. code-block:: make

   BOARD = qemu_x86
   CONF_FILE = prj.conf

   include ${ZEPHYR_BASE}/Makefile.inc