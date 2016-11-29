:orphan:

.. title:: UART_STELLARIS

.. option:: CONFIG_UART_STELLARIS:
.. _CONFIG_UART_STELLARIS:

This option enables the Stellaris serial driver.
This specific driver can be used for the serial hardware
available at the Texas Instrument LM3S6965 board.



:Symbol:           UART_STELLARIS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Stellaris serial driver"
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
 * ../drivers/serial/Kconfig.stellaris:1