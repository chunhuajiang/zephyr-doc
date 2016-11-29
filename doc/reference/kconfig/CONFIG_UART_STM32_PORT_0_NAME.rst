:orphan:

.. title:: UART_STM32_PORT_0_NAME

.. option:: CONFIG_UART_STM32_PORT_0_NAME:
.. _CONFIG_UART_STM32_PORT_0_NAME:

This is the device name for USART1 port, and is
included in the device struct.



:Symbol:           UART_STM32_PORT_0_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name for STM32 USART1 Port" if UART_STM32_PORT_0 (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: UART_STM32_PORT_0 (value: "n")
 *  UART_0 (value: "UART_0")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stm32:38
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:46