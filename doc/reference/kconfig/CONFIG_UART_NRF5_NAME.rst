:orphan:

.. title:: UART_NRF5_NAME

.. option:: CONFIG_UART_NRF5_NAME:
.. _CONFIG_UART_NRF5_NAME:

This is the device name for UART, and is included in the device
struct.



:Symbol:           UART_NRF5_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name for Nordic Semiconductor nRF5 UART" if UART_NRF5 (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: UART_NRF5 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:29