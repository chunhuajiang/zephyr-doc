:orphan:

.. title:: CLOCK_STM32F10X_APB1_PRESCALER

.. option:: CONFIG_CLOCK_STM32F10X_APB1_PRESCALER:
.. _CONFIG_CLOCK_STM32F10X_APB1_PRESCALER:

APB1 Low speed clock (PCLK1) prescaler, allowed values:
0, 2, 4, 8, 16. The APB1 clock must not exceed 36MHz.



:Symbol:           CLOCK_STM32F10X_APB1_PRESCALER
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 16]
:Prompts:

 *  "APB1 prescaler" if CLOCK_CONTROL_STM32F10X (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F10X (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F1X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f10x:105