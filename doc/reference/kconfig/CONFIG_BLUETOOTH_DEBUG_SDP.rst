:orphan:

.. title:: BLUETOOTH_DEBUG_SDP

.. option:: CONFIG_BLUETOOTH_DEBUG_SDP:
.. _CONFIG_BLUETOOTH_DEBUG_SDP:

This option enables debug support for the Bluetooth
Service Discovery Protocol (SDP).



:Symbol:           BLUETOOTH_DEBUG_SDP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth Service Discovery Protocol (SDP) debug" if BLUETOOTH_BREDR (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:417