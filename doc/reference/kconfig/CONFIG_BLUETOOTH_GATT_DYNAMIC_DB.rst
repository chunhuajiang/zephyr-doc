:orphan:

.. title:: BLUETOOTH_GATT_DYNAMIC_DB

.. option:: CONFIG_BLUETOOTH_GATT_DYNAMIC_DB:
.. _CONFIG_BLUETOOTH_GATT_DYNAMIC_DB:

This option enables GATT services to be added dynamically to database.



:Symbol:           BLUETOOTH_GATT_DYNAMIC_DB
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GATT dynamic database support"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:226