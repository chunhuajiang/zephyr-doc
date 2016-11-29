:orphan:

.. title:: BLUETOOTH_RFCOMM_L2CAP_MTU

.. option:: CONFIG_BLUETOOTH_RFCOMM_L2CAP_MTU:
.. _CONFIG_BLUETOOTH_RFCOMM_L2CAP_MTU:

Maximum size of L2CAP PDU for RFCOMM frames.



:Symbol:           BLUETOOTH_RFCOMM_L2CAP_MTU
:Type:             int
:Value:            "23"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [BLUETOOTH_L2CAP_IN_MTU, 32767]
:Prompts:

 *  "L2CAP MTU for RFCOMM frames" if BLUETOOTH_RFCOMM (value: "n")
:Default values:

 *  BLUETOOTH_L2CAP_IN_MTU (value: "n")
 *   Condition: BLUETOOTH_RFCOMM (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:442