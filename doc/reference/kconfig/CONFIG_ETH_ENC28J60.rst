:orphan:

.. title:: ETH_ENC28J60

.. option:: CONFIG_ETH_ENC28J60:
.. _CONFIG_ETH_ENC28J60:

ENC28J60C Stand-Alone Ethernet Controller
with SPI Interface



:Symbol:           ETH_ENC28J60
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ENC28J60C Ethernet Controller" if ETHERNET && SPI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: ETHERNET && SPI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/ethernet/Kconfig.enc28j60:19