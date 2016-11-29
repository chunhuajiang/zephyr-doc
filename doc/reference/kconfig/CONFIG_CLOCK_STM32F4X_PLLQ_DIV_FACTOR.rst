:orphan:

.. title:: CLOCK_STM32F4X_PLLQ_DIV_FACTOR

.. option:: CONFIG_CLOCK_STM32F4X_PLLQ_DIV_FACTOR:
.. _CONFIG_CLOCK_STM32F4X_PLLQ_DIV_FACTOR:

The USB OTG FS requires a 48MHz clock to work correctly. SDIO and RNG
need a frequency lower than or equal to 48 MHz to work correctly.
Allowed values: 2-15



:Symbol:           CLOCK_STM32F4X_PLLQ_DIV_FACTOR
:Type:             int
:Value:            "2"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [2, 15]
:Prompts:

 *  "Division factor for OTG FS, SDIO and RNG clocks" if CLOCK_CONTROL_STM32F4X && CLOCK_STM32F4X_SYSCLK_SRC_PLL (value: "n")
:Default values:

 *  7 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F4X && CLOCK_STM32F4X_SYSCLK_SRC_PLL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:113