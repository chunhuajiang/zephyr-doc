:orphan:

.. title:: UART_NS16550_PORT_0_IRQ_PRI

.. option:: CONFIG_UART_NS16550_PORT_0_IRQ_PRI:
.. _CONFIG_UART_NS16550_PORT_0_IRQ_PRI:

The interrupt priority for UART port.



:Symbol:           UART_NS16550_PORT_0_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 Interrupt Priority" if UART_NS16550_PORT_0 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_NS16550_PORT_0 (value: "n")
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
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
 UART_NS16550 && SOC_NIOS2F_ZEPHYR && UART_NS16550_PORT_0 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:67
 * ../arch/arc/soc/em11d/Kconfig.defconfig:185
 * ../arch/arc/soc/em7d/Kconfig.defconfig:185
 * ../arch/arc/soc/em9d/Kconfig.defconfig:183
 * ../arch/x86/soc/ia32/Kconfig.defconfig:56
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:215
 * ../arch/x86/soc/atom/Kconfig.defconfig:56
 * ../arch/nios2/soc/nios2f-zephyr/Kconfig.defconfig:23