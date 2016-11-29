:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_IPV4_ARP

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_IPV4_ARP:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_IPV4_ARP:

Enables core ARP code part to output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_IPV4_ARP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug IPv4 ARP" if NETWORKING_WITH_IPV4 || NET_IPV4 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_IPV4 || NET_IPV4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:215