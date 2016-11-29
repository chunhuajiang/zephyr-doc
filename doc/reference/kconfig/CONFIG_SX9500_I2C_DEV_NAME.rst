:orphan:

.. title:: SX9500_I2C_DEV_NAME

.. option:: CONFIG_SX9500_I2C_DEV_NAME:
.. _CONFIG_SX9500_I2C_DEV_NAME:

Specify the device name of the I2C master device to which SX9500 is
connected.



:Symbol:           SX9500_I2C_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where SX9500 is connected" if SX9500 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: SX9500 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sx9500/Kconfig:38