:orphan:

.. title:: GPIO_DW_0_NAME

.. option:: CONFIG_GPIO_DW_0_NAME:
.. _CONFIG_GPIO_DW_0_NAME:

The configuration item CONFIG_GPIO_DW_0_NAME:

:Symbol:           GPIO_DW_0_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Driver name" if GPIO_DW_0 (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: GPIO_DW_0 (value: "n")
 *  "GPIO_PORTA"
 *   Condition: (none)
 *  "GPIO_PORTA"
 *   Condition: (none)
 *  "GPIO_PORTA"
 *   Condition: (none)
 *  "GPIO_0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_QUARK_X1000 && GPIO_DW && GPIO_DW_0 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:60
 * ../arch/arc/soc/em11d/Kconfig.defconfig:83
 * ../arch/arc/soc/em7d/Kconfig.defconfig:83
 * ../arch/arc/soc/em9d/Kconfig.defconfig:81
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:145