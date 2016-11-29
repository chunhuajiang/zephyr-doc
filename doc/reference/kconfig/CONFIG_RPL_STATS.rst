:orphan:

.. title:: RPL_STATS

.. option:: CONFIG_RPL_STATS:
.. _CONFIG_RPL_STATS:

Enable RPL statistics support.



:Symbol:           RPL_STATS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable RPL statistics" if NETWORKING_WITH_RPL (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_RPL (value: "n")
:Selects:

 *  :option:`CONFIG_NETWORKING_STATISTICS` if NETWORKING_WITH_RPL (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:209