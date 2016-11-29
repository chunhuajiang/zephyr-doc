:orphan:

.. title:: MAX44009_I2C_DEV_NAME

.. option:: CONFIG_MAX44009_I2C_DEV_NAME:
.. _CONFIG_MAX44009_I2C_DEV_NAME:

Specify the device name of the I2C master device to which the
MAX44009 chip is connected.


:Symbol:           MAX44009_I2C_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where MAX44009 is connected" if MAX44009 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: MAX44009 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/max44009/Kconfig:47