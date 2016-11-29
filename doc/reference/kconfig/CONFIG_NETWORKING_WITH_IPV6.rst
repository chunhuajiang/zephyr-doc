:orphan:

.. title:: NETWORKING_WITH_IPV6

.. option:: CONFIG_NETWORKING_WITH_IPV6:
.. _CONFIG_NETWORKING_WITH_IPV6:

Choose this if unsure.


:Symbol:           NETWORKING_WITH_IPV6
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IPv6"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:110