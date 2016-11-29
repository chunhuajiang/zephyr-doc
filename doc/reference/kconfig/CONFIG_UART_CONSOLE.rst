:orphan:

.. title:: UART_CONSOLE

.. option:: CONFIG_UART_CONSOLE:
.. _CONFIG_UART_CONSOLE:

Enable this option to use one UART for console. Make sure
CONFIG_UART_CONSOLE_ON_DEV_NAME is also set correctly.



:Symbol:           UART_CONSOLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use UART for console" if SERIAL && SERIAL_HAS_DRIVER (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SERIAL && SERIAL_HAS_DRIVER (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_CONSOLE_HAS_DRIVER` if SERIAL && SERIAL_HAS_DRIVER (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/console/Kconfig:58
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:37