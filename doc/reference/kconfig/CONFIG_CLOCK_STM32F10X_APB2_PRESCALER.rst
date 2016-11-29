:orphan:

.. title:: CLOCK_STM32F10X_APB2_PRESCALER

.. option:: CONFIG_CLOCK_STM32F10X_APB2_PRESCALER:
.. _CONFIG_CLOCK_STM32F10X_APB2_PRESCALER:

APB2 High speed clock (PCLK2) prescaler, allowed values:
0, 2, 4, 8, 16



:Symbol:           CLOCK_STM32F10X_APB2_PRESCALER
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

 *  "APB2 prescaler" if CLOCK_CONTROL_STM32F10X (value: "n")
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
 * ../drivers/clock_control/Kconfig.stm32f10x:114