:orphan:

.. title:: INT_LATENCY_BENCHMARK

.. option:: CONFIG_INT_LATENCY_BENCHMARK:
.. _CONFIG_INT_LATENCY_BENCHMARK:

This option enables the tracking of interrupt latency metrics;
the exact set of metrics being tracked is board-dependent.
Tracking begins when int_latency_init() is invoked by an application.
The metrics are displayed (and a new sampling interval is started)
each time int_latency_show() is called thereafter.



:Symbol:           INT_LATENCY_BENCHMARK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt latency metrics [EXPERIMENTAL]" if ARCH = "x86" (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: ARCH = "x86" (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:101