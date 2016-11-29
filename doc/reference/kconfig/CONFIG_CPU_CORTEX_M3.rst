:orphan:

.. title:: CPU_CORTEX_M3

.. option:: CONFIG_CPU_CORTEX_M3:
.. _CONFIG_CPU_CORTEX_M3:

This option signifies the use of a Cortex-M3 CPU



:Symbol:           CPU_CORTEX_M3
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
 (no default values)
:Selects:

 *  :option:`CONFIG_CPU_CORTEX_M3_M4`
:Reverse (select-related) dependencies:
 SOC_SERIES_STM32F1X || SOC_SERIES_BEETLE && ARM || SOC_TI_LM3S6965 || SOC_ATMEL_SAM3X8E (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:80