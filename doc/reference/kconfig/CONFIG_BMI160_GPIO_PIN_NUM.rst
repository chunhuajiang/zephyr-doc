:orphan:

.. title:: BMI160_GPIO_PIN_NUM

.. option:: CONFIG_BMI160_GPIO_PIN_NUM:
.. _CONFIG_BMI160_GPIO_PIN_NUM:

The number of the GPIO pin which is connected to BMI160 interrupt pin.



:Symbol:           BMI160_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if BMI160 && BMI160_TRIGGER && BMI160_TRIGGER_SOURCE_GPIO (value: "n")
:Default values:

 *  4 (value: "n")
 *   Condition: BMI160 && BMI160_TRIGGER && BMI160_TRIGGER_SOURCE_GPIO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmi160/Kconfig:97