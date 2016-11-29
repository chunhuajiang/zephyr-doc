:orphan:

.. title:: UART_QMSI_1_IRQ_PRI

.. option:: CONFIG_UART_QMSI_1_IRQ_PRI:
.. _CONFIG_UART_QMSI_1_IRQ_PRI:

The configuration item CONFIG_UART_QMSI_1_IRQ_PRI:

:Symbol:           UART_QMSI_1_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IRQ priority from UART_1 controller" if UART_QMSI_1 (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_QMSI && SOC_SERIES_QUARK_SE && UART_QMSI_1 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.qmsi:64
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:202
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:72
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:210