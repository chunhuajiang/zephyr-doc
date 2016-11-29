:orphan:

.. title:: NBLE_DEBUG_GAP

.. option:: CONFIG_NBLE_DEBUG_GAP:
.. _CONFIG_NBLE_DEBUG_GAP:

This option enables debug support for the Bluetooth
Generic Access Profile (GAP) in the interfaces to the
Nordic chip.



:Symbol:           NBLE_DEBUG_GAP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "NBLE Generic Access Profile (GAP) debug"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_CUSTOM && BLUETOOTH && NBLE && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:98