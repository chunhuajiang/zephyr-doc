.. _apps_common_procedures:

通用规程
#################

这里提供了许多规程所通用的指令。

规程
**********

.. _set_environment_variables:

设置环境变量
=============================

当您每次打开终端时，都需要设置环境变量。

步骤
-----

1. 在 Shell 终端控制台输入与您工具链相符的 :command:`export` 目录

   对于Zephyr SDK:

     .. code-block:: console

      $ export ZEPHYR_GCC_VARIANT=zephyr
      $ export ZEPHYR_SDK_INSTALL_DIR=<yocto-installation-path>

2. 设置环境变量 :envvar:`\$ZEPHYR_BASE`。进入内核的安装目录，输入：

      .. code-block:: console

         $ source zephyr-env.sh
