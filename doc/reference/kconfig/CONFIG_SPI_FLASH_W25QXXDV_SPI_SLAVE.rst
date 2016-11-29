:orphan:

.. title:: SPI_FLASH_W25QXXDV_SPI_SLAVE

.. option:: CONFIG_SPI_FLASH_W25QXXDV_SPI_SLAVE:
.. _CONFIG_SPI_FLASH_W25QXXDV_SPI_SLAVE:

This option sets the SPI slave number the SPI controller has to switch
to when dealing with WinBond SPI flash chip.



:Symbol:           SPI_FLASH_W25QXXDV_SPI_SLAVE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI slave linked to spi flash" if SPI_FLASH_W25QXXDV (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 FLASH && SPI && BOARD_ARDUINO_101 && SPI_FLASH_W25QXXDV (value: "n")
:Locations:
 * ../drivers/flash/Kconfig:64
 * ../boards/x86/arduino_101/Kconfig.defconfig:64