:orphan:

.. title:: MPU6050_TRIGGER

.. option:: CONFIG_MPU6050_TRIGGER:
.. _CONFIG_MPU6050_TRIGGER:

The configuration item CONFIG_MPU6050_TRIGGER:

:Symbol:           MPU6050_TRIGGER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 MPU6050_TRIGGER_GLOBAL_THREAD && GPIO || MPU6050_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:80