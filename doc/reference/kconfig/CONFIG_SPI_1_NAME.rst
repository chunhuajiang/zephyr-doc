:orphan:

.. title:: SPI_1_NAME

.. option:: CONFIG_SPI_1_NAME:
.. _CONFIG_SPI_1_NAME:

The configuration item CONFIG_SPI_1_NAME:

:Symbol:           SPI_1_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI port 1 device name" if SPI_1 (value: "n")
:Default values:

 *  "SPI_1"
 *   Condition: SPI_1 (value: "n")
 *  "SPI_1"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_SERIES_QUARK_X1000 && SPI_INTEL && SPI_1 (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:128
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:188