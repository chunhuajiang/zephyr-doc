:orphan:

.. title:: LSM6DS0_GYRO_FULLSCALE

.. option:: CONFIG_LSM6DS0_GYRO_FULLSCALE:
.. _CONFIG_LSM6DS0_GYRO_FULLSCALE:

Specify the default gyroscope full-scale range.
An X value for the config represents a range of +/- X degree per
second. Valid values are 245, 500 and 2000.



:Symbol:           LSM6DS0_GYRO_FULLSCALE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Gyroscope full-scale range" if LSM6DS0 (value: "n")
:Default values:

 *  245 (value: "n")
 *   Condition: LSM6DS0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 LSM6DS0 (value: "n")
:Locations:
 * ../drivers/sensor/lsm6ds0/Kconfig:129