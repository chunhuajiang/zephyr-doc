:orphan:

.. title:: BLUETOOTH_DEBUG_HCI_DRIVER

.. option:: CONFIG_BLUETOOTH_DEBUG_HCI_DRIVER:
.. _CONFIG_BLUETOOTH_DEBUG_HCI_DRIVER:

This option enables debug support for the chosen
Bluetooth UART driver to Nordic chip.



:Symbol:           BLUETOOTH_DEBUG_HCI_DRIVER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth HCI driver debug" if BLUETOOTH_DEBUG (value: "n")
 *  "Bluetooth driver debug"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_CUSTOM && BLUETOOTH && NBLE && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../drivers/bluetooth/hci/Kconfig:73
 * ../drivers/bluetooth/nble/Kconfig:86