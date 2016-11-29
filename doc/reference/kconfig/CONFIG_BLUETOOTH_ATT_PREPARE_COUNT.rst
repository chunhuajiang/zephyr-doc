:orphan:

.. title:: BLUETOOTH_ATT_PREPARE_COUNT

.. option:: CONFIG_BLUETOOTH_ATT_PREPARE_COUNT:
.. _CONFIG_BLUETOOTH_ATT_PREPARE_COUNT:

Number of buffers available for ATT prepare write, setting
this to 0 disables GATT long/reliable writes.



:Symbol:           BLUETOOTH_ATT_PREPARE_COUNT
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 64]
 *  [0, 64]
:Prompts:

 *  "Number of ATT prepare write buffers"
 *  "Number of ATT prepare write buffers"
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:48
 * ../subsys/bluetooth/host/Kconfig:151