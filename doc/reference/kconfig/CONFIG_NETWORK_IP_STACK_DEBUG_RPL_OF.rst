:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_RPL_OF

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_RPL_OF:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_RPL_OF:

Enables RPL Objective Function related debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_RPL_OF
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug RPL objective function messages" if NETWORKING_WITH_RPL (value: "n")
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
 * ../net/ip/Kconfig.debug:194