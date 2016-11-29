:orphan:

.. title:: LSM6DS0_ACCEL_FULLSCALE

.. option:: CONFIG_LSM6DS0_ACCEL_FULLSCALE:
.. _CONFIG_LSM6DS0_ACCEL_FULLSCALE:

Specify the default accelerometer full-scale range.
An X value for the config represents a range of +/- X G. Valid values
are 2, 4, 8 and 16.



:Symbol:           LSM6DS0_ACCEL_FULLSCALE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Accelerometer full-scale range" if LSM6DS0 (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: LSM6DS0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 LSM6DS0 (value: "n")
:Locations:
 * ../drivers/sensor/lsm6ds0/Kconfig:150