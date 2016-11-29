:orphan:

.. title:: MPU6050_GPIO_DEV_NAME

.. option:: CONFIG_MPU6050_GPIO_DEV_NAME:
.. _CONFIG_MPU6050_GPIO_DEV_NAME:

The device name of the GPIO device to which the MPU6050 interrupt pin
is connected.



:Symbol:           MPU6050_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if MPU6050 && MPU6050_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: MPU6050 && MPU6050_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:84