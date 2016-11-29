:orphan:

.. title:: LSM9DS0_GYRO_I2C_ADDR

.. option:: CONFIG_LSM9DS0_GYRO_I2C_ADDR:
.. _CONFIG_LSM9DS0_GYRO_I2C_ADDR:

Specify the I2C slave address for the LSM9DS0_GYRO.

0x6A: GND
0x6B: VCC



:Symbol:           LSM9DS0_GYRO_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LSM9DS0_GYRO I2C slave address" if LSM9DS0_GYRO (value: "n")
:Default values:

 *  0x6A (value: "n")
 *   Condition: LSM9DS0_GYRO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm9ds0_gyro/Kconfig:31