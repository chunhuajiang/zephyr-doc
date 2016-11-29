:orphan:

.. title:: BMI160_GPIO_DEV_NAME

.. option:: CONFIG_BMI160_GPIO_DEV_NAME:
.. _CONFIG_BMI160_GPIO_DEV_NAME:

The name of the GPIO device to which the BMI160 interrupt pin is
connected.



:Symbol:           BMI160_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Gpio device" if BMI160 && BMI160_TRIGGER && BMI160_TRIGGER_SOURCE_GPIO (value: "n")
:Default values:

 *  "GPIO_1"
 *   Condition: BMI160 && BMI160_TRIGGER && BMI160_TRIGGER_SOURCE_GPIO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmi160/Kconfig:89