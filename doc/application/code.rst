.. _code:

应用程序相关代码
###########################

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
