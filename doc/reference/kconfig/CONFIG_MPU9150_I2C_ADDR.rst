:orphan:

.. title:: MPU9150_I2C_ADDR

.. option:: CONFIG_MPU9150_I2C_ADDR:
.. _CONFIG_MPU9150_I2C_ADDR:

I2C address of the MPU9150. If the driver for MPU6050 is enabled,
its address will be used and this option made unavailable.


:Symbol:           MPU9150_I2C_ADDR
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

 *  "MPU9180 I2C address" if AK8975 && MPU9150 && !MPU6050 (value: "n")
:Default values:

 *  0x68 (value: "n")
 *   Condition: AK8975 && MPU9150 && !MPU6050 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/ak8975/Kconfig:70