:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_NET_BUF

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_NET_BUF:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_NET_BUF:

Enables printing of network buffer allocations and frees.



:Symbol:           NETWORK_IP_STACK_DEBUG_NET_BUF
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug network buffer allocation"
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
 * ../net/ip/Kconfig.debug:49