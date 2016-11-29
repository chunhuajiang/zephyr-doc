:orphan:

.. title:: GPIO_STM32_PORTC

.. option:: CONFIG_GPIO_STM32_PORTC:
.. _CONFIG_GPIO_STM32_PORTC:

The configuration item CONFIG_GPIO_STM32_PORTC:

:Symbol:           GPIO_STM32_PORTC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable GPIO port C support"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.stm32:35
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:81