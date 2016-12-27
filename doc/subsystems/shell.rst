.. _shell:

Zephyr OS Shell
###############

概述
********

Zephyr OS Shell 支持 Zephyr OS 模块能够同时使用/暴露它们的 shell 接口。

每个模块可以通过它们的 Kconfig 文件动态地支持 shell 功能。Kconfig 文件可以使能/禁止 shell。

使用 shell 命令
********************

使用下列格式中的某一个：

指定模块的命令
==========================
   `MODULE_NAME COMMAND`
	一个有效的模块是 “KERNEL” —— 内核模块。更多信息请查看 :c:macro:`SHELL_REGISTER` 。

帮助命令
=============
   `help`
	打印有效的模块。
   `help MODULE_NAME`
   	打印该模块的有效命令的名字。
   `help MODULE_NAME COMMAND`
   	打印该命令的帮助信息（帮助信息应当显示函数的功能和参数）。

选择模块命令
======================
   `set_module MODULE_NAME`
	当 shell 只用于某个模块时使用这个命令。输入这个命令后，您在今后输入命令时不再需要输入模块名。如果所选模块在初始化时设置了默认的 shell 提示符，shell 中的提示符会变换成这个提示符。否则，提示符会变换成所选模块的名字，以表示当前正在使用该模块。
   `set_module`
	清除对模块的选定。提示符也会恢复。

Shell 配置
*******************
存在两级配置：架构层和模块层。

架构层
====================
每个产品都应当关注 ENABLE_SHELL 标志的默认值。该标志用于使能 shell 服务。如果它被使能，内核的 shell 命令也会可用。更多信息请参考 Kconfig 配置选项 :option:`CONFIG_ENABLE_SHELL` 。

模块层
============
使用 shell 服务的每个模块都需要在它的 Kconfig 文件中加上一个独有的标志。

例如：
CONFIG_SAMPLE_MODULE_USE_SHELL=y

在模块的代码中，shell 的用法依赖于这个配置参数。模块相关的参数依赖于 ENABLE_FLAG 标志。

因此，每个模块除了独有标志之外还存在一个全局标志。

每个产品都应当关注 ENABLE_SHELL 标志的默认值。

向模块中添加新功能的配置步骤
==========================================================
 #. 检查 ENABLE_SHELL 是否被设为 yes。
 #. 向它的 Kconfig 文件中添加模块独有标志。


写一个新的 shell 模块
**********************
如果您的模块也需要支持 shell，应用程序必须按照如下步骤：

 #. 模块配置标志：
	在您的模块 Kconfig 文件中申明一个新的标志。它依赖于 `ENABLE_SHELL` 标志。

 #. 模块注册到 shell 中：
	添加您的 shell 标识符，并使用 :c:macro:`SHELL_REGISTER` 将它的回调函数注册到 shell 的数据库中。

 #. 可选：
	:c:func:`shell_register_default_module`

	:c:func:`shell_register_prompt_handler`

	用法：
		在例程应用程序以及测试环境中，用户可以在代码层设置一个默认模块。在这种情况下，函数 shell_register_default_module 应该在应用程序调用 SHELL_REGISTER 之后调用。如果函数 shell_register_prompt_handler 也被调用了，提示符会做相应的改变。否则，提示符会变为所需模块的名字。

	注意：
		即使在代码曾设置了默认模块，它也可以被 shell 命令 “set_module” 覆盖。

	当使用 shell_register_default_module 时：

	* 当 shell 只用于一个模块时使用这个命令。输入这个命令后，在今后输入命令时不再需要输入模块名。

	* 如果要向后兼容，使用这个函数。

	可选函数的更多信息请参考  :ref:`shell_api_functions` 。


.. _shell_api_functions:

Shell Api 函数
*******************
.. doxygengroup:: _shell_api_functions
   :project: Zephyr
   :content-only:
