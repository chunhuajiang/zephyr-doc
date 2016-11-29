:orphan:

.. title:: CLOCK_STM32F4X_PLL_SRC_HSE

.. option:: CONFIG_CLOCK_STM32F4X_PLL_SRC_HSE:
.. _CONFIG_CLOCK_STM32F4X_PLL_SRC_HSE:

Use HSE as source of PLL



:Symbol:           CLOCK_STM32F4X_PLL_SRC_HSE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HSE"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:70