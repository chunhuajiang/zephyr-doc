:orphan:

.. title:: BLUETOOTH_DEBUG_NONE

.. option:: CONFIG_BLUETOOTH_DEBUG_NONE:
.. _CONFIG_BLUETOOTH_DEBUG_NONE:

Select this to disable all Bluetooth debug logs.



:Symbol:           BLUETOOTH_DEBUG_NONE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "No debug log"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:275