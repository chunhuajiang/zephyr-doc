:orphan:

.. title:: BMC150_MAGN_I2C_ADDR

.. option:: CONFIG_BMC150_MAGN_I2C_ADDR:
.. _CONFIG_BMC150_MAGN_I2C_ADDR:

Specify the I2C slave address for the BMC150_MAGN.

0x12: GND
0x13: VCC



:Symbol:           BMC150_MAGN_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "BMC150_MAGN I2C slave address" if BMC150_MAGN (value: "n")
:Default values:

 *  0x12 (value: "n")
 *   Condition: BMC150_MAGN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmc150_magn/Kconfig:31