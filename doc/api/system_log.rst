.. _system_log:

系统日志 API
#################

.. contents::
   :depth: 1
   :local:
   :backlinks: top

系统日志
************

.. doxygengroup:: system_log
   :project: Zephyr
   :content-only:

系统日志 API 提供了一个通用接口，它可以处理由开发者发出的消息。虽然这些消息当前会被打印到终端，但是 API 其实是以通用方式进行定义的。

这些 API 的功能可以通过配置选项进行关闭，参考 :ref:`global_kconfig` 。当不需要系统日志时，使用这种方法能减小镜像尺寸和执行时间。

每个 ``SYS_LOG_X`` 宏代表一个不同的日志等级。高于等于所设置的日志等级的宏会被激活。

存在两种配置：模块配置和全局配置。当日志被全局使能时，它对模块有效。不过，模块可以本地禁止日志。每个模块可以指定它自己的日志等级。模块在包含头文件 :file:`<misc/sys_log.h>` 前必须定义 :c:macro:`SYS_LOG_LEVEL` 。除非设置了全局覆盖，否则必须设置模块日志等级。全局覆盖设置只能增加日志等级，它不能降低之前被设置为更高等级的模块的等级。

您可以设置本地域来区分消息。当没有设置域时， ``[general]`` 域会在消息前出现。设置域时，需要在包含头文件 :file:`misc/sys_log.h` 前定义宏 :c:macro:`SYS_LOG_DOMAIN` 。

当多个宏被激活时，有两种方式区分所打印的消息：消息前所打印的标签；ANSI 颜色。更多信息请查看配置选项 :option:`CONFIG_SYS_LOG_SHOW_TAGS` 和 :option:`CONFIG_SYS_LOG_SHOW_COLOR` 。

在包含头文件 :file:`misc/sys_log.h` 前定义宏 :c:macro:`SYS_LOG_NO_NEWLINE` 可以防止宏在日志消息的默认追加换行。

.. _global_kconfig:

全局 Kconfig 选项
**********************

这些选项可以在 :file:`misc/Kconfig` 中找到。

:option:`CONFIG_SYS_LOG`: 全局切换，关闭/打开所有的系统日志。

:option:`CONFIG_SYS_LOG_DEFAULT_LEVEL`: 默认级别，如果模块没有设置它自己的日志级别，则使用该级别。

:option:`CONFIG_SYS_LOG_SHOW_TAGS`: 全局设置是否在日志中显示级别标签。

:option:`CONFIG_SYS_LOG_SHOW_COLOR`: 全局设置是否在系统日志中使用 ANSI 颜色。

:option:`CONFIG_SYS_LOG_OVERRIDE_LEVEL`: 当模块没有设置日志级别，或者它的日志级别比它低时，它会覆盖模块的日志级别。

例程
*******

下面的宏：

    .. code-block:: c

     SYS_LOG_WRN("hi!");

将会产生：

    .. code-block:: console

     [general] [WRN] main: Hi!

上面的例程如果要工作，下列设置中至少有一个要为 true：

- :option:`CONFIG_SYS_LOG_DEFAULT_LEVEL` 被设为 2 以上（包括），且模块的配置未被设置。
- 模块的配置被设置为 2 以上（包括）。
- :option:`CONFIG_SYS_LOG_OVERRIDE_LEVEL` 被设置为 2 以上（包括）。
