:orphan:

.. title:: CPU_CORTEX_M0PLUS

.. option:: CONFIG_CPU_CORTEX_M0PLUS:
.. _CONFIG_CPU_CORTEX_M0PLUS:

This option signifies the use of a Cortex-M0+ CPU



:Symbol:           CPU_CORTEX_M0PLUS
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
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:73