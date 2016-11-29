:orphan:

.. title:: LSM9DS0_GYRO

.. option:: CONFIG_LSM9DS0_GYRO:
.. _CONFIG_LSM9DS0_GYRO:

Enable driver for LSM9DS0 I2C-based gyroscope sensor.



:Symbol:           LSM9DS0_GYRO
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LSM9DS0 I2C gyroscope Chip" if SENSOR && I2C && NANO_TIMEOUTS (value: "n")
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
 * ../drivers/sensor/lsm9ds0_gyro/Kconfig:19