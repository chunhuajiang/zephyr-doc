:orphan:

.. title:: BLUETOOTH_CONTROLLER_RX_BUFFERS

.. option:: CONFIG_BLUETOOTH_CONTROLLER_RX_BUFFERS:
.. _CONFIG_BLUETOOTH_CONTROLLER_RX_BUFFERS:

Set the number of Rx PDUs to be buffered in the controller.



:Symbol:           BLUETOOTH_CONTROLLER_RX_BUFFERS
:Type:             int
:Value:            "1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1, 10]
:Prompts:

 *  "Number of Rx buffers"
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
 *  6 (value: "n")
 *   Condition: BLUETOOTH_HCI_RAW (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_CONTROLLER && BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../subsys/bluetooth/controller/Kconfig:13