:orphan:

.. title:: ETH_ENC28J60_0_SPI_BUS_FREQ

.. option:: CONFIG_ETH_ENC28J60_0_SPI_BUS_FREQ:
.. _CONFIG_ETH_ENC28J60_0_SPI_BUS_FREQ:

This is the maximum supported SPI bus frequency.



:Symbol:           ETH_ENC28J60_0_SPI_BUS_FREQ
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ENC28J60C SPI bus speed in Hz"
:Default values:

 *  128 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_ENC28J60 && ETH_ENC28J60_0 (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.enc28j60:80