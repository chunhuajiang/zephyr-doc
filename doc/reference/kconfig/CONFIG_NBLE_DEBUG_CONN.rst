:orphan:

.. title:: NBLE_DEBUG_CONN

.. option:: CONFIG_NBLE_DEBUG_CONN:
.. _CONFIG_NBLE_DEBUG_CONN:

This option enables debug support for Bluetooth
connections in the nble driver.



:Symbol:           NBLE_DEBUG_CONN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "NBLE connection debug"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_CUSTOM && BLUETOOTH && NBLE && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:105