:orphan:

.. title:: UART_NS16550_PORT_0_PCI

.. option:: CONFIG_UART_NS16550_PORT_0_PCI:
.. _CONFIG_UART_NS16550_PORT_0_PCI:

Obtain port information from PCI.



:Symbol:           UART_NS16550_PORT_0_PCI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 is PCI-based" if UART_NS16550_PCI && UART_NS16550_PORT_0 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_NS16550_PCI && UART_NS16550_PORT_0 (value: "n")
 *  y (value: "y")
 *   Condition: UART_NS16550_PCI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_SERIES_QUARK_X1000 && UART_NS16550_PORT_0 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:97
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:221