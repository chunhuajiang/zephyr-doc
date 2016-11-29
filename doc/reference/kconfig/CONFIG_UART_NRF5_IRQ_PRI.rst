:orphan:

.. title:: UART_NRF5_IRQ_PRI

.. option:: CONFIG_UART_NRF5_IRQ_PRI:
.. _CONFIG_UART_NRF5_IRQ_PRI:

The interrupt priority for UART port.



:Symbol:           UART_NRF5_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 1] if SOC_SERIES_NRF51X (value: "n")
 *  [0, 5] if SOC_SERIES_NRF52X (value: "n")
:Prompts:

 *  "UART Interrupt Priority (Interrupt support)" if UART_NRF5 && UART_INTERRUPT_DRIVEN (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: UART_NRF5 && UART_INTERRUPT_DRIVEN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:37