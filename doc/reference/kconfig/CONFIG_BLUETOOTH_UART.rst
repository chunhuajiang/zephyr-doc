:orphan:

.. title:: BLUETOOTH_UART

.. option:: CONFIG_BLUETOOTH_UART:
.. _CONFIG_BLUETOOTH_UART:

The configuration item CONFIG_BLUETOOTH_UART:

:Symbol:           BLUETOOTH_UART
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER && SERIAL && BLUETOOTH_H4 || BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER && SERIAL && BLUETOOTH_H5 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../drivers/bluetooth/hci/Kconfig:25