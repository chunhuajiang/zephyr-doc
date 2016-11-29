:orphan:

.. title:: TI_CC2520_CHANNEL

.. option:: CONFIG_TI_CC2520_CHANNEL:
.. _CONFIG_TI_CC2520_CHANNEL:

All the 802.15.4 devices that want to connect to each other need
to have same channel. Default channel is 26.



:Symbol:           TI_CC2520_CHANNEL
:Type:             int
:Value:            "11"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [11, 26]
:Prompts:

 *  "TI CC2520 Channel"
:Default values:

 *  26 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:96