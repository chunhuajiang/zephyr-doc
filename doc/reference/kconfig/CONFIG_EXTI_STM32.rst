:orphan:

.. title:: EXTI_STM32

.. option:: CONFIG_EXTI_STM32:
.. _CONFIG_EXTI_STM32:

Enable EXTI driver for STM32 line of MCUs



:Symbol:           EXTI_STM32
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "External Interrupt/Event Controller (EXTI) Driver for STM32 family of MCUs"
:Default values:

 *  y (value: "y")
 *   Condition: SOC_FAMILY_STM32 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_FAMILY_STM32 (value: "n")
:Locations:
 * ../drivers/interrupt_controller/Kconfig.stm32:20