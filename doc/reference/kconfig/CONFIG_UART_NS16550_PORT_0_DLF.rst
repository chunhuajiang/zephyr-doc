:orphan:

.. title:: UART_NS16550_PORT_0_DLF

.. option:: CONFIG_UART_NS16550_PORT_0_DLF:
.. _CONFIG_UART_NS16550_PORT_0_DLF:

Value for DLF register.



:Symbol:           UART_NS16550_PORT_0_DLF
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 DLF value" if UART_NS16550_PORT_0 && UART_NS16550_DLF (value: "n")
:Default values:

 *  0x0 (value: "n")
 *   Condition: UART_NS16550_PORT_0 && UART_NS16550_DLF (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:90