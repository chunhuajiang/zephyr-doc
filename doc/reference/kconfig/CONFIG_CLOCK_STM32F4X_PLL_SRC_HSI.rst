:orphan:

.. title:: CLOCK_STM32F4X_PLL_SRC_HSI

.. option:: CONFIG_CLOCK_STM32F4X_PLL_SRC_HSI:
.. _CONFIG_CLOCK_STM32F4X_PLL_SRC_HSI:

Use HSI as source of PLL



:Symbol:           CLOCK_STM32F4X_PLL_SRC_HSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HSI"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:65