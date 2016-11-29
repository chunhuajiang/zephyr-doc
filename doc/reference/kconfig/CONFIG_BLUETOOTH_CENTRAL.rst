:orphan:

.. title:: BLUETOOTH_CENTRAL

.. option:: CONFIG_BLUETOOTH_CENTRAL:
.. _CONFIG_BLUETOOTH_CENTRAL:

Select this for LE Central role support.



:Symbol:           BLUETOOTH_CENTRAL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Central Role support"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_BLUETOOTH_CONN`
:Reverse (select-related) dependencies:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_BREDR (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:44
 * ../subsys/bluetooth/host/Kconfig:131