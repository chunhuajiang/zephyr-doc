:orphan:

.. title:: FIRQ_STACK_SIZE

.. option:: CONFIG_FIRQ_STACK_SIZE:
.. _CONFIG_FIRQ_STACK_SIZE:

FIRQs and regular IRQs have different stacks so that a FIRQ can start
running without doing stack switching in software.



:Symbol:           FIRQ_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Size of stack for FIRQs (in bytes)" if CPU_ARCV2 (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: CPU_ARCV2 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARC (value: "n")
:Locations:
 * ../arch/arc/Kconfig:113