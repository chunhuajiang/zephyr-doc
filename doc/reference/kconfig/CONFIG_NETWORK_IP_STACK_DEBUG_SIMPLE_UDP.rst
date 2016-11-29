:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_SIMPLE_UDP

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_SIMPLE_UDP:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_SIMPLE_UDP:

Enables network simple udp debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_SIMPLE_UDP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug simple udp" if NET_UIP (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NET_UIP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:75