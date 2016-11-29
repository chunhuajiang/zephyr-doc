:orphan:

.. title:: BMG160_THREAD_PRIORITY

.. option:: CONFIG_BMG160_THREAD_PRIORITY:
.. _CONFIG_BMG160_THREAD_PRIORITY:

The priority of the thread used for handling interrupts.



:Symbol:           BMG160_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Own thread priority" if BMG160 && BMG160_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: BMG160 && BMG160_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmg160/Kconfig:71