:orphan:

.. title:: GDB_SERVER_INTERRUPT_DRIVEN

.. option:: CONFIG_GDB_SERVER_INTERRUPT_DRIVEN:
.. _CONFIG_GDB_SERVER_INTERRUPT_DRIVEN:

This option enables interrupt support for GDB Server.



:Symbol:           GDB_SERVER_INTERRUPT_DRIVEN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable GDB interrupt mode" if GDB_SERVER (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: GDB_SERVER (value: "n")
:Selects:

 *  :option:`CONFIG_CONSOLE_HANDLER` if GDB_SERVER (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/debug/Kconfig:103