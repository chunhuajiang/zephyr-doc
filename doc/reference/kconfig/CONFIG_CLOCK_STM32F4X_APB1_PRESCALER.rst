:orphan:

.. title:: CLOCK_STM32F4X_APB1_PRESCALER

.. option:: CONFIG_CLOCK_STM32F4X_APB1_PRESCALER:
.. _CONFIG_CLOCK_STM32F4X_APB1_PRESCALER:

APB1 Low speed clock (PCLK1) prescaler, allowed values:
0, 2, 4, 8, 16. The APB1 clock must not exceed 42MHz.



:Symbol:           CLOCK_STM32F4X_APB1_PRESCALER
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

 *  "APB1 low speed clock prescaler" if CLOCK_CONTROL_STM32F4X (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F4X (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:132