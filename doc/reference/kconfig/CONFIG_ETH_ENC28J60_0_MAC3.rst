:orphan:

.. title:: ETH_ENC28J60_0_MAC3

.. option:: CONFIG_ETH_ENC28J60_0_MAC3:
.. _CONFIG_ETH_ENC28J60_0_MAC3:

MACADDR<0:23> are Microchip's OUI.
This is the byte 3 of the MAC address.
MACADDR<31:24>



:Symbol:           ETH_ENC28J60_0_MAC3
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "MAC Address Byte 3"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_ENC28J60 && ETH_ENC28J60_0 (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.enc28j60:86