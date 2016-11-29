:orphan:

.. title:: TCP_MAX_CONNECTIONS

.. option:: CONFIG_TCP_MAX_CONNECTIONS:
.. _CONFIG_TCP_MAX_CONNECTIONS:

Tweak the TCP maximum segment size. Normally one should
not change this but let the IP stack to calculate a best
size for it.



:Symbol:           TCP_MAX_CONNECTIONS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Maximum number of connections" if NETWORKING_WITH_TCP (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: NETWORKING_WITH_TCP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:160