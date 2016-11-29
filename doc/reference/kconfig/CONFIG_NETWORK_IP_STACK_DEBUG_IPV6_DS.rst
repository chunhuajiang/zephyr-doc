:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_IPV6_DS

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_IPV6_DS:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_IPV6_DS:

Enables IPv6 Data Structures code part to output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_IPV6_DS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug IPv6 Data Structures" if NETWORKING_WITH_IPV6 && NET_UIP (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_IPV6 && NET_UIP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:88