:orphan:

.. title:: BLUETOOTH_AVDTP

.. option:: CONFIG_BLUETOOTH_AVDTP:
.. _CONFIG_BLUETOOTH_AVDTP:

This option enables Bluetooth AVDTP support



:Symbol:           BLUETOOTH_AVDTP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth AVDTP protocol support [EXPERIMENTAL]"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR && BLUETOOTH_A2DP (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:456