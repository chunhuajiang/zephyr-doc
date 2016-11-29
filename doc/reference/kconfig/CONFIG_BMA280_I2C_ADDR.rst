:orphan:

.. title:: BMA280_I2C_ADDR

.. option:: CONFIG_BMA280_I2C_ADDR:
.. _CONFIG_BMA280_I2C_ADDR:

I2C address of the BMA280 sensor.

0x10: Use if the SDO pin is pulled to GND.
0x10: Use if the SDO pin is pulled to VDDIO.
0x18: Use if the SDO pin is pulled to GND.
0x19: Use if the SDO pin is pulled to VDDIO.



:Symbol:           BMA280_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "BMA280 I2C address" if BMA280 (value: "n")
:Default values:

 *  0x18 (value: "n")
 *   Condition: BMA280_CHIP_BMA280 && BMA280 (value: "n")
 *  0x10 (value: "n")
 *   Condition: BMA280_CHIP_BMC150_ACCEL && BMA280 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bma280/Kconfig:58