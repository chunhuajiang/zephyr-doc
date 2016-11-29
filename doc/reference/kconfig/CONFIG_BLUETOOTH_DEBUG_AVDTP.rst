:orphan:

.. title:: BLUETOOTH_DEBUG_AVDTP

.. option:: CONFIG_BLUETOOTH_DEBUG_AVDTP:
.. _CONFIG_BLUETOOTH_DEBUG_AVDTP:

This option enables debug support for the Bluetooth AVDTP.



:Symbol:           BLUETOOTH_DEBUG_AVDTP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth AVDTP debug" if BLUETOOTH_AVDTP (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:404