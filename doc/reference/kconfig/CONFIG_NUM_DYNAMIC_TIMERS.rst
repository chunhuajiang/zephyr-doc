:orphan:

.. title:: NUM_DYNAMIC_TIMERS

.. option:: CONFIG_NUM_DYNAMIC_TIMERS:
.. _CONFIG_NUM_DYNAMIC_TIMERS:

Number of timers available for dynamic allocation via the
k_timer_alloc()/k_timer_free() API.



:Symbol:           NUM_DYNAMIC_TIMERS
:Type:             int
:Value:            "0"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Number of timers available for dynamic allocation" if NANO_TIMERS (value: "y")
:Default values:

 *  0 (value: "n")
 *   Condition: NANO_TIMERS (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:176