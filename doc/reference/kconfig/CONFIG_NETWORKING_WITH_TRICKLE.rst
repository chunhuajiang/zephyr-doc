:orphan:

.. title:: NETWORKING_WITH_TRICKLE

.. option:: CONFIG_NETWORKING_WITH_TRICKLE:
.. _CONFIG_NETWORKING_WITH_TRICKLE:

Enable Trickle algorithm (RFC 6206) support. This only
includes Trickle library but IP stack does not call its
functions.



:Symbol:           NETWORKING_WITH_TRICKLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Trickle algorithm" if NETWORKING (value: "n")
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
 * ../net/ip/Kconfig:246