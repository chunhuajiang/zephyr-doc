:orphan:

.. title:: PINMUX_BEETLE

.. option:: CONFIG_PINMUX_BEETLE:
.. _CONFIG_PINMUX_BEETLE:

Enable driver for ARM V2M Beetle Pin multiplexer.


:Symbol:           PINMUX_BEETLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ARM V2M Beetle Pin multiplexer driver" if PINMUX && SOC_SERIES_BEETLE (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PINMUX && SOC_SERIES_BEETLE (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX && BOARD_V2M_BEETLE (value: "n")
:Locations:
 * ../drivers/pinmux/Kconfig.beetle:19
 * ../boards/arm/v2m_beetle/Kconfig.defconfig:45