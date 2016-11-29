:orphan:

.. title:: TH02_I2C_MASTER_DEV_NAME

.. option:: CONFIG_TH02_I2C_MASTER_DEV_NAME:
.. _CONFIG_TH02_I2C_MASTER_DEV_NAME:

The device name of the I2C master device to which the TH02
chip is connected.



:Symbol:           TH02_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C Master"
:Default values:

 *  "I2C_0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 TH02 (value: "n")
:Locations:
 * ../drivers/sensor/th02/Kconfig:33