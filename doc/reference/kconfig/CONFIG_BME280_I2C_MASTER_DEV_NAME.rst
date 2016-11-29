:orphan:

.. title:: BME280_I2C_MASTER_DEV_NAME

.. option:: CONFIG_BME280_I2C_MASTER_DEV_NAME:
.. _CONFIG_BME280_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which BME280 is
connected.



:Symbol:           BME280_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where BME280 is connected" if BME280 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: BME280 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bme280/Kconfig:40