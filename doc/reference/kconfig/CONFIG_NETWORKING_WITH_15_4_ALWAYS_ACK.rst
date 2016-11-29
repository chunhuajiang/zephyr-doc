:orphan:

.. title:: NETWORKING_WITH_15_4_ALWAYS_ACK

.. option:: CONFIG_NETWORKING_WITH_15_4_ALWAYS_ACK:
.. _CONFIG_NETWORKING_WITH_15_4_ALWAYS_ACK:

This is meant to be used for testing only. Requesting an
acknowledgment on all data packet will draw power resource.
Use case for this option it for testing only.



:Symbol:           NETWORKING_WITH_15_4_ALWAYS_ACK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Always request 802.15.4 packet acknowledgment" if NETWORKING_WITH_15_4 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_15_4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:332