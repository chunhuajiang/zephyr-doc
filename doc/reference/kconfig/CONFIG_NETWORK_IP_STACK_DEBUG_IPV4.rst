:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_IPV4

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_IPV4:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_IPV4:

Enables core IPv4 code part to output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_IPV4
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug core IPv4" if NETWORKING_WITH_IPV4 || NET_IPV4 (value: "n")
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
 * ../net/ip/Kconfig.debug:208