:orphan:

.. title:: 15_4_BEACON_SUPPORT

.. option:: CONFIG_15_4_BEACON_SUPPORT:
.. _CONFIG_15_4_BEACON_SUPPORT:

Enable 802.15.4 beacon support



:Symbol:           15_4_BEACON_SUPPORT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable 802.15.4 beacon support" if NETWORKING_WITH_15_4 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_15_4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:388