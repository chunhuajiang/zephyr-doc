:orphan:

.. title:: BLUETOOTH_A2DP

.. option:: CONFIG_BLUETOOTH_A2DP:
.. _CONFIG_BLUETOOTH_A2DP:

This option enables the A2DP profile



:Symbol:           BLUETOOTH_A2DP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth A2DP Profile [EXPERIMENTAL]"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_BLUETOOTH_AVDTP`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:461