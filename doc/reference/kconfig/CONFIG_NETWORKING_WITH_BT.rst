:orphan:

.. title:: NETWORKING_WITH_BT

.. option:: CONFIG_NETWORKING_WITH_BT:
.. _CONFIG_NETWORKING_WITH_BT:

Enable Bluetooth driver that send and receives IPv6 packets,
does header compression on it and writes it to the
Bluetooth stack via L2CAP channel.



:Symbol:           NETWORKING_WITH_BT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Bluetooth driver" if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
:Selects:

 *  :option:`CONFIG_L2_BUFFERS` if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
 *  :option:`CONFIG_NETWORKING_IPV6_NO_ND` if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
 *  :option:`CONFIG_NETWORKING_WITH_6LOWPAN` if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
 *  :option:`CONFIG_6LOWPAN_COMPRESSION_IPHC` if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
 *  :option:`CONFIG_BLUETOOTH` if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
 *  :option:`CONFIG_BLUETOOTH_PERIPHERAL` if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
 *  :option:`CONFIG_BLUETOOTH_L2CAP_DYNAMIC_CHANNEL` if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
 *  :option:`CONFIG_BLUETOOTH_SMP` if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:449