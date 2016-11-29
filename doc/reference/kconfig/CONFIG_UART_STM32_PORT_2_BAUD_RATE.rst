:orphan:

.. title:: UART_STM32_PORT_2_BAUD_RATE

.. option:: CONFIG_UART_STM32_PORT_2_BAUD_RATE:
.. _CONFIG_UART_STM32_PORT_2_BAUD_RATE:

The baud rate for USART3 port to be set to at boot.



:Symbol:           UART_STM32_PORT_2_BAUD_RATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "STM32 USART1 Baud Rate" if UART_STM32_PORT_2 (value: "n")
:Default values:

 *  9600 (value: "n")
 *   Condition: UART_STM32_PORT_2 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stm32:110