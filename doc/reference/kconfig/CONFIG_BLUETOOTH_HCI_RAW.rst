:orphan:

.. title:: BLUETOOTH_HCI_RAW

.. option:: CONFIG_BLUETOOTH_HCI_RAW:
.. _CONFIG_BLUETOOTH_HCI_RAW:

This option allows to access Bluetooth controller
from the application with the RAW HCI protocol.



:Symbol:           BLUETOOTH_HCI_RAW
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "RAW HCI access"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:21