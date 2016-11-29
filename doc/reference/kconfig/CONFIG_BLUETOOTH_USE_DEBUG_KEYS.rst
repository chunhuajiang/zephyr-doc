:orphan:

.. title:: BLUETOOTH_USE_DEBUG_KEYS

.. option:: CONFIG_BLUETOOTH_USE_DEBUG_KEYS:
.. _CONFIG_BLUETOOTH_USE_DEBUG_KEYS:

This option places Security Manager in a Debug Mode. In this mode
predefined Diffie-Hellman private/public key pair is used as described
in Core Specification Vol. 3, Part H, 2.3.5.6.1. This option should
only be enabled for debugging and should never be used in production.
If this option is enabled anyone is able to decipher encrypted air
traffic.



:Symbol:           BLUETOOTH_USE_DEBUG_KEYS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Security Manager Debug Mode" if BLUETOOTH_TINYCRYPT_ECC (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN && BLUETOOTH_SMP (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:206