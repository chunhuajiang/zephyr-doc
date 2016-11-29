:orphan:

.. title:: LSM9DS0_MFD

.. option:: CONFIG_LSM9DS0_MFD:
.. _CONFIG_LSM9DS0_MFD:

Enable driver for LSM9DS0 I2C-based MFD sensor.



:Symbol:           LSM9DS0_MFD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LSM9DS0 I2C accelerometer, magnetometer and temperature sensor chip" if SENSOR && I2C && NANO_TIMEOUTS (value: "n")
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
 * ../drivers/sensor/lsm9ds0_mfd/Kconfig:20