:orphan:

.. title:: ETH_KSDK_0

.. option:: CONFIG_ETH_KSDK_0:
.. _CONFIG_ETH_KSDK_0:

Include port 0 driver



:Symbol:           ETH_KSDK_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "KSDK Ethernet port 0"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETHERNET && BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.ksdk:44
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:176
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:176