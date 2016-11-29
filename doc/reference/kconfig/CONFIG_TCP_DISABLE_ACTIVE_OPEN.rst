:orphan:

.. title:: TCP_DISABLE_ACTIVE_OPEN

.. option:: CONFIG_TCP_DISABLE_ACTIVE_OPEN:
.. _CONFIG_TCP_DISABLE_ACTIVE_OPEN:

By default application is allowed to initiate a TCP
connection attempt. If the application is only acting
as a server, then some memory can be saved by disabling
the client role.



:Symbol:           TCP_DISABLE_ACTIVE_OPEN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Disallow host to initiate connection attempt" if NETWORKING_WITH_TCP (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_TCP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:169