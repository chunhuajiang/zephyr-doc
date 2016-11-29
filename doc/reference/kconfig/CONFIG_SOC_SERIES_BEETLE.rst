:orphan:

.. title:: SOC_SERIES_BEETLE

.. option:: CONFIG_SOC_SERIES_BEETLE:
.. _CONFIG_SOC_SERIES_BEETLE:

Enable support for Beetle MCU Series


:Symbol:           SOC_SERIES_BEETLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ARM Beetle MCU Series" if ARM (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_CPU_CORTEX_M` if ARM (value: "n")
 *  :option:`CONFIG_CPU_CORTEX_M3` if ARM (value: "n")
 *  :option:`CONFIG_SOC_FAMILY_ARM` if ARM (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/arm/soc/arm/beetle/Kconfig.series:19