:orphan:

.. title:: HPET_TIMER_IRQ_PRIORITY

.. option:: CONFIG_HPET_TIMER_IRQ_PRIORITY:
.. _CONFIG_HPET_TIMER_IRQ_PRIORITY:

This option specifies the IRQ priority used by the HPET timer.



:Symbol:           HPET_TIMER_IRQ_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HPET Timer IRQ Priority" if HPET_TIMER (value: "n")
:Default values:

 *  4 (value: "n")
 *   Condition: HPET_TIMER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:63