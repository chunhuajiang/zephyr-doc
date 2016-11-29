:orphan:

.. title:: TIMESLICE_PRIORITY

.. option:: CONFIG_TIMESLICE_PRIORITY:
.. _CONFIG_TIMESLICE_PRIORITY:

This option specifies the thread priority level at which time slicing
takes effect; threads having a higher priority than this ceiling are
not subject to time slicing.



:Symbol:           TIMESLICE_PRIORITY
:Type:             int
:Value:            "0"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, NUM_PREEMPT_PRIORITIES]
:Prompts:

 *  "Time slicing thread priority ceiling" if TIMESLICING (value: "y")
:Default values:

 *  0 (value: "n")
 *   Condition: TIMESLICING (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:283