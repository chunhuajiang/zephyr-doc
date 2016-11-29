:orphan:

.. title:: NETWORKING_WITH_15_4_LOOPBACK

.. option:: CONFIG_NETWORKING_WITH_15_4_LOOPBACK:
.. _CONFIG_NETWORKING_WITH_15_4_LOOPBACK:

Enable 802.15.4 loopback radio driver that receives
the 802.15.4 frame and put it back 802.15.4 Rx Fifo.



:Symbol:           NETWORKING_WITH_15_4_LOOPBACK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Loopback"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:431