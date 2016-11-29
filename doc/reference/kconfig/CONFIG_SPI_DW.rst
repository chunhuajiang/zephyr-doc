:orphan:

.. title:: SPI_DW

.. option:: CONFIG_SPI_DW:
.. _CONFIG_SPI_DW:

Enable support for Designware's SPI controllers.



:Symbol:           SPI_DW
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Designware SPI controller driver" if SPI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SPI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_EM9D (value: "n")
:Locations:
 * ../drivers/spi/Kconfig.dw:19
 * ../arch/arc/soc/em11d/Kconfig.defconfig:221
 * ../arch/arc/soc/em7d/Kconfig.defconfig:221
 * ../arch/arc/soc/em9d/Kconfig.defconfig:219