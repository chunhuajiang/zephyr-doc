.. _application:

应用程序开发入门
##############################


概述
********
Zephyr 内核的编译系统是基于 Linux 内核所只用的 Kbuild 系统之上而来的。

编译系统是一个以应用程序为中心的系统，它需要一个应用程序来初始化需要编译的内核源码树。应用程序的编译会驱使应用程序和内核的配置、编译过程的发生，并将它们最终编译成一个单一的二进制文件。

Zephyr 内核的基本目录包括内核源代码、配置选项以及内核的一些预定义编译选项。

位于应用程序目录中的文件包括应用程序的预定义（例如应用程序相关的配置选项）和应用程序的源代码，它最终会与内核链接在一起。

一个最简单的应用程序由如下结构构成：

* **应用程序源代码文件**: 应用程序通常会提供一个或多个由 C 或者汇编语言编写的应用程序相关的文件。这些文件通常位于一个叫做 :file:`src` 的子目录中。

* **内核配置文件**: 应用程序通常还会提供一个配置文件（:file:`.conf`），用于指定一个或多个内核配置后选项相关的值。如果被忽略，则将会使用应用程序已存在的内核配置选项值；如果应用程序没有该选项值，则将会使用内核的默认配置值。

* **Makefile**: 该文件用于告诉编译系统如何查找上面所提供到文件以及目标板配置文件。

编写好应用程序后，您只需要一个简单的 ``make`` 命令即可进行编译。编译结果位于一个叫做 :file:`outdir/BOARD` 的子目录中。 该目录中包含了编译的过程中产生的文件，其中比较重要的几个文件包括：

* :file:`.config` 文件，包含用于编译应用程序的配置。

* 各种目标文件（:file:`.o` 和 :file:`.a`），包含自定义编译的内核和应用程序相关的代码。

* :file:`zephyr.elf` 文件，是最终由内核和应用程序链接在一起生成的可执行文件。

应用程序的组织结构
*********************

开发一个新的应用程序时，您需要为应用程序创建一个目录，为应用程序源代码创建一个子目录；这种方式更容易以内核所期望的结构来组织目录和文件。

#. 在内核的安装目录树外面创建一个新的目录。通常，这是你的工作空间目录。

#. 在控制台终端，进入一个您所虚妄存放应用程序的目录。

#. 创建应用程序目录，输入：

   .. code-block:: console

      $ mkdir app

   .. note::

      本文假设该目录是 :file:`~/app`。

#. 在 :file:`~/app` 下面创建一个源码目录：

   .. code-block:: console

      $ cd app
      $ mkdir src

   创建之后，该应用程序的目录结构是：

   .. code-block:: console

      -- app
         |-- src


应用程序的预定义
**********************

应用程序通过包含内核所提供的 Makefile.inc 文件集成到编译系统中。

.. code-block:: make

   include $(ZEPHYR_BASE)/Makefile.inc

下列预定义变量用于配置工程：

* :makevar:`ZEPHYR_BASE`: Sets the path to the kernel's base directory.
  This variable is usually set by the :file:`zephyr_env.sh` script.
  It can be used to get the kernel's base directory, as used in the
  Makefile.inc inclusion above, or it can be overridden to select an
  specific instance of the kernel.

* :makevar:`PROJECT_BASE`: Provides the developer's application project
  directory path. It is set by the :file:`Makefile.inc` file.

* :makevar:`SOURCE_DIR`: Overrides the default value for the application's
  source code directory. The developer source code directory is set to
  :file:`$(PROJECT_BASE/)src/` by default. This directory name should end
  with slash **'/'**.

* :makevar:`BOARD`: Selects the board that the application's
  build will use for the default configuration.

* :makevar:`CONF_FILE`: Indicates the name of a configuration fragment file.
  This file includes the kconfig configuration values that override the
  default configuration values.

* :makevar:`O`: Optional. Indicates the output directory that Kconfig uses.
  The output directory stores all the files generated during the build
  process. The default output directory is the :file:`$(PROJECT_BASE)/outdir`
  directory.


Makefile
*********

概述
========

The build system defines a set of conventions for the correct use of Makefiles
in the kernel source directories. The correct use of Makefiles is driven by the
concept of recursion.

In the recursion model, each Makefile within a directory includes the source
code and any subdirectories to the build process. Each subdirectory follows
the same principle. Developers can focus exclusively in their own work. They
integrate their module with the build system by adding a very simple Makefile
following the recursive model.

.. _makefile_conventions:

Makefile 的约定
====================

The following conventions restrict how to add modules and Makefiles to the
build system. These conventions ensure the correct implementation of the
recursive model.

