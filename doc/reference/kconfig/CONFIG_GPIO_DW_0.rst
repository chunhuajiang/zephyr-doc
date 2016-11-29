:orphan:

.. title:: GPIO_DW_0

.. option:: CONFIG_GPIO_DW_0:
.. _CONFIG_GPIO_DW_0:

Include Designware GPIO driver



:Symbol:           GPIO_DW_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Designware GPIO block 0" if GPIO_DW (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_DW (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_GPIO_DW_0_IRQ_SHARED` if SHARED_IRQ (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_QUARK_X1000 && GPIO_DW (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:53
 * ../arch/arc/soc/em11d/Kconfig.defconfig:78
 * ../arch/arc/soc/em7d/Kconfig.defconfig:78
 * ../arch/arc/soc/em9d/Kconfig.defconfig:76
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:139