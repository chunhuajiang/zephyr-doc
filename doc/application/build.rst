.. _build:

编译
######################

编译应用程序
********************

Zephyr 的编译系统能够将应用程序的所有组件编译成一个单一的既可以运行在仿真硬件，又可以运行在真实硬件之上的应用程序镜像。

#. 进入应用程序所在目录 :file:`~/app`。

#. 使用下面的命令可以使用应用程序的 :file:`Makefile` 中所指定的开发板的配置来编译生成 :file:`zephyr.elf` 镜像。

   .. code-block:: console

       $ make

   如果有需要，您可以通过参数 :code:`CONF_FILE` 来指定某个 :file:`.conf` 文件来作为应用程序的配置文件。该文件中的配置值将覆盖应用程序的 :file:`.config` 文件或其默认 :file:`.conf` 中的配置值。例如：

   .. code-block:: console

       $ make CONF_FILE=prj.alternate.conf

   如果有需要，您也可以通过参数 :code:`BOARD` 来指定应用程序所使用的开发板，而忽略其 :file:`Makefile` 中所指定的开发板。例如：

   .. code-block:: console

       $ make BOARD=arduino_101

   编译应用程序时，您可以同时指定 :code:`CONF_FILE` 和 :code:`BOARD` 这两个参数。

运行应用程序
*************************

当应用程序的功能变动，导致源代码、Makefile 或配置设置有变动时，需要重新编译应用程序。、

.. important::

    Zephyr 的编译系统只会编译那些与改动部分相关的文件，因此，重新编译应用程序比第一次编译会快很多。

有时候，由于重新编译某一个或多个必须文件时失败，编译系统不能正确地重新编译应用程序，您可以按照下面的流程强制编译系统重新编译整个应用程序：


#. 进入应用程序所在目录 :file:`~/app`。

#. 使用下面的命令可以为指定的开发板删除在编译应用程序时所产生的除文件 :file:`.config` 之外的其它所有文件。文件 :file:`.config` 中包含了应用程序当前的配置信息。

   .. code-block:: console

       $ make [BOARD=<type>] clean

   此外，您也可以使用下面的命令为 *所有* 开发板删除包括文件 :file:`.config` 在内的 *所有* 文件。

   .. code-block:: console

       $ make pristine

#. 按照上面 `编译应用程序`_ 中所描述的方法来重新编译应用程序。