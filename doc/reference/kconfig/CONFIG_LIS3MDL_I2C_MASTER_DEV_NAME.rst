:orphan:

.. title:: LIS3MDL_I2C_MASTER_DEV_NAME

.. option:: CONFIG_LIS3MDL_I2C_MASTER_DEV_NAME:
.. _CONFIG_LIS3MDL_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which LIS3MDL is
connected.



:Symbol:           LIS3MDL_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where LIS3MDL is connected" if LIS3MDL (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: LIS3MDL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3mdl/Kconfig:43