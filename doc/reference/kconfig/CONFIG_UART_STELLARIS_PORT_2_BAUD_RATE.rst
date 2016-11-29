:orphan:

.. title:: UART_STELLARIS_PORT_2_BAUD_RATE

.. option:: CONFIG_UART_STELLARIS_PORT_2_BAUD_RATE:
.. _CONFIG_UART_STELLARIS_PORT_2_BAUD_RATE:

The baud rate for UART port to be set to at boot.

Leave at 0 to skip initialization.


:Symbol:           UART_STELLARIS_PORT_2_BAUD_RATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 2 Baud Rate" if UART_STELLARIS_PORT_2 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_STELLARIS_PORT_2 (value: "n")
 *  115200 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_STELLARIS && SOC_TI_LM3S6965 && UART_STELLARIS_PORT_2 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stellaris:103
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:71