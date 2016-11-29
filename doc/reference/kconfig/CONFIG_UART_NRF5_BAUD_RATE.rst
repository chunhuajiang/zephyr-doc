:orphan:

.. title:: UART_NRF5_BAUD_RATE

.. option:: CONFIG_UART_NRF5_BAUD_RATE:
.. _CONFIG_UART_NRF5_BAUD_RATE:

The baud rate for UART port to be set to at boot.



:Symbol:           UART_NRF5_BAUD_RATE
:Type:             int
:Value:            "1200"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1200, 1000000]
:Prompts:

 *  "Baud Rate" if UART_NRF5 (value: "n")
:Default values:

 *  115200 (value: "n")
 *   Condition: UART_NRF5 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:47