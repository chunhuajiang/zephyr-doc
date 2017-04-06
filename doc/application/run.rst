.. _run:

运行与调试
###########################

运行应用程序
******************

应用程序镜像既可以运行在真实硬件上，也可以运行在模拟器上。Zephyr 内核已经包含了一个支持 QEMU 的内置模拟器，它允许你在将镜像加载、运行到真实目标硬件之前进行模拟仿真测试。

#. 打开一个中断控制台，并进入应用程序目录 :file:`~/app`。

#. 输入如下命令来使用一个 QEMU 所支持的板级配置（例如 qemu_cortex_m3 或者 qemu_x86）来编译、运行应用程序：

   .. code-block:: console

       $ make [BOARD=<type> ...] run

   Zephyr 编译系统先产生一个 :file:`zephyr.elf` 镜像文件，然后在终端控制台上面运行它。
   
#. 输入 :kbd:`Ctrl A, X` 可停止 QEMU 仿真的过程。

   应用程序将停止运行，然后终端会重新显示控制台的提示符。

调试应用程序
*********************

本节是利用 QEMU 调试应用程序的快速上手参考手册，里面的多数内容都已在 `QEMU`_ 和 `GNU_Debugger`_ 参考手册中涵盖。

.. _QEMU: http://wiki.qemu.org/Main_Page

.. _GNU_Debugger: http://www.gnu.org/software/gdb

在这个快速参考手册中，您可以找到有助于您快速设置您的调试环境的捷径、环境变量和参数。

调试运行在 QEMU 中的应用程序的最简单的方法是使用 GNU Debugger —— 通过 QEMU 在您的开发系统中设置一个本地的 GDB Server。

为了调试，您需要一个 ELF 格式的二进制镜像文件。编译系统会在输出目录里自动产生该镜像。默认情况下，内核镜像的名字是 :file:`zephyr.elf`，但是您也可以通过 Kconfig 选项对其进行修改。 

我们将使用表示的 1234 TCP 端口来打开一个 :abbr:`GDB (GNU Debugger)` 服务实例。您可以根据您的实际开发环境修改该端口号。

您可以让 QEMU 在执行代码前先监听 gdb 连接：

.. code-block:: bash

   qemu -s -S <image>

上面的代码会让 QEMU 监听端口 1234，并等待一个 GDB 连接。

上面使用的选项的含义是：

* ``-S`` 在 QEMU 启动时先不要启动 CPU；您需要在监视器中输入 'c' 时它才会继续运行。
* ``-s`` 这是 :literal:`-gdb tcp::1234`: 的简写，用于在 TCP 端口 1234 上面打开一个 GDB Server。

要达到上面的目录，您可以直接在应用程序的目录下输入如下命令：

.. code-block:: bash

   make BOARD=qemu_x86 debugserver

上面的命令会使编译系统启动 QEMU 实例，并让它在启动时挂起 CPU，并开启一个监听 1234 端口的 GDB Server。

使用本地 GDB 配置文件 :file:`.gdbinit` 有助于您每次运行时初始化 GDB 实例。在这个例子中，当初始化文件执行 GDB Server 实例时，它会尝试连接本地主机的端口号 1234 的 TCP 连接。初始化时会将内核的根目录作为参考目录。


The :file:`.gdbinit` file contains the following lines:

.. code-block:: bash

   target remote localhost:1234
   dir ZEPHYR_BASE

.. note::

   可以通过变量 ZEPHYR_BASE 替换当前内核的根目录。

在 :file:`gdbinit` 文件的同一目录下执行应用程序。如果需要使用中断用户接口，您可以在命令行包含 ``--tui`` 选项。 下面的命令将使用 :file:`gdb` 来连接 GDB Server。在这个例子里面，elf 文件的名字是 :file:`zephyr.elf`：

.. code-block:: bash

   $ gdb --tui zephyr.elf

.. note::

   某些开发系统的 GDB 版本可能不支持 --tui 选项。、

如果您没有使用 .gdbinit 文件，则需要在 GDB 里面发出如下命令来连接 GDB Server：

.. code-block:: bash

   (gdb) target remote localhost:1234

最后，您可以使用下面的命令来使用数据显示器调试器 （Data Displayer Debugger (:file:`ddd`)）来连接 GDB Server。 这个命令会从 elf 二进制文件中加载符号表。


.. code-block:: bash

   ddd --gdb --debugger "gdb zephyr.elf"

如果您的开发系统中默认没有安装 :abbr:`DDD (Data Displayer Debugger)`，请按照您系统对应的方法进行安装。
