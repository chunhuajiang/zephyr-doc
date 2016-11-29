:orphan:

.. title:: UART_NS16550_DRV_CMD

.. option:: CONFIG_UART_NS16550_DRV_CMD:
.. _CONFIG_UART_NS16550_DRV_CMD:

This enables the API for apps to send commands to driver.

Says n if not sure.



:Symbol:           UART_NS16550_DRV_CMD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Driver Commands" if UART_DRV_CMD && UART_NS16550 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_DRV_CMD && UART_NS16550 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:40