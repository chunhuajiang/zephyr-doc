:orphan:

.. title:: CLOCK_CONTROL

.. option:: CONFIG_CLOCK_CONTROL:
.. _CONFIG_CLOCK_CONTROL:

Enable support for hardware clock controller. Such hardware can
provide clock for other subsystem, and thus can be also used for
power efficiency by controlling their clock. Note that this has
nothing to do with RTC.



:Symbol:           CLOCK_CONTROL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Hardware clock controller support"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 GPIO_DW && GPIO && GPIO_DW && GPIO_DW_CLOCK_GATE || SPI_DW && SOC_QUARK_SE_C1000 && SPI_DW && SPI && SPI_DW_CLOCK_GATE (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig:22
 * ../arch/arm/soc/nordic_nrf5/Kconfig.defconfig:20