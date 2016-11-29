:orphan:

.. title:: NETWORKING_WITH_15_4_LOOPBACK_UART

.. option:: CONFIG_NETWORKING_WITH_15_4_LOOPBACK_UART:
.. _CONFIG_NETWORKING_WITH_15_4_LOOPBACK_UART:

Enable 802.15.4 loopback radio driver that sends
802.15.4 frames out of qemu through uart and receive
frames through uart. This way one can test 802.15.4 frames
between two qemus


:Symbol:           NETWORKING_WITH_15_4_LOOPBACK_UART
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Loopback with UART"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_UART_PIPE`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:438