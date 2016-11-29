:orphan:

.. title:: CPU_CORTEX

.. option:: CONFIG_CPU_CORTEX:
.. _CONFIG_CPU_CORTEX:

This option signifies the use of a CPU of the Cortex family.



:Symbol:           CPU_CORTEX
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
 CPU_CORTEX_M && ARM (value: "n")
:Additional dependencies from enclosing menus and ifs:
 ARM (value: "n")
:Locations:
 * ../arch/arm/core/Kconfig:19