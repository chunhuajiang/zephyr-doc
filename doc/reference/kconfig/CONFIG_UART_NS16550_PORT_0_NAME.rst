:orphan:

.. title:: UART_NS16550_PORT_0_NAME

.. option:: CONFIG_UART_NS16550_PORT_0_NAME:
.. _CONFIG_UART_NS16550_PORT_0_NAME:

This is the device name for UART, and is included in the device
struct.



:Symbol:           UART_NS16550_PORT_0_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 Device Name" if UART_NS16550_PORT_0 (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: UART_NS16550_PORT_0 (value: "n")
 *  "UART_0"
 *   Condition: (none)
 *  "UART_0"
 *   Condition: (none)
 *  "UART_0"
 *   Condition: (none)
 *  "UART_0"
 *   Condition: (none)
 *  "UART_0"
 *   Condition: (none)
 *  "UART_0"
 *   Condition: (none)
 *  "UART_0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_NIOS2F_ZEPHYR && UART_NS16550_PORT_0 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:59
 * ../arch/arc/soc/em11d/Kconfig.defconfig:183
 * ../arch/arc/soc/em7d/Kconfig.defconfig:183
 * ../arch/arc/soc/em9d/Kconfig.defconfig:181
 * ../arch/x86/soc/ia32/Kconfig.defconfig:54
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:213
 * ../arch/x86/soc/atom/Kconfig.defconfig:54
 * ../arch/nios2/soc/nios2f-zephyr/Kconfig.defconfig:21