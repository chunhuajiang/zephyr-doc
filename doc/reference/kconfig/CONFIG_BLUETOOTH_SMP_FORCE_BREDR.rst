:orphan:

.. title:: BLUETOOTH_SMP_FORCE_BREDR

.. option:: CONFIG_BLUETOOTH_SMP_FORCE_BREDR:
.. _CONFIG_BLUETOOTH_SMP_FORCE_BREDR:

This option enables SMP over BR/EDR even if controller is not
supporting BR/EDR Secure Connections. This optino is solely for
testing and should never be enabled on production devices.



:Symbol:           BLUETOOTH_SMP_FORCE_BREDR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Force Bluetooth SMP over BR/EDR" if BLUETOOTH_DEBUG_SMP (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:368