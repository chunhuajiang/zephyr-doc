:orphan:

.. title:: SPI_CS_GPIO

.. option:: CONFIG_SPI_CS_GPIO:
.. _CONFIG_SPI_CS_GPIO:

The configuration item CONFIG_SPI_CS_GPIO:

:Symbol:           SPI_CS_GPIO
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI port CS pin is controlled via a GPIO port" if GPIO (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO (value: "n")
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
 NETWORKING_WITH_15_4_TI_CC2520 && BOARD_QUARK_SE_C1000_DEVBOARD && SPI_QMSI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:87
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:166
 * ../boards/x86/arduino_101/Kconfig.defconfig:54
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:74