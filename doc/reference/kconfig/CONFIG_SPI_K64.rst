:orphan:

.. title:: SPI_K64

.. option:: CONFIG_SPI_K64:
.. _CONFIG_SPI_K64:

Enable support for Freescale K64-based SPI controllers.



:Symbol:           SPI_K64
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based SPI controller driver" if SPI && SOC_MK64F12 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SPI && SOC_MK64F12 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_MK64F12 && SOC_SERIES_KINETIS_K6X && SPI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:46
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:61