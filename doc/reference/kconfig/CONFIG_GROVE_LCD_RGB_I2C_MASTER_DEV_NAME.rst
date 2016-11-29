:orphan:

.. title:: GROVE_LCD_RGB_I2C_MASTER_DEV_NAME

.. option:: CONFIG_GROVE_LCD_RGB_I2C_MASTER_DEV_NAME:
.. _CONFIG_GROVE_LCD_RGB_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which the
Grove LCD is connected.



:Symbol:           GROVE_LCD_RGB_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C Master where Grove LCD is connected" if GROVE_LCD_RGB (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: GROVE_LCD_RGB (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/grove/Kconfig:52