:orphan:

.. title:: NUM_PREEMPT_PRIORITIES

.. option:: CONFIG_NUM_PREEMPT_PRIORITIES:
.. _CONFIG_NUM_PREEMPT_PRIORITIES:

Number of preemptible priorities available in the system. Gives access
to priorities 0 to CONFIG_NUM_PREEMPT_PRIORITIES - 1.

This can be set to 0 to disable preemptible scheduling.

Each priority requires an extra 8 bytes of RAM. Each set of 32 extra
total priorities require an extra 4 bytes and add one possible
iteration to loops that search for the next thread to run.

The total number of priorities is

   NUM_COOP_PRIORITIES + NUM_PREEMPT_PRIORITIES + 1

The extra one is for the idle thread, which must run at the lowest
priority, and be the only thread at that priority.



:Symbol:           NUM_PREEMPT_PRIORITIES
:Type:             int
:Value:            "15"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Number of preemptible priorities"
:Default values:

 *  15 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:59