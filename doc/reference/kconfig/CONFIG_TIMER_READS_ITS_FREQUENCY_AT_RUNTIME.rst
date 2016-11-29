:orphan:

.. title:: TIMER_READS_ITS_FREQUENCY_AT_RUNTIME

.. option:: CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME:
.. _CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME:

The drivers select this option automatically when needed. Do not modify
this unless you have a very good reason for it.



:Symbol:           TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Timer queries its hardware to find its frequency at runtime"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 HPET_TIMER && X86 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:160