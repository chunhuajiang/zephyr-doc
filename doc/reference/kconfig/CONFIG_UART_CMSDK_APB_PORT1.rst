:orphan:

.. title:: UART_CMSDK_APB_PORT1

.. option:: CONFIG_UART_CMSDK_APB_PORT1:
.. _CONFIG_UART_CMSDK_APB_PORT1:

Build the driver to utilize UART controller Port 1.



:Symbol:           UART_CMSDK_APB_PORT1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable driver for UART 1"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL && BOARD_V2M_BEETLE (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cmsdk_apb:63
 * ../boards/arm/v2m_beetle/Kconfig.defconfig:65