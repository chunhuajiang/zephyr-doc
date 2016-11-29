:orphan:

.. title:: THREAD_MONITOR

.. option:: CONFIG_THREAD_MONITOR:
.. _CONFIG_THREAD_MONITOR:

This option instructs the kernel to maintain a list of all tasks
and fibers (excluding those that have not yet started or have
already terminated).



:Symbol:           THREAD_MONITOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Task and fiber monitoring [EXPERIMENTAL]"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:125