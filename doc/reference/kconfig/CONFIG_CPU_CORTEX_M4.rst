:orphan:

.. title:: CPU_CORTEX_M4

.. option:: CONFIG_CPU_CORTEX_M4:
.. _CONFIG_CPU_CORTEX_M4:

This option signifies the use of a Cortex-M4 CPU



:Symbol:           CPU_CORTEX_M4
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
 SOC_SERIES_KINETIS_K6X || SOC_SERIES_NRF52X || SOC_SERIES_CC32XX || SOC_SERIES_STM32F4X (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:87