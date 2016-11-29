:orphan:

.. title:: UART_STM32_PORT_0_BAUD_RATE

.. option:: CONFIG_UART_STM32_PORT_0_BAUD_RATE:
.. _CONFIG_UART_STM32_PORT_0_BAUD_RATE:

The baud rate for USART1 port to be set to at boot.



:Symbol:           UART_STM32_PORT_0_BAUD_RATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "STM32 USART1 Baud Rate" if UART_STM32_PORT_0 (value: "n")
:Default values:

 *  9600 (value: "n")
 *   Condition: UART_STM32_PORT_0 (value: "n")
 *  115200 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stm32:46
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:49