:orphan:

.. title:: LOAPIC_SPURIOUS_VECTOR

.. option:: CONFIG_LOAPIC_SPURIOUS_VECTOR:
.. _CONFIG_LOAPIC_SPURIOUS_VECTOR:

A special situation may occur when a processor raises its task
priority to be greater than or equal to the level of the
interrupt for which the processor INTR signal is currently being
asserted. If at the time the INTA cycle is issued, the
interrupt that was to be dispensed has become masked (programmed
by software), the local APIC will deliver a spurious-interrupt
vector. Dispensing the spurious-interrupt vector does not affect
the ISR, so the handler for this vector should return without an EOI.
From x86 manual Volume 3 Section 10.9.



:Symbol:           LOAPIC_SPURIOUS_VECTOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Handle LOAPIC spurious interrupts" if LOAPIC (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: LOAPIC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/interrupt_controller/Kconfig:37