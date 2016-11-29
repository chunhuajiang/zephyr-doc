:orphan:

.. title:: CONSOLE

.. option:: CONFIG_CONSOLE:
.. _CONFIG_CONSOLE:

The configuration item CONFIG_CONSOLE:

:Symbol:           CONSOLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Console drivers"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/console/Kconfig:19
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:34