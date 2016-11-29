:orphan:

.. title:: SPI_FLASH_W25QXXDV_INIT_PRIORITY

.. option:: CONFIG_SPI_FLASH_W25QXXDV_INIT_PRIORITY:
.. _CONFIG_SPI_FLASH_W25QXXDV_INIT_PRIORITY:

Device driver initialization priority.
Device is connected to SPI bus, it has to
be initialized after SPI driver.



:Symbol:           SPI_FLASH_W25QXXDV_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  80 (value: "n")
 *   Condition: SPI_FLASH_W25QXXDV (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/flash/Kconfig:46