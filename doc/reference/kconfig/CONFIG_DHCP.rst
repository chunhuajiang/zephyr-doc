:orphan:

.. title:: DHCP

.. option:: CONFIG_DHCP:
.. _CONFIG_DHCP:

Enable DHCP support so that applications can use it.


:Symbol:           DHCP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable DHCP support." if NETWORKING && NETWORKING_WITH_IPV4 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING && NETWORKING_WITH_IPV4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:553