* Each source code directory must contain a single Makefile. Directories
  without a Makefile are not considered source code directories.

* The scope of every Makefile is restricted to the contents of that directory.
  A Makefile can only make a direct reference to files and subdirectories on the
  same level or below.

* Makefiles list the object files that are included in the link process. The
  build system finds the source file that generates the object file by matching
  the object file name to the source file.

* Parent directories add their child directories into the recursion model.

* The root Makefile adds the directories in the kernel base directory into the
  recursion model.

添加源文件
===================

The Makefile must refer the source build indirectly, specifying the object file
that results from the source file using the :literal:`obj-y` variable. For
example, if the file that we want to add is a C file named :file:`<file>.c` the
following line should be added in the Makefile:

.. code-block:: make

   obj-y += <file>.o

.. note::

   The same method applies for assembly files with the .S extension.

Source files can be added conditionally using configuration options.  For
example, if the option ``CONFIG_VAR`` is set and it implies that a source
file must be added in the compilation process, then the following line adds the
source code conditionally:

.. code-block:: none

   obj-$(CONFIG_VAR) += <file>.o

添加目录 
==================

Add a subdirectory to the build system by editing the Makefile in its
directory.  The subdirectory is added using the :literal:`obj-y` variable. The
correct syntax to add a subdirectory into the build queue is:

.. code-block:: make

   obj-y += <directory_name>/

The backslash at the end of the directory name signals the build system that a
directory, and not a file, is being added to the build queue.

The conventions require us to add only one directory per line and never to mix
source code with directory recursion in a single :literal:`obj-y` line. This
helps keep the readability of the Makefile by making it clear when an item adds
an additional lever of recursion.

Directories can also be conditionally added:

.. code-block:: none

   obj-y-$(CONFIG_VAR) += <directory_name>/

The subdirectory must contain its own Makefile following the rules described in
:ref:`makefile_conventions`.


应用程序的 Makefile
********************

Create an application Makefile to define basic information, such as the board
configuration used by the application. The build system uses the Makefile to
build a :file:`zephyr.elf` image that contains both the application and the
kernel libraries.

#. Open the :file:`Makefile` and add the following mandatory
   entries using any standard text editor.

   .. note::

      Ensure that there is a space before and after each ``=``.

#. Add the name of the default board configuration for your application on a
   new line:

   .. code-block:: make

      BOARD = board_configuration_name

   The supported boards can be found in :ref:`boards`.

#. Add the name of the default kernel configuration file for your
   application on a new line:

   .. code-block:: make

      CONF_FILE ?= kernel_configuration_name

#. Include the mandatory :file:`Makefile` on a new line:

   .. code-block:: make

      include ${ZEPHYR_BASE}/Makefile.inc

#. Save and close the :file:`Makefile`.


Below is an example Makefile:

.. code-block:: make

   BOARD = qemu_x86
   CONF_FILE = prj.conf

   include ${ZEPHYR_BASE}/Makefile.inc

////////////////HERE/////////////////////   
   
Application Configuration
*************************

The application's kernel is configured using a set of configuration options
that can be customized for application-specific purposes.
The Zephyr build system takes a configuration option's value from the first
source in which it is specified.

The available sources are (in order):

#. The application's current configuration. (i.e. The :file:`.config` file.)

#. The application's default configuration. (i.e. The :file:`.conf` file.)

#. The board configuration used by the application.
   (i.e. The board's :file:`.defconfig` file.)

#. The kernel's default configuration.
   (i.e. One of the kernel's :file:`Kconfig` files.)

For information on available kernel configuration options, including
inter-dependencies between options, see the :ref:`configuration`.

Default Board Configuration
===========================

An application's :file:`.conf` file defines its default kernel configuration.
The settings in this file override or augment the board configuration settings.

The board configuration settings can be viewed
in :file:`\$ZEPHYR_BASE/boards/ARCHITECTURE/BOARD/BOARD_defconfig`.

.. note::

   When the default board configuration settings are sufficient for your
   application, a :file:`.conf` file is not needed. Skip ahead to
   :ref:`override_kernel_conf`.


#. Navigate to the :file:`app`, and create the :file:`prj.conf` file. Enter:

   .. code-block:: bash

       $ vim prj.conf

   The default name is :file:`prj.conf`. The filename must match the
   ``CONF_FILE`` entry in the application :file:`Makefile`.

#. Edit the file and add the appropriate configuration entries.

   a) Add each configuration entry on a new line.

   b) Begin each entry with ``CONFIG_``.

   c) Ensure that each entry contains no spaces
      (including on either side of the = sign).

   d) Use a # followed by a space to comment a line.

   The example below shows a comment line and a board
   configuration override in the :file:`prj.conf`.

   .. code-block:: c

       # Enable printk for debugging
       CONFIG_PRINTK=y

