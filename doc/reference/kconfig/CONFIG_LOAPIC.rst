:orphan:

.. title:: LOAPIC

.. option:: CONFIG_LOAPIC:
.. _CONFIG_LOAPIC:

This option selects local APIC as the interrupt controller.



:Symbol:           LOAPIC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LOAPIC" if X86 (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: X86 (value: "y")
:Selects:

 *  :option:`CONFIG_IOAPIC` if X86 (value: "y")
:Reverse (select-related) dependencies:
 SOC_SERIES_QUARK_SE || HPET_TIMER && X86 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/interrupt_controller/Kconfig:22