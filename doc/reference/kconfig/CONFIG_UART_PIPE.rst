:orphan:

.. title:: UART_PIPE

.. option:: CONFIG_UART_PIPE:
.. _CONFIG_UART_PIPE:

Enable pipe UART driver. This driver allows application to communicate
over UART with custom defined protocol. Driver doesn't inspect received
data (as contrary to console UART driver) and all aspects of received
protocol data are handled by application provided callback.



:Symbol:           UART_PIPE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable pipe UART driver"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_UART_INTERRUPT_DRIVEN`
:Reverse (select-related) dependencies:
 NETWORKING && NET_UIP && NETWORKING_UART || NETWORKING && NET_UIP && NETWORKING_WITH_15_4_LOOPBACK_UART (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:156