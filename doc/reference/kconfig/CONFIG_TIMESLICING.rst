:orphan:

.. title:: TIMESLICING

.. option:: CONFIG_TIMESLICING:
.. _CONFIG_TIMESLICING:

This option enables time slicing between preemptible threads of
equal priority.



:Symbol:           TIMESLICING
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread time slicing" if SYS_CLOCK_EXISTS && NUM_PREEMPT_PRIORITIES != 0 (value: "y")
:Default values:

 *  y (value: "y")
 *   Condition: SYS_CLOCK_EXISTS && NUM_PREEMPT_PRIORITIES != 0 (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:264