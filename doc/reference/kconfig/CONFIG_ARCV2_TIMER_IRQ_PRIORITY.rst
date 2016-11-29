:orphan:

.. title:: ARCV2_TIMER_IRQ_PRIORITY

.. option:: CONFIG_ARCV2_TIMER_IRQ_PRIORITY:
.. _CONFIG_ARCV2_TIMER_IRQ_PRIORITY:

This option specifies the IRQ priority used by the ARC timer. Lower
values have higher priority.



:Symbol:           ARCV2_TIMER_IRQ_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ARC timer interrupt priority" if ARCV2_TIMER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: ARCV2_TIMER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:126