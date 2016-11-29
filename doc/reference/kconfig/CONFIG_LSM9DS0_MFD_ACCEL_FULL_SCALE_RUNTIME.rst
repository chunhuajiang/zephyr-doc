:orphan:

.. title:: LSM9DS0_MFD_ACCEL_FULL_SCALE_RUNTIME

.. option:: CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_RUNTIME:
.. _CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_RUNTIME:

Enable alteration of accelerometer full-scale attribute at
runtime.



:Symbol:           LSM9DS0_MFD_ACCEL_FULL_SCALE_RUNTIME
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable dynamic full-scale for accelerometer" if LSM9DS0_MFD_ACCEL_ENABLE (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: LSM9DS0_MFD_ACCEL_ENABLE (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 LSM9DS0_MFD (value: "n")
:Locations:
 * ../drivers/sensor/lsm9ds0_mfd/Kconfig:167