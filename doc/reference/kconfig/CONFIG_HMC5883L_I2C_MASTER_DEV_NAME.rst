:orphan:

.. title:: HMC5883L_I2C_MASTER_DEV_NAME

.. option:: CONFIG_HMC5883L_I2C_MASTER_DEV_NAME:
.. _CONFIG_HMC5883L_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which HMC5883L
is connected.



:Symbol:           HMC5883L_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where HMC5883L is connected" if HMC5883L (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: HMC5883L (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hmc5883l/Kconfig:33