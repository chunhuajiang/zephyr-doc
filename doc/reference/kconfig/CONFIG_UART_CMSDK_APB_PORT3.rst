:orphan:

.. title:: UART_CMSDK_APB_PORT3

.. option:: CONFIG_UART_CMSDK_APB_PORT3:
.. _CONFIG_UART_CMSDK_APB_PORT3:

Build the driver to utilize UART controller Port 3.



:Symbol:           UART_CMSDK_APB_PORT3
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable driver for UART 3"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_CMSDK_APB && SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cmsdk_apb:127