:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_TCP_PSOCK

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_TCP_PSOCK:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_TCP_PSOCK:

Enables debugging the protosockets used in TCP engine.



:Symbol:           NETWORK_IP_STACK_DEBUG_TCP_PSOCK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug network TCP protosockets" if NETWORKING_WITH_TCP && NET_UIP (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_TCP && NET_UIP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:61