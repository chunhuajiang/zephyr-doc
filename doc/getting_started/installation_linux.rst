.. _installation_linux:

在 Linux 下搭建开发环境
######################################

本节描述如何搭建一个 Linux 开发环境。

完成这些操作后，您将能够在如下 Linux 发行版上编译、运行您的 Zephyr 应用程序：

* Ubuntu 14.04 LTS 64-bit
* Fedora 22 64-bit

您应该根据需要选择 Ubuntu 或者 Fedora 的指令。

安装主机操作系统
**************************************
Zephyr 项目的软件组件（包括内核）已经在 Ubuntu 和 Fedora 上面测试通过了。
安装 Ubuntu 和 Fedora 的方法不在本文档的讨论范围内。

更新您的操作系统
****************************

在进行编译前，请先确保您的操作系统已经更新到最新了。对于 Ubuntu，您需要先
更新可用软件包的本地数据库列表：

.. code-block:: console

   $ sudo apt-get update
   $ sudo apt-get upgrade

对于 Fedora：

.. code-block:: console

   $ sudo dnf upgrade

.. _linux_required_software:

安装需求和依赖
****************************************

请按照下面的方法使用 apt-get 或者 dnf 进行安装。

对于 Ubuntu：

.. code-block:: console

   $ sudo apt-get install git make gcc g++ python3-ply ncurses-dev

对于 Fedora：

.. code-block:: console

   $ sudo dnf group install "Development Tools"
   $ sudo dnf install git make gcc glibc-static libstdc++-static python3-ply ncurses-devel

.. _zephyr_sdk:

安装 Zephyr 软件开发套件（SDK）
==============================================

Zephyr 的 :abbr:`SDK (Software Development Kit)` 中包含为其支持的所有架构编译内核
所需的工具和交叉编译器。此外，它还包括主机上的工具，例如定制的 QEMU 以及编译主机
工具的主机编译器。SDK 支持如下架构：

* :abbr:`IA-32 (Intel Architecture 32 bits)`

* :abbr:`ARM (Advanced RISC Machines)`

* :abbr:`ARC (Argonaut RISC Core)`

按照下面的步骤就能在您的 Linux 主机系统上安装 SDK。

#. 下载最新的 SDK 自解压二进制文件。

   访问 `Zephyr SDK archive`_ 可查找到所有可有的（包括最新的） SDK。

   您也可以使用下面的摩纳哥咯来现在所需的版本，其中需要将 <version> 替换为您想下载的版本号。

   .. code-block:: console

      $ wget https://nexus.zephyrproject.org/content/repositories/releases/org/zephyrproject/zephyr-sdk/<version>-i686/zephyr-sdk-<version>-i686-setup.run

#. 运行自解压二进制文件。

   .. code-block:: console

      $ chmod +x zephyr-sdk-<version>-i686-setup.run

      $ ./zephyr-sdk-<version>-i686-setup.run

   如果将 SDK 按照到用户的 home 目录，则没有必要是使用 `sudo` 权限。

#. 遵循屏幕上提上的指令进行操作。工具链的默认安装路径位于 :file:`/opt/zephyr-sdk/`。如果要
   安装到默认路径，您需要使用 sudo。推荐将 SDK 安装到您的 home 目录，而不是系统目录。

#. 要使用 Zephyr SDK，您还需要 export 如下的环境变量，并指明 SDK 的安装路径，输入：

   .. code-block:: console

      $ export ZEPHYR_GCC_VARIANT=zephyr

      $ export ZEPHYR_SDK_INSTALL_DIR=<sdk installation directory>

如果您希望将来在新的会话中也是使用该工具链，您可以上面的设置添加到文件 :file:`${HOME}/.zephyrrc` 中，例如：

  .. code-block:: console

     $ cat <<EOF > ~/.zephyrrc
     export ZEPHYR_GCC_VARIANT=zephyr
     export ZEPHYR_SDK_INSTALL_DIR=/opt/zephyr-sdk
     EOF

.. _Zephyr SDK archive:
   https://nexus.zephyrproject.org/content/repositories/releases/org/zephyrproject/zephyr-sdk/
