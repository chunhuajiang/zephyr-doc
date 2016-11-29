:orphan:

.. title:: MAIN_THREAD_PRIORITY

.. option:: CONFIG_MAIN_THREAD_PRIORITY:
.. _CONFIG_MAIN_THREAD_PRIORITY:

Priority at which the initialization thread runs, including the start
of the main() function. main() can then change its priority if desired.



:Symbol:           MAIN_THREAD_PRIORITY
:Type:             int
:Value:            "0"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Priority of initialization/main thread"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
 *  -1 (value: "n")
 *   Condition: NUM_PREEMPT_PRIORITIES = 0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:113