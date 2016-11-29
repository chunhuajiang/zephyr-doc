:orphan:

.. title:: TCP_RECEIVE_WINDOW

.. option:: CONFIG_TCP_RECEIVE_WINDOW:
.. _CONFIG_TCP_RECEIVE_WINDOW:

Tweak the TCP receive window size. Normally one should
not change this but let the IP stack to calculate a best
size for it.



:Symbol:           TCP_RECEIVE_WINDOW
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "TCP receive window size" if NETWORKING_WITH_TCP (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: NETWORKING_WITH_TCP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:190