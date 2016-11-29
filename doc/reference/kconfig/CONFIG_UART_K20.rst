:orphan:

.. title:: UART_K20

.. option:: CONFIG_UART_K20:
.. _CONFIG_UART_K20:

This option enables the K20 serial driver.
This specific driver can be used for the serial hardware
available at the Freescale FRDM K64F board.



:Symbol:           UART_K20
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "K20 serial driver"
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
 * ../drivers/serial/Kconfig.k20:1