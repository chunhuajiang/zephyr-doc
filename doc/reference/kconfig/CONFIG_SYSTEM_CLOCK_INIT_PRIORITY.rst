:orphan:

.. title:: SYSTEM_CLOCK_INIT_PRIORITY

.. option:: CONFIG_SYSTEM_CLOCK_INIT_PRIORITY:
.. _CONFIG_SYSTEM_CLOCK_INIT_PRIORITY:

This options can be used to set a specific initialization priority
value for the system clock driver. As drivers on nanokernel
initialization level might need the clock to be running already, you
should let the default value as it is (0).


:Symbol:           SYSTEM_CLOCK_INIT_PRIORITY
:Type:             int
:Value:            "0"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "System clock driver initialization priority"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:167