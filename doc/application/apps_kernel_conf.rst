.. _apps_kernel_conf:

为应用程序配置内核
#################################

应用程序的内核由一系列可根据应用程序自定义的配置选项进行配置。Zephyr 的编译系统从所指定的第一个源中获取配置选项的值。可用的源包括（按顺序）：

#. 应用程序当前的配置，例如 :file:`.config` 文件。

#. 应用程序的默认配置，例如 :file:`.conf` 文件。

#. 应用程序所使用的板级配置，例如开发板的 :file:`.defconfig` 文件。

#. 内核的默认配置，例如内核的某个 :file:`Kconfig` 文件。

如果您需要了解所有可用的内核配置选项以及选项间的内部依赖关系，请移步 :ref:`configuration` 。需要注意的是，如果某个选项是实验选项，则它的功能还不健全。

.. contents:: Procedures
   :local:
   :depth: 1

定义应用程序的默认内核配置
=======================================================

应用程序的 :file:`.conf` 文件定义了它的默认内核配置。该文件中的设置将会覆盖或补充板级配置设置。

板级配置设置位于 :file:`\$ZEPHYR_BASE/boards/ARCHITECTURE/BOARD/BOARD_defconfig` 。

.. note::

   当默认的板级配置设置足够用于您的应用程序时，不需要再使用 :file:`.conf` 文件。跳转到 :ref:`override_kernel_conf` 。

开始前
----------------

* 确保您已创建了应用程序目录，参考 :ref:`apps_structure` 。

* 检查内核的可用配置选项，并明确您想用哪个选项来设置应用程序。请注意到这些选项间的依赖关系。每个选项的剪短介绍请移步 :ref:`configuration` 。

步骤
-----

1. 进入 :file:`appDir` 并创建一个 :file:`prj.conf` 文件。输入：

   .. code-block:: bash

       $ touch prj.conf

  默认的名字是 :file:`prj.conf`。该文件名必须与应用程序 :file:`Makefile` 中的 ``CONF_FILE`` 条目相匹配。

2. 编辑文件，并添加恰当的配置条目。

   a) 每添加一个配置条目时应该另起一行。

   b) 条目以 ``CONFIG_`` 作为前缀。

   c) 确保每个条目不包含空格（包括 ``=`` 的左右两侧）。

   d) 使用 ``#`` 以及空格添加行注释

   下面的例子演示了行注释以及覆盖 :file:`prj.conf` 中的开发板配置的方法。

   .. code-block:: c

       # Change the number of IRQs supported by the application
       CONFIG_NUM_IRQS=43

3. 保存并关闭文件。


.. _override_kernel_conf:

覆盖应用程序的默认内核配置
=========================================================

覆盖应用程序的默认内核配置可临时修改应用程序的配置。您可以测试改动的效果。

.. note::

   如果您想永久性修改配置，则需要修改 :file:`.conf` 文件。

Zephyr 的编译系统使用多驱动接口配置内核选项。尽管您也可以手工添加条目，但是我们推荐使用配置菜单进行添加。


开始前
----------------

* 确保已也创建了应用程序目录，参考 :ref:`apps_structure` 。

* 检查内核的可用配置选项，并明确您想用哪个选项来设置应用程序。请注意到这些选项间的依赖关系。每个选项的剪短介绍请移步 :ref:`configuration` 。

* 确保为每个控制台终端都设置了 Zephyr 环境变量。参考 :ref:`apps_common_procedures` 。

步骤
-----

1.  运行 :command:`make menuconfig` 规则加载多驱动接口。

 a) 通过终端会话进入应用程序目录（:file:`~/appDir`）。

 b) 输入下面的命令：

  .. code-block:: bash

   $ make [BOARD=<type>] menuconfig

  基于问题的菜单允许您设置单个配置选项。

.. image:: figures/app_kernel_conf_1.png
    :width: 400px
    :align: center
    :height: 375px
    :alt: Main Configuration Menu

2.  使用下面的关键命令设置内核配置选项值：

   * 使用上下箭头键在菜单或者列表中移动。

   * 按下 :kbd:`Enter` 键选择某个菜单项。

   * 在中括号 :guilabel:`[ ]` 中输入大写的 :kbd:`Y` 或者 :kbd:`N` 来使能/禁止某个内核配置选项。

   * 在原括号 :guilabel:`( )` 中输入数字值。

   * 按下 :kbd:`Tab` 键进入下面的目录菜单。

   .. note::

    当非默认的非数值化的条目被选择时，中括号中接会显示 :kbd:`*` 。当您选择选项的默认值时，不会显示任何东西。

3.  如果需要查看任何关于选项的信息，先选择该选项，然后利用 tab 键进入 :guilabel:`< Help >`，然后输入 :kbd:`Enter` 。

    按 :kbd:`Enter` 键可返回菜单。

4.  为您的应用程序配置完内核选项后，利用 tab 键进入 :guilabel:`< Save >`，然后输入 :kbd:`Enter` 。

    下列对话框使用 :guilabel:`< Ok >` 命令选择：

.. image:: figures/app_kernel_conf_2.png
    :width: 400px
    :align: center
    :height: 100px
    :alt: Save Configuration Dialog


5.  按下 :kbd:`Enter` 键会将内核配置选项保存为默认文件名。您也可以输入一个文件名后再按 :kbd:`Enter` 键。

    通常，除非您在实验各种不同配置的效果，您需要保存为默认的文件名。

    编译系统会自动在应用程序目录下创建一个 :file:`outdir` 目录。该目录包含 :file:`\$ZEPHYR_BASE` 下的文件的符号链接。

   .. note::

    当前，只能使用 :file:`.config` 文件进行编译。如果您保存了多种文件名不同的文件，但是又想使用它们其中的某个文件进行编译，您可以将该文件重命名为 :file:`.config` 。在重命名前可将原先的 :file:`.config` 进行备份。

    内核配置文件（例如 :file:`.config`）被保存为 :file:`outdir` 下面的隐藏文件。要查看所有的内核配置文件，在终端提示符中输入 :command:`ls -a`。

    下面的对话框打开并显示了所保存的配置文件名。

.. image:: figures/app_kernel_conf_3.png
    :width: 400px
    :align: center
    :height: 150px
    :alt: Saved Configuration Name Dialog

6.  按下 :kbd:`Enter` 键返回选项菜单。

7.  如果需要加载某个已保存的配置文件，利用 tab 键跳转到 :guilabel:`< Load >` 并按下 :kbd:`Enter`。

    下面的对话框打开时光标位于 :guilabel:`< Ok >` 命令处。

.. image:: figures/app_kernel_conf_4.png
    :width: 400px
    :align: center
    :height: 175px
    :alt: Configuration File Load Dialog

8.  如果需要加载最后保存的内核配置文件，直接选择 :guilabel:`< Ok >`；如果要加载其它的配置文件，先输入文件名，再选择 :guilabel:`< Ok >`。

9.  按下 :kbd:`Enter` 键加载文件并返回主菜单。

10. 如果要退出主配置菜单，利用 tab 键调到 :guilabel:`< Exit >`，并按下 :kbd:`Enter`。

    下面的对话框打开时光标位于 :guilabel:`< Yes >` 命令处。

.. image:: figures/app_kernel_conf_5.png
    :width: 400px
    :align: center
    :height: 100px
    :alt: Exit Dialog

11. 按下 :kbd:`Enter` 键退出显示菜单并返回控制台命令行。
