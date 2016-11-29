:orphan:

.. title:: HDC1008_I2C_MASTER_DEV_NAME

.. option:: CONFIG_HDC1008_I2C_MASTER_DEV_NAME:
.. _CONFIG_HDC1008_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which the
HDC1008 chip is connected.



:Symbol:           HDC1008_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where HDC1008 is connected" if HDC1008 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: HDC1008 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hdc1008/Kconfig:46