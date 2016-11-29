:orphan:

.. title:: UART_NS16550_LINE_CTRL

.. option:: CONFIG_UART_NS16550_LINE_CTRL:
.. _CONFIG_UART_NS16550_LINE_CTRL:

This enables the API for apps to control the serial line,
such as CTS and RTS.

Says n if not sure.



:Symbol:           UART_NS16550_LINE_CTRL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Serial Line Control for Apps" if UART_LINE_CTRL && UART_NS16550 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_LINE_CTRL && UART_NS16550 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:30