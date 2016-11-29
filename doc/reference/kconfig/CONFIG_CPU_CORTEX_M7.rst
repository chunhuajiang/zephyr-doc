:orphan:

.. title:: CPU_CORTEX_M7

.. option:: CONFIG_CPU_CORTEX_M7:
.. _CONFIG_CPU_CORTEX_M7:

This option signifies the use of a Cortex-M7 CPU



:Symbol:           CPU_CORTEX_M7
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

 *  :option:`CONFIG_ATOMIC_OPERATIONS_BUILTIN`
 *  :option:`CONFIG_ISA_THUMB2`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:94