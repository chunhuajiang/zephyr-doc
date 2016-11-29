:orphan:

.. title:: CLOCK_CONTROL_STM32F4X

.. option:: CONFIG_CLOCK_CONTROL_STM32F4X:
.. _CONFIG_CLOCK_CONTROL_STM32F4X:

Enable driver for Reset & Clock Control subsystem found
in STM32F4 family of MCUs



:Symbol:           CLOCK_CONTROL_STM32F4X
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "STM32F4X Reset & Clock Control" if CLOCK_CONTROL && SOC_SERIES_STM32F4X (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: CLOCK_CONTROL && SOC_SERIES_STM32F4X && SOC_SERIES_STM32F4X (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CLOCK_CONTROL && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:21
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:65