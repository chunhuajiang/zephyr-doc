:orphan:

.. title:: BLUETOOTH_DEBUG_MONITOR

.. option:: CONFIG_BLUETOOTH_DEBUG_MONITOR:
.. _CONFIG_BLUETOOTH_DEBUG_MONITOR:

Use a custom logging protocol over the console UART
instead of plain-text output. Requires a special application
on the host side that can decode this protocol. Currently
the 'btmon' tool from BlueZ is capable of doing this.

If the target board has two or more external UARTs it is
possible to keep using UART_CONSOLE together with this option,
however if there is only a single external UART then
UART_CONSOLE needs to be disabled (in which case printk/printf
will get encoded into the monitor protocol).



:Symbol:           BLUETOOTH_DEBUG_MONITOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Monitor protocol over UART"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_BLUETOOTH_DEBUG`
 *  :option:`CONFIG_CONSOLE_HAS_DRIVER`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:289