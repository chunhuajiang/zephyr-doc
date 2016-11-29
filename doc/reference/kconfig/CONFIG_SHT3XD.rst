:orphan:

.. title:: SHT3XD

.. option:: CONFIG_SHT3XD:
.. _CONFIG_SHT3XD:

Enable driver for SHT3xD temperature and humidity sensors.



:Symbol:           SHT3XD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SHT3xD Temperature and Humidity Sensor" if SENSOR && I2C (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && I2C (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sht3xd/Kconfig:19