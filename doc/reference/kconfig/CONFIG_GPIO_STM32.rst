:orphan:

.. title:: GPIO_STM32

.. option:: CONFIG_GPIO_STM32:
.. _CONFIG_GPIO_STM32:

Enable GPIO driver for STM32 line of MCUs



:Symbol:           GPIO_STM32
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO Driver for STM32 family of MCUs" if GPIO && SOC_FAMILY_STM32 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO && SOC_FAMILY_STM32 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.stm32:18
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:72