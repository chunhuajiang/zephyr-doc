:orphan:

.. title:: NETWORKING_WITH_6LOWPAN

.. option:: CONFIG_NETWORKING_WITH_6LOWPAN:
.. _CONFIG_NETWORKING_WITH_6LOWPAN:

Enable 6LoWPAN in uIP stack. Currently this requires 802.15.4
stack to be enabled.



:Symbol:           NETWORKING_WITH_6LOWPAN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable 6LoWPAN (IPv6 compression) in the uIP stack" if NETWORKING && (NETWORKING_WITH_15_4 || NETWORKING_WITH_BT) (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING && (NETWORKING_WITH_15_4 || NETWORKING_WITH_BT) (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING && NETWORKING_WITH_IPV6 && NETWORKING && NET_UIP && NETWORKING_WITH_BT (value: "n")
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:467