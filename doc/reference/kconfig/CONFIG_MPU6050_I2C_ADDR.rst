:orphan:

.. title:: MPU6050_I2C_ADDR

.. option:: CONFIG_MPU6050_I2C_ADDR:
.. _CONFIG_MPU6050_I2C_ADDR:

I2C address of the MPU6050 sensor.
Choose 0x68 if the AD0 pin is pulled to GND or 0x69 if the AD0 pin
is pulled to VDD.



:Symbol:           MPU6050_I2C_ADDR
:Type:             hex
:Value:            "0x68"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0x68, 0x69]
:Prompts:

 *  "I2C address" if MPU6050 (value: "n")
:Default values:

 *  0x68 (value: "n")
 *   Condition: MPU6050 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:35