:orphan:

.. title:: SPI_FLASH_W25QXXDV

.. option:: CONFIG_SPI_FLASH_W25QXXDV:
.. _CONFIG_SPI_FLASH_W25QXXDV:

The configuration item CONFIG_SPI_FLASH_W25QXXDV:

:Symbol:           SPI_FLASH_W25QXXDV
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI NOR Flash Winbond W25QXXDV" if SPI && FLASH (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 FLASH && SPI && BOARD_ARDUINO_101 (value: "n")
:Locations:
 * ../drivers/flash/Kconfig:29
 * ../boards/x86/arduino_101/Kconfig.defconfig:51