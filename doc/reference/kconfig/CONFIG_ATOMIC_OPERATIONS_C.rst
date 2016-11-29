:orphan:

.. title:: ATOMIC_OPERATIONS_C

.. option:: CONFIG_ATOMIC_OPERATIONS_C:
.. _CONFIG_ATOMIC_OPERATIONS_C:

Use atomic operations routines that are implemented entirely
in C by locking interrupts. Selected by architectures which either
do not have support for atomic operations in their instruction
set, or haven't been implemented yet during bring-up, and also
the compiler does not have support for the atomic __sync_* builtins.



:Symbol:           ATOMIC_OPERATIONS_C
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
 (no selects)
:Reverse (select-related) dependencies:
 NIOS2 || CPU_ARCEM4 && ARC || CPU_CORTEX_M && ARM && CPU_CORTEX_M0_M0PLUS (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:253