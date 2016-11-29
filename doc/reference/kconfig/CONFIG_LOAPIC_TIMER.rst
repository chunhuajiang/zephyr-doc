:orphan:

.. title:: LOAPIC_TIMER

.. option:: CONFIG_LOAPIC_TIMER:
.. _CONFIG_LOAPIC_TIMER:

This option selects LOAPIC timer as a system timer.



:Symbol:           LOAPIC_TIMER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LOAPIC timer" if (LOAPIC || MVIC) && X86 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: (LOAPIC || MVIC) && X86 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_SERIES_QUARK_D2000 || SOC_SERIES_QUARK_SE (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:97