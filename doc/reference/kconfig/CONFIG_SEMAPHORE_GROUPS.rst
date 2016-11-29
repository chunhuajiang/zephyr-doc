:orphan:

.. title:: SEMAPHORE_GROUPS

.. option:: CONFIG_SEMAPHORE_GROUPS:
.. _CONFIG_SEMAPHORE_GROUPS:

This option enables support for semaphore groups. Threads that use
semaphore groups require more stack space. Disabling this option will
both decrease the footprint as well as improve the performance of
the k_sem_give() routine.



:Symbol:           SEMAPHORE_GROUPS
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable semaphore groups"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:295