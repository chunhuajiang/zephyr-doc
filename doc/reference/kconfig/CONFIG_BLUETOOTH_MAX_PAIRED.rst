:orphan:

.. title:: BLUETOOTH_MAX_PAIRED

.. option:: CONFIG_BLUETOOTH_MAX_PAIRED:
.. _CONFIG_BLUETOOTH_MAX_PAIRED:

Maximum number of paired Bluetooth devices. The minimum (and
default) number is 1.



:Symbol:           BLUETOOTH_MAX_PAIRED
:Type:             int
:Value:            "1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1, 128]
:Prompts:

 *  "Maximum number of paired devices"
:Default values:

 *  7 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:68
 * ../subsys/bluetooth/host/Kconfig:236