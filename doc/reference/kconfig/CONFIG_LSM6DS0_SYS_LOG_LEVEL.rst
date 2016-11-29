:orphan:

.. title:: LSM6DS0_SYS_LOG_LEVEL

.. option:: CONFIG_LSM6DS0_SYS_LOG_LEVEL:
.. _CONFIG_LSM6DS0_SYS_LOG_LEVEL:

Sets log level for LSM6DS0 driver.
Levels are:

- 0 OFF: do not write

- 1 ERROR: only write SYS_LOG_ERR

- 2 WARNING: write SYS_LOG_WRN in addition to previous level

- 3 INFO: write SYS_LOG_INF in addition to previous levels

- 4 DEBUG: write SYS_LOG_DBG in addition to previous levels



:Symbol:           LSM6DS0_SYS_LOG_LEVEL
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

 *  "LSM6DS0 Log level" if SYS_LOG && LSM6DS0 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SYS_LOG && LSM6DS0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm6ds0/Kconfig:28