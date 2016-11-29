:orphan:

.. title:: UART_STELLARIS_PORT_1_IRQ_PRI

.. option:: CONFIG_UART_STELLARIS_PORT_1_IRQ_PRI:
.. _CONFIG_UART_STELLARIS_PORT_1_IRQ_PRI:

The interrupt priority for UART port.



:Symbol:           UART_STELLARIS_PORT_1_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 1 Interrupt Priority" if UART_STELLARIS_PORT_1 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_STELLARIS_PORT_1 (value: "n")
 *  3 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_STELLARIS && SOC_TI_LM3S6965 && UART_STELLARIS_PORT_1 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stellaris:62
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:60