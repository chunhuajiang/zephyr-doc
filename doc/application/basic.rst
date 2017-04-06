.. _basic:

基础知识
##############################

应用程序的组织结构
*********************

开发一个新的应用程序时，您需要为应用程序创建一个目录，为应用程序源代码创建一个子目录；这种方式更容易以内核所期望的结构来组织目录和文件。

#. 在内核的安装目录树外面创建一个新的目录。通常，这是你的工作空间目录。

#. 在控制台终端，进入一个您所虚妄存放应用程序的目录。

#. 创建应用程序目录，输入：

   .. code-block:: console

      $ mkdir app

   .. note::

      本文假设该目录是 :file:`~/app`。

#. 在 :file:`~/app` 下面创建一个源码目录：

   .. code-block:: console

      $ cd app
      $ mkdir src

   创建之后，该应用程序的目录结构是：

   .. code-block:: console

      -- app
         |-- src


应用程序的预定义
**********************

应用程序通过包含内核所提供的 Makefile.inc 文件集成到编译系统中。

.. code-block:: make

   include $(ZEPHYR_BASE)/Makefile.inc

下列预定义变量用于配置工程：

* :makevar:`ZEPHYR_BASE`: 设置内核所在目录的路径。该变量通常由脚本 :file:`zephyr_env.sh` 进行设置。您可以通过它来获取内核所在目录，也可以通过选择一个指定的内核实例将它覆盖。


* :makevar:`PROJECT_BASE`: 指定开发者的应用程序项目所在目录的路径。该办理通常由文件 :file:`Makefile.inc` 进行设置。

* :makevar:`SOURCE_DIR`: 覆盖应用程序的源代码路径的默认值。源代码路径的默认值是 :file:`$(PROJECT_BASE/)src/`。目录的名字应当以斜线 **'/'** 结尾。

* :makevar:`BOARD`: 选择应用程序将要运行到的开发板的默认配置。

* :makevar:`CONF_FILE`: 配置文件的文件名，它包含用于覆盖默认配置值的 kconfig 配置值。

* :makevar:`O`: 可选。Kconfig 需要使用的输出文件夹。输出文件夹用于存储在编译期间产生的所有文件。默认的输出文件夹的路径是 :file:`$(PROJECT_BASE)/outdir`。

