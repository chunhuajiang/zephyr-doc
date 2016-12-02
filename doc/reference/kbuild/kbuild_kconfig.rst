.. _kconfig:

Kconfig 文件结构
**************************

简介
============

Kconfig 文件用于描述：编译系统所支持的配置符号、菜单和子菜单中符号组的逻辑组织结构、不同配置符号之间的关系。

Kconfig 文件遍布于编译目录树中，这些文件是基于其通用特性和增加到配置菜单中的新符号组织起来的。例如：

* 根目录的 Kconfig 文件包含通用的配置选项，例如 :option:`CONFIG_ARCH` 和 ``CONFIG_KERNEL VERSION``。这些符号被定义用于整个编译系统。

* :file:`kernel` 目录下的 Kconfig 文件包含与核心内核相关的通用配置。

* :file:`drivers` 目录下的 Kconfig 文件包含系统所支持的各种驱动程序的配置。

* :file:`misc` 目录下的 Kconfig 文件包含与编译系统相关的配置符号。例如，*Custom Compiler Options* 和 ``Minimal Libc`` 是用于编译系统的选项。*Debugging Options* 和 *System Monitoring Options* 是适用于整个编译系统的选项。

* :file:`net` 目录下的 Kconfig 文件包含为通信协议栈定义的配置选项。

* :file:`crypto` 目录下的 Kconfig 文件包含为加密算法定义的配置选项。

依赖
============

依赖允许您在系统中定义有效的、无效的配置组合。每个依赖都是一条规则，即一个特殊的符号必须被选择，或者被设置一个值。例如，配置符号 *B* 依赖于另一符号 *A*。

.. code-block:: kconfig

   config B bool

   config A depends on B

如果符号 A 要存在于系统中，则符号 B 必须被设为 true。

完整的依赖规则定义了系统可使用的有效配置组合。

默认配置
======================

默认的配置文件为特定的 SoC 的内核定义了默认的配置。例如：

* :file:`arch/arm/configs`，
* :file:`arch/x86/configs` 和
* :file:`arch/arc/configs`。

所有默认配置文件的后缀必须是 _defconfig。例如，文件 :file:`galileo_defconfig` 包含了 galileo 开发板的配置信息。

文件 :file:`Makefile.inc` 使用定义系统类型的环境变量，通过 defconfig 文件给开发者提供一个干净的接口。开发者可以提供一个带有目标 defconfig 文件的编译系统。编译系统将使用所指定的 defconfig 文件，并将其作为当工程的 :file:`.config` 文件。例如：

.. code-block:: console

   $ make galileo_defconfig

上述命令将使用架构的默认配置和 galileo 开发板配置来编译内核。

.. _configuration_snippets:

合并配置碎片
===============================

配置文件碎片可以在编译时与当前过程的配置进行合并。

开发者可以提供一个定义了配置选项子集的配置文件。该子集中必须包含与默认配置不同的相关选项。

目标 **initconfig** 将拉取默认的配置文件，并将之与本地配置碎片合并。例如，例程 **hello world** 将使用 :file:`prj.conf` 中的配置碎片覆盖基本的配置。

.. caution::
   合并的过程会忽略无效的配置以及 Kconfig 文件中不符合依赖要求的配置。当通过配置碎片增加依赖选项时，请确保其顺序遵循在 Kconfig 文件中定义的依赖规则。
