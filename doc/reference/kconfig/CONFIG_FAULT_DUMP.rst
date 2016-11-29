:orphan:

.. title:: FAULT_DUMP

.. option:: CONFIG_FAULT_DUMP:
.. _CONFIG_FAULT_DUMP:

Different levels for display information when a fault occurs.

2: The default. Display specific and verbose information. Consumes
        the most memory (long strings).

1: Display general and short information. Consumes less memory
        (short strings).

0: Off.



:Symbol:           FAULT_DUMP
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 2]
 *  [0, 2]
:Prompts:

 *  "Fault dump level"
 *  "Fault dump level"
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM && CPU_CORTEX_M (value: "n")
:Locations:
 * ../arch/arc/Kconfig:130
 * ../arch/arm/core/cortex_m/Kconfig:146