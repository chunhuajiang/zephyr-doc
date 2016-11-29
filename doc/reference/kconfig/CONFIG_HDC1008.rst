:orphan:

.. title:: HDC1008

.. option:: CONFIG_HDC1008:
.. _CONFIG_HDC1008:

Enable driver for HDC1008 temperature and humidity sensors.



:Symbol:           HDC1008
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HDC1008 Temperature and Humidity Sensor" if SENSOR && I2C && GPIO (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && I2C && GPIO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hdc1008/Kconfig:19