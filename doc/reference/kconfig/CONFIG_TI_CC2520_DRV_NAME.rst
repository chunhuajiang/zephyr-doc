:orphan:

.. title:: TI_CC2520_DRV_NAME

.. option:: CONFIG_TI_CC2520_DRV_NAME:
.. _CONFIG_TI_CC2520_DRV_NAME:

This option sets the driver name



:Symbol:           TI_CC2520_DRV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "TI CC2520 Driver's name"
:Default values:

 *  "cc2520"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:60