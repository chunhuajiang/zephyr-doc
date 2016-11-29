:orphan:

.. title:: FXOS8700

.. option:: CONFIG_FXOS8700:
.. _CONFIG_FXOS8700:

Enable driver for the FXOS8700 accelerometer/magnetometer



:Symbol:           FXOS8700
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "FXOS8700 accelerometer/magnetometer driver" if SENSOR && I2C (value: "n")
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
 * ../drivers/sensor/fxos8700/Kconfig:18