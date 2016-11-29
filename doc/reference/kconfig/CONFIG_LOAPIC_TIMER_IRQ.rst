:orphan:

.. title:: LOAPIC_TIMER_IRQ

.. option:: CONFIG_LOAPIC_TIMER_IRQ:
.. _CONFIG_LOAPIC_TIMER_IRQ:

This option specifies the IRQ used by the LOAPIC timer.



:Symbol:           LOAPIC_TIMER_IRQ
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Local APIC Timer IRQ" if LOAPIC_TIMER (value: "n")
:Default values:

 *  24 (value: "n")
 *   Condition: LOAPIC_TIMER (value: "n")
 *  10 (value: "n")
 *   Condition: (none)
 *  64 (value: "n")
 *   Condition: LOAPIC_TIMER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/timer/Kconfig:104
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:48
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:47