:orphan:

.. title:: UART_CC32XX_NAME

.. option:: CONFIG_UART_CC32XX_NAME:
.. _CONFIG_UART_CC32XX_NAME:

This is the UART's device name binding.



:Symbol:           UART_CC32XX_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name for CC32XX UART" if UART_CC32XX (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: UART_CC32XX (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cc32xx:10