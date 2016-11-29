:orphan:

.. title:: NET_15_4_LOOPBACK_NUM

.. option:: CONFIG_NET_15_4_LOOPBACK_NUM:
.. _CONFIG_NET_15_4_LOOPBACK_NUM:

Number of times loopback test runs, 0 means infinite.



:Symbol:           NET_15_4_LOOPBACK_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Number of times loopback test runs" if (NETWORKING_WITH_15_4_LOOPBACK || NETWORKING_WITH_15_4_LOOPBACK_UART) && NET_SANITY_TEST (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: (NETWORKING_WITH_15_4_LOOPBACK || NETWORKING_WITH_15_4_LOOPBACK_UART) && NET_SANITY_TEST (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:586