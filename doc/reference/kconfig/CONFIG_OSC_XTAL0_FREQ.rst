:orphan:

.. title:: OSC_XTAL0_FREQ

.. option:: CONFIG_OSC_XTAL0_FREQ:
.. _CONFIG_OSC_XTAL0_FREQ:

Set the external oscillator frequency in Hz. This should be set by the
board's defconfig.



:Symbol:           OSC_XTAL0_FREQ
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "External oscillator frequency"
:Default values:

 *  12000000 (value: "n")
 *   Condition: (none)
 *  50000000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:80
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:29
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:29