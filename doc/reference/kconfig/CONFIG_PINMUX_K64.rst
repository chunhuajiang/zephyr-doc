:orphan:

.. title:: PINMUX_K64

.. option:: CONFIG_PINMUX_K64:
.. _CONFIG_PINMUX_K64:

Enable driver for Freescale K64-based Pin multiplexer.



:Symbol:           PINMUX_K64
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based Pin multiplexer driver" if SOC_MK64F12 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SOC_MK64F12 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_MK64F12 && SOC_SERIES_KINETIS_K6X && PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/Kconfig:52
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:27