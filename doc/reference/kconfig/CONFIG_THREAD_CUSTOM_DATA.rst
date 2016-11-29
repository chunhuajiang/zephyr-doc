:orphan:

.. title:: THREAD_CUSTOM_DATA

.. option:: CONFIG_THREAD_CUSTOM_DATA:
.. _CONFIG_THREAD_CUSTOM_DATA:

This option allows each task and fiber to store 32 bits of custom data,
which can be accessed using the sys_thread_custom_data_xxx() APIs.



:Symbol:           THREAD_CUSTOM_DATA
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Task and fiber custom data"
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
 * ../kernel/unified/Kconfig:152