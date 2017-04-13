.. _code:

应用程序相关代码
###########################

应用程序相关的源代码通常被添加到应用程序的 :file:`src` 目录。如果应用程序需要添加大量的源文件，开发者可以在 :file:`src` 将它们组织为子目录形式（目录深度没有限制）。开发者必须为 :file:`src` 目录及其每个子目录提供相应的 Makefile 文件。

.. note::

   这些 Makefile 与位于应用程序顶层 :file:`~/app` 下的 Makefile 有一定的区别。

应用程序相关的源代码不能使用内核所保留的符号名前缀。详细信息请参考 `命名规范 <https://wiki.zephyrproject.org/view/Coding_conventions#Naming_Conventions>`_.

下列需且适用于 :file:`src` 目录及其子目录下的所有 Makefile。

* 在编译过程中，Kbuild 通过匹配应用程序的 Makefile 中的文件名来标识需要被编译到目标文件中的源文件。

  .. important::

    编译应用程序时，未被任何 Makefile 引用的源文件不会被编译。

* Makefile 不能直接引用源代码，它只能引用由源代码文件生成的目标文件（:file:`.o` 文件）。

* Makefile 只能引用当前目录或者其子目录中的文件。

* Makefile 可以在一行引用多个实体，但是一行中最多引用一个目录。


#. 在 :file:`src` 下面为您的源代码创建目录结构，并将源代码添加到里面。

#. 在 :file:`src` 目录下创建一个 :file:`Makefile`，并为 :file:`src` 下面的每个子目录创建一个 :file:`Makefile`。

   a) 使用下面的语法添加引用：

      .. code-block:: make

         obj-y += file1.o file2.o

   b) 使用下面的语法添加对目录的引用：

      .. code-block:: make

         obj-y += directory_name/**


这个例子来自于哲学家例程，相应目录是 :file:`\$ZEPHYR_BASE/samples/philosophers/src`。

.. code-block:: make

   obj-y = main.o

支持编译第三方库
=============================================

您可以编译位于应用程序的 :file:`src` 目录之外的库代码，但是需要牢记的是，应用程序代码和库代码最终会被编译为同一个应用程序二进制接口（Application Binary Interface，ABI）。对于大多数架构，都存在用于控制 ABI 的编译标志。库和应用程序的编译标志通常都是相同的。 It may also be useful for glue code to have access to Zephyr kernel header files.

为了便于集成第三方组件，Zephyr 编译系统包含了一个特殊的编译对象 —— ``outputexports``。``outputexports``从 Zephyr 编译系统中拿取了大量临界变量（critical variables），并将它们拷贝到了 :file:`Makefile.export` 中，因此三方库的编译系统可以使用这些临界变量。

推荐将下列变量用于第三方库的编译中（完整的变量列表请参考 :file:`Makefile.export`）：

* ``CROSS_COMPILE``，以及一些相关的约定俗成的用于调用交叉工具的变量（包括  ``AR``、``AS``、``CC``、``CXX``、``CPP`` 和 ``LD``）。

* ``ARCH``、``BOARD``，以及一些用于标识 Zephyr 内核版本的变量。

* 需要按顺序添加到 ``CFLAGS``（或者 ``CXXFLAGS``）的变量 ``KBUILD_CFLAGS``、``NOSTDINC_FLAGS`` 和 ``ZEPHYRINCLUDE``。

* 所有的 Kconfig 变量，以基于 Zephyr 内核配置自动使能/禁止库代码的功能。

:file:`samples/static_lib` 是用于演示这些功能的示例工程。
