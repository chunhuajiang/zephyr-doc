:orphan:

.. title:: 15_4_BEACON_STATS

.. option:: CONFIG_15_4_BEACON_STATS:
.. _CONFIG_15_4_BEACON_STATS:

Enable 802.15.4 beacon statistics support.



:Symbol:           15_4_BEACON_STATS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable 802.15.4 beacon statistics" if NETWORKING_WITH_15_4 && 15_4_BEACON_SUPPORT (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_15_4 && 15_4_BEACON_SUPPORT (value: "n")
:Selects:

 *  :option:`CONFIG_NETWORKING_STATISTICS` if NETWORKING_WITH_15_4 && 15_4_BEACON_SUPPORT (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:396