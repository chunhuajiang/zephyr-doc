:orphan:

.. title:: BLUETOOTH_ACL_IN_COUNT

.. option:: CONFIG_BLUETOOTH_ACL_IN_COUNT:
.. _CONFIG_BLUETOOTH_ACL_IN_COUNT:

Number of buffers available for incoming ACL data.



:Symbol:           BLUETOOTH_ACL_IN_COUNT
:Type:             int
:Value:            "2"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [2, 64]
:Prompts:

 *  "Number of incoming ACL data buffers"
:Default values:

 *  6 (value: "n")
 *   Condition: (none)
 *  BLUETOOTH_CONTROLLER_RX_BUFFERS (value: "n")
 *   Condition: BLUETOOTH_CONTROLLER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && (BLUETOOTH_CONN || BLUETOOTH_HCI_RAW) (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:85