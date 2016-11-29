:orphan:

.. title:: UART_NS16550_PORT_0_OPTIONS

.. option:: CONFIG_UART_NS16550_PORT_0_OPTIONS:
.. _CONFIG_UART_NS16550_PORT_0_OPTIONS:

Options used for port initialization.



:Symbol:           UART_NS16550_PORT_0_OPTIONS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 Options" if UART_NS16550_PORT_0 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_NS16550_PORT_0 (value: "n")
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_NIOS2F_ZEPHYR && UART_NS16550_PORT_0 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:83
 * ../arch/arc/soc/em11d/Kconfig.defconfig:189
 * ../arch/arc/soc/em7d/Kconfig.defconfig:189
 * ../arch/arc/soc/em9d/Kconfig.defconfig:187
 * ../arch/x86/soc/ia32/Kconfig.defconfig:60
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:219
 * ../arch/x86/soc/atom/Kconfig.defconfig:60
 * ../arch/nios2/soc/nios2f-zephyr/Kconfig.defconfig:27