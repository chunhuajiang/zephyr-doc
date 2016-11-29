:orphan:

.. title:: MVIC

.. option:: CONFIG_MVIC:
.. _CONFIG_MVIC:

The MVIC (Intel Quark microcontroller D2000 Interrupt Controller) is
configured by default to support 32 external interrupt lines. Unlike the
traditional IA LAPIC/IOAPIC, the interrupt vectors in MVIC are fixed and
not programmable. In addition, the priorities of these interrupt
lines are also fixed.



:Symbol:           MVIC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Intel Quark D2000 Interrupt Controller (MVIC)" if X86 (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: X86 (value: "y")
:Selects:

 *  :option:`CONFIG_X86_FIXED_IRQ_MAPPING` if X86 (value: "y")
:Reverse (select-related) dependencies:
 SOC_SERIES_QUARK_D2000 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/interrupt_controller/Kconfig:104