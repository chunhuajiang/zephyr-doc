:orphan:

.. title:: BLUETOOTH_GATT_CLIENT

.. option:: CONFIG_BLUETOOTH_GATT_CLIENT:
.. _CONFIG_BLUETOOTH_GATT_CLIENT:

This option enables support for the GATT Client role.



:Symbol:           BLUETOOTH_GATT_CLIENT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GATT client support"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:56
 * ../subsys/bluetooth/host/Kconfig:231