:orphan:

.. title:: MVIC_TIMER_IRQ

.. option:: CONFIG_MVIC_TIMER_IRQ:
.. _CONFIG_MVIC_TIMER_IRQ:

Specify the IRQ line to use for the timer interrupt. This should be
an IRQ line unused by any hardware. If nested interrupts are enabled,
higher interrupt lines have priority.



:Symbol:           MVIC_TIMER_IRQ
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 15]
:Prompts:

 *  "IRQ line to use for timer interrupt" if MVIC (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: MVIC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/interrupt_controller/Kconfig:116