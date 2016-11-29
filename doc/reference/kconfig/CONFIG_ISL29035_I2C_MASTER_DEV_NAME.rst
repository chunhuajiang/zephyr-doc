:orphan:

.. title:: ISL29035_I2C_MASTER_DEV_NAME

.. option:: CONFIG_ISL29035_I2C_MASTER_DEV_NAME:
.. _CONFIG_ISL29035_I2C_MASTER_DEV_NAME:

The device name of the I2C master device to which the ISL29035
chip is connected.



:Symbol:           ISL29035_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C Master" if ISL29035 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: ISL29035 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/isl29035/Kconfig:35