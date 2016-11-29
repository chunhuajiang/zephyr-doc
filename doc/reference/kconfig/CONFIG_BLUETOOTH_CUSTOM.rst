:orphan:

.. title:: BLUETOOTH_CUSTOM

.. option:: CONFIG_BLUETOOTH_CUSTOM:
.. _CONFIG_BLUETOOTH_CUSTOM:

Select a custom, non-HCI based stack. If you're not sure what
this is, you probably want the HCI-based stack instead.



:Symbol:           BLUETOOTH_CUSTOM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Custom"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/Kconfig:38