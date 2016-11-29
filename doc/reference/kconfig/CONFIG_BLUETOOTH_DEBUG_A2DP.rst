:orphan:

.. title:: BLUETOOTH_DEBUG_A2DP

.. option:: CONFIG_BLUETOOTH_DEBUG_A2DP:
.. _CONFIG_BLUETOOTH_DEBUG_A2DP:

This option enables debug support for the Bluetooth
A2DP profile.



:Symbol:           BLUETOOTH_DEBUG_A2DP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth A2DP debug" if BLUETOOTH_A2DP (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:410