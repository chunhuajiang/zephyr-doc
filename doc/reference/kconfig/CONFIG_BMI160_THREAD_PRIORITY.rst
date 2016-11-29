:orphan:

.. title:: BMI160_THREAD_PRIORITY

.. option:: CONFIG_BMI160_THREAD_PRIORITY:
.. _CONFIG_BMI160_THREAD_PRIORITY:

The priority of the thread used for handling interrupts.



:Symbol:           BMI160_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Own thread priority" if BMI160 && BMI160_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: BMI160 && BMI160_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmi160/Kconfig:75