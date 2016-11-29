:orphan:

.. title:: MAX_IRQ_LINES

.. option:: CONFIG_MAX_IRQ_LINES:
.. _CONFIG_MAX_IRQ_LINES:

This option specifies the number of IRQ lines in the system.
It can be tuned to save some bytes in ROM, as it determines the
size of the _irq_to_interrupt_vector_table, which is used at runtime
to program to the PIC the association between vectors and
interrupts.



:Symbol:           MAX_IRQ_LINES
:Type:             int
:Value:            "128"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 256]
:Prompts:

 *  "Number of IRQ lines"
:Default values:

 *  128 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/core/Kconfig:51