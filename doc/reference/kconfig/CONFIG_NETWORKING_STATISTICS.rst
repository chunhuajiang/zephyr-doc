:orphan:

.. title:: NETWORKING_STATISTICS

.. option:: CONFIG_NETWORKING_STATISTICS:
.. _CONFIG_NETWORKING_STATISTICS:

This is only for debugging the network. Do not activate
this in live system! The option uses memory and slows
down IP packet processing.



:Symbol:           NETWORKING_STATISTICS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable IP statistics gathering" if NETWORKING (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING && NET_UIP && NETWORKING_WITH_RPL && RPL_STATS || NETWORKING_WITH_15_4 && 15_4_BEACON_SUPPORT && NETWORKING && NET_UIP && 15_4_BEACON_STATS || NETWORKING && NET_UIP && ER_COAP && COAP_STATS (value: "n")
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:120