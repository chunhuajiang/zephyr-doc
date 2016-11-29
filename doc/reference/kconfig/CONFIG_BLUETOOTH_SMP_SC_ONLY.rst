:orphan:

.. title:: BLUETOOTH_SMP_SC_ONLY

.. option:: CONFIG_BLUETOOTH_SMP_SC_ONLY:
.. _CONFIG_BLUETOOTH_SMP_SC_ONLY:

This option enables support for Secure Connection Only Mode. In this
mode device shall only use Security Mode 1 Level 4 with exception
for services that only require Security Mode 1 Level 1 (no security).
Security Mode 1 Level 4 stands for authenticated LE Secure Connections
pairing with encryption. Enabling this option disables legacy pairing.



:Symbol:           BLUETOOTH_SMP_SC_ONLY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Secure Connections Only Mode"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN && BLUETOOTH_SMP (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:197