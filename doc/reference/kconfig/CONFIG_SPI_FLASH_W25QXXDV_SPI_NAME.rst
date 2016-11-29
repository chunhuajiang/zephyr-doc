:orphan:

.. title:: SPI_FLASH_W25QXXDV_SPI_NAME

.. option:: CONFIG_SPI_FLASH_W25QXXDV_SPI_NAME:
.. _CONFIG_SPI_FLASH_W25QXXDV_SPI_NAME:

The configuration item CONFIG_SPI_FLASH_W25QXXDV_SPI_NAME:

:Symbol:           SPI_FLASH_W25QXXDV_SPI_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "spi controller device name" if SPI_FLASH_W25QXXDV (value: "n")
:Default values:

 *  ""
 *   Condition: SPI_FLASH_W25QXXDV (value: "n")
 *  "SPI_0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 FLASH && SPI && BOARD_ARDUINO_101 && SPI_FLASH_W25QXXDV (value: "n")
:Locations:
 * ../drivers/flash/Kconfig:34
 * ../boards/x86/arduino_101/Kconfig.defconfig:62