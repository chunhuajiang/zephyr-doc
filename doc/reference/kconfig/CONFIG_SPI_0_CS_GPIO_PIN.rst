:orphan:

.. title:: SPI_0_CS_GPIO_PIN

.. option:: CONFIG_SPI_0_CS_GPIO_PIN:
.. _CONFIG_SPI_0_CS_GPIO_PIN:

The configuration item CONFIG_SPI_0_CS_GPIO_PIN:

:Symbol:           SPI_0_CS_GPIO_PIN
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "The GPIO PIN which is used to act as a CS pin" if SPI_0 && SPI_CS_GPIO (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SPI_0 && SPI_CS_GPIO (value: "n")
 *  0 (value: "n")
 *   Condition: (none)
 *  24 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 FLASH && SPI && BOARD_ARDUINO_101 (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:116
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:178
 * ../boards/x86/arduino_101/Kconfig.defconfig:57