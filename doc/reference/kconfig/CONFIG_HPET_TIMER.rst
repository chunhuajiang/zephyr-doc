:orphan:

.. title:: HPET_TIMER

.. option:: CONFIG_HPET_TIMER:
.. _CONFIG_HPET_TIMER:

This option selects High Precision Event Timer (HPET) as a
system timer.



:Symbol:           HPET_TIMER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HPET timer" if X86 (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: X86 (value: "y")
:Selects:

 *  :option:`CONFIG_IOAPIC` if X86 (value: "y")
 *  :option:`CONFIG_LOAPIC` if X86 (value: "y")
 *  :option:`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME` if X86 (value: "y")
:Reverse (select-related) dependencies:
 SOC_SERIES_QUARK_X1000 || SOC_SERIES_QUARK_X1000 && X86 && SOC_QUARK_X1000 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:22