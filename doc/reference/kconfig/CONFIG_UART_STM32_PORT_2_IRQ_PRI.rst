:orphan:

.. title:: UART_STM32_PORT_2_IRQ_PRI

.. option:: CONFIG_UART_STM32_PORT_2_IRQ_PRI:
.. _CONFIG_UART_STM32_PORT_2_IRQ_PRI:

The interrupt priority for USART3 port.


:Symbol:           UART_STM32_PORT_2_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "STM32 USART3 Interrupt Priority" if UART_STM32_PORT_2 && UART_INTERRUPT_DRIVEN (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_STM32_PORT_2 && UART_INTERRUPT_DRIVEN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stm32:117