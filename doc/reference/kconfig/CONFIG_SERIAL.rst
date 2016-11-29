:orphan:

.. title:: SERIAL

.. option:: CONFIG_SERIAL:
.. _CONFIG_SERIAL:

Enable options for serial drivers.



:Symbol:           SERIAL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Serial Drivers"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/serial/Kconfig:19
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:29