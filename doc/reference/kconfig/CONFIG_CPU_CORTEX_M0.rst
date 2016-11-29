:orphan:

.. title:: CPU_CORTEX_M0

.. option:: CONFIG_CPU_CORTEX_M0:
.. _CONFIG_CPU_CORTEX_M0:

This option signifies the use of a Cortex-M0 CPU



:Symbol:           CPU_CORTEX_M0
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

 *  :option:`CONFIG_CPU_CORTEX_M0_M0PLUS`
:Reverse (select-related) dependencies:
 SOC_SERIES_NRF51X (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:66