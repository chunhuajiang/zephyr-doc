:orphan:

.. title:: HPET_TIMER_DEBUG

.. option:: CONFIG_HPET_TIMER_DEBUG:
.. _CONFIG_HPET_TIMER_DEBUG:

This option enables HPET debugging output.



:Symbol:           HPET_TIMER_DEBUG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable HPET debug output" if HPET_TIMER && PRINTK (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: HPET_TIMER && PRINTK (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:42