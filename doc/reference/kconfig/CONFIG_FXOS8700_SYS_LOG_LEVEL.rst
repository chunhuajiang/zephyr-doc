:orphan:

.. title:: FXOS8700_SYS_LOG_LEVEL

.. option:: CONFIG_FXOS8700_SYS_LOG_LEVEL:
.. _CONFIG_FXOS8700_SYS_LOG_LEVEL:

Sets log level for FXOS8700 driver.
Levels are:

- 0 OFF: do not write

- 1 ERROR: only write SYS_LOG_ERR

- 2 WARNING: write SYS_LOG_WRN in addition to previous level

- 3 INFO: write SYS_LOG_INF in addition to previous levels

- 4 DEBUG: write SYS_LOG_DBG in addition to previous levels



:Symbol:           FXOS8700_SYS_LOG_LEVEL
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

 *  "Log level" if SYS_LOG && FXOS8700 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SYS_LOG && FXOS8700 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/fxos8700/Kconfig:25