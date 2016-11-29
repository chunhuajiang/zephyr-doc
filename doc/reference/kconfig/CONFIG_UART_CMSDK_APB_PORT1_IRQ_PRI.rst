:orphan:

.. title:: UART_CMSDK_APB_PORT1_IRQ_PRI

.. option:: CONFIG_UART_CMSDK_APB_PORT1_IRQ_PRI:
.. _CONFIG_UART_CMSDK_APB_PORT1_IRQ_PRI:

The interrupt priority for UART port.



:Symbol:           UART_CMSDK_APB_PORT1_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "UART Interrupt Priority (Interrupt support)" if UART_CMSDK_APB_PORT1 && UART_INTERRUPT_DRIVEN (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: UART_CMSDK_APB_PORT1 && UART_INTERRUPT_DRIVEN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_CMSDK_APB && SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cmsdk_apb:77