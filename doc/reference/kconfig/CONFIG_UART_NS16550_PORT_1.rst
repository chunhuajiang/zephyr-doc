:orphan:

.. title:: UART_NS16550_PORT_1

.. option:: CONFIG_UART_NS16550_PORT_1:
.. _CONFIG_UART_NS16550_PORT_1:

This tells the driver to configure the UART port at boot, depending on
the additional configure options below.



:Symbol:           UART_NS16550_PORT_1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable NS16550 Port 1" if UART_NS16550 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_NS16550 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: PCI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_ATOM (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:106
 * ../arch/arc/soc/em11d/Kconfig.defconfig:194
 * ../arch/arc/soc/em7d/Kconfig.defconfig:194
 * ../arch/arc/soc/em9d/Kconfig.defconfig:192
 * ../arch/x86/soc/ia32/Kconfig.defconfig:65
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:226
 * ../arch/x86/soc/atom/Kconfig.defconfig:65