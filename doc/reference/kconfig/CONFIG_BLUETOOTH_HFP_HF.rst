:orphan:

.. title:: BLUETOOTH_HFP_HF

.. option:: CONFIG_BLUETOOTH_HFP_HF:
.. _CONFIG_BLUETOOTH_HFP_HF:

This option enables Bluetooth HF support



:Symbol:           BLUETOOTH_HFP_HF
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth Handsfree profile HF Role support [EXPERIMENTAL]"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_BLUETOOTH_RFCOMM`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:450