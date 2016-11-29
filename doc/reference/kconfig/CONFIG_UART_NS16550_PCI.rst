:orphan:

.. title:: UART_NS16550_PCI

.. option:: CONFIG_UART_NS16550_PCI:
.. _CONFIG_UART_NS16550_PCI:

This enables NS16550 to probe for PCI-based serial devices.

This option enables the driver to auto-detect the device
configuration required to access those ports.



:Symbol:           UART_NS16550_PCI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable PCI Support" if PCI && UART_NS16550 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PCI && UART_NS16550 (value: "n")
 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: PCI (value: "n")
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_NIOS2F_ZEPHYR (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:10
 * ../arch/x86/soc/ia32/Kconfig.defconfig:46
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:205
 * ../arch/x86/soc/atom/Kconfig.defconfig:46
 * ../arch/nios2/soc/nios2f-zephyr/Kconfig.defconfig:13