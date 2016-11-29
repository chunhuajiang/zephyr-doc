:orphan:

.. title:: UART_NS16550

.. option:: CONFIG_UART_NS16550:
.. _CONFIG_UART_NS16550:

This option enables the NS16550 serial driver.
This driver can be used for the serial hardware
available on x86 boards.



:Symbol:           UART_NS16550
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "NS16550 serial driver"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_SERIAL_HAS_DRIVER`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:1