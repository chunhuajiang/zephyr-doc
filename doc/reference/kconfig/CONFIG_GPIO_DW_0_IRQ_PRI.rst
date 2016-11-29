:orphan:

.. title:: GPIO_DW_0_IRQ_PRI

.. option:: CONFIG_GPIO_DW_0_IRQ_PRI:
.. _CONFIG_GPIO_DW_0_IRQ_PRI:

IRQ priority



:Symbol:           GPIO_DW_0_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Controller interrupt priority" if GPIO_DW_0 && GPIO_DW_0_IRQ_DIRECT (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_QUARK_X1000 && GPIO_DW && GPIO_DW_0 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:97
 * ../arch/arc/soc/em11d/Kconfig.defconfig:86
 * ../arch/arc/soc/em7d/Kconfig.defconfig:86
 * ../arch/arc/soc/em9d/Kconfig.defconfig:84
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:147