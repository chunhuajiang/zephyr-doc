:orphan:

.. title:: AK8975_I2C_MASTER_DEV_NAME

.. option:: CONFIG_AK8975_I2C_MASTER_DEV_NAME:
.. _CONFIG_AK8975_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which the
AK8975 chip is connected.



:Symbol:           AK8975_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where AK8975 is connected" if AK8975 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: AK8975 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/ak8975/Kconfig:52