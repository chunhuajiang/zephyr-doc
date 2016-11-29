:orphan:

.. title:: BLUETOOTH_TINYCRYPT_ECC

.. option:: CONFIG_BLUETOOTH_TINYCRYPT_ECC:
.. _CONFIG_BLUETOOTH_TINYCRYPT_ECC:

If this option is set TinyCrypt library is used for emulating the
ECDH HCI commands and events needed by e.g. LE Secure Connections.
If not set controller crypto is used for ECDH and if
controller doesn't support required HCI commands LE Secure
Connections support will be disabled.



:Symbol:           BLUETOOTH_TINYCRYPT_ECC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use TinyCrypt library for ECDH"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_TINYCRYPT_ECC_DH`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:246