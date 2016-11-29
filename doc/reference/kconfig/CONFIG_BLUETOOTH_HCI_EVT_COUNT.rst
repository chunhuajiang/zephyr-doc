:orphan:

.. title:: BLUETOOTH_HCI_EVT_COUNT

.. option:: CONFIG_BLUETOOTH_HCI_EVT_COUNT:
.. _CONFIG_BLUETOOTH_HCI_EVT_COUNT:

Number of buffers available for HCI events. This number should
ideally be at least as large as the available outgoing buffers
to make sure we've got enough buffers to handle bursts of
Number of Completed Packets HCI events.



:Symbol:           BLUETOOTH_HCI_EVT_COUNT
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

 *  "Number of HCI event buffers"
:Default values:

 *  4 (value: "n")
 *   Condition: (none)
 *  8 (value: "n")
 *   Condition: BLUETOOTH_CONN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:53