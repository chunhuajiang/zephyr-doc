:orphan:

.. title:: GPIO_DW_1_NAME

.. option:: CONFIG_GPIO_DW_1_NAME:
.. _CONFIG_GPIO_DW_1_NAME:

The configuration item CONFIG_GPIO_DW_1_NAME:

:Symbol:           GPIO_DW_1_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Driver name" if GPIO_DW_1 (value: "n")
:Default values:

 *  "GPIO_1"
 *   Condition: GPIO_DW_1 (value: "n")
 *  "GPIO_PORTB"
 *   Condition: (none)
 *  "GPIO_PORTB"
 *   Condition: (none)
 *  "GPIO_PORTB"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_EM9D && GPIO_DW && GPIO_DW_1 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:110
 * ../arch/arc/soc/em11d/Kconfig.defconfig:96
 * ../arch/arc/soc/em7d/Kconfig.defconfig:96
 * ../arch/arc/soc/em9d/Kconfig.defconfig:94