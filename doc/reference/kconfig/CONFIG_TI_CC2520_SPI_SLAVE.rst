:orphan:

.. title:: TI_CC2520_SPI_SLAVE

.. option:: CONFIG_TI_CC2520_SPI_SLAVE:
.. _CONFIG_TI_CC2520_SPI_SLAVE:

This option sets the SPI slave number SPI controller has to switch
to when dealing with CC2520 chip.



:Symbol:           TI_CC2520_SPI_SLAVE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI slave linked to CC2520"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:81
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:60