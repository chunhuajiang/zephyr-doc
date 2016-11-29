:orphan:

.. title:: SOC_FAMILY_STM32

.. option:: CONFIG_SOC_FAMILY_STM32:
.. _CONFIG_SOC_FAMILY_STM32:

The configuration item CONFIG_SOC_FAMILY_STM32:

:Symbol:           SOC_FAMILY_STM32
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_SERIES_STM32F4X || SOC_SERIES_STM32F1X (value: "n")
:Additional dependencies from enclosing menus and ifs:
 ARM (value: "n")
:Locations:
 * ../arch/arm/soc/st_stm32/Kconfig:18