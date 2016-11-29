:orphan:

.. title:: GPIO_SCH

.. option:: CONFIG_GPIO_SCH:
.. _CONFIG_GPIO_SCH:

Enable the SCH GPIO driver found on Intel boards



:Symbol:           GPIO_SCH
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Intel SCH GPIO controller" if GPIO (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.sch:19
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:107