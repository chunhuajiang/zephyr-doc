:orphan:

.. title:: CLOCK_CONTROL_STM32F10X

.. option:: CONFIG_CLOCK_CONTROL_STM32F10X:
.. _CONFIG_CLOCK_CONTROL_STM32F10X:

Enable driver for Reset & Clock Control subsystem found
in STM32F1 family of MCUs



:Symbol:           CLOCK_CONTROL_STM32F10X
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "STM32F10x Reset & Clock Control" if CLOCK_CONTROL && SOC_SERIES_STM32F1X (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: CLOCK_CONTROL && SOC_SERIES_STM32F1X && SOC_SERIES_STM32F1X (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F1X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f10x:20