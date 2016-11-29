:orphan:

.. title:: PINMUX_STM32

.. option:: CONFIG_PINMUX_STM32:
.. _CONFIG_PINMUX_STM32:

Enable pin multiplexter for STM32 MCUs



:Symbol:           PINMUX_STM32
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Pinmux driver for STM32 MCUs" if PINMUX && SOC_FAMILY_STM32 (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX && SOC_SERIES_STM32F4X (value: "n")
:Locations:
 * ../drivers/pinmux/Kconfig.stm32:18
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:88