:orphan:

.. title:: LSM9DS0_MFD_ACCEL_ENABLE

.. option:: CONFIG_LSM9DS0_MFD_ACCEL_ENABLE:
.. _CONFIG_LSM9DS0_MFD_ACCEL_ENABLE:

Enable/disable accelerometer totally by stripping everything related
in driver.



:Symbol:           LSM9DS0_MFD_ACCEL_ENABLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable accelerometer" if LSM9DS0_MFD (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: LSM9DS0_MFD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm9ds0_mfd/Kconfig:50