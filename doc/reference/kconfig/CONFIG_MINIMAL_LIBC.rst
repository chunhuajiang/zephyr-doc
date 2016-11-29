:orphan:

.. title:: MINIMAL_LIBC

.. option:: CONFIG_MINIMAL_LIBC:
.. _CONFIG_MINIMAL_LIBC:

Build integrated minimal c library. This integrated library is available
to support kernel functionality and test cases. It is not designed to be
used with applications. For applications, please use an external C
library such as newlib.



:Symbol:           MINIMAL_LIBC
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Build minimal c library"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:108