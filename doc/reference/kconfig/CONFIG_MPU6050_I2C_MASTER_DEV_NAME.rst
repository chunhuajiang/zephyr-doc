:orphan:

.. title:: MPU6050_I2C_MASTER_DEV_NAME

.. option:: CONFIG_MPU6050_I2C_MASTER_DEV_NAME:
.. _CONFIG_MPU6050_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which MPU6050 is
connected.



:Symbol:           MPU6050_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where MPU6050 is connected" if MPU6050 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: MPU6050 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:46