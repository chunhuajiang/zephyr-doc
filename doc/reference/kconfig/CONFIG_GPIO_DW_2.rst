:orphan:

.. title:: GPIO_DW_2

.. option:: CONFIG_GPIO_DW_2:
.. _CONFIG_GPIO_DW_2:

Include Designware GPIO driver



:Symbol:           GPIO_DW_2
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Designware GPIO block 1" if GPIO_DW (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_DW (value: "n")
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
 GPIO && SOC_EM9D && GPIO_DW (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:153
 * ../arch/arc/soc/em11d/Kconfig.defconfig:104
 * ../arch/arc/soc/em7d/Kconfig.defconfig:104
 * ../arch/arc/soc/em9d/Kconfig.defconfig:102