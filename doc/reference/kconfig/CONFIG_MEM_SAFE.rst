:orphan:

.. title:: MEM_SAFE

.. option:: CONFIG_MEM_SAFE:
.. _CONFIG_MEM_SAFE:

Add the routines available in mem_safe.h to the system. This is added
as a kconfig option instead of simply linking against the library
because some implementations might require initialization.



:Symbol:           MEM_SAFE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable safe memory access"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 GDB_SERVER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/debug/Kconfig:22