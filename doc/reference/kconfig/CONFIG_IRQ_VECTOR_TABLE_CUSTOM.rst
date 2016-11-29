:orphan:

.. title:: IRQ_VECTOR_TABLE_CUSTOM

.. option:: CONFIG_IRQ_VECTOR_TABLE_CUSTOM:
.. _CONFIG_IRQ_VECTOR_TABLE_CUSTOM:

Projects, not the board, provide the IRQ part of the vector table.

This is the table of interrupt handlers with the best potential
performance, but is the less flexible.

The ISRs are installed directly in the vector table, thus are
directly called by the CPU when an interrupt is taken. This adds
the least overhead when handling an interrupt.

Downsides:

- ISRs cannot have a parameter
- ISRs cannot be connected at runtime
- ISRs must notify the kernel manually by invoking _IntExit() when
  then are about to return.



:Symbol:           IRQ_VECTOR_TABLE_CUSTOM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Projects provide a custom static IRQ part of vector table" if !SW_ISR_TABLE (value: "y")
 *  "Projects provide a custom static IRQ part of vector table" if !SW_ISR_TABLE (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: !SW_ISR_TABLE (value: "y")
 *  n (value: "n")
 *   Condition: !SW_ISR_TABLE (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM && (CPU_CORTEX_M0_M0PLUS || CPU_CORTEX_M3_M4 || CPU_CORTEX_M7) (value: "n")
:Locations:
 * ../arch/arc/Kconfig:232
 * ../arch/arm/core/cortex_m/Kconfig:215