:orphan:

.. title:: ATOMIC_OPERATIONS_BUILTIN

.. option:: CONFIG_ATOMIC_OPERATIONS_BUILTIN:
.. _CONFIG_ATOMIC_OPERATIONS_BUILTIN:

Use the compiler builtin functions for atomic operations. This is
the preferred method. However, support for all arches in GCC is
incomplete.



:Symbol:           ATOMIC_OPERATIONS_BUILTIN
:Type:             bool
:Value:            "y"
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
 (no selects)
:Reverse (select-related) dependencies:
 X86 || CPU_CORTEX_M && ARM && CPU_CORTEX_M3_M4 || CPU_CORTEX_M && ARM && CPU_CORTEX_M7 (value: "y")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:240