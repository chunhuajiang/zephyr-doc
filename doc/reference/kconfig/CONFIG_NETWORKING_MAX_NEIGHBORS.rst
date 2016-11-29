:orphan:

.. title:: NETWORKING_MAX_NEIGHBORS

.. option:: CONFIG_NETWORKING_MAX_NEIGHBORS:
.. _CONFIG_NETWORKING_MAX_NEIGHBORS:

Specifies the maximum number of neighbors that each node will
be able to handle.


:Symbol:           NETWORKING_MAX_NEIGHBORS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Max number of neighbors" if NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
:Default values:

 *  4 (value: "n")
 *   Condition: NETWORKING && NETWORKING_WITH_IPV6 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP && NETWORKING_WITH_IPV6 (value: "n")
:Locations:
 * ../net/ip/Kconfig:142