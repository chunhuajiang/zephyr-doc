:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_15_4_FRAMING

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_15_4_FRAMING:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_15_4_FRAMING:

Enables 802.15.4 packet framing to output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_15_4_FRAMING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug 802.15.4 packet framing" if NETWORKING_WITH_15_4 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_15_4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:151