:orphan:

.. title:: UART_QMSI_0

.. option:: CONFIG_UART_QMSI_0:
.. _CONFIG_UART_QMSI_0:

The configuration item CONFIG_UART_QMSI_0:

:Symbol:           UART_QMSI_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable UART 0 controller" if UART_QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_QMSI (value: "n")
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
 UART_QMSI && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.qmsi:12
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:187
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:66
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:195