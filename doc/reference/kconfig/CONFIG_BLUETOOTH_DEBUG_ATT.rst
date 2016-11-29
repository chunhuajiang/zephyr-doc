:orphan:

.. title:: BLUETOOTH_DEBUG_ATT

.. option:: CONFIG_BLUETOOTH_DEBUG_ATT:
.. _CONFIG_BLUETOOTH_DEBUG_ATT:

This option enables debug support for the Bluetooth
Attribute Protocol (ATT).



:Symbol:           BLUETOOTH_DEBUG_ATT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth Attribute Protocol (ATT) debug" if BLUETOOTH_CONN (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:376