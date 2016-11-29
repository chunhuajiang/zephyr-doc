:orphan:

.. title:: TI_CC2520_SPI_DRV_NAME

.. option:: CONFIG_TI_CC2520_SPI_DRV_NAME:
.. _CONFIG_TI_CC2520_SPI_DRV_NAME:

This option is mandatory to set which SPI controller to use in order
to actually control the CC2520 chip.



:Symbol:           TI_CC2520_SPI_DRV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI driver's name to use to access CC2520"
:Default values:

 *  ""
 *   Condition: (none)
 *  SPI_1_NAME (value: "")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:66
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:56