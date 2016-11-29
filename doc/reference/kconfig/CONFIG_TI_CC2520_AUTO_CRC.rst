:orphan:

.. title:: TI_CC2520_AUTO_CRC

.. option:: CONFIG_TI_CC2520_AUTO_CRC:
.. _CONFIG_TI_CC2520_AUTO_CRC:

When receiving a packet, the hardware can verify the CRC by itself
and will provide a flag letting know the success - or not - on
a flag on the footer.



:Symbol:           TI_CC2520_AUTO_CRC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Let the chip handling CRC on reception"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 && TI_CC2520_LINK_DETAILS || NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 && TI_CC2520_AUTO_ACK (value: "n")
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:104