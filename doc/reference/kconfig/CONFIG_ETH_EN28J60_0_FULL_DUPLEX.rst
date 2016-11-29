:orphan:

.. title:: ETH_EN28J60_0_FULL_DUPLEX

.. option:: CONFIG_ETH_EN28J60_0_FULL_DUPLEX:
.. _CONFIG_ETH_EN28J60_0_FULL_DUPLEX:

Enable Full Duplex. Device is configured half duplex
when disabled.



:Symbol:           ETH_EN28J60_0_FULL_DUPLEX
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ENC28J60 full duplex"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_ENC28J60 && ETH_ENC28J60_0 (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.enc28j60:40