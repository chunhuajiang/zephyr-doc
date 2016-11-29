:orphan:

.. title:: UART_NS16550_PORT_0

.. option:: CONFIG_UART_NS16550_PORT_0:
.. _CONFIG_UART_NS16550_PORT_0:

This tells the driver to configure the UART port at boot, depending on
the additional configure options below.



:Symbol:           UART_NS16550_PORT_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable NS16550 Port 0" if UART_NS16550 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_NS16550 (value: "n")
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NS16550 && SOC_NIOS2F_ZEPHYR (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.ns16550:51
 * ../arch/arc/soc/em11d/Kconfig.defconfig:178
 * ../arch/arc/soc/em7d/Kconfig.defconfig:178
 * ../arch/arc/soc/em9d/Kconfig.defconfig:176
 * ../arch/x86/soc/ia32/Kconfig.defconfig:49
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:208
 * ../arch/x86/soc/atom/Kconfig.defconfig:49
 * ../arch/nios2/soc/nios2f-zephyr/Kconfig.defconfig:16