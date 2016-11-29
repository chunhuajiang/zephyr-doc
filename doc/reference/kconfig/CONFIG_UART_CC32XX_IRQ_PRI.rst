:orphan:

.. title:: UART_CC32XX_IRQ_PRI

.. option:: CONFIG_UART_CC32XX_IRQ_PRI:
.. _CONFIG_UART_CC32XX_IRQ_PRI:

The configuration item CONFIG_UART_CC32XX_IRQ_PRI:

:Symbol:           UART_CC32XX_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IRQ priority from UART controller" if UART_CC32XX (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_CC3200 && SOC_SERIES_CC32XX && UART_CC32XX (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cc32xx:17
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.cc3200:33