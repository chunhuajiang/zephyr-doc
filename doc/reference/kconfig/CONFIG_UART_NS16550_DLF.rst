:orphan:

.. title:: UART_NS16550_DLF

.. option:: CONFIG_UART_NS16550_DLF:
.. _CONFIG_UART_NS16550_DLF:

This enables support for divisor latch fraction (DLF).
It is used to limit frequency error.

Says n if you are not sure if hardware supports this.



:Symbol:           UART_NS16550_DLF
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Divisor Latch Fraction (DLF) support" if UART_NS16550 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_NS16550 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:20