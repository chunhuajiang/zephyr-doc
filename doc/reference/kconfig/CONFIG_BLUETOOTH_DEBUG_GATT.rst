:orphan:

.. title:: BLUETOOTH_DEBUG_GATT

.. option:: CONFIG_BLUETOOTH_DEBUG_GATT:
.. _CONFIG_BLUETOOTH_DEBUG_GATT:

This option enables debug support for the Bluetooth
Generic Attribute Profile (GATT).



:Symbol:           BLUETOOTH_DEBUG_GATT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth Generic Attribute Profile (GATT) debug"
 *  "Bluetooth Generic Attribute Profile (GATT) debug" if BLUETOOTH_CONN (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:92
 * ../subsys/bluetooth/host/Kconfig:383