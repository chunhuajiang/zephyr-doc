:orphan:

.. title:: UART_STM32_PORT_2

.. option:: CONFIG_UART_STM32_PORT_2:
.. _CONFIG_UART_STM32_PORT_2:

Enable support for USART3 port in the driver. Say y here
if you want to use USART3 device.



:Symbol:           UART_STM32_PORT_2
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable STM32 USART3 Port" if UART_STM32 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_STM32 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stm32:94