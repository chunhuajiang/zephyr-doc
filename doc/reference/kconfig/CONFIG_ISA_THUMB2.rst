:orphan:

.. title:: ISA_THUMB2

.. option:: CONFIG_ISA_THUMB2:
.. _CONFIG_ISA_THUMB2:

From: http://www.arm.com/products/processors/technologies/instruction-set-architectures.php

Thumb-2 technology is the instruction set underlying the ARM Cortex
architecture which provides enhanced levels of performance, energy
efficiency, and code density for a wide range of embedded
applications.

Thumb-2 technology builds on the success of Thumb, the innovative
high code density instruction set for ARM microprocessor cores, to
increase the power of the ARM microprocessor core available to
developers of low cost, high performance systems.

The technology is backwards compatible with existing ARM and Thumb
solutions, while significantly extending the features available to
the Thumb instructions set. This allows more of the application to
benefit from the best in class code density of Thumb.

For performance optimised code Thumb-2 technology uses 31 percent
less memory to reduce system cost, while providing up to 38 percent
higher performance than existing high density code, which can be used
to prolong battery-life or to enrich the product feature set. Thumb-2
technology is featured in the  processor, and in all ARMv7
architecture-based processors.



:Symbol:           ISA_THUMB2
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
 CPU_CORTEX_M && ARM && CPU_CORTEX_M0_M0PLUS || CPU_CORTEX_M && ARM && CPU_CORTEX_M3_M4 || CPU_CORTEX_M && ARM && CPU_CORTEX_M7 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:19