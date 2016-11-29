:orphan:

.. title:: BLUETOOTH_NO_DRIVER

.. option:: CONFIG_BLUETOOTH_NO_DRIVER:
.. _CONFIG_BLUETOOTH_NO_DRIVER:

This is intended for unit tests where no internal driver
should be selected.



:Symbol:           BLUETOOTH_NO_DRIVER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "No default HCI driver"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../drivers/bluetooth/hci/Kconfig:52