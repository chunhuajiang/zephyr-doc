:orphan:

.. title:: ETH_KSDK_0_RANDOM_MAC

.. option:: CONFIG_ETH_KSDK_0_RANDOM_MAC:
.. _CONFIG_ETH_KSDK_0_RANDOM_MAC:

Generate a random MAC address dynamically.



:Symbol:           ETH_KSDK_0_RANDOM_MAC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Random MAC address" if ETH_KSDK_0 && RANDOM_GENERATOR (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: ETH_KSDK_0 && RANDOM_GENERATOR (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_KSDK (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.ksdk:62