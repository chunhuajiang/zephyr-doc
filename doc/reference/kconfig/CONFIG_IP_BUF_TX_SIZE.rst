:orphan:

.. title:: IP_BUF_TX_SIZE

.. option:: CONFIG_IP_BUF_TX_SIZE:
.. _CONFIG_IP_BUF_TX_SIZE:

Each network buffer will contain one sent IPv6 or IPv4 packet.
Each buffer will occupy 1280 bytes of memory.



:Symbol:           IP_BUF_TX_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Number of IP net buffers to use when sending data"
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:55