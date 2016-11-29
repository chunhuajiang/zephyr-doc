:orphan:

.. title:: BLUETOOTH_DEBUG_SMP

.. option:: CONFIG_BLUETOOTH_DEBUG_SMP:
.. _CONFIG_BLUETOOTH_DEBUG_SMP:

This option enables debug support for the Bluetooth
Security Manager Protocol (SMP).



:Symbol:           BLUETOOTH_DEBUG_SMP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth Security Manager Protocol (SMP) debug" if BLUETOOTH_HCI_HOST && BLUETOOTH_SMP (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:353