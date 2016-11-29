:orphan:

.. title:: UART_NS16550_PORT_0_BAUD_RATE

.. option:: CONFIG_UART_NS16550_PORT_0_BAUD_RATE:
.. _CONFIG_UART_NS16550_PORT_0_BAUD_RATE:

The baud rate for UART port to be set to at boot.

Leave at 0 to skip initialization.



:Symbol:           UART_NS16550_PORT_0_BAUD_RATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 Baud Rate" if UART_NS16550_PORT_0 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_NS16550_PORT_0 (value: "n")
 *  115200 (value: "n")
 *   Condition: (none)
 *  115200 (value: "n")
 *   Condition: (none)
 *  115200 (value: "n")
 *   Condition: (none)
 *  115200 (value: "n")
 *   Condition: (none)
 *  115200 (value: "n")
 *   Condition: (none)
 *  115200 (value: "n")
 *   Condition: (none)
 *  115200 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_NIOS2F_ZEPHYR && UART_NS16550_PORT_0 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:74
 * ../arch/arc/soc/em11d/Kconfig.defconfig:187
 * ../arch/arc/soc/em7d/Kconfig.defconfig:187
 * ../arch/arc/soc/em9d/Kconfig.defconfig:185
 * ../arch/x86/soc/ia32/Kconfig.defconfig:58
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:217
 * ../arch/x86/soc/atom/Kconfig.defconfig:58
 * ../arch/nios2/soc/nios2f-zephyr/Kconfig.defconfig:25