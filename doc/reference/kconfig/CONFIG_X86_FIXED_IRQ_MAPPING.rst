:orphan:

.. title:: X86_FIXED_IRQ_MAPPING

.. option:: CONFIG_X86_FIXED_IRQ_MAPPING:
.. _CONFIG_X86_FIXED_IRQ_MAPPING:

Specify whether the current interrupt controller in use has a fixed
mapping between IDT vectors and IRQ lines.



:Symbol:           X86_FIXED_IRQ_MAPPING
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
 MVIC && X86 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:272