:orphan:

.. title:: SPI

.. option:: CONFIG_SPI:
.. _CONFIG_SPI:

Enable support for the SPI hardware bus.



:Symbol:           SPI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI hardware bus support"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 ADC_TI_ADC108S102 && ADC (value: "n")
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:22
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:56
 * ../boards/x86/galileo/Kconfig.defconfig:19
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:51