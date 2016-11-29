:orphan:

.. title:: UART_STM32_PORT_0

.. option:: CONFIG_UART_STM32_PORT_0:
.. _CONFIG_UART_STM32_PORT_0:

Enable support for USART1 port in the driver. Say y here
if you want to use USART1 device.



:Symbol:           UART_STM32_PORT_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable STM32 USART1 Port" if UART_STM32 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_STM32 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stm32:30
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:43