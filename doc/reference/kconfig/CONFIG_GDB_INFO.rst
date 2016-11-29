:orphan:

.. title:: GDB_INFO

.. option:: CONFIG_GDB_INFO:
.. _CONFIG_GDB_INFO:

This option enables the kernel to collect additional information
during interrupts, exceptions, and context switches. This information
is required for task-aware debugging with GDB.



:Symbol:           GDB_INFO
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Task-aware debugging with GDB"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:64