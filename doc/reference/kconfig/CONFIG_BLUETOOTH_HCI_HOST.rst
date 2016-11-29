:orphan:

.. title:: BLUETOOTH_HCI_HOST

.. option:: CONFIG_BLUETOOTH_HCI_HOST:
.. _CONFIG_BLUETOOTH_HCI_HOST:

The configuration item CONFIG_BLUETOOTH_HCI_HOST:

:Symbol:           BLUETOOTH_HCI_HOST
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  y (value: "y")
 *   Condition: !BLUETOOTH_HCI_RAW (value: "y")
:Selects:

 *  :option:`CONFIG_TINYCRYPT` if !BLUETOOTH_HCI_RAW (value: "y")
 *  :option:`CONFIG_TINYCRYPT_SHA256` if !BLUETOOTH_HCI_RAW (value: "y")
 *  :option:`CONFIG_TINYCRYPT_SHA256_HMAC` if !BLUETOOTH_HCI_RAW (value: "y")
 *  :option:`CONFIG_TINYCRYPT_SHA256_HMAC_PRNG` if !BLUETOOTH_HCI_RAW (value: "y")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:28