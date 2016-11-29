:orphan:

.. title:: NETWORKING_NO_WIRED

.. option:: CONFIG_NETWORKING_NO_WIRED:
.. _CONFIG_NETWORKING_NO_WIRED:

Do not enable any wired network driver. It is still
possible to select other types of network drivers if
this option is selected.


:Symbol:           NETWORKING_NO_WIRED
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "No wired network driver"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:277