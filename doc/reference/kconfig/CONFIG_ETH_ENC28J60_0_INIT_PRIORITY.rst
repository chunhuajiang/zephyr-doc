:orphan:

.. title:: ETH_ENC28J60_0_INIT_PRIORITY

.. option:: CONFIG_ETH_ENC28J60_0_INIT_PRIORITY:
.. _CONFIG_ETH_ENC28J60_0_INIT_PRIORITY:

Device driver initialization priority.
Since the device is connected to SPI bus, its driver has
to be initialized after the SPI one.



:Symbol:           ETH_ENC28J60_0_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ENC28J60C init priority"
:Default values:

 *  80 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_ENC28J60 && ETH_ENC28J60_0 (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.enc28j60:47