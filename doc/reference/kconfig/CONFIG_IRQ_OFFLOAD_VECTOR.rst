:orphan:

.. title:: IRQ_OFFLOAD_VECTOR

.. option:: CONFIG_IRQ_OFFLOAD_VECTOR:
.. _CONFIG_IRQ_OFFLOAD_VECTOR:

Specify the IDT vector to use for the IRQ offload interrupt handler.
The default should be fine for most arches, but on systems like MVIC
where there is a fixed IRQ-to-vector mapping another value may be
needed to avoid collision.



:Symbol:           IRQ_OFFLOAD_VECTOR
:Type:             int
:Value:            "32"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [32, 255]
:Prompts:

 *  "IDT vector to use for IRQ offload" if IRQ_OFFLOAD (value: "n")
:Default values:

 *  63 (value: "n")
 *   Condition: MVIC && IRQ_OFFLOAD (value: "n")
 *  32 (value: "n")
 *   Condition: !MVIC && IRQ_OFFLOAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:257