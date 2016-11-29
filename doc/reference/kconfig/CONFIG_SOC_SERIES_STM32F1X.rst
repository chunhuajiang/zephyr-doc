:orphan:

.. title:: SOC_SERIES_STM32F1X

.. option:: CONFIG_SOC_SERIES_STM32F1X:
.. _CONFIG_SOC_SERIES_STM32F1X:

Enable support for STM32F1 MCU series


:Symbol:           SOC_SERIES_STM32F1X
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "STM32F1x Series MCU"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_CPU_CORTEX_M`
 *  :option:`CONFIG_CPU_CORTEX_M3`
 *  :option:`CONFIG_SOC_FAMILY_STM32`
 *  :option:`CONFIG_SYS_POWER_LOW_POWER_STATE_SUPPORTED`
 *  :option:`CONFIG_HAS_STM32CUBE`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.series:18