:orphan:

.. title:: GPIO_QMSI_1_IRQ_PRI

.. option:: CONFIG_GPIO_QMSI_1_IRQ_PRI:
.. _CONFIG_GPIO_QMSI_1_IRQ_PRI:

IRQ priority



:Symbol:           GPIO_QMSI_1_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Controller interrupt priority" if GPIO_QMSI_1 (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.qmsi:83
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:105
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:73