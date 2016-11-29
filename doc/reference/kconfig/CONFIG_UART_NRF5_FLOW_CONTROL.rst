:orphan:

.. title:: UART_NRF5_FLOW_CONTROL

.. option:: CONFIG_UART_NRF5_FLOW_CONTROL:
.. _CONFIG_UART_NRF5_FLOW_CONTROL:

Enable Flow Control. If selected, additionally two pins, RTS and CTS
has to be configured.



:Symbol:           UART_NRF5_FLOW_CONTROL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Flow Control" if UART_NRF5 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_NRF5 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:60