:orphan:

.. title:: LSM6DS0_ACCEL_ENABLE_Y_AXIS

.. option:: CONFIG_LSM6DS0_ACCEL_ENABLE_Y_AXIS:
.. _CONFIG_LSM6DS0_ACCEL_ENABLE_Y_AXIS:

Enable/disable accelerometer Y axis totally by stripping everything
related in driver.



:Symbol:           LSM6DS0_ACCEL_ENABLE_Y_AXIS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable accelerometer Y axis" if LSM6DS0 (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: LSM6DS0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm6ds0/Kconfig:78