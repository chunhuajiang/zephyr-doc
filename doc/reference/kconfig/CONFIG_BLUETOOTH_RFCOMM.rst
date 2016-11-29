:orphan:

.. title:: BLUETOOTH_RFCOMM

.. option:: CONFIG_BLUETOOTH_RFCOMM:
.. _CONFIG_BLUETOOTH_RFCOMM:

This option enables Bluetooth RFCOMM support



:Symbol:           BLUETOOTH_RFCOMM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth RFCOMM protocol support [EXPERIMENTAL]"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR && BLUETOOTH_HFP_HF (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:437