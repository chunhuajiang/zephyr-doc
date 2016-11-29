:orphan:

.. title:: BLUETOOTH_DEBUG_CONN

.. option:: CONFIG_BLUETOOTH_DEBUG_CONN:
.. _CONFIG_BLUETOOTH_DEBUG_CONN:

This option enables debug support for Bluetooth
connection handling.



:Symbol:           BLUETOOTH_DEBUG_CONN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth connection debug" if BLUETOOTH_CONN (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:331