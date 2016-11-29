:orphan:

.. title:: UART_ALTERA_JTAG

.. option:: CONFIG_UART_ALTERA_JTAG:
.. _CONFIG_UART_ALTERA_JTAG:

Enable the Altera JTAG UART driver, built in to many Nios II CPU
designs.



:Symbol:           UART_ALTERA_JTAG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Nios II JTAG UART driver"
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
 * ../drivers/serial/Kconfig.altera_jtag:1