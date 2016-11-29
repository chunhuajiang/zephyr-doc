:orphan:

.. title:: BMA280

.. option:: CONFIG_BMA280:
.. _CONFIG_BMA280:

Enable driver for BMA280 I2C-based triaxial accelerometer sensor
family.



:Symbol:           BMA280
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "BMA280 Three Axis Accelerometer Family" if SENSOR && I2C (value: "n")
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
 * ../drivers/sensor/bma280/Kconfig:19