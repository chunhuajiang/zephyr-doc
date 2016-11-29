:orphan:

.. title:: BLUETOOTH_HCI_CMD_COUNT

.. option:: CONFIG_BLUETOOTH_HCI_CMD_COUNT:
.. _CONFIG_BLUETOOTH_HCI_CMD_COUNT:

Number of buffers available for HCI commands.



:Symbol:           BLUETOOTH_HCI_CMD_COUNT
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

 *  "Number of HCI command buffers"
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:37