:orphan:

.. title:: MCG_PRDIV0

.. option:: CONFIG_MCG_PRDIV0:
.. _CONFIG_MCG_PRDIV0:

Selects the amount to divide down the external reference clock for the PLL.
The resulting frequency must be in the range of 2 MHz to 4 MHz.



:Symbol:           MCG_PRDIV0
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 0x18]
:Prompts:

 *  "PLL external reference divider"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
 *  0x02 (value: "n")
 *   Condition: (none)
 *  0x13 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:90
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:32
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:32