:orphan:

.. title:: BMI160_SPI_BUS_FREQ

.. option:: CONFIG_BMI160_SPI_BUS_FREQ:
.. _CONFIG_BMI160_SPI_BUS_FREQ:

This is the maximum supported SPI bus frequency. The chip supports a
frequency up to 10MHz.



:Symbol:           BMI160_SPI_BUS_FREQ
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "BMI160 SPI bus speed in Hz" if BMI160 (value: "n")
:Default values:

 *  640000 (value: "n")
 *   Condition: BMI160 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmi160/Kconfig:29