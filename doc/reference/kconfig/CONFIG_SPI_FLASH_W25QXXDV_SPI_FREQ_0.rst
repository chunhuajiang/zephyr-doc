:orphan:

.. title:: SPI_FLASH_W25QXXDV_SPI_FREQ_0

.. option:: CONFIG_SPI_FLASH_W25QXXDV_SPI_FREQ_0:
.. _CONFIG_SPI_FLASH_W25QXXDV_SPI_FREQ_0:

This option sets the SPI controller's frequency. Beware this value
depends on the SPI controller being used and also on the system
clock.



:Symbol:           SPI_FLASH_W25QXXDV_SPI_FREQ_0
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI system frequency" if SPI_FLASH_W25QXXDV (value: "n")
:Default values:

 *  4 (value: "n")
 *   Condition: SPI_FLASH_W25QXXDV (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/flash/Kconfig:55