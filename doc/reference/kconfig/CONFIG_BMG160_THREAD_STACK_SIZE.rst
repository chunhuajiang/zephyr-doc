:orphan:

.. title:: BMG160_THREAD_STACK_SIZE

.. option:: CONFIG_BMG160_THREAD_STACK_SIZE:
.. _CONFIG_BMG160_THREAD_STACK_SIZE:

The thread stack size.



:Symbol:           BMG160_THREAD_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Own thread stack size" if BMG160 && BMG160_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: BMG160 && BMG160_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmg160/Kconfig:78