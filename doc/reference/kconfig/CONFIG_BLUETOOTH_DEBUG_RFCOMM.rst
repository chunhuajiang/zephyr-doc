:orphan:

.. title:: BLUETOOTH_DEBUG_RFCOMM

.. option:: CONFIG_BLUETOOTH_DEBUG_RFCOMM:
.. _CONFIG_BLUETOOTH_DEBUG_RFCOMM:

This option enables debug support for the Bluetooth
RFCOMM layer.



:Symbol:           BLUETOOTH_DEBUG_RFCOMM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth RFCOMM debug" if BLUETOOTH_RFCOMM (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:390