:orphan:

.. title:: UART_NS16550_PORT_1_NAME

.. option:: CONFIG_UART_NS16550_PORT_1_NAME:
.. _CONFIG_UART_NS16550_PORT_1_NAME:

This is the device name for UART, and is included in the device
struct.



:Symbol:           UART_NS16550_PORT_1_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 1 Device Name" if UART_NS16550_PORT_1 (value: "n")
:Default values:

 *  "UART_1"
 *   Condition: UART_NS16550_PORT_1 (value: "n")
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_ATOM && UART_NS16550_PORT_1 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:114
 * ../arch/arc/soc/em11d/Kconfig.defconfig:199
 * ../arch/arc/soc/em7d/Kconfig.defconfig:199
 * ../arch/arc/soc/em9d/Kconfig.defconfig:197
 * ../arch/x86/soc/ia32/Kconfig.defconfig:70
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:231
 * ../arch/x86/soc/atom/Kconfig.defconfig:70