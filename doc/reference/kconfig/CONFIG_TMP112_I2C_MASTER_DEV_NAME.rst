:orphan:

.. title:: TMP112_I2C_MASTER_DEV_NAME

.. option:: CONFIG_TMP112_I2C_MASTER_DEV_NAME:
.. _CONFIG_TMP112_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which the
TMP112 chip is connected.


:Symbol:           TMP112_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where TMP112 is connected" if TMP112 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: TMP112 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/tmp112/Kconfig:48