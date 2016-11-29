:orphan:

.. title:: LPS25HB_I2C_MASTER_DEV_NAME

.. option:: CONFIG_LPS25HB_I2C_MASTER_DEV_NAME:
.. _CONFIG_LPS25HB_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which
LPS25HB is connected.



:Symbol:           LPS25HB_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where LPS25HB is connected" if LPS25HB (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: LPS25HB (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lps25hb/Kconfig:64