#. Save and close the file.

.. _override_kernel_conf:

Overriding Default Configuration
================================

Override the default board and kernel configuration to temporarily alter the
application's configuration, perhaps to test the effect of a change.

.. note::

   If you want to permanently alter the configuration you
   should revise the :file:`.conf` file.

Configure the kernel options using a menu-driven interface. While you can add
entries manually, using the configuration menu is a preferred method.


#. Run the :command:`make menuconfig` rule to launch the menu-driven interface.

   a) In a terminal session, navigate to the application directory
      (:file:`~/app`).

   b) Enter the following command:

      .. code-block:: bash

          $ make [BOARD=<type>] menuconfig

      A question-based menu opens that allows you to set individual configuration
      options.

      .. image:: figures/app_kernel_conf_1.png
           :width: 600px
           :align: center
           :alt: Main Configuration Menu

#. Set kernel configuration values using the following
   key commands:

   * Use the arrow keys to navigate within any menu or list.

   * Press :kbd:`Enter` to select a menu item.

   * Type an upper case :kbd:`Y` or :kbd:`N` in the
      square brackets :guilabel:`[ ]` to
      enable or disable a kernel configuration option.

   * Type a numerical value in the round brackets :guilabel:`( )`.

   * Press :kbd:`Tab` to navigate the command menu at the bottom of the display.

     .. note::

       When a non-default entry is selected for options that are non-numerical,
       an asterisk :kbd:`*` appears between the square brackets in the display.
       There is nothing added added the display when you select the option's
       default.

#. For information about any option, select the option and tab to
   :guilabel:`<Help >` and press :kbd:`Enter`.

   Press :kbd:`Enter` to return to the menu.

#. After configuring the kernel options for your application, tab to
   :guilabel:`< Save >` and press :kbd:`Enter`.

   The following dialog opens with the :guilabel:`< Ok >` command selected:

   .. image:: figures/app_kernel_conf_2.png
      :width: 400px
      :align: center
      :height: 100px
      :alt: Save Configuration Dialog


#. Press :kbd:`Enter` to save the kernel configuration options to the default
   file name; alternatively, type a file name and press :kbd:`Enter`.

   Typically, you will save to the default file name unless you are
   experimenting with various configuration scenarios.

   An :file:`outdir` directory is created in the application directory. The
   outdir directory contains symbolic links to files under
   :file:`\$ZEPHYR_BASE`.

   .. note::

      At present, only a :file:`.config` file can be built. If you have saved
      files with different file names and want to build with one of these,
      change the file name to :file:`.config`. To keep your original
      :file:`.config`, rename it to something other than :file:`.config`.

   Kernel configuration files, such as the :file:`.config` file, are saved
   as hidden files in :file:`outdir`. To list all your kernel configuration
   files, enter :command:`ls -a` at the terminal prompt.

   The following dialog opens, displaying the file name the configuration
   was saved to.

   .. image:: figures/app_kernel_conf_3.png
         :width: 400px
         :align: center
         :height: 150px
         :alt: Saved Configuration Name Dialog

#. Press :kbd:`Enter` to return to the options menu.

#. To load any saved kernel configuration file, tab to :guilabel:`< Load >` and
   press :kbd:`Enter`.

   The following dialog opens with the :guilabel:`< Ok >` command selected:

   .. image:: figures/app_kernel_conf_4.png
      :width: 400px
      :align: center
      :height: 175px
      :alt: Configuration File Load Dialog

#. To load the last saved kernel configuration file, press :guilabel:`< Ok >`,
   or to load another saved configuration file, type the file name, then select
   :guilabel:`< Ok >`.

#. Press :kbd:`Enter` to load the file and return to the main menu.

#. To exit the menu configuration, tab to :guilabel:`< Exit >` and press
   :kbd:`Enter`.

   The following confirmation dialog opens with the :guilabel:`< Yes >`
   command selected.

   .. image:: figures/app_kernel_conf_5.png
      :width: 400px
      :align: center
      :height: 100px
      :alt: Exit Dialog

#. Press :kbd:`Enter` to retire the menu display and return to the console
   command line.

Application-Specific Code
*************************

Application-specific source code files are normally added to the application's
:file:`src` directory. If the application adds a large number of files the
developer can group them into sub-directories under :file:`src`, to whatever
depth is needed. The developer must supply a :file:`Makefile` for the
:file:`src` directory, as well as for each sub-directory under :file:`src`.

.. note::

   These Makefiles are distinct from the top-level application Makefile
   that appears in :file:`~/app`.

Application-specific source code should not use symbol name prefixes that have
been reserved by the kernel for its own use. For more information, see

`Naming Conventions <https://wiki.zephyrproject.org/view/Coding_conventions#Naming_Conventions>`_.


The following requirements apply to all Makefiles in the :file:`src`
directory, including any sub-directories it may have.

* During the build process, Kbuild identifies the source files to compile
  into object files by matching the file names identified in
  the application's Makefile(s).

  .. important::

    A source file that is not referenced by any Makefile is not included
    when the application is built.

* A Makefile cannot directly reference source code. It can only
  reference object files (:file:`.o` files) produced from source code files.

* A Makefile can only reference files in its own directory or in the
  sub-directories of that directory.

* A Makefile may reference multiple files from a single-line entry.
  However, a separate line must be used to reference each directory.



#. Create a directory structure for your source code in :file:`src`
   and add your source code files to it.

#. Create a :file:`Makefile` in the :file:`src` directory. Then create
   an additional :file:`Makefile` in each of the sub-directories under
   the :file:`src` directory, if any.

   a) Use the following syntax to add file references:

      .. code-block:: make

         obj-y += file1.o file2.o

   b) Use the following syntax to add directory references:

      .. code-block:: make

         obj-y += directory_name/**


This example is taken from the Philosopher's Sample. To examine this file in
context, navigate to: :file:`\$ZEPHYR_BASE/samples/philosophers/src`.

.. code-block:: make

   obj-y = main.o


Support for building third-party library code
=============================================

It is possible to build library code outside the application's :file:`src`
directory but it is important that both application and library code targets
the same Application Binary Interface (ABI). On most architectures there are
compiler flags that control the ABI targeted, making it important that both
libraries and applications have certain compiler flags in common. It may also
be useful for glue code to have access to Zephyr kernel header files.

To make it easier to integrate third-party components, the Zephyr build system
includes a special build target, ``outputexports``, that takes a number of
critical variables from the Zephyr build system and copies them into
:file:`Makefile.export`. This allows the critical variables to be included by
wrapper code for use in a third-party build system.

The following variables are recommended for use within the third-party build
(see :file:`Makefile.export` for the complete list of exported variables):

* ``CROSS_COMPILE``, together with related convenience variables to call the
  cross-tools directly (including ``AR``, ``AS``, ``CC``, ``CXX``, ``CPP``
  and ``LD``).

* ``ARCH`` and ``BOARD``, together with several variables that identify the
  Zephyr kernel version.

* ``KBUILD_CFLAGS``, ``NOSTDINC_FLAGS`` and ``ZEPHYRINCLUDE`` all of which
  should normally be added, in that order, to ``CFLAGS`` (or
  ``CXXFLAGS``).

* All kconfig variables, allowing features of the library code to be
  enabled/disabled automatically based on the Zephyr kernel configuration.

:file:`samples/static_lib` is a sample project that demonstrates
some of these features.

Build an Application
********************

The Zephyr build system compiles and links all components of an application
into a single application image that can be run on simulated hardware or real
hardware.


#. Navigate to the application directory :file:`~/app`.

#. Enter the following command to build the application's :file:`zephyr.elf`
   image using the configuration settings for the board type specified
   in the application's :file:`Makefile`.

   .. code-block:: console

       $ make

   If desired, you can build the application using the configuration settings
   specified in an alternate :file:`.conf` file using the :code:`CONF_FILE`
   parameter. These settings will override the settings in the application's
   :file:`.config` file or its default :file:`.conf` file. For example:

   .. code-block:: console

       $ make CONF_FILE=prj.alternate.conf

   If desired, you can build the application for a different board type than the
   one specified in the application's :file:`Makefile` using the :code:`BOARD`
   parameter. For example:

   .. code-block:: console

       $ make BOARD=arduino_101

   Both the :code:`CONF_FILE` and :code:`BOARD` parameters can be specified
   when building the application.

Rebuilding an Application
*************************

Application development is usually fastest when changes are continually tested.
Frequently rebuilding your application makes debugging less painful
as the application becomes more complex. It's usually a good idea to
rebuild and test after any major changes to the application's source files,
Makefiles, or configuration settings.

.. important::

    The Zephyr build system rebuilds only the parts of the application image
    potentially affected by the changes. Consequently, rebuilding an application
    is often significantly faster than building it the first time.

Sometimes the build system doesn't rebuild the application correctly
because it fails to recompile one or more necessary files. You can force
the build system to rebuild the entire application from scratch with the
following procedure:


#. Navigate to the application directory :file:`~/app`.

#. Enter the following command to delete the application's generated files
   for the specified board type, except for the :file:`.config` file that
   contains the application's current configuration information.

   .. code-block:: console

       $ make [BOARD=<type>] clean

   Alternatively, enter the following command to delete *all* generated files
   for *all* board types, including the :file:`.config` files that contain
   the application's current configuration information for those board types.

   .. code-block:: console

       $ make pristine

#. Rebuild the application normally following the steps specified
   in `Build an Application`_ above.



Run an Application
******************

An application image can be run on real or emulated hardware. The kernel has
built-in emulator support for QEMU. It allows you to run and test an application
virtually, before (or in lieu of) loading and running it on actual target
hardware.

#. Open a terminal console and navigate to the application directory
   :file:`~/app`.

#. Enter the following command to build and run the application
   using a QEMU-supported board configuration, such as qemu_cortex_m3 or
   qemu_x86.

   .. code-block:: console

       $ make [BOARD=<type> ...] run

   The Zephyr build system generates a :file:`zephyr.elf` image file
   and then begins running it in the terminal console.

#. Press :kbd:`Ctrl A, X` to stop the application from running
   in QEMU.

   The application stops running and the terminal console prompt
   redisplays.

Application Debugging
*********************

This section is a quick hands-on reference to start debugging your
application with QEMU. Most content in this section is already covered on
`QEMU`_ and `GNU_Debugger`_ reference manuals.

.. _QEMU: http://wiki.qemu.org/Main_Page

.. _GNU_Debugger: http://www.gnu.org/software/gdb

In this quick reference you find shortcuts, specific environmental variables and
parameters that can help you to quickly set up your debugging environment.

The simplest way to debug an application running in QEMU is using the GNU
Debugger and setting a local GDB server in your development system through QEMU.

You will need an ELF binary image for debugging purposes.  The build system
generates the image in the output directory.  By default, the kernel binary name
is :file:`zephyr.elf`. The name can be changed using a Kconfig option.

We will use the standard 1234 TCP port to open a :abbr:`GDB (GNU Debugger)`
server instance. This port number can be changed for a port that best suits the
development environment.

You can run Qemu to listen for a "gdb connection" before it starts executing any
code to debug it.

.. code-block:: bash

   qemu -s -S <image>

will setup Qemu to listen on port 1234 and wait for a GDB connection to it.

The options used above have the following meaning:

* ``-S`` Do not start CPU at startup; rather, you must type 'c' in the
  monitor.
* ``-s`` Shorthand for :literal:`-gdb tcp::1234`: open a GDB server on
  TCP port 1234.

To debug with QEMU and to start a GDB server and wait for a remote connect, run
the following inside an application:

.. code-block:: bash

   make BOARD=qemu_x86 debugserver

The build system will start a QEMU instance with the CPU halted at startup
and with a GDB server instance listening at the TCP port 1234.

Using a local GDB configuration :file:`.gdbinit` can help initialize your GDB
instance on every run.
In this example, the initialization file points to the GDB server instance.
It configures a connection to a remote target at the local host on the TCP
port 1234. The initialization sets the kernel's root directory as a
reference.

The :file:`.gdbinit` file contains the following lines:

.. code-block:: bash

   target remote localhost:1234
   dir ZEPHYR_BASE

.. note::

   Substitute ZEPHYR_BASE for the current kernel's root directory.

Execute the application to debug from the same directory that you chose for
the :file:`gdbinit` file. The command can include the ``--tui`` option
to enable the use of a terminal user interface. The following commands
connects to the GDB server using :file:`gdb`. The command loads the symbol
table from the elf binary file. In this example, the elf binary file name
corresponds to :file:`zephyr.elf` file:

.. code-block:: bash

   $ gdb --tui zephyr.elf

.. note::

   The GDB version on the development system might not support the --tui
   option.

If you are not using a .gdbinit file, issue the following command inside GDB to
connect to the remove GDB server on port 1234:

.. code-block:: bash

   (gdb) target remote localhost:1234

Finally, The command below connects to the GDB server using the Data
Displayer Debugger (:file:`ddd`). The command loads the symbol table from the
elf binary file, in this instance, the :file:`zephyr.elf` file.

The :abbr:`DDD (Data Displayer Debugger)` may not be installed in your
development system by default. Follow your system instructions to install
it.

.. code-block:: bash

   ddd --gdb --debugger "gdb zephyr.elf"


Both commands execute the :abbr:`gdb (GNU Debugger)`. The command name might
change depending on the toolchain you are using and your cross-development
tools.
