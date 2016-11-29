:orphan:

.. title:: MCG_VDIV0

.. option:: CONFIG_MCG_VDIV0:
.. _CONFIG_MCG_VDIV0:

Selects the amount to divide the VCO output of the PLL. The VDIV 0 bits
establish the multiplication factor (M) applied to the reference clock
frequency.



:Symbol:           MCG_VDIV0
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 0x1F]
:Prompts:

 *  "VCO 0 divider"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
 *  0x06 (value: "n")
 *   Condition: (none)
 *  0x18 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:98
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:35
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:35