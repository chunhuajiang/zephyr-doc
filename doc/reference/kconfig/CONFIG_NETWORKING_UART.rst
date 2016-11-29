:orphan:

.. title:: NETWORKING_UART

.. option:: CONFIG_NETWORKING_UART:
.. _CONFIG_NETWORKING_UART:

Enable UART driver for passing IPv6 packets using slip.


:Symbol:           NETWORKING_UART
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Network UART/slip driver"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_UART_PIPE`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:283