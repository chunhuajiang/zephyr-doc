:orphan:

.. title:: SPI_0_CS_GPIO_PORT

.. option:: CONFIG_SPI_0_CS_GPIO_PORT:
.. _CONFIG_SPI_0_CS_GPIO_PORT:

The configuration item CONFIG_SPI_0_CS_GPIO_PORT:

:Symbol:           SPI_0_CS_GPIO_PORT
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "The GPIO port which is used to control CS" if SPI_0 && SPI_CS_GPIO (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: SPI_0 && SPI_CS_GPIO (value: "n")
 *  "GPIO_0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_SERIES_QUARK_X1000 && SPI_INTEL && SPI_0 (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:110
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:176