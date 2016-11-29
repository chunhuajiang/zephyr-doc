:orphan:

.. title:: LIS3DH_I2C_ADDR

.. option:: CONFIG_LIS3DH_I2C_ADDR:
.. _CONFIG_LIS3DH_I2C_ADDR:

I2C address of the LIS3DH sensor.

0x18: Choose this option if the SDO pin is pulled to GND.
0x19: Choose this option if the SDO pin is pulled to VDDIO.



:Symbol:           LIS3DH_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LIS3DH I2C address" if LIS3DH (value: "n")
:Default values:

 *  0x18 (value: "n")
 *   Condition: LIS3DH (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3dh/Kconfig:35