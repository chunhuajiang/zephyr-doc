:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_TRICKLE

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_TRICKLE:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_TRICKLE:

Enables Trickle library output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_TRICKLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug Trickle algorithm"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:278