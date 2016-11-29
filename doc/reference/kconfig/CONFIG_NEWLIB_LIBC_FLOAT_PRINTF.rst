:orphan:

.. title:: NEWLIB_LIBC_FLOAT_PRINTF

.. option:: CONFIG_NEWLIB_LIBC_FLOAT_PRINTF:
.. _CONFIG_NEWLIB_LIBC_FLOAT_PRINTF:

Build with floating point printf enabled. This will increase the size of
the image.



:Symbol:           NEWLIB_LIBC_FLOAT_PRINTF
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Build with newlib float printf" if NEWLIB_LIBC (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NEWLIB_LIBC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:126