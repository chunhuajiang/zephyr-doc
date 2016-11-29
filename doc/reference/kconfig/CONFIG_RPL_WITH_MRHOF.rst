:orphan:

.. title:: RPL_WITH_MRHOF

.. option:: CONFIG_RPL_WITH_MRHOF:
.. _CONFIG_RPL_WITH_MRHOF:

Choose this (MRHOF) if unsure.


:Symbol:           RPL_WITH_MRHOF
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Minimum Rank with Hysteresis, RFC 6719"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:236