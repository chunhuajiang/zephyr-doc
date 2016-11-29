:orphan:

.. title:: CLOCK_STM32F4X_PLLP_DIV_FACTOR

.. option:: CONFIG_CLOCK_STM32F4X_PLLP_DIV_FACTOR:
.. _CONFIG_CLOCK_STM32F4X_PLLP_DIV_FACTOR:

PLLP division factor needs to be set correctly to not exceed 84MHz.
Allowed values: 2, 4, 6, 8



:Symbol:           CLOCK_STM32F4X_PLLP_DIV_FACTOR
:Type:             int
:Value:            "2"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [2, 8]
:Prompts:

 *  "PLL division factor for main system clock" if CLOCK_CONTROL_STM32F4X && CLOCK_STM32F4X_SYSCLK_SRC_PLL (value: "n")
:Default values:

 *  4 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F4X && CLOCK_STM32F4X_SYSCLK_SRC_PLL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:104