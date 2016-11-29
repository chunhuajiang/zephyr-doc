:orphan:

.. title:: MPU6050_ACCEL_FS

.. option:: CONFIG_MPU6050_ACCEL_FS:
.. _CONFIG_MPU6050_ACCEL_FS:

Magnetometer full-scale range.
An X value for the config represents a range of +/- X g. Valid
values are 2, 4, 8 and 16.



:Symbol:           MPU6050_ACCEL_FS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Accelerometer full-scale range" if MPU6050 (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: MPU6050 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:118