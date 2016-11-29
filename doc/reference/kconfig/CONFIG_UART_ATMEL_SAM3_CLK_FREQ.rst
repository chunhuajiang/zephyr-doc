:orphan:

.. title:: UART_ATMEL_SAM3_CLK_FREQ

.. option:: CONFIG_UART_ATMEL_SAM3_CLK_FREQ:
.. _CONFIG_UART_ATMEL_SAM3_CLK_FREQ:

The clock frequency for UART port.


:Symbol:           UART_ATMEL_SAM3_CLK_FREQ
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Atmel SAM3 UART Clock Frequency" if UART_ATMEL_SAM3 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_ATMEL_SAM3 (value: "n")
 *  84000000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_ATMEL_SAM3 && SOC_ATMEL_SAM3 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.atmel_sam3:35
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:73