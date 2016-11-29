:orphan:

.. title:: CLOCK_CONTROL_NRF5

.. option:: CONFIG_CLOCK_CONTROL_NRF5:
.. _CONFIG_CLOCK_CONTROL_NRF5:

Enable support for the Nordic Semiconductor nRF5x series SoC clock
driver.



:Symbol:           CLOCK_CONTROL_NRF5
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "NRF5 Clock controller support" if CLOCK_CONTROL && SOC_FAMILY_NRF5 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: CLOCK_CONTROL && SOC_FAMILY_NRF5 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.nrf5:17
 * ../arch/arm/soc/nordic_nrf5/Kconfig.defconfig:23