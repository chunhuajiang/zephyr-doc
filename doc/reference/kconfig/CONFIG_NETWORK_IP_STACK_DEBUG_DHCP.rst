:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_DHCP

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_DHCP:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_DHCP:

Enables DHCP output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_DHCP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug DHCP" if DHCP (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: DHCP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:271