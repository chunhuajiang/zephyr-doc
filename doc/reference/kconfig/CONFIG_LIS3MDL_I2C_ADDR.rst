:orphan:

.. title:: LIS3MDL_I2C_ADDR

.. option:: CONFIG_LIS3MDL_I2C_ADDR:
.. _CONFIG_LIS3MDL_I2C_ADDR:

I2C address of the LIS3MDL sensor.
Use 0x1C if the SA1 pin is pulled to GND or 0x1E if the SA1 pin
is pulled to VDD.



:Symbol:           LIS3MDL_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C address" if LIS3MDL (value: "n")
:Default values:

 *  0x1C (value: "n")
 *   Condition: LIS3MDL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3mdl/Kconfig:33