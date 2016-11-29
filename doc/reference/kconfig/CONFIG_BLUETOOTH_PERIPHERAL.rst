:orphan:

.. title:: BLUETOOTH_PERIPHERAL

.. option:: CONFIG_BLUETOOTH_PERIPHERAL:
.. _CONFIG_BLUETOOTH_PERIPHERAL:

Select this for LE Peripheral role support.



:Symbol:           BLUETOOTH_PERIPHERAL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Peripheral Role support"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_BLUETOOTH_CONN`
:Reverse (select-related) dependencies:
 NETWORKING && NETWORKING_WITH_IPV6 && NETWORKING && NET_UIP && NETWORKING_WITH_BT || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_BREDR (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:40
 * ../subsys/bluetooth/host/Kconfig:125