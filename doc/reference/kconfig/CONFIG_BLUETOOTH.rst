:orphan:

.. title:: BLUETOOTH

.. option:: CONFIG_BLUETOOTH:
.. _CONFIG_BLUETOOTH:

This option enables Bluetooth support.



:Symbol:           BLUETOOTH
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth support"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_NET_BUF`
:Reverse (select-related) dependencies:
 NETWORKING && NETWORKING_WITH_IPV6 && NETWORKING && NET_UIP && NETWORKING_WITH_BT (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../subsys/bluetooth/Kconfig:18