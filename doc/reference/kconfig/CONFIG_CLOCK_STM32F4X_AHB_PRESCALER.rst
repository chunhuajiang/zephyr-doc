:orphan:

.. title:: CLOCK_STM32F4X_AHB_PRESCALER

.. option:: CONFIG_CLOCK_STM32F4X_AHB_PRESCALER:
.. _CONFIG_CLOCK_STM32F4X_AHB_PRESCALER:

AHB prescaler, allowed values: 0, 2, 4, 8, 16, 64, 128,
256, 512.



:Symbol:           CLOCK_STM32F4X_AHB_PRESCALER
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 512]
:Prompts:

 *  "AHB prescaler" if CLOCK_CONTROL_STM32F4X (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F4X (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:123