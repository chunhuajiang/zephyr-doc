:orphan:

.. title:: UART_CMSDK_APB

.. option:: CONFIG_UART_CMSDK_APB:
.. _CONFIG_UART_CMSDK_APB:

This option enables the UART driver for ARM CMSDK APB UART.



:Symbol:           UART_CMSDK_APB
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ARM CMSDK APB UART driver" if SOC_FAMILY_ARM (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SOC_FAMILY_ARM (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_SERIAL_HAS_DRIVER` if SOC_FAMILY_ARM (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL && BOARD_V2M_BEETLE (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cmsdk_apb:19
 * ../boards/arm/v2m_beetle/Kconfig.defconfig:59