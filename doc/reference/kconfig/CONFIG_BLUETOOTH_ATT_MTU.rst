:orphan:

.. title:: BLUETOOTH_ATT_MTU

.. option:: CONFIG_BLUETOOTH_ATT_MTU:
.. _CONFIG_BLUETOOTH_ATT_MTU:

The MTU for the ATT channel. The minimum and default is 23,
whereas the maximum is limited by CONFIG_BLUETOOTH_L2CAP_IN_MTU.



:Symbol:           BLUETOOTH_ATT_MTU
:Type:             int
:Value:            "23"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [23, BLUETOOTH_L2CAP_IN_MTU]
:Prompts:

 *  "Attribute Protocol (ATT) channel MTU"
:Default values:

 *  23 (value: "n")
 *   Condition: (none)
 *  50 (value: "n")
 *   Condition: BLUETOOTH_SMP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:141