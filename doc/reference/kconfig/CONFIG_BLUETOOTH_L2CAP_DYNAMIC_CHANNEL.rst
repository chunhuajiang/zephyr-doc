:orphan:

.. title:: BLUETOOTH_L2CAP_DYNAMIC_CHANNEL

.. option:: CONFIG_BLUETOOTH_L2CAP_DYNAMIC_CHANNEL:
.. _CONFIG_BLUETOOTH_L2CAP_DYNAMIC_CHANNEL:

This option enables support for LE Connection oriented Channels,
allowing the creation of dynamic L2CAP Channels.



:Symbol:           BLUETOOTH_L2CAP_DYNAMIC_CHANNEL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "L2CAP Dynamic Channel support" if BLUETOOTH_SMP (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING && NETWORKING_WITH_IPV6 && NETWORKING && NET_UIP && NETWORKING_WITH_BT || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_BREDR (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:219