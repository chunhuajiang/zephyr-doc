:orphan:

.. title:: BMC150_MAGN_I2C_MASTER_DEV_NAME

.. option:: CONFIG_BMC150_MAGN_I2C_MASTER_DEV_NAME:
.. _CONFIG_BMC150_MAGN_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which BMC150_MAGN
is connected.



:Symbol:           BMC150_MAGN_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where BMC150_MAGN is connected" if BMC150_MAGN (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: BMC150_MAGN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmc150_magn/Kconfig:41