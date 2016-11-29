:orphan:

.. title:: SYS_LOG_OVERRIDE_LEVEL

.. option:: CONFIG_SYS_LOG_OVERRIDE_LEVEL:
.. _CONFIG_SYS_LOG_OVERRIDE_LEVEL:

Forces a minimum log level for all modules. Modules use their
specified level if it is greater than this option, otherwise they use
the level specified by this option instead of their default or
whatever was manually set.
Levels are:
0 OFF, do not override
1 ERROR, override to write SYS_LOG_ERR
2 WARNING, override to write SYS_LOG_WRN in adition to previous level
3 INFO, override to write SYS_LOG_INF in adition to previous levels
4 DEBUG, override to write SYS_LOG_DBG in adition to previous levels



:Symbol:           SYS_LOG_OVERRIDE_LEVEL
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 4]
:Prompts:

 *  "Override lowest log level" if SYS_LOG (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SYS_LOG (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:308