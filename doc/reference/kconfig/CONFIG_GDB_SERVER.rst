:orphan:

.. title:: GDB_SERVER

.. option:: CONFIG_GDB_SERVER:
.. _CONFIG_GDB_SERVER:

This option enables the GDB Server support.



:Symbol:           GDB_SERVER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable GDB Server [EXPERIMENTAL]"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_CACHE_FLUSHING`
 *  :option:`CONFIG_REBOOT`
 *  :option:`CONFIG_MEM_SAFE`
 *  :option:`CONFIG_DEBUG_INFO`
 *  :option:`CONFIG_UART_CONSOLE_DEBUG_SERVER_HOOKS`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/debug/Kconfig:84