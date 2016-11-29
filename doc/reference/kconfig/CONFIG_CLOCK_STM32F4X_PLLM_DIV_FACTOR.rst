:orphan:

.. title:: CLOCK_STM32F4X_PLLM_DIV_FACTOR

.. option:: CONFIG_CLOCK_STM32F4X_PLLM_DIV_FACTOR:
.. _CONFIG_CLOCK_STM32F4X_PLLM_DIV_FACTOR:

PLLM division factor needs to be set correctly to ensure that the VCO
input frequency ranges from 1 to 2 MHz. It is recommended to select a
frequency of 2 MHz to limit PLL jitter.
Allowed values: 2-63



:Symbol:           CLOCK_STM32F4X_PLLM_DIV_FACTOR
:Type:             int
:Value:            "2"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [2, 63]
:Prompts:

 *  "Division factor for PLL VCO input clock" if CLOCK_CONTROL_STM32F4X && CLOCK_STM32F4X_SYSCLK_SRC_PLL (value: "n")
:Default values:

 *  8 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F4X && CLOCK_STM32F4X_SYSCLK_SRC_PLL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:83