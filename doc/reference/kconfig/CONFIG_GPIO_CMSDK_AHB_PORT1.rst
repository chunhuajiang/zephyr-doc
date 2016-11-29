:orphan:

.. title:: GPIO_CMSDK_AHB_PORT1

.. option:: CONFIG_GPIO_CMSDK_AHB_PORT1:
.. _CONFIG_GPIO_CMSDK_AHB_PORT1:

Build the driver to utilize GPIO controller Port 1.



:Symbol:           GPIO_CMSDK_AHB_PORT1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable driver for GPIO Port 1" if GPIO_CMSDK_AHB (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_CMSDK_AHB (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && BOARD_V2M_BEETLE (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.cmsdk_ahb:55
 * ../boards/arm/v2m_beetle/Kconfig.defconfig:32