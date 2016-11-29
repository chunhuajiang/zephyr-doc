:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_RPL_TIMERS

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_RPL_TIMERS:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_RPL_TIMERS:

Enables RPL timers related debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_RPL_TIMERS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug RPL timer functionality" if NETWORKING_WITH_RPL (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_RPL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:201