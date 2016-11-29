:orphan:

.. title:: BLUETOOTH_L2CAP_IN_MTU

.. option:: CONFIG_BLUETOOTH_L2CAP_IN_MTU:
.. _CONFIG_BLUETOOTH_L2CAP_IN_MTU:

Maximum size of each incoming L2CAP PDU.


:Symbol:           BLUETOOTH_L2CAP_IN_MTU
:Type:             int
:Value:            "23"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [23, 1300]
 *  [65, 1300] if BLUETOOTH_SMP (value: "n")
:Prompts:

 *  "Maximum supported L2CAP MTU for incoming data"
:Default values:

 *  23 (value: "n")
 *   Condition: (none)
 *  65 (value: "n")
 *   Condition: BLUETOOTH_SMP (value: "n")
 *  200 (value: "n")
 *   Condition: BLUETOOTH_BREDR (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && (BLUETOOTH_CONN || BLUETOOTH_HCI_RAW) (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:93