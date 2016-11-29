:orphan:

.. title:: BLUETOOTH_BREDR_NAME

.. option:: CONFIG_BLUETOOTH_BREDR_NAME:
.. _CONFIG_BLUETOOTH_BREDR_NAME:

Bluetooth BR/EDR name. Name can be up to 248 bytes long (excluding
NULL termination). Can be empty string.


:Symbol:           BLUETOOTH_BREDR_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth BR/EDR device name"
:Default values:

 *  "Zephyr"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:475