:orphan:

.. title:: ETH_KSDK_0_MAC1

.. option:: CONFIG_ETH_KSDK_0_MAC1:
.. _CONFIG_ETH_KSDK_0_MAC1:

This is the byte 1 of the MAC address.



:Symbol:           ETH_KSDK_0_MAC1
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, ff]
:Prompts:

 *  "MAC Address Byte 1"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_KSDK_0 && !ETH_KSDK_0_RANDOM_MAC && ETH_KSDK (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.ksdk:78