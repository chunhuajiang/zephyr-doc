.. _installing_zephyr_mac:

在 Mac OS 下搭建开发环境
#######################################

本节描述如何搭建 Mac OS 开发环境。

完成这些操作后，您将能够在如下版本的 Mac OS 下编译、运行 Zephyr 应用程序。

* Mac OS X 10.11 (El Capitan)

在 OS X 上开发 Zephyr 需要您自己编译工具链。不过，如果您的目标架构已经有 OS X 
的工具链了，您可以直接使用它。

使用三方工具链
***************************

如果你想使用的架构已经有工具链，您可以参考 :ref:`third_party_x_compilers` 使用它。

例如，对于 Coretex-M 家族的核心，您可以使用三方工具链 GCC ARM Embedded。

.. _mac_requirements:

安装需求和依赖
****************************************

要在 Mac 上安装编译 Zephyr 内核的软件组件，您需要为使用编译系统的目标设备编译一个交叉编译器。

.. note::
   Minor version updates of the listed required packages might also
   work.

在进行编译前，请先确保您的系统已经更新到最新了。

首先，您需要安装 :program:`Homebrew` （OS X 默认未安装该包）。Homebrew 是一个免费、开源
的软件包管理系统，能简化苹果 OS X 操作系统上安装软件的过程。

请访问 `Homebrew site`_ 并按照该网站的安装指示安装 :program:`Homebrew`

在安装 Homebrew 的过程中，系统可能会提示您安装一些缺失的依赖，请按照指示进行安装。

安装完 Homebrew 后，请使用 brew 的命令行安装如下工具。

.. code-block:: console

   $ brew install gettext qemu help2man mpfr gmp coreutils wget python3

   $ brew tap homebrew/dupes

   $ brew install grep --with-default-names

   $ pip3 install ply

.. code-block:: console

   $ brew install crosstool-ng

您也可以从源码安装最新版的 :program:`crosstool-ng`。从 `crosstool-ng site`_ 下载最新版。
最新版通常支持最新发布的编译器。

.. code-block:: console

   $ wget
   http://crosstool-ng.org/download/crosstool-ng/crosstool-ng-1.22.0.tar.bz2

   $ tar xvf crosstool-ng-1.22.0.tar.bz2

   $ cd crosstool-ng/

   $ ./configure

   $ make

   $ make install

.. _setting_up_mac_toolchain:

设置工具链
************************

创建一个大小写敏感的文件系统
=====================================

编译编译器需要一个大小写敏感的文件系统。使用程序 :program:`diskutil` 创建一个 8 GB 的空白
镜像，且选择大小写敏感的文件系统（OS X 扩展（大小写敏感，日志式）），然后挂在它。

您也可以直接使用下面的脚本创建镜像：

.. code-block:: bash

   #!/bin/bash
   ImageName=CrossToolNG ImageNameExt=${ImageName}.sparseimage
   diskutil umount force /Volumes/${ImageName} && true
   rm -f ${ImageNameExt} && true
   hdiutil create ${ImageName} -volname ${ImageName} -type SPARSE -size 8g -fs HFSX
   hdiutil mount ${ImageNameExt}
   cd /Volumes/$ImageName

镜像被挂载后，它将位于目录 :file:`/Volumes` 下。进入该目录：

.. code-block:: console

   $ cd /Volumes/CrossToolNG

   $ mkdir build

   $ cd build

设置工具链选项
=============================

在 Zephyr 内核源码树下，我们为 ARM 和 X86 提供了两种配置，可用于预选择编译工具链的选项。
配置文件位于 :file:`${ZEPHYR_BASE}/scripts/cross_compiler/`。

.. code-block:: console

   $ cp ${ZEPHYR_BASE}/scripts/cross_compiler/x86.config .config


您可以使用配置菜单创建一个新的配置或者基于已有的配置进行修改：

.. code-block:: console

   $ ct-ng menuconfig

验证工具链的配置
============================================

建议在编译工具链前对配置进行一个快速校验。

1. 打开生成的配置文件 :file:`.config`。

2. 假设镜像被挂在到目录 :file:`/Volumes/CrossToolNG` 下。确认存在以下代码：

.. code-block:: bash

   ...
   CT_LOCAL_TARBALLS_DIR="/Volumes/CrossToolNG/src"
   # CT_SAVE_TARBALLS is not set
   CT_WORK_DIR="${CT_TOP_DIR}/.build"
   CT_PREFIX_DIR="/Volumes/CrossToolNG/x-tools/${CT_TARGET}"
   CT_INSTALL_DIR="${CT_PREFIX_DIR}"
   # Following options prevent link errors
   CT_WANTS_STATIC_LINK=n
   CT_CC_STATIC_LIBSTDCXX=n
   ...

编译工具链
======================

要编译工具链，请输入：

.. code-block:: console

   $ ct-ng build

上面的过程需要一定的事件。当编译完成后，工具链将位于 :file:`/Volumes/CrossToolNG/x-tools`
 目录下。

如果您还需要在您的环境中支持其它架构，请重复上面的步骤。

要在 Zephyr 中使用工具链，您还需要 export 下面的环境变量，知名工具链的安装路径：

.. code-block:: console

   $ export ZEPHYR_GCC_VARIANT=xtools

   $ export XTOOLS_TOOLCHAIN_PATH=/Volumes/CrossToolNG/x-tools


如果您希望将来新在的会话中也是使用该工具链，您可以上面的设置添加到文件 :file:`${HOME}/.zephyrrc` 中，例如：

.. code-block:: console

   $ cat <<EOF > ~/.zephyrrc
   export XTOOLS_TOOLCHAIN_PATH=/Volumes/CrossToolNG/x-tools
   export ZEPHYR_GCC_VARIANT=xtools
   EOF

.. _Homebrew site: http://brew.sh/

.. _crosstool-ng site: http://crosstool-ng.org
