:orphan:

.. title:: GPIO_CMSDK_AHB

.. option:: CONFIG_GPIO_CMSDK_AHB:
.. _CONFIG_GPIO_CMSDK_AHB:

Enable config options to support the ARM CMSDK GPIO controllers.

Says n if not sure.



:Symbol:           GPIO_CMSDK_AHB
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ARM CMSDK (Cortex-M System Design Kit) AHB GPIO Controllers" if GPIO && SOC_SERIES_BEETLE (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO && SOC_SERIES_BEETLE (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && BOARD_V2M_BEETLE (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.cmsdk_ahb:19
 * ../boards/arm/v2m_beetle/Kconfig.defconfig:26