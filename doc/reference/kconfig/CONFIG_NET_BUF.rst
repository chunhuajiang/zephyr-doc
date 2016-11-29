:orphan:

.. title:: NET_BUF

.. option:: CONFIG_NET_BUF:
.. _CONFIG_NET_BUF:

This option enables support for generic network protocol
buffers.



:Symbol:           NET_BUF
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Network buffer support"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_CUSTOM && BLUETOOTH && SERIAL && NBLE || NETWORKING || BLUETOOTH (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../net/Kconfig:23