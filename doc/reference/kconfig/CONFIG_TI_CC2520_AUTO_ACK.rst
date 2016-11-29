:orphan:

.. title:: TI_CC2520_AUTO_ACK

.. option:: CONFIG_TI_CC2520_AUTO_ACK:
.. _CONFIG_TI_CC2520_AUTO_ACK:

The chip is able to reply by itself to ACK requests as well as
waiting for an ACK when a TX packet is requesting an ACK. However,
this feature requires the chip to get hardware filtering on, and
thus the above stack needs to provide the right information for such
filtering feature to work.



:Symbol:           TI_CC2520_AUTO_ACK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Let the chip handle TX/RX IEEE 802.15.4 ACK requests"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_TI_CC2520_AUTO_CRC`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:120