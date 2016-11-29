:orphan:

.. title:: UART_ATMEL_SAM3_IRQ_PRI

.. option:: CONFIG_UART_ATMEL_SAM3_IRQ_PRI:
.. _CONFIG_UART_ATMEL_SAM3_IRQ_PRI:

The interrupt priority for UART port.



:Symbol:           UART_ATMEL_SAM3_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Atmel SAM3 UART Interrupt Priority" if UART_ATMEL_SAM3 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_ATMEL_SAM3 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.atmel_sam3:21