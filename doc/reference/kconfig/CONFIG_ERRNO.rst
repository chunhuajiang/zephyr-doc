:orphan:

.. title:: ERRNO

.. option:: CONFIG_ERRNO:
.. _CONFIG_ERRNO:

Enable per-thread errno in the kernel. Application and library code must
include errno.h provided by the C library (libc) to use the errno
symbol. The C library must access the per-thread errno via the
_get_errno() symbol.



:Symbol:           ERRNO
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable errno support"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:192