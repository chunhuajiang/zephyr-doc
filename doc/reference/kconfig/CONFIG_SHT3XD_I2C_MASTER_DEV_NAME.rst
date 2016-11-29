:orphan:

.. title:: SHT3XD_I2C_MASTER_DEV_NAME

.. option:: CONFIG_SHT3XD_I2C_MASTER_DEV_NAME:
.. _CONFIG_SHT3XD_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which the
SHT3xD chip is connected.



:Symbol:           SHT3XD_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where SHT3xD is connected" if SHT3XD (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: SHT3XD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sht3xd/Kconfig:45