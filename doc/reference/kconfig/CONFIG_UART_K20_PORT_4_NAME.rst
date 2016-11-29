:orphan:

.. title:: UART_K20_PORT_4_NAME

.. option:: CONFIG_UART_K20_PORT_4_NAME:
.. _CONFIG_UART_K20_PORT_4_NAME:

This is the device name for UART, and is included in the device
struct.



:Symbol:           UART_K20_PORT_4_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 4 Device Name" if UART_K20_PORT_4 (value: "n")
:Default values:

 *  "UART_4"
 *   Condition: UART_K20_PORT_4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.k20:156