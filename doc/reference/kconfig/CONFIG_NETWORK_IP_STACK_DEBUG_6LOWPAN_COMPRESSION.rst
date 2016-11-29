:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_6LOWPAN_COMPRESSION

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_6LOWPAN_COMPRESSION:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_6LOWPAN_COMPRESSION:

Enables generic (802.15.4 or Bluetooth) 6LoWPAN compression
to output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_6LOWPAN_COMPRESSION
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug generic 6LoWPAN compression" if NETWORKING_WITH_IPV6 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_IPV6 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:165