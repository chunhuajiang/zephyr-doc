:orphan:

.. title:: BME280_I2C_ADDR

.. option:: CONFIG_BME280_I2C_ADDR:
.. _CONFIG_BME280_I2C_ADDR:

Specify the I2C slave address for the BME280.

0x76: Ground
0x77: VCC



:Symbol:           BME280_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "BME280 I2C slave address" if BME280 (value: "n")
:Default values:

 *  0x76 (value: "n")
 *   Condition: BME280 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bme280/Kconfig:30