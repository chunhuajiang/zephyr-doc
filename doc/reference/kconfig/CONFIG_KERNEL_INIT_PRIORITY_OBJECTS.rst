:orphan:

.. title:: KERNEL_INIT_PRIORITY_OBJECTS

.. option:: CONFIG_KERNEL_INIT_PRIORITY_OBJECTS:
.. _CONFIG_KERNEL_INIT_PRIORITY_OBJECTS:

Kernel objects use this priority for initialization. This
priority needs to be higher than minimal default initialization
priority.



:Symbol:           KERNEL_INIT_PRIORITY_OBJECTS
:Type:             int
:Value:            "30"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Kernel objects initialization priority"
:Default values:

 *  30 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:134