:orphan:

.. title:: CONSOLE_HAS_DRIVER

.. option:: CONFIG_CONSOLE_HAS_DRIVER:
.. _CONFIG_CONSOLE_HAS_DRIVER:

This is an option to be enabled by console drivers to signal
that some kind of console exists.



:Symbol:           CONSOLE_HAS_DRIVER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SERIAL && SERIAL_HAS_DRIVER && CONSOLE && UART_CONSOLE || SERIAL && CONSOLE && USB_UART_CONSOLE || RAM_CONSOLE && CONSOLE || IPM_CONSOLE_SENDER && CONSOLE || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG_MONITOR (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:25