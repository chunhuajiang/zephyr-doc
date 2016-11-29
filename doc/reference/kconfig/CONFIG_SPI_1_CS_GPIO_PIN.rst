:orphan:

.. title:: SPI_1_CS_GPIO_PIN

.. option:: CONFIG_SPI_1_CS_GPIO_PIN:
.. _CONFIG_SPI_1_CS_GPIO_PIN:

The configuration item CONFIG_SPI_1_CS_GPIO_PIN:

:Symbol:           SPI_1_CS_GPIO_PIN
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "The GPIO PIN which is used to act as a CS pin" if SPI_1 && SPI_CS_GPIO (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SPI_1 && SPI_CS_GPIO (value: "n")
 *  2 (value: "n")
 *   Condition: (none)
 *  11 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && BOARD_QUARK_SE_C1000_DEVBOARD && SPI_QMSI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:145
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:194
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:78