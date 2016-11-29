:orphan:

.. title:: SPI_INIT_PRIORITY

.. option:: CONFIG_SPI_INIT_PRIORITY:
.. _CONFIG_SPI_INIT_PRIORITY:

Device driver initialization priority.



:Symbol:           SPI_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Init priority"
:Default values:

 *  70 (value: "n")
 *   Condition: (none)
 *  90 (value: "n")
 *   Condition: SPI_INTEL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:66
 * ../boards/x86/galileo/Kconfig.defconfig:127