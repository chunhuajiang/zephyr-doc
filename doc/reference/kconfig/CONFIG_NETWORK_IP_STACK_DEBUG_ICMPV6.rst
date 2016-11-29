:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_ICMPV6

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_ICMPV6:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_ICMPV6:

Enables ICMPv6 code part to output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_ICMPV6
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug ICMPv6" if NET_IPV6 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NET_IPV6 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:102