:orphan:

.. title:: MPU6050_GPIO_PIN_NUM

.. option:: CONFIG_MPU6050_GPIO_PIN_NUM:
.. _CONFIG_MPU6050_GPIO_PIN_NUM:

The number of the GPIO on which the interrupt signal from the MPU6050
chip will be received.



:Symbol:           MPU6050_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if MPU6050 && MPU6050_TRIGGER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: MPU6050 && MPU6050_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:93