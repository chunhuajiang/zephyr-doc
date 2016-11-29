:orphan:

.. title:: CLOCK_STM32F4X_PLLN_MULTIPLIER

.. option:: CONFIG_CLOCK_STM32F4X_PLLN_MULTIPLIER:
.. _CONFIG_CLOCK_STM32F4X_PLLN_MULTIPLIER:

PLLN multiplier factor needs to be set correctly to ensure that the
VCO output frequency is between 192 and 432 MHz.
Allowed values: 192-432



:Symbol:           CLOCK_STM32F4X_PLLN_MULTIPLIER
:Type:             int
:Value:            "192"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [192, 432]
:Prompts:

 *  "Multiplier factor for PLL VCO output clock" if CLOCK_CONTROL_STM32F4X && CLOCK_STM32F4X_SYSCLK_SRC_PLL (value: "n")
:Default values:

 *  336 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F4X && CLOCK_STM32F4X_SYSCLK_SRC_PLL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:94