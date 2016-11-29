:orphan:

.. title:: NBLE_DEBUG_RPC

.. option:: CONFIG_NBLE_DEBUG_RPC:
.. _CONFIG_NBLE_DEBUG_RPC:

This option enables debug for RPC interface to the Nordic
Bluetooth LE chip.



:Symbol:           NBLE_DEBUG_RPC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "NBLE RPC debug"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_CUSTOM && BLUETOOTH && NBLE && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:111