:orphan:

.. title:: NETWORKING_WITH_TCP

.. option:: CONFIG_NETWORKING_WITH_TCP:
.. _CONFIG_NETWORKING_WITH_TCP:

Enable Transmission and Control Protocol (TCP) support.



:Symbol:           NETWORKING_WITH_TCP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable TCP protocol" if NETWORKING (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:152