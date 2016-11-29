:orphan:

.. title:: ETH_KSDK_TX_BUFFERS

.. option:: CONFIG_ETH_KSDK_TX_BUFFERS:
.. _CONFIG_ETH_KSDK_TX_BUFFERS:

Set the number of TX buffers provided to the KSDK driver.



:Symbol:           ETH_KSDK_TX_BUFFERS
:Type:             int
:Value:            "1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1, 16]
:Prompts:

 *  "Number of KSDK TX buffers" if ETH_KSDK (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: ETH_KSDK (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_KSDK (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.ksdk:36