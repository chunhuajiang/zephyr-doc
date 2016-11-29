:orphan:

.. title:: SPI_1_CS_GPIO_PORT

.. option:: CONFIG_SPI_1_CS_GPIO_PORT:
.. _CONFIG_SPI_1_CS_GPIO_PORT:

The configuration item CONFIG_SPI_1_CS_GPIO_PORT:

:Symbol:           SPI_1_CS_GPIO_PORT
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "The GPIO port which is used to control CS" if SPI_1 && SPI_CS_GPIO (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: SPI_1 && SPI_CS_GPIO (value: "n")
 *  "GPIO_0"
 *   Condition: (none)
 *  GPIO_QMSI_0_NAME (value: "")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && BOARD_QUARK_SE_C1000_DEVBOARD && SPI_QMSI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:139
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:192
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:76