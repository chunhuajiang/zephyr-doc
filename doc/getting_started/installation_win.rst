.. _installing_zephyr_win:

在 Windows 下设置开发环境
########################################

本节描述如何在微软的 Windows 环境下配置您的开发环境并编译 Zephyr 应用程序。

本节的内容在如下的 Windows 版本下进行了编译、运行 Zephyr 应用程序例程的测试：

* Windows 8.1

更新您的操作系统
****************************

在编译之前，请确保你所运行的 Windows 系统已经安装了最新的更新包。

.. _windows_requirements:

安装需求和依赖
****************************************

为了在 Windows 上安装编译 Zephyr 应用程序所需的软件组件，您需要编译或运行
一个工具链。

安装 :program:`GIT`。进入 `GIT Download`_ 获取最新版的软件副本。

安装 :program:`Python 2.7`。进入 `Python Download`_ 获取 2.7 版的 Python。

安装 :program:`MinGW`。MinGW 是本地 Windows 应用程序的最小化 GNU 开发环境。
Zephyr 的编译系统将在该工具集上运行。进入站点 `MinGW Home`_  下载程序，并使用
它的安装器 `mingw-get-setup.exe` 安装如下程序：

* mingw-developer-toolkit
* mingw32-base
* msys-base
* msys-binutils
* msys-console
* msys-w32api

启动 `MSYS console`。安装器不会为您创建快捷方式，启动脚本是 :file:`C:\\MinGW\\msys\\1.0\\msys.bat.`。
我们需要在文件 :file:`/etc/fstab` 中添加如下两行：

.. code-block:: console

   #Win32_Path     Mount_Point
   c:/mingw             /mingw

最简单的方法是将文件 :file:`fstab.sample` 拷贝为 :file:`fstab`，并确定新文件
:file:`fstab` 中包含上面两行。

.. code-block:: console

   $ cp /etc/fstab.sample /etc/fstab
   $ cat /etc/fstab

在环境变量 :envvar:`PATH` 中配置 Python 和 MinGW 的安装路劲。

.. note:: `PYTHON_PATH` 路劲的格式必须是 linux 格式。例如，Python 默认的安装路劲是 :file:`C:\\python27`，
   应该写为 :file:`/c/python27/`。

.. code-block:: console

   export PYTHON_PATH=/c/python27
   export PATH=$PATH:${PYTHON_PATH}
   export MINGW_DIR=/c/MinGW

Pthread 库
===============

Zephyr OS 编译时依赖于 Pthread 库。安装 Msys 时会安装该库。不过，如果最小化安
装没有提供该库，您也可以根据下面的命令安装：

.. code-block:: console

   mingw-get install libpthread

GNU Regex C 库
===================

Zephyr 编译时也依赖于 GNU regex 库。Msys 自身已实现了该库，您可以在 MinGw 和 Msys 的官方仓库 
 :`MinGW Repository`_ 下载。使用下面的命令安装该库：

.. code-block:: console

   mingw-get update
   mingw-get install msys-libregex-dev --all-related

更新您系统的环境变量，以确保 C 编译器和链接器能找到库文件：

.. code-block:: console

   export LIBRARY_PATH=$LIBRARY_PATH:/c/mingw/msys/1.0/lib
   export C_INCLUDE_PATH=$C_INCLUDE_PATH:/c/mingw/msys/1.0/include

安装工具链
======================

编译系统能使用您系统上所安装的任何工具链。

Zephyr 的编译系统使用 ISSM 2016 (Intel System Studio for Microcontrollers) 测试过。

您可以从 Inter 开发者专区 `ISSM 2016 Download`_ 下载 ISSM，然后将其安装到您的系统上。

最后，您还需要为 ISSM 2016 配置环境变量。例如，使用 ISSM 的默认安装路径：
:file:`C:/IntelSWTools/ISSM_2016`

.. code-block:: console

    export ZEPHYR_GCC_VARIANT=issm
    export ISSM_INSTALLATION_PATH=C:/IntelSWTools/ISSM_2016

.. note:: The format of the location for the ISSM installation directory
   (e.g. :envvar:`ISSM_INSTALLATION_PATH`) must be in the windows format.

.. _GIT Download: https://git-scm.com/download/win
.. _Python Download: https://www.python.org/downloads/
.. _MinGW Home: http://www.mingw.org/
.. _MinGW Repository: http:sourceforge.net/projects/mingw/files/
.. _ISSM 2016 Download: https://software.intel.com/en-us/intel-system-studio-microcontrollers
