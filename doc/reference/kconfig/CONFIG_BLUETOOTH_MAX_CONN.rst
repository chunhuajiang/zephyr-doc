:orphan:

.. title:: BLUETOOTH_MAX_CONN

.. option:: CONFIG_BLUETOOTH_MAX_CONN:
.. _CONFIG_BLUETOOTH_MAX_CONN:

Maximum number of simultaneous Bluetooth connections
supported. The minimum (and default) number is 1.



:Symbol:           BLUETOOTH_MAX_CONN
:Type:             int
:Value:            "1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1, 64]
:Prompts:

 *  "Maximum number of simultaneous connections" if BLUETOOTH_CONN || BLUETOOTH_CONTROLLER (value: "n")
:Default values:

 *  6 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: BLUETOOTH_CONN || BLUETOOTH_CONTROLLER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:64
 * ../subsys/bluetooth/host/Kconfig:258