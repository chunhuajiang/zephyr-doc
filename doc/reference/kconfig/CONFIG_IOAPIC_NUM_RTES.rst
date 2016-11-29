:orphan:

.. title:: IOAPIC_NUM_RTES

.. option:: CONFIG_IOAPIC_NUM_RTES:
.. _CONFIG_IOAPIC_NUM_RTES:

This option indicates the maximum number of Redirection Table Entries
(RTEs) (one per IRQ available to the IO-APIC) made available to the
kernel, regardless of the number provided by the hardware itself. For
most efficient usage of memory, it should match the number of IRQ lines
needed by devices connected to the IO-APIC.



:Symbol:           IOAPIC_NUM_RTES
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Number of Redirection Table Entries available" if IOAPIC (value: "n")
:Default values:

 *  24 (value: "n")
 *   Condition: IOAPIC (value: "n")
 *  32 (value: "n")
 *   Condition: (none)
 *  64 (value: "n")
 *   Condition: IOAPIC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/interrupt_controller/Kconfig:83
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:45
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:44