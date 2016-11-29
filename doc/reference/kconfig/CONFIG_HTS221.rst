:orphan:

.. title:: HTS221

.. option:: CONFIG_HTS221:
.. _CONFIG_HTS221:

Enable driver for HTS221 I2C-based temperature and humidity sensor.



:Symbol:           HTS221
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HTS221 temperature and humidity sensor" if SENSOR && I2C (value: "n")
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
 * ../drivers/sensor/hts221/Kconfig:17