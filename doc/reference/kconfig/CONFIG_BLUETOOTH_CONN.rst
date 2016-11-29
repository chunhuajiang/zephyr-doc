:orphan:

.. title:: BLUETOOTH_CONN

.. option:: CONFIG_BLUETOOTH_CONN:
.. _CONFIG_BLUETOOTH_CONN:

The configuration item CONFIG_BLUETOOTH_CONN:

:Symbol:           BLUETOOTH_CONN
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
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_PERIPHERAL || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CENTRAL (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:137