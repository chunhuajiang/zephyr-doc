:orphan:

.. title:: GPIO_DW

.. option:: CONFIG_GPIO_DW:
.. _CONFIG_GPIO_DW:

Enable driver for Designware GPIO



:Symbol:           GPIO_DW
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Designware GPIO" if GPIO (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO (value: "n")
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
 GPIO && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:19
 * ../arch/arc/soc/em11d/Kconfig.defconfig:73
 * ../arch/arc/soc/em7d/Kconfig.defconfig:73
 * ../arch/arc/soc/em9d/Kconfig.defconfig:71
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:134