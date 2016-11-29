:orphan:

.. title:: MPU6050_GYRO_FS

.. option:: CONFIG_MPU6050_GYRO_FS:
.. _CONFIG_MPU6050_GYRO_FS:

Gyroscope full-scale range.
An X value for the config represents a range of +/- X degrees/second.
Valid values are 250, 500, 1000, 2000.


:Symbol:           MPU6050_GYRO_FS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Gyroscope full-scale range" if MPU6050 (value: "n")
:Default values:

 *  250 (value: "n")
 *   Condition: MPU6050 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:128