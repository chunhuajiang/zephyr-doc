:orphan:

.. title:: EOI_FORWARDING_BUG

.. option:: CONFIG_EOI_FORWARDING_BUG:
.. _CONFIG_EOI_FORWARDING_BUG:

Quark SE LOAPIC has issues with forwarding EOI to the IOAPIC for level
triggered interrupts, this is a SW workaround.



:Symbol:           EOI_FORWARDING_BUG
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

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 && SOC_QUARK_SE_C1000 && X86 (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig:21