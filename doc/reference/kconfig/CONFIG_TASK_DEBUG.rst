:orphan:

.. title:: TASK_DEBUG

.. option:: CONFIG_TASK_DEBUG:
.. _CONFIG_TASK_DEBUG:

This option allows execution of all tasks (with the exception of
essential system tasks) to be suspended so that debugging operations
can be performed.



:Symbol:           TASK_DEBUG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Task debugging [EXPERIMENTAL]"
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
 * ../misc/Kconfig:168