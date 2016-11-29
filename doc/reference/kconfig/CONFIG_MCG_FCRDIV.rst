:orphan:

.. title:: MCG_FCRDIV

.. option:: CONFIG_MCG_FCRDIV:
.. _CONFIG_MCG_FCRDIV:

Selects the amount to divide down the fast internal reference clock. The
resulting frequency must be in the range 31.25 kHz to 4 MHz.



:Symbol:           MCG_FCRDIV
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 7]
:Prompts:

 *  "Fast internal reference clock divider"
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:107
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:38
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:38