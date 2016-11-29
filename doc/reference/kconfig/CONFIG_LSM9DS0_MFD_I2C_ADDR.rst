:orphan:

.. title:: LSM9DS0_MFD_I2C_ADDR

.. option:: CONFIG_LSM9DS0_MFD_I2C_ADDR:
.. _CONFIG_LSM9DS0_MFD_I2C_ADDR:

Specify the I2C slave address for the LSM9DS0_MFD.

0x1E: GND
0x1F: VCC



:Symbol:           LSM9DS0_MFD_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LSM9DS0_MFD I2C slave address" if LSM9DS0_MFD (value: "n")
:Default values:

 *  0x1E (value: "n")
 *   Condition: LSM9DS0_MFD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm9ds0_mfd/Kconfig:32