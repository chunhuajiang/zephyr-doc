:orphan:

.. title:: NETWORKING_WITH_15_4_PAN_ID

.. option:: CONFIG_NETWORKING_WITH_15_4_PAN_ID:
.. _CONFIG_NETWORKING_WITH_15_4_PAN_ID:

All the 802.15.4 devices that want to connect to each
other need to have same PAN id (address).
Default PAN id is 0xABCD



:Symbol:           NETWORKING_WITH_15_4_PAN_ID
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IEEE 802.15.4 PAN id/address" if NETWORKING_WITH_15_4 (value: "n")
:Default values:

 *  0xabcd (value: "n")
 *   Condition: NETWORKING_WITH_15_4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:406