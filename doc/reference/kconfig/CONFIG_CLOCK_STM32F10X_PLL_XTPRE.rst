:orphan:

.. title:: CLOCK_STM32F10X_PLL_XTPRE

.. option:: CONFIG_CLOCK_STM32F10X_PLL_XTPRE:
.. _CONFIG_CLOCK_STM32F10X_PLL_XTPRE:

Enable this option to enable /2 prescaler on HSE to PLL clock signal



:Symbol:           CLOCK_STM32F10X_PLL_XTPRE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HSE to PLL /2 prescaler" if CLOCK_CONTROL_STM32F10X && CLOCK_STM32F10X_PLL_SRC_HSE (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F1X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f10x:82