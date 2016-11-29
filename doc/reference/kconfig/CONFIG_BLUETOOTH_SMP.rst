:orphan:

.. title:: BLUETOOTH_SMP

.. option:: CONFIG_BLUETOOTH_SMP:
.. _CONFIG_BLUETOOTH_SMP:

This option enables support for the Security Manager Protocol
(SMP), making it possible to pair devices over LE.



:Symbol:           BLUETOOTH_SMP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Security Manager Protocol support"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_TINYCRYPT_AES`
 *  :option:`CONFIG_TINYCRYPT_AES_CMAC`
:Reverse (select-related) dependencies:
 NETWORKING && NETWORKING_WITH_IPV6 && NETWORKING && NET_UIP && NETWORKING_WITH_BT || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_BREDR (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:60
 * ../subsys/bluetooth/host/Kconfig:167