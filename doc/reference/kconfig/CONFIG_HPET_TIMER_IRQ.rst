:orphan:

.. title:: HPET_TIMER_IRQ

.. option:: CONFIG_HPET_TIMER_IRQ:
.. _CONFIG_HPET_TIMER_IRQ:

This option specifies the IRQ used by the HPET timer.



:Symbol:           HPET_TIMER_IRQ
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HPET Timer IRQ" if HPET_TIMER (value: "n")
:Default values:

 *  20 (value: "n")
 *   Condition: HPET_TIMER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:56