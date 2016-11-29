:orphan:

.. title:: CPU_CORTEX_M

.. option:: CONFIG_CPU_CORTEX_M:
.. _CONFIG_CPU_CORTEX_M:

This option signifies the use of a CPU of the Cortex-M family.



:Symbol:           CPU_CORTEX_M
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

 *  :option:`CONFIG_CPU_CORTEX`
 *  :option:`CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN`
:Reverse (select-related) dependencies:
 SOC_SERIES_KINETIS_K6X || SOC_SERIES_NRF51X || SOC_SERIES_NRF52X || SOC_SERIES_CC32XX || SOC_SERIES_STM32F4X || SOC_SERIES_STM32F1X || SOC_SERIES_BEETLE && ARM || SOC_TI_LM3S6965 || SOC_ATMEL_SAM3X8E (value: "n")
:Additional dependencies from enclosing menus and ifs:
 ARM (value: "n")
:Locations:
 * ../arch/arm/core/Kconfig:26