:orphan:

.. title:: SYS_LOG_SENSOR_LEVEL

.. option:: CONFIG_SYS_LOG_SENSOR_LEVEL:
.. _CONFIG_SYS_LOG_SENSOR_LEVEL:

Sets log level for sensor driver.
Levels are:

- 0 OFF: do not write

- 1 ERROR: only write SYS_LOG_ERR

- 2 WARNING: write SYS_LOG_WRN in addition to previous level

- 3 INFO: write SYS_LOG_INF in addition to previous levels

- 4 DEBUG: write SYS_LOG_DBG in addition to previous levels



:Symbol:           SYS_LOG_SENSOR_LEVEL
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

 *  "Sensor Log level" if SYS_LOG && SENSOR (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SYS_LOG && SENSOR (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/Kconfig:26