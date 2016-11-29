:orphan:

.. title:: EXTI_STM32_EXTI17_IRQ_PRI

.. option:: CONFIG_EXTI_STM32_EXTI17_IRQ_PRI:
.. _CONFIG_EXTI_STM32_EXTI17_IRQ_PRI:

IRQ priority of EXTI17 interrupt



:Symbol:           EXTI_STM32_EXTI17_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "EXTI17 IRQ priority" if EXTI_STM32 && SOC_SERIES_STM32F4X (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: EXTI_STM32 && SOC_SERIES_STM32F4X (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_FAMILY_STM32 (value: "n")
:Locations:
 * ../drivers/interrupt_controller/Kconfig.stm32:83