.. _kbuild:

编译系统用户指南
#######################

Zephyr 内核的编译系统基于 Linux 内核所使用的 Kbuild。这样，内核包含了 Linux 所使用的递归模型和使用 Kconfig 实现的配置模型。

与 Linux 的 Kbuild 不同的是，Zephyr 的编译过程是由应用程序触发。因此，该编译系统需要一个应用程序来进行初始化，然后才会编译内核源代码。该系统将内核和应用程序编译为一个单一的镜像。

.. toctree::
   :maxdepth: 1

   kbuild_kconfig
   ../kconfig/index.rst
   kbuild_makefiles
   kbuild_project
