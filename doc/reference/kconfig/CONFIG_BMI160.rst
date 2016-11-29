:orphan:

.. title:: BMI160

.. option:: CONFIG_BMI160:
.. _CONFIG_BMI160:

Enable Bosch BMI160 inertial measurement unit that provides acceleration
and angular rate measurements.



:Symbol:           BMI160
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bosch BMI160 inertial measurement unit" if SENSOR && SPI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && SPI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmi160/Kconfig:1