:orphan:

.. title:: CPU_CORTEX_M0_M0PLUS

.. option:: CONFIG_CPU_CORTEX_M0_M0PLUS:
.. _CONFIG_CPU_CORTEX_M0_M0PLUS:

This option signifies the use of either a Cortex-M0 or Cortex-M0+ CPU.



:Symbol:           CPU_CORTEX_M0_M0PLUS
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

 *  :option:`CONFIG_ATOMIC_OPERATIONS_C`
 *  :option:`CONFIG_ISA_THUMB2`
:Reverse (select-related) dependencies:
 CPU_CORTEX_M && ARM && CPU_CORTEX_M0 || CPU_CORTEX_M && ARM && CPU_CORTEX_M0PLUS (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:48