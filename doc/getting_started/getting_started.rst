.. _getting_started:

入门指南
#####################

使用本文档开始您的 :ref:`Zephyr <introducing_zephyr>` 开发之旅吧！

设置开发环境
**********************************

Zephyr 项目支持如下操作系统：

* Linux
* Mac OS
* Windows 8.1

您可以按照下面的步骤搭建一个新的开发环境。

.. toctree::
   :maxdepth: 1

   installation_linux.rst
   installation_mac.rst
   installation_win.rst


匿名检出源代码
========================================

Zephyr 托管在 Linux 基金会的 Gerrit 后台上，且支持通过 git 匿名克隆。

匿名克隆仓库，请输入：

.. code-block:: console

   $ git clone https://gerrit.zephyrproject.org/r/zephyr zephyr-project

这样，您将在您的本地机器上成功地检出源代码的副本。

如果您打算贡献代码，请先到 `Gerrit Accounts`_ 创建一个 Linux 基金会账户。

.. _Gerrit Accounts: https://wiki.zephyrproject.org/view/Gerrit_accounts

编译、运行应用程序
***********************************

下面的章节将利用一个简单的 'Hello World' 作为基础模型，向您展示创建一个 Zephyr 应用程序所涉及到的内容。

各种操作系统上编译、运行 Zephyr 应用程序的过程是类似的。尽管如此，不同操作系统的命令会略有区别。本节所有的命令都是基于 Linux 开发环境的，如果您使用的是 Mac 
OS，请使用该操作系统所对应的命令。

编译一个简单的例子
=============================

请按照下面的步骤编译一个简单的应用程序例程：


#. export 下列环境变量，以确保您的环境被正确地设置。以 Linux 为例，输入：

   .. code-block:: console

      $ export ZEPHYR_GCC_VARIANT=zephyr

      $ export ZEPHYR_SDK_INSTALL_DIR=<sdk installation directory>

#. 进入项目主目录：

   .. code-block:: console

      $ cd zephyr-project

#. 对环境变量文件执行 source 操作，使其生效：

   .. code-block:: console

      $ source zephyr-env.sh

#. 编译应用程序。输入：

   .. code-block:: console

      $ cd $ZEPHYR_BASE/samples/hello_world

      $ make

上面的 make 命令将使用在应用程序 Makefile 中的定义编译 hello_world 例程。
您可以通过指定变量 BOARD 为不同的开发板编译不同的程序，例如：

.. code-block:: console

   $ make BOARD=arduino_101

关于 Zephyr 所支持的开发板，请参考 :ref:`这里 <board>`。您也可以输入以下命令
查看 Zephyr 所支持的开发板。

.. code-block:: console

   $ make help

目录 :file:`$ZEPHYR_BASE/samples` 下包含了 Zephyr 各种功能特性的例程工程。当应用程序
编译成功后，您可以在应用程序根目录下的 :file:`outdir` 子目录中看到编译生成的文件。

编译系统默认会生成名为 :file:`zephyr.elf` 的可执行文件。您也可以在应用程序的配置文件中
进行配置，为不同的硬件和开发板指定不同的可执行文件名字。

.. _third_party_x_compilers:

使用自定义/三方交叉编译器
==========================================

为了便于使用，Zephyr 提供了一套软件开发工具（SDK）。Zephyr SDK 为所有所支持的操作系统都提供了交叉编译器，因此您无需进行额外的配置。

如果您想使用自定义的交叉编译器，或者如果您想使用厂家提供的 SDK，
您可以按照下列步骤进行设置：

#. 为了避免与 Zephyr SDK 冲突，先输入如下命令：

   .. code-block:: console

      $ unset ZEPHYR_GCC_VARIANT

      $ unset ZEPHYR_SDK_INSTALL_DIR

#. 我们以 `GCC ARM Embedded`_ 编译器为例。从 `GCC ARM Embedded`_ 下载一个适合您的操作系统的
   软件包，然后将其解压到您的文件系统中。假设该编译器被解压到： :file:`~/gcc-arm-none-eabi-5_3-2016q1/`。

#. 进入项目主目录：

   .. code-block:: console

      $ cd zephyr-project

#. 对项目环境文件执行 source 操作：

   .. code-block:: console

      $ source zephyr-env.sh

#. 编译例程，且在命令行指明 CROSS_COMPILE：

   .. code-block:: console

      $ cd $ZEPHYR_BASE/samples/hello_world

      $ make CROSS_COMPILE=~/gcc-arm-none-eabi-5_3-2016q1/bin/arm-none-eabi- BOARD=arduino_due

上面的命令将使用您从 `GCC ARM Embedded`_ 下载的工具链编译应用例程。

您也可以已存在的支持 GCC ARM Embedded 的工具链：

   .. code-block:: console

      $ export GCCARMEMB_TOOLCHAIN_PATH="~/gcc-arm-none-eabi-5_3-2016q1/"

      $ export ZEPHYR_GCC_VARIANT=gccarmemb

      $ cd zephyr-project

      $ source zephyr-env.sh

      $ cd $ZEPHYR_BASE/samples/hello_world

      $ make BOARD=arduino_due

在 QEMU 中运行应用程序例程
====================================

为了在开发环境中进行快速测试，您可以使用能够 qemu 仿真器。qemu 仿真器支持 x86 和 ARM Cortex-M3。
进行 qemu 仿真非常简单，您只需要在编译应用程序时指定一个目标，编译系统会自动调用 QEMU 进行编译。

如果要使用 x86 qemu 仿真开发板配置(qemu_x86)编译应用程序，输入：

.. code-block:: console

   $ make BOARD=qemu_x86 qemu

如果要使用 ARM qemu_cortex_m3 开发板配置编译应用程序，输入：

.. code-block:: console

   $ make BOARD=qemu_cortex_m3 qemu

QEMU 并非支持所有的开发板和 SoC。当为一个特定硬件开发应用时，您需要在实际的硬件平台上进行测试，而不要仅仅依赖于 QEMU 仿真环境。

.. _Linux Foundation ID website: https://identity.linuxfoundation.org

.. _Gerrit: https://gerrit.zephyrproject.org/

.. _GCC ARM Embedded: https://launchpad.net/gcc-arm-embedded
