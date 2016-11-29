:orphan:

.. title:: BMI160_THREAD_STACK_SIZE

.. option:: CONFIG_BMI160_THREAD_STACK_SIZE:
.. _CONFIG_BMI160_THREAD_STACK_SIZE:

The thread stack size.



:Symbol:           BMI160_THREAD_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Own thread stack size" if BMI160 && BMI160_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: BMI160 && BMI160_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmi160/Kconfig:82