:orphan:

.. title:: SYS_LOG_DEFAULT_LEVEL

.. option:: CONFIG_SYS_LOG_DEFAULT_LEVEL:
.. _CONFIG_SYS_LOG_DEFAULT_LEVEL:

Sets log level for modules which don't specify it explicitly. When
set to 0 it means log wont be activated for those modules.
Levels are:
0 OFF, do not write by default
1 ERROR, default to only write SYS_LOG_ERR
2 WARNING, default to write SYS_LOG_WRN in adition to previous level
3 INFO, default to write SYS_LOG_INF in adition to previous levels
4 DEBUG, default to write SYS_LOG_DBG in adition to previous levels



:Symbol:           SYS_LOG_DEFAULT_LEVEL
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

 *  "Default log level" if SYS_LOG (value: "n")
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
 * ../misc/Kconfig:292