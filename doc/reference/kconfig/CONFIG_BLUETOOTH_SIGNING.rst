:orphan:

.. title:: BLUETOOTH_SIGNING

.. option:: CONFIG_BLUETOOTH_SIGNING:
.. _CONFIG_BLUETOOTH_SIGNING:

This option enables data signing which is used for transferring
authenticated data in an unencrypted connection.



:Symbol:           BLUETOOTH_SIGNING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Data signing support"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN && BLUETOOTH_SMP (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:191