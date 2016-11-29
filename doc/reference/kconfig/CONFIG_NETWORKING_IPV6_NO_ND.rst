:orphan:

.. title:: NETWORKING_IPV6_NO_ND

.. option:: CONFIG_NETWORKING_IPV6_NO_ND:
.. _CONFIG_NETWORKING_IPV6_NO_ND:

Normally ND should be enabled but in order to simplify
the network setup it can be turned off if using
slip and tun device.



:Symbol:           NETWORKING_IPV6_NO_ND
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Disable IPv6 neighbor discovery" if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING && NETWORKING_WITH_IPV6 && NETWORKING && NET_UIP && NETWORKING_WITH_BT (value: "n")
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP && NETWORKING_WITH_IPV6 (value: "n")
:Locations:
 * ../net/ip/Kconfig:131