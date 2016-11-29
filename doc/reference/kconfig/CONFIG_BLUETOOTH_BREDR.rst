:orphan:

.. title:: BLUETOOTH_BREDR

.. option:: CONFIG_BLUETOOTH_BREDR:
.. _CONFIG_BLUETOOTH_BREDR:

This option enables Bluetooth BR/EDR support"



:Symbol:           BLUETOOTH_BREDR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth BR/EDR support [EXPERIMENTAL]" if BLUETOOTH_HCI_HOST (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_BLUETOOTH_PERIPHERAL` if BLUETOOTH_HCI_HOST (value: "n")
 *  :option:`CONFIG_BLUETOOTH_CENTRAL` if BLUETOOTH_HCI_HOST (value: "n")
 *  :option:`CONFIG_BLUETOOTH_SMP` if BLUETOOTH_HCI_HOST (value: "n")
 *  :option:`CONFIG_BLUETOOTH_L2CAP_DYNAMIC_CHANNEL` if BLUETOOTH_HCI_HOST (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:426