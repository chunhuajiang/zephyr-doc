:orphan:

.. title:: LSM9DS0_GYRO_SAMPLING_RATE_RUNTIME

.. option:: CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_RUNTIME:
.. _CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_RUNTIME:

Enable alteration of sampling rate frequency at runtime.



:Symbol:           LSM9DS0_GYRO_SAMPLING_RATE_RUNTIME
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable dynamic sampling rate" if LSM9DS0_GYRO (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: LSM9DS0_GYRO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 LSM9DS0_GYRO (value: "n")
:Locations:
 * ../drivers/sensor/lsm9ds0_gyro/Kconfig:106