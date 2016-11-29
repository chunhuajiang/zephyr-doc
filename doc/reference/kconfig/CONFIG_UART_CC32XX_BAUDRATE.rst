:orphan:

.. title:: UART_CC32XX_BAUDRATE

.. option:: CONFIG_UART_CC32XX_BAUDRATE:
.. _CONFIG_UART_CC32XX_BAUDRATE:

This option sets the baud rate for the CC32XX UART.


:Symbol:           UART_CC32XX_BAUDRATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "UART_0 baud rate" if UART_CC32XX (value: "n")
:Default values:

 *  115200 (value: "n")
 *   Condition: UART_CC32XX (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cc32xx:21