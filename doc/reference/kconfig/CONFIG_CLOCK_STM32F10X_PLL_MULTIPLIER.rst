:orphan:

.. title:: CLOCK_STM32F10X_PLL_MULTIPLIER

.. option:: CONFIG_CLOCK_STM32F10X_PLL_MULTIPLIER:
.. _CONFIG_CLOCK_STM32F10X_PLL_MULTIPLIER:

PLL multiplier, allowed values: 2-16. PLL output must not exceed 72MHz.



:Symbol:           CLOCK_STM32F10X_PLL_MULTIPLIER
:Type:             int
:Value:            "2"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [2, 16]
:Prompts:

 *  "PLL multiplier" if CLOCK_CONTROL_STM32F10X && CLOCK_STM32F10X_SYSCLK_SRC_PLL (value: "n")
:Default values:

 *  9 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F10X && CLOCK_STM32F10X_SYSCLK_SRC_PLL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F1X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f10x:88