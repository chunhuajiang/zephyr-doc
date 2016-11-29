:orphan:

.. title:: BLUETOOTH_SMP_SELFTEST

.. option:: CONFIG_BLUETOOTH_SMP_SELFTEST:
.. _CONFIG_BLUETOOTH_SMP_SELFTEST:

This option enables SMP self-tests executed on startup
to verify security and crypto functions.



:Symbol:           BLUETOOTH_SMP_SELFTEST
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth SMP self tests executed on init" if BLUETOOTH_DEBUG_SMP (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:361