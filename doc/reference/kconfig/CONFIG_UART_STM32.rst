:orphan:

.. title:: UART_STM32

.. option:: CONFIG_UART_STM32:
.. _CONFIG_UART_STM32:

This option enables the UART driver for STM32F10x family of
processors. Say y if you wish to use serial port on STM32F10x
MCU.



:Symbol:           UART_STM32
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "STM32 MCU serial driver" if SOC_FAMILY_STM32 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SOC_FAMILY_STM32 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_SERIAL_HAS_DRIVER` if SOC_FAMILY_STM32 (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stm32:18
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:40