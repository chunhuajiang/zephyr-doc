:orphan:

.. title:: GPIO_SCH_1_DEV_NAME

.. option:: CONFIG_GPIO_SCH_1_DEV_NAME:
.. _CONFIG_GPIO_SCH_1_DEV_NAME:

The configuration item CONFIG_GPIO_SCH_1_DEV_NAME:

:Symbol:           GPIO_SCH_1_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Name of the device" if GPIO_SCH_1 (value: "n")
:Default values:

 *  "GPIO_1"
 *   Condition: GPIO_SCH_1 (value: "n")
 *  "GPIO_RW"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_QUARK_X1000 && GPIO_SCH && GPIO_SCH_1 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.sch:51
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:127