:orphan:

.. title:: ETHERNET_DEBUG

.. option:: CONFIG_ETHERNET_DEBUG:
.. _CONFIG_ETHERNET_DEBUG:

This option enables debug support for Ethernet drivers.



:Symbol:           ETHERNET_DEBUG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Network Ethernet driver debug" if NETWORKING_WITH_LOGGING && ETHERNET (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_LOGGING && ETHERNET (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:306