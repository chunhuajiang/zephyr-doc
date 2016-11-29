:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_IPV6

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_IPV6:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_IPV6:

Enables core IPv6 code part to output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_IPV6
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug core IPv6" if NETWORKING_WITH_IPV6 || NET_IPV6 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_IPV6 || NET_IPV6 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:68