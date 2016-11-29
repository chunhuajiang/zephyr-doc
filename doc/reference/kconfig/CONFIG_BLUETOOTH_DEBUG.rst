:orphan:

.. title:: BLUETOOTH_DEBUG

.. option:: CONFIG_BLUETOOTH_DEBUG:
.. _CONFIG_BLUETOOTH_DEBUG:

The configuration item CONFIG_BLUETOOTH_DEBUG:

:Symbol:           BLUETOOTH_DEBUG
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
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG_LOG || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG_MONITOR (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:267