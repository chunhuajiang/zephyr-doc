:orphan:

.. title:: UART_CMSDK_APB_PORT2_NAME

.. option:: CONFIG_UART_CMSDK_APB_PORT2_NAME:
.. _CONFIG_UART_CMSDK_APB_PORT2_NAME:

This is the device name for UART, and is included in the device
struct.



:Symbol:           UART_CMSDK_APB_PORT2_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name for UART 2" if UART_CMSDK_APB_PORT2 (value: "n")
:Default values:

 *  "UART_2"
 *   Condition: UART_CMSDK_APB_PORT2 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_CMSDK_APB && SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cmsdk_apb:101