:orphan:

.. title:: LSM6DS0_I2C_MASTER_DEV_NAME

.. option:: CONFIG_LSM6DS0_I2C_MASTER_DEV_NAME:
.. _CONFIG_LSM6DS0_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which LSM6DS0 is
connected.



:Symbol:           LSM6DS0_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where LSM6DS0 chip is connected" if LSM6DS0 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: LSM6DS0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm6ds0/Kconfig:62