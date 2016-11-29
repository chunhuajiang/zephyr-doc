:orphan:

.. title:: BMI160_SPI_PORT_NAME

.. option:: CONFIG_BMI160_SPI_PORT_NAME:
.. _CONFIG_BMI160_SPI_PORT_NAME:

Master I2C port name through which BMI160 chip is accessed.



:Symbol:           BMI160_SPI_PORT_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI master controller port name" if BMI160 (value: "n")
:Default values:

 *  ""
 *   Condition: BMI160 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmi160/Kconfig:15