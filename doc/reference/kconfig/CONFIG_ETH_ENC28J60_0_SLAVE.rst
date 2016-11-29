:orphan:

.. title:: ETH_ENC28J60_0_SLAVE

.. option:: CONFIG_ETH_ENC28J60_0_SLAVE:
.. _CONFIG_ETH_ENC28J60_0_SLAVE:

ENC28J60C chip select pin.



:Symbol:           ETH_ENC28J60_0_SLAVE
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ETH_ENC28J60 SPI slave select pin"
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_ENC28J60 && ETH_ENC28J60_0 (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.enc28j60:74