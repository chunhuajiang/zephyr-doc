:orphan:

.. title:: GPIO_SCH_1

.. option:: CONFIG_GPIO_SCH_1:
.. _CONFIG_GPIO_SCH_1:

The configuration item CONFIG_GPIO_SCH_1:

:Symbol:           GPIO_SCH_1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable SCH GPIO port 1" if GPIO_SCH (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_SCH (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_QUARK_X1000 && GPIO_SCH (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.sch:46
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:115