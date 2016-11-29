:orphan:

.. title:: SERIAL_HAS_DRIVER

.. option:: CONFIG_SERIAL_HAS_DRIVER:
.. _CONFIG_SERIAL_HAS_DRIVER:

This is an option to be enabled by individual serial driver
to signal that there is a serial driver. This is being used
by other drivers which are dependent on serial.



:Symbol:           SERIAL_HAS_DRIVER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 UART_NS16550 && SERIAL || UART_K20 && SERIAL || UART_STELLARIS && SERIAL || SOC_ATMEL_SAM3 && SERIAL && UART_ATMEL_SAM3 || QMSI && SERIAL && UART_QMSI || SOC_FAMILY_STM32 && SERIAL && UART_STM32 || SOC_FAMILY_NRF5 && SERIAL && UART_NRF5 || UART_ALTERA_JTAG && SERIAL || SOC_SERIES_CC32XX && SOC_FAMILY_TISIMPLELINK && SERIAL && UART_CC32XX || SOC_FAMILY_ARM && SERIAL && UART_CMSDK_APB (value: "n")
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig:30