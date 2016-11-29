:orphan:

.. title:: UART_STM32_PORT_0_IRQ_PRI

.. option:: CONFIG_UART_STM32_PORT_0_IRQ_PRI:
.. _CONFIG_UART_STM32_PORT_0_IRQ_PRI:

The interrupt priority for USART1 port.



:Symbol:           UART_STM32_PORT_0_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "STM32 USART1 Interrupt Priority" if UART_STM32_PORT_0 && UART_INTERRUPT_DRIVEN (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_STM32_PORT_0 && UART_INTERRUPT_DRIVEN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stm32:53