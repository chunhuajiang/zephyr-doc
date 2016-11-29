:orphan:

.. title:: BLUETOOTH_CONTROLLER

.. option:: CONFIG_BLUETOOTH_CONTROLLER:
.. _CONFIG_BLUETOOTH_CONTROLLER:

Enables support for SoC native controller implementation.



:Symbol:           BLUETOOTH_CONTROLLER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth Controller"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_BLUETOOTH_HOST_BUFFERS`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/Kconfig:48