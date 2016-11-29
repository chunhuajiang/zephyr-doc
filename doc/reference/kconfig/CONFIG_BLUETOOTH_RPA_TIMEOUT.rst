:orphan:

.. title:: BLUETOOTH_RPA_TIMEOUT

.. option:: CONFIG_BLUETOOTH_RPA_TIMEOUT:
.. _CONFIG_BLUETOOTH_RPA_TIMEOUT:

This option defines how often resolvable private address is rotated.
Value is provided in seconds and defaults to 900 seconds (15 minutes).



:Symbol:           BLUETOOTH_RPA_TIMEOUT
:Type:             int
:Value:            "1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1, 65535]
:Prompts:

 *  "Resolvable Private Address timeout" if BLUETOOTH_PRIVACY (value: "n")
:Default values:

 *  900 (value: "n")
 *   Condition: BLUETOOTH_PRIVACY (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN && BLUETOOTH_SMP (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:182