:orphan:

.. title:: SYS_LOG_GPIO_LEVEL

.. option:: CONFIG_SYS_LOG_GPIO_LEVEL:
.. _CONFIG_SYS_LOG_GPIO_LEVEL:

Sets log level for GPIO drivers

Levels are:

- 0 OFF, do not write

- 1 ERROR, only write SYS_LOG_ERR

- 2 WARNING, write SYS_LOG_WRN in adition to previous level

- 3 INFO, write SYS_LOG_INF in adition to previous levels

- 4 DEBUG, write SYS_LOG_DBG in adition to previous levels



:Symbol:           SYS_LOG_GPIO_LEVEL
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO drivers log level" if SYS_LOG (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SYS_LOG (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig:28