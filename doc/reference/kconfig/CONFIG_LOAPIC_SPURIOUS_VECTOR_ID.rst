:orphan:

.. title:: LOAPIC_SPURIOUS_VECTOR_ID

.. option:: CONFIG_LOAPIC_SPURIOUS_VECTOR_ID:
.. _CONFIG_LOAPIC_SPURIOUS_VECTOR_ID:

IDT vector to use for spurious LOAPIC interrupts. Note that some
arches (P6, Pentium) ignore the low 4 bits and fix them at 0xF.
If this value is left at -1 the last entry in the IDT will be used.



:Symbol:           LOAPIC_SPURIOUS_VECTOR_ID
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LOAPIC spurious vector ID" if LOAPIC_SPURIOUS_VECTOR (value: "n")
:Default values:

 *  -1 (value: "n")
 *   Condition: LOAPIC_SPURIOUS_VECTOR (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/interrupt_controller/Kconfig:52