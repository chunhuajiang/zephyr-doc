:orphan:

.. title:: LSM6DS0

.. option:: CONFIG_LSM6DS0:
.. _CONFIG_LSM6DS0:

Enable driver for LSM6DS0 I2C-based accelerometer and gyroscope
sensor.



:Symbol:           LSM6DS0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LSM6DS0 I2C accelerometer and gyroscope Chip" if SENSOR && I2C && NANO_TIMEOUTS (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && I2C && NANO_TIMEOUTS (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm6ds0/Kconfig:20