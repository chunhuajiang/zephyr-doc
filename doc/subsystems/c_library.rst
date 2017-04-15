.. _c_library_v2:

标准 C 库
##################

为了满足内核的需求，Zephyr 当前提供了标准 C 库的一个最小子集，主要用于字符串的操作和显示。

如果您的应用程序需要更多功能，您可以提交贡献的代码以扩展 C 库，或者用其它的库作为替代。

Zephyr SDK 以及 Zephyr 所支持的其它工具链都带有基于 ``newlib`` 的裸机 C 库。您可以通过在应用程序的配置文件中添加选项 :option:`CONFIG_NEWLIB_LIBC` 来使能该库。:file:`lib/libc/newlib/libc-hooks.c` 是 ``newlib`` 中的一部分，它包含一系列的钩子。Zephyr 内核服务中会使用到这些钩子。
