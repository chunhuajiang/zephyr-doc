:orphan:

.. title:: BLUETOOTH_CONTROLLER_DATA_LENGTH

.. option:: CONFIG_BLUETOOTH_CONTROLLER_DATA_LENGTH:
.. _CONFIG_BLUETOOTH_CONTROLLER_DATA_LENGTH:

Set the maximum data length of PDU supported in the stack.



:Symbol:           BLUETOOTH_CONTROLLER_DATA_LENGTH
:Type:             int
:Value:            "27"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [27, 251]
:Prompts:

 *  "Maximum data length supported"
:Default values:

 *  27 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_CONTROLLER && BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../subsys/bluetooth/controller/Kconfig:5