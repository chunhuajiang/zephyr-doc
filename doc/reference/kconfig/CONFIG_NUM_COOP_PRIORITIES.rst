:orphan:

.. title:: NUM_COOP_PRIORITIES

.. option:: CONFIG_NUM_COOP_PRIORITIES:
.. _CONFIG_NUM_COOP_PRIORITIES:

Number of cooperative priorities configured in the system. Gives access
to priorities:

        K_PRIO_COOP(0) to K_PRIO_COOP(CONFIG_NUM_COOP_PRIORITIES - 1)

or seen another way, priorities:

        -CONFIG_NUM_COOP_PRIORITIES to -1

This can be set to zero to disable cooperative scheduling. Cooperative
threads always preempt preemptible threads.

Each priority requires an extra 8 bytes of RAM. Each set of 32 extra
total priorities require an extra 4 bytes and add one possible
iteration to loops that search for the next thread to run.

The total number of priorities is

   NUM_COOP_PRIORITIES + NUM_PREEMPT_PRIORITIES + 1

The extra one is for the idle thread, which must run at the lowest
priority, and be the only thread at that priority.



:Symbol:           NUM_COOP_PRIORITIES
:Type:             int
:Value:            "16"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Number of coop priorities"
:Default values:

 *  16 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:31