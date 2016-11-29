:orphan:

.. title:: SYS_LOG_TI_CC2520_LEVEL

.. option:: CONFIG_SYS_LOG_TI_CC2520_LEVEL:
.. _CONFIG_SYS_LOG_TI_CC2520_LEVEL:

Sets log level for 802.15.4 CC2520 driver.

Levels are:

- 0 OFF, do not write

- 1 ERROR, only write SYS_LOG_ERR

- 2 WARNING, write SYS_LOG_WRN in adition to previous level

- 3 INFO, write SYS_LOG_INF in adition to previous levels

- 4 DEBUG, write SYS_LOG_DBG in adition to previous levels



:Symbol:           SYS_LOG_TI_CC2520_LEVEL
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "CC2520 driver log level"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:41