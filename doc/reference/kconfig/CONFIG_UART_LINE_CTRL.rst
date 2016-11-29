:orphan:

.. title:: UART_LINE_CTRL

.. option:: CONFIG_UART_LINE_CTRL:
.. _CONFIG_UART_LINE_CTRL:

This enables the API for apps to control the serial line,
such as baud rate, CTS and RTS.

Implementation is up to individual driver.

Says no if not sure.



:Symbol:           UART_LINE_CTRL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Serial Line Control API"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig:46