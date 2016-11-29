:orphan:

.. title:: UART_NS16550_PORT_1_IRQ_PRI

.. option:: CONFIG_UART_NS16550_PORT_1_IRQ_PRI:
.. _CONFIG_UART_NS16550_PORT_1_IRQ_PRI:

The interrupt priority for UART port.



:Symbol:           UART_NS16550_PORT_1_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 1 Interrupt Priority" if UART_NS16550_PORT_1 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_NS16550_PORT_1 (value: "n")
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_ATOM && UART_NS16550_PORT_1 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:122
 * ../arch/arc/soc/em11d/Kconfig.defconfig:201
 * ../arch/arc/soc/em7d/Kconfig.defconfig:201
 * ../arch/arc/soc/em9d/Kconfig.defconfig:199
 * ../arch/x86/soc/ia32/Kconfig.defconfig:72
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:233
 * ../arch/x86/soc/atom/Kconfig.defconfig:72