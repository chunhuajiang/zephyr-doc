:orphan:

.. title:: TIMESLICE_SIZE

.. option:: CONFIG_TIMESLICE_SIZE:
.. _CONFIG_TIMESLICE_SIZE:

This option specifies the maximum amount of time a thread can execute
before other threads of equal priority are given an opportunity to run.
A time slice size of zero means "no limit" (i.e. an infinitely large
time slice).



:Symbol:           TIMESLICE_SIZE
:Type:             int
:Value:            "0"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 2147483647]
:Prompts:

 *  "Time slice size (in ms)" if TIMESLICING (value: "y")
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
 * ../kernel/unified/Kconfig:272