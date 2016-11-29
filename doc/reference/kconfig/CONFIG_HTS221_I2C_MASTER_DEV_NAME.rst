:orphan:

.. title:: HTS221_I2C_MASTER_DEV_NAME

.. option:: CONFIG_HTS221_I2C_MASTER_DEV_NAME:
.. _CONFIG_HTS221_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which HTS221 is
connected.



:Symbol:           HTS221_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where HTS221 is connected" if HTS221 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: HTS221 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hts221/Kconfig:33