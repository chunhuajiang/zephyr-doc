:orphan:

.. title:: BLUETOOTH_DEBUG_HFP_HF

.. option:: CONFIG_BLUETOOTH_DEBUG_HFP_HF:
.. _CONFIG_BLUETOOTH_DEBUG_HFP_HF:

This option enables debug support for the Bluetooth
Hands Free Profile (HFP).



:Symbol:           BLUETOOTH_DEBUG_HFP_HF
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth Hands Free Profile (HFP) debug" if BLUETOOTH_HFP_HF (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:397