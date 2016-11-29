:orphan:

.. title:: APPLICATION_INIT_PRIORITY

.. option:: CONFIG_APPLICATION_INIT_PRIORITY:
.. _CONFIG_APPLICATION_INIT_PRIORITY:

This priority level is for end-user drivers such as sensors and display
which have no inward dependencies.



:Symbol:           APPLICATION_INIT_PRIORITY
:Type:             int
:Value:            "90"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Default init priority for application level drivers"
:Default values:

 *  90 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:159