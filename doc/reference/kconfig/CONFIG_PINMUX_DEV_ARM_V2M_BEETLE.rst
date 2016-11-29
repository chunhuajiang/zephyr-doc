:orphan:

.. title:: PINMUX_DEV_ARM_V2M_BEETLE

.. option:: CONFIG_PINMUX_DEV_ARM_V2M_BEETLE:
.. _CONFIG_PINMUX_DEV_ARM_V2M_BEETLE:

Enables the pinmux dev driver for boards based on the
ARM Beetle SoC MCUs.
default n


:Symbol:           PINMUX_DEV_ARM_V2M_BEETLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable pinmux dev driver for ARM V2M Beetle boards" if PINMUX_DEV && SOC_SERIES_BEETLE (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX && BOARD_V2M_BEETLE && PINMUX_DEV (value: "n")
:Locations:
 * ../drivers/pinmux/dev/Kconfig:71
 * ../boards/arm/v2m_beetle/Kconfig.defconfig:50