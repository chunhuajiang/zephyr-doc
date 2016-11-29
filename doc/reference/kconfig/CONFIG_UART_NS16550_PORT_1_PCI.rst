:orphan:

.. title:: UART_NS16550_PORT_1_PCI

.. option:: CONFIG_UART_NS16550_PORT_1_PCI:
.. _CONFIG_UART_NS16550_PORT_1_PCI:

The configuration item CONFIG_UART_NS16550_PORT_1_PCI:

:Symbol:           UART_NS16550_PORT_1_PCI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  y (value: "y")
 *   Condition: UART_NS16550_PCI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_SERIES_QUARK_X1000 && UART_NS16550_PORT_1 (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:239