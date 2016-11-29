:orphan:

.. title:: TMP007_I2C_MASTER_DEV_NAME

.. option:: CONFIG_TMP007_I2C_MASTER_DEV_NAME:
.. _CONFIG_TMP007_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which the
TMP007 chip is connected.



:Symbol:           TMP007_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where TMP007 is connected" if TMP007 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: TMP007 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/tmp007/Kconfig:52