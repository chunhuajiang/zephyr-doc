:orphan:

.. title:: BLUETOOTH_DEBUG_HCI_CORE

.. option:: CONFIG_BLUETOOTH_DEBUG_HCI_CORE:
.. _CONFIG_BLUETOOTH_DEBUG_HCI_CORE:

This option enables debug support for Bluetooth HCI
core.



:Symbol:           BLUETOOTH_DEBUG_HCI_CORE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth HCI core debug" if BLUETOOTH_HCI_HOST (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:324