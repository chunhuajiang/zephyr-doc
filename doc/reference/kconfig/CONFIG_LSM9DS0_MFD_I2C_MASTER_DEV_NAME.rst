:orphan:

.. title:: LSM9DS0_MFD_I2C_MASTER_DEV_NAME

.. option:: CONFIG_LSM9DS0_MFD_I2C_MASTER_DEV_NAME:
.. _CONFIG_LSM9DS0_MFD_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which LSM9DS0_MFD
is connected.



:Symbol:           LSM9DS0_MFD_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where LSM9DS0 gyroscope is connected" if LSM9DS0_MFD (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: LSM9DS0_MFD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm9ds0_mfd/Kconfig:42