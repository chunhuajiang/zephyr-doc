:orphan:

.. title:: UART_CMSDK_APB_PORT1_BAUD_RATE

.. option:: CONFIG_UART_CMSDK_APB_PORT1_BAUD_RATE:
.. _CONFIG_UART_CMSDK_APB_PORT1_BAUD_RATE:

The baud rate for UART port to be set to at boot.



:Symbol:           UART_CMSDK_APB_PORT1_BAUD_RATE
:Type:             int
:Value:            "9600"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [9600, 115200]
:Prompts:

 *  "Baud Rate" if UART_CMSDK_APB_PORT1 (value: "n")
:Default values:

 *  115200 (value: "n")
 *   Condition: UART_CMSDK_APB_PORT1 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_CMSDK_APB && SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cmsdk_apb